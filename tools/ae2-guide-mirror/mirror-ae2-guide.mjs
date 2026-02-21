#!/usr/bin/env node
/**
 * AE2 guide mirror + zh-TW (繁體中文／台灣) translation pipeline (Node-only, no deps).
 *
 * Mirrors https://guide.appliedenergistics.org/1.21.1/ into
 *   atm/docs/external/ae2-guide/1.21.1/
 */

import { mkdir, writeFile, readFile, stat } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import path from 'node:path';
import process from 'node:process';

const BASE_ORIGIN = 'https://guide.appliedenergistics.org';
const BASE_PATH = '/1.21.1/';
const BASE_PATH_NO_SLASH = '/1.21.1';

const ATM_ROOT = path.resolve(process.cwd());
const DEFAULT_OUT_ROOT = path.resolve(ATM_ROOT, 'docs/external/ae2-guide/1.21.1');

const argv = process.argv.slice(2);
const flags = new Set(argv.filter(a => a.startsWith('--')));
const getArg = (name, def) => {
  const idx = argv.indexOf(`--${name}`);
  if (idx === -1) return def;
  const v = argv[idx + 1];
  if (!v || v.startsWith('--')) return def;
  return v;
};

const LIMIT = Number(getArg('limit', flags.has('--limit') ? '2' : '0')) || 0; // 0 = no limit
const OUT_ROOT = path.resolve(getArg('out', DEFAULT_OUT_ROOT));
const HOTLINK_GUIDE_ASSETS = flags.has('--hotlink-guide-assets');
const VERBOSE = flags.has('--verbose');

function log(...args) {
  if (VERBOSE) console.log(...args);
}

function sha1(s) {
  return createHash('sha1').update(s).digest('hex');
}

async function exists(p) {
  try {
    await stat(p);
    return true;
  } catch {
    return false;
  }
}

async function fetchText(url, { retries = 3 } = {}) {
  let lastErr;
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url, {
        redirect: 'follow',
        headers: {
          // avoid some bot protections; keep simple
          'user-agent': 'ae2-guide-mirror/1.0 (+offline)'
        }
      });
      if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
      return await res.text();
    } catch (e) {
      lastErr = e;
      await new Promise(r => setTimeout(r, 400 * (i + 1)));
    }
  }
  throw lastErr;
}

async function fetchBuffer(url, { retries = 3 } = {}) {
  let lastErr;
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url, {
        redirect: 'follow',
        headers: {
          'user-agent': 'ae2-guide-mirror/1.0 (+offline)'
        }
      });
      if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
      const ab = await res.arrayBuffer();
      return Buffer.from(ab);
    } catch (e) {
      lastErr = e;
      await new Promise(r => setTimeout(r, 400 * (i + 1)));
    }
  }
  throw lastErr;
}

