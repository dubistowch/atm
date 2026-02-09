"""
Convert all zh_cn.json language files under a given directory to zh_tw.json
with Traditional Chinese (Taiwan) text.

Requirements:
- Python 3.8+
- Recommended: opencc-python-reimplemented (for high quality Simplified -> Traditional conversion)

Install OpenCC:
    pip install opencc-python-reimplemented

Usage:
    python convert_zh_cn_to_zh_tw_in_dir.py <root_directory>

This script will:
- Recursively search for all zh_cn.json files under <root_directory>.
- Convert all string values in those files from Simplified Chinese to Traditional Chinese (Taiwan).
- Write the converted content to sibling zh_tw.json files (same directory, same keys/structure).

Notes:
- Existing zh_tw.json files will be overwritten if they exist.
- Keys/structure are preserved; only string values are converted.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable


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


def convert_obj(obj: Any, convert_str: Callable[[str], str]) -> Any:
    """
    Recursively convert all string values in a JSON-compatible object.

    Args:
        obj: JSON-compatible object.
        convert_str: Callable that converts a string to another string.

    Returns:
        Converted object with the same structure.
    """

    if isinstance(obj, str):
        return convert_str(obj)
    if isinstance(obj, list):
        return [convert_obj(item, convert_str) for item in obj]
    if isinstance(obj, dict):
        return {key: convert_obj(value, convert_str) for key, value in obj.items()}
    return obj


def process_directory(root: Path) -> None:
    """
    Process all zh_cn.json files under the given root directory.

    Args:
        root: Root directory to search under.
    """

    if not root.is_dir():
        print(f"錯誤：'{root}' 不是目錄或不存在。")
        return

    convert_str = get_converter()
    used_opencc = convert_str("測試") != "測試"

    zh_cn_files = sorted(root.rglob("zh_cn.json"))
    if not zh_cn_files:
        print(f"提示：在 '{root}' 底下沒有找到任何 zh_cn.json 檔案。")
        return

    total = 0
    for zh_cn_path in zh_cn_files:
        try:
            with zh_cn_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            print(f"[SKIP] 讀取失敗 '{zh_cn_path}': {exc}")
            continue

        converted = convert_obj(data, convert_str)

        zh_tw_path = zh_cn_path.with_name("zh_tw.json")
        try:
            with zh_tw_path.open("w", encoding="utf-8") as f:
                json.dump(converted, f, ensure_ascii=False, indent=2)
            print(f"[OK] {zh_cn_path} -> {zh_tw_path}")
            total += 1
        except Exception as exc:
            print(f"[SKIP] 寫入失敗 '{zh_tw_path}': {exc}")

    print()
    print(f"完成：共轉換 {total} 個 zh_cn.json 為 zh_tw.json。")
    if not used_opencc:
        print(
            "警告：未安裝 opencc-python-reimplemented，文字實際上未轉為繁體（台灣）。\n"
            "請先使用 'pip install opencc-python-reimplemented' 安裝後再執行，"
            "以取得正確的簡體 -> 繁體（台灣）轉換效果。"
        )


def main() -> None:
    # CLI: expect one argument, the path to the root directory.
    if len(sys.argv) != 2:
        print("用法：python convert_zh_cn_to_zh_tw_in_dir.py <root_directory>")
        print("說明：遞迴搜尋目錄中所有 zh_cn.json，產生對應的 zh_tw.json。")
        sys.exit(1)

    root = Path(sys.argv[1]).resolve()
    process_directory(root)


if __name__ == "__main__":
    main()
