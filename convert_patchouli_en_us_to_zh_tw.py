"""
Script to duplicate 'en_us' directories to 'zh_tw' within Patchouli books
and convert Simplified Chinese content to Traditional Chinese (Taiwan).

This is useful for resource packs that put translations directly in 'en_us'
to force a language, but we want to provide a proper 'zh_tw' alternative.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import Callable

def get_converter() -> Callable[[str], str]:
    try:
        from opencc import OpenCC
        cc = OpenCC("s2twp")
        return cc.convert
    except ImportError:
        print("Warning: opencc-python-reimplemented not installed. Using identity converter.")
        return lambda x: x

def convert_file_content(file_path: Path, converter: Callable[[str], str]):
    if file_path.suffix not in ['.json', '.txt', '.snbt']:
        return
    
    try:
        content = file_path.read_text(encoding="utf-8")
        # We want to convert all text, but mostly it's JSON values.
        # For simplicity and since these are translation files, we convert the whole block.
        # But to be safer with keys, we could use the general converter logic.
        # However, for Patchouli books, almost everything is display text.
        
        # Using a simple regex-based replacement for JSON values to avoid breaking keys if possible,
        # but in many Patchouli files, keys are also descriptive.
        # Let's use the logic from convert_to_zh_tw_general.py
        import re
        DOUBLE_QUOTE_RE = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')
        SINGLE_QUOTE_RE = re.compile(r"'([^'\\]*(?:\\.[^'\\]*)*)'")
        
        def replace_double(match):
            return f'"{converter(match.group(1))}"'
        def replace_single(match):
            return f"'{converter(match.group(1))}'"
            
        converted = DOUBLE_QUOTE_RE.sub(replace_double, content)
        converted = SINGLE_QUOTE_RE.sub(replace_single, converted)
        
        if content != converted:
            file_path.write_text(converted, encoding="utf-8")
            # print(f"  [CONVERTED] {file_path.name}")
    except Exception as e:
        print(f"  [ERROR] Failed to convert {file_path}: {e}")

def process_resource_pack(root_path: Path):
    converter = get_converter()
    
    # 1. Find all en_us directories
    en_us_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        if "en_us" in dirnames:
            en_us_dirs.append(Path(dirpath) / "en_us")
            
    if not en_us_dirs:
        print("No 'en_us' directories found.")
        return

    for en_us_path in en_us_dirs:
        zh_tw_path = en_us_path.parent / "zh_tw"
        print(f"Processing: {en_us_path} -> {zh_tw_path}")
        
        # 2. Copy en_us to zh_tw (overwriting if exists)
        if zh_tw_path.exists():
            shutil.rmtree(zh_tw_path)
        shutil.copytree(en_us_path, zh_tw_path)
        
        # 3. Convert all files in zh_tw
        for f in zh_tw_path.rglob("*"):
            if f.is_file():
                convert_file_content(f, converter)

    print("\nSuccessfully added zh_tw to all Patchouli books.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_patchouli_en_us_to_zh_tw.py <resource_pack_directory>")
        sys.exit(1)
        
    target_dir = Path(sys.argv[1]).resolve()
    if not target_dir.is_dir():
        print(f"Error: {target_dir} is not a directory.")
        sys.exit(1)
        
    process_resource_pack(target_dir)