function extractNextDataJson(html) {
  // Next.js uses: <script id="__NEXT_DATA__" type="application/json">{...}</script>
  const m = html.match(/<script[^>]+id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
  if (!m) return null;
  try {
    return JSON.parse(m[1]);
  } catch {
    return null;
  }
}

function normalizeRoute(routePath) {
  if (!routePath) return null;
  if (routePath === BASE_PATH_NO_SLASH) return BASE_PATH;
  if (routePath.startsWith(BASE_PATH_NO_SLASH + '/')) {
    // ensure trailing slash is preserved if present; both should work
    return routePath;
  }
  if (routePath.startsWith(BASE_PATH)) return routePath;
  return null;
}

function collectRoutesFromNextData(nextData) {
  // Heuristic: in this site, navigation tree is under props.pageProps.navigationNodes
  const nodes = nextData?.props?.pageProps?.navigationNodes;
  if (!nodes) return [];

  const routes = new Set();
  const walk = (n) => {
    if (!n || typeof n !== 'object') return;
    // observed fields: url, path, href (varies)
    for (const k of ['url', 'path', 'href']) {
      const v = n[k];
      if (typeof v === 'string') {
        const norm = normalizeRoute(v);
        if (norm) routes.add(norm);
      }
    }
    for (const k of Object.keys(n)) {
      const v = n[k];
      if (Array.isArray(v)) v.forEach(walk);
      else if (v && typeof v === 'object') walk(v);
    }
  };
  if (Array.isArray(nodes)) nodes.forEach(walk);
  else walk(nodes);

  // Always include index
  routes.add(BASE_PATH);

  return [...routes].sort();
}

function collectInternalLinks(html) {
  const out = new Set();
  // href="/1.21.1/..." or href='/1.21.1/...'
  for (const m of html.matchAll(/href=("|')((?:\/1\.21\.1)(?:\/[^"]*)?)(?:[^"']*)\1/g)) {
    const href = m[2];
    const clean = href.split('#')[0].split('?')[0];
    const norm = normalizeRoute(clean);
    if (norm) out.add(norm);
  }
  // also include the base index
  out.add(BASE_PATH);
  return [...out];
}

function collectAssetUrls(html) {
  const out = new Set();
  // src/href with absolute site paths
  for (const m of html.matchAll(/\b(?:src|href)=("|')((?:\/_next\/static\/)[^"']+)\1/g)) {
    out.add(m[2]);
  }
  // favicons, manifest, etc
  for (const m of html.matchAll(/\b(?:href)=("|')((?:\/favicon[^"']*|\/site\.webmanifest|\/robots\.txt))\1/g)) {
    out.add(m[2]);
  }
  // guide-assets.* (optional)
  for (const m of html.matchAll(/\b(?:src|href)=("|')((?:\/guide-assets\.)[^"']+)\1/g)) {
    out.add(m[2]);
  }
  return [...out];
}

function urlToOutPath(u) {
  // u is site-absolute path like /_next/static/... or /favicon.ico
  const clean = u.replace(/^\//, '');
  return path.join(OUT_ROOT, clean);
}

function routeToOutFile(routePath) {
  // routePath is /1.21.1/... or /1.21.1/
  if (!routePath.startsWith(BASE_PATH)) throw new Error(`not under base path: ${routePath}`);
  const rel = routePath.slice(BASE_PATH.length); // '' or 'foo/bar'
  // Ensure trailing slash behavior: treat route as directory with index.html
  const dir = path.join(OUT_ROOT, rel);
  return path.join(dir, 'index.html');
}

function relativeFromPageToRoot(routePath) {
  // for /1.21.1/ => '.'
  // for /1.21.1/foo/ => '..'
  // for /1.21.1/foo/bar/ => '../..'
  const rel = routePath.slice(BASE_PATH.length).replace(/^\//, '').replace(/\/$/, '');
  if (!rel) return '.';
  const depth = rel.split('/').filter(Boolean).length;
  return Array(depth).fill('..').join('/') || '.';
}

function rewriteLinks(html, routePath) {
  const rootRel = relativeFromPageToRoot(routePath);
  const fromPageToMirrorRoot = rootRel === '.' ? '.' : rootRel;

  // 1) /_next/static/... -> <rel>/_next/static/...
  html = html.replaceAll('/_next/static/', `${fromPageToMirrorRoot}/_next/static/`);

  // 2) /favicon..., /site.webmanifest, /robots.txt, /guide-assets. -> <rel>/...
  // Only rewrite *site-relative* URLs (attribute values starting with '/'),
  // so we don't corrupt absolute URLs like https://guide-assets....
  html = html.replace(/(href|src)=("|')\/(favicon[^"']*)\2/g, (full, attr, q, rest) => {
    return `${attr}=${q}${fromPageToMirrorRoot}/${rest}${q}`;
  });
  html = html.replace(/(href|src)=("|')\/(site\.webmanifest|robots\.txt)\2/g, (full, attr, q, rest) => {
    return `${attr}=${q}${fromPageToMirrorRoot}/${rest}${q}`;
  });

  if (!HOTLINK_GUIDE_ASSETS) {
    html = html.replace(/(href|src)=("|')\/(guide-assets\.[^"']+)\2/g, (full, attr, q, rest) => {
      return `${attr}=${q}${fromPageToMirrorRoot}/${rest}${q}`;
    });
  }

  // 3) internal route links /1.21.1/... -> relative
  // Replace href="/1.21.1/..." and src="/1.21.1/..." (rare)
  html = html.replace(/(href|src)=("|')\/(1\.21\.1\/[^"'#?]+)([^"']*)\2/g, (full, attr, q, rest, tail) => {
    // rest begins with '1.21.1/...'
    const target = '/' + rest; // '/1.21.1/...'
    const relTarget = target.slice(BASE_PATH.length); // '...'
    const rel = relTarget ? `${fromPageToMirrorRoot}/${relTarget}` : `${fromPageToMirrorRoot}/`;
    return `${attr}=${q}${rel}${tail}${q}`;
  });

  return html;
}

// --- Translation (conservative) ---

const GLOSSARY = new Map([
  ['Getting Started', '入門'],
  ['Installation', '安裝'],
  ['Guide', '指南'],
  ['Recipes', '配方'],
  ['Items', '物品'],
  ['Blocks', '方塊'],
  ['Fluix', '福魯伊斯'],
  ['Controller', '控制器'],
  ['Energy', '能量'],
  ['Network', '網路'],
]);

function looksLikeIdToken(s) {
  // Avoid translating mod/item IDs and similar tokens.
  // Examples: ae2:controller, minecraft:iron_ingot, ae2:facade
  return /^[a-z0-9_]+:[a-z0-9_\/]+$/i.test(s);
}

function translateText(text) {
  // Minimal translator: glossary + passthrough.
  // Keeps whitespace-only untouched.
  if (!text || !text.trim()) return text;
  if (looksLikeIdToken(text.trim())) return text;

  // apply simple phrase replacements (case sensitive)
  let out = text;
  for (const [en, zh] of GLOSSARY.entries()) {
    out = out.split(en).join(zh);
  }
  return out;
}

function translateHtmlFragmentPreserveTags(html) {
  // Split into tags and text. Track <code>/<pre> blocks to skip translation.
  const parts = html.split(/(<[^>]+>)/g);
  let inCode = 0;

  const out = parts.map(p => {
    if (p.startsWith('<')) {
      const tag = p.toLowerCase();
      if (tag.startsWith('<code') || tag.startsWith('<pre')) inCode++;
      if (tag.startsWith('</code') || tag.startsWith('</pre')) inCode = Math.max(0, inCode - 1);
      return p;
    }
    if (inCode > 0) return p;

    // Translate text nodes, but avoid translating standalone id-tokens within a sentence.
    // Do a token-wise pass while keeping punctuation.
    return p.replace(/[A-Za-z0-9_]+:[A-Za-z0-9_\/]+|[^A-Za-z0-9_:]+|[A-Za-z][A-Za-z'\-]+/g, (tok) => {
      if (!tok) return tok;
      if (looksLikeIdToken(tok)) return tok;
      // Only attempt translation on alphabetic words / phrases; keep punctuation/whitespace
      if (/^[A-Za-z]/.test(tok)) return translateText(tok);
      return tok;
    });
  }).join('');

  return out;
}

function translateArticleOnly(html) {
  const m = html.match(/<article\b[\s\S]*?<\/article>/i);
  if (!m) return html;
  const articleHtml = m[0];
  const inner = articleHtml.replace(/^<article\b([^>]*)>/i, '').replace(/<\/article>$/i, '');
  const translatedInner = translateHtmlFragmentPreserveTags(inner);
  const rebuilt = articleHtml
    .replace(inner, translatedInner);
  return html.replace(articleHtml, rebuilt);
}

async function ensureDirForFile(filePath) {
  await mkdir(path.dirname(filePath), { recursive: true });
}

async function downloadAsset(sitePath) {
  if (HOTLINK_GUIDE_ASSETS && sitePath.startsWith('/guide-assets.')) return;

  const outPath = urlToOutPath(sitePath);
  if (await exists(outPath)) return;
  await ensureDirForFile(outPath);
  const url = `${BASE_ORIGIN}${sitePath}`;
  log('asset', url);
  const buf = await fetchBuffer(url);
  await writeFile(outPath, buf);
}

async function mirrorRoute(routePath) {
  const url = `${BASE_ORIGIN}${routePath}`;
  log('page', url);
  const html = await fetchText(url);

  const assets = collectAssetUrls(html);
  await Promise.all(assets.map(downloadAsset));

  let outHtml = html;
  outHtml = rewriteLinks(outHtml, routePath);
  outHtml = translateArticleOnly(outHtml);

  const outFile = routeToOutFile(routePath);
  await ensureDirForFile(outFile);
  await writeFile(outFile, outHtml, 'utf8');

  return { html, outFile };
}

async function main() {
  await mkdir(OUT_ROOT, { recursive: true });

  // Seed: fetch index
  const indexUrl = `${BASE_ORIGIN}${BASE_PATH}`;
  const indexHtml = await fetchText(indexUrl);
  const nextData = extractNextDataJson(indexHtml);
  const routes = collectRoutesFromNextData(nextData);

  // Always include internal links from index too
  const discovered = new Set(routes);
  for (const l of collectInternalLinks(indexHtml)) discovered.add(l);

  const ordered = [...discovered].sort();
  const toFetch = LIMIT > 0 ? ordered.slice(0, LIMIT) : ordered;

  console.log(`[ae2-guide] outRoot: ${OUT_ROOT}`);
  console.log(`[ae2-guide] routes discovered: ${ordered.length}; fetching: ${toFetch.length}${LIMIT > 0 ? ' (limited)' : ''}`);

  const fetched = [];
  for (const r of toFetch) {
    const { html } = await mirrorRoute(r);
    fetched.push({ route: r, html });

    // second-pass discovery from fetched pages (only within LIMIT budget if set)
    for (const l of collectInternalLinks(html)) discovered.add(l);
  }

  // If limited, stop here (prototype).
  if (LIMIT > 0) {
    console.log(`[ae2-guide] prototype done. Tip: re-run without --limit for full mirror.`);
    return;
  }

  // Full crawl: keep fetching until queue drains
  const done = new Set();
  const queue = [...discovered].sort();

  while (queue.length) {
    const r = queue.shift();
    if (!r || done.has(r)) continue;
    done.add(r);

    const { html } = await mirrorRoute(r);
    for (const l of collectInternalLinks(html)) {
      if (!discovered.has(l)) {
        discovered.add(l);
        queue.push(l);
      }
    }
  }

  console.log(`[ae2-guide] full mirror done. pages: ${done.size}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
