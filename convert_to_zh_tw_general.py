"""
General purpose script to convert Simplified Chinese to Traditional Chinese (Taiwan)
in text files (JSON, JS, SNBT, etc.).

Requirements:
    pip install opencc-python-reimplemented

Usage:
    python convert_to_zh_tw_general.py "<path_to_directory_or_file>"
"""

import re
import sys
from pathlib import Path
from typing import Callable

def get_converter() -> Callable[[str], str]:
    try:
        from opencc import OpenCC
        cc = OpenCC("s2twp")  # Simplified Chinese to Traditional Chinese (Taiwan)
        return cc.convert
    except ImportError:
        print("Warning: opencc-python-reimplemented not installed. No conversion will occur.")
        return lambda x: x

# Regex to match double-quoted string literals: " ... "
DOUBLE_QUOTE_RE = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')
# Regex to match single-quoted string literals: ' ... '
SINGLE_QUOTE_RE = re.compile(r"'([^'\\]*(?:\\.[^'\\]*)*)'")

def convert_text(text: str, converter: Callable[[str], str]) -> str:
    def replace_double(match: re.Match[str]) -> str:
        return f'"{converter(match.group(1))}"'
    
    def replace_single(match: re.Match[str]) -> str:
        return f"'{converter(match.group(1))}'"

    text = DOUBLE_QUOTE_RE.sub(replace_double, text)
    text = SINGLE_QUOTE_RE.sub(replace_single, text)
    return text

def process_file(file_path: Path, converter: Callable[[str], str]):
    if file_path.suffix not in ['.json', '.js', '.snbt', '.txt']:
        return

    try:
        content = file_path.read_text(encoding="utf-8")
        converted = convert_text(content, converter)
        if content != converted:
            file_path.write_text(converted, encoding="utf-8")
            print(f"[CONVERTED] {file_path}")
        else:
            # print(f"[SKIP] No changes in {file_path}")
            pass
    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_zh_tw_general.py <path>")
        sys.exit(1)

    path = Path(sys.argv[1]).resolve()
    converter = get_converter()

    if path.is_file():
        process_file(path, converter)
    elif path.is_dir():
        for f in path.rglob("*"):
            if f.is_file():
                process_file(f, converter)
    else:
        print(f"Error: {path} not found.")

if __name__ == "__main__":
    main()
