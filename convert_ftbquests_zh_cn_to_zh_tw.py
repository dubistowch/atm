"""
Convert FTB Quests zh_cn language files under a given ftbquests config directory
to zh_tw (Traditional Chinese, Taiwan).

Requirements:
- Python 3.8+
- Recommended: opencc-python-reimplemented (for high quality Simplified -> Traditional conversion)

Install OpenCC:
    pip install opencc-python-reimplemented

Usage:
    python convert_ftbquests_zh_cn_to_zh_tw.py "<path_to_ftbquests_dir>"

Example:
    python convert_ftbquests_zh_cn_to_zh_tw.py "minecraft/config/ftbquests"

This script will:
- Assume the given directory is the FTB Quests config directory (contains 'quests/').
- Work inside 'quests/lang':
    - Convert 'zh_cn.snbt' to 'zh_tw.snbt'.
    - Convert all files under 'lang/zh_cn/' to a mirrored structure under 'lang/zh_tw/'.

Notes:
- Existing zh_tw files will be overwritten.
- Only string literals (text inside double quotes) are converted; structure and keys are preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Callable


def get_converter() -> Callable[[str], str]:
    """
    Try to create an OpenCC converter.

    Returns:
        A callable(str) -> str that converts Simplified Chinese to Traditional Chinese (Taiwan),
        or an identity function if OpenCC is not available.
    """

    try:
        from opencc import OpenCC  # type: ignore[import]

        cc = OpenCC("s2twp")  # Simplified Chinese to Traditional Chinese (Taiwan)

        def _convert(text: str) -> str:
            return cc.convert(text)

        return _convert
    except Exception:
        # Fallback: no-op converter. User should install opencc-python-reimplemented.
        def _identity(text: str) -> str:
            return text

        return _identity


# Regex to match SNBT string literals: " ... ", with backslash escapes supported.
STRING_LITERAL_RE = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')


def convert_snbt_text(text: str, convert_str: Callable[[str], str]) -> str:
    """
    Convert all string literals in an SNBT text using the given converter.

    Args:
        text: Full SNBT file content as text.
        convert_str: Callable that converts a string to another string.

    Returns:
        Converted text with the same structure and escaping.
    """

    def _replace(match: re.Match[str]) -> str:
        inner = match.group(1)
        converted = convert_str(inner)
        return f'"{converted}"'

    return STRING_LITERAL_RE.sub(_replace, text)


def convert_snbt_file(src: Path, dst: Path, convert_str: Callable[[str], str]) -> bool:
    """
    Convert a single SNBT file from Simplified to Traditional Chinese (Taiwan).

    Args:
        src: Source SNBT file path.
        dst: Destination SNBT file path.
        convert_str: Callable that converts a string to another string.

    Returns:
        True if conversion succeeded, False otherwise.
    """

    try:
        text = src.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"[SKIP] 讀取失敗 '{src}': {exc}")
        return False

    converted = convert_snbt_text(text, convert_str)

    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(converted, encoding="utf-8")
        print(f"[OK] {src} -> {dst}")
        return True
    except Exception as exc:
        print(f"[SKIP] 寫入失敗 '{dst}': {exc}")
        return False


def process_ftbquests_dir(ftbquests_root: Path) -> None:
    """
    Process the FTB Quests config directory.

    Args:
        ftbquests_root: Path to 'minecraft/config/ftbquests'.
    """

    if not ftbquests_root.is_dir():
        print(f"錯誤：'{ftbquests_root}' 不是目錄或不存在。")
        return

    quests_dir = ftbquests_root / "quests"
    if not quests_dir.is_dir():
        print(f"錯誤：'{ftbquests_root}' 底下找不到 'quests' 資料夾，這可能不是正確的 FTB Quests 設定目錄。")
        return

    lang_dir = quests_dir / "lang"
    if not lang_dir.is_dir():
        print(f"錯誤：'{quests_dir}' 底下找不到 'lang' 資料夾。")
        return

    convert_str = get_converter()
    used_opencc = convert_str("測試") != "測試"

    total = 0

    # 1) Convert root-level zh_cn.snbt -> zh_tw.snbt
    zh_cn_root_file = lang_dir / "zh_cn.snbt"
    if zh_cn_root_file.is_file():
        zh_tw_root_file = lang_dir / "zh_tw.snbt"
        if convert_snbt_file(zh_cn_root_file, zh_tw_root_file, convert_str):
            total += 1
    else:
        print(f"提示：未找到 '{zh_cn_root_file}'，略過。")

    # 2) Convert all files under lang/zh_cn/ -> lang/zh_tw/
    zh_cn_dir = lang_dir / "zh_cn"
    if zh_cn_dir.is_dir():
        zh_tw_dir = lang_dir / "zh_tw"
        for src in sorted(zh_cn_dir.rglob("*.snbt")):
            rel = src.relative_to(zh_cn_dir)
            dst = zh_tw_dir / rel
            if convert_snbt_file(src, dst, convert_str):
                total += 1
    else:
        print(f"提示：未找到 '{zh_cn_dir}' 資料夾，略過子檔案。")

    print()
    print(f"完成：共轉換 {total} 個 zh_cn SNBT 檔案為 zh_tw。")
    if not used_opencc:
        print(
            "警告：未安裝 opencc-python-reimplemented，文字實際上未轉為繁體（台灣）。\n"
            "請先使用 'pip install opencc-python-reimplemented' 安裝後再執行，"
            "以取得正確的簡體 -> 繁體（台灣）轉換效果。"
        )


def main() -> None:
    # CLI: expect one argument, the path to the ftbquests config directory.
    if len(sys.argv) != 2:
        print("用法：python convert_ftbquests_zh_cn_to_zh_tw.py <path_to_ftbquests_dir>")
        print("範例：python convert_ftbquests_zh_cn_to_zh_tw.py \"minecraft/config/ftbquests\"")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    process_ftbquests_dir(root)


if __name__ == "__main__":
    main()
