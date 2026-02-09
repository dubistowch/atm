"""
Convert all zh_cn.json language files under assets/**/lang/ to zh_tw.json with Traditional Chinese (Taiwan) text.

Requirements:
- Python 3.8+
- Recommended: opencc-python-reimplemented (for high quality Simplified -> Traditional conversion)

Install OpenCC:
    pip install opencc-python-reimplemented

Usage (run from the top-level directory where the zip is located):
    python convert_zh_cn_to_zh_tw.py <resource_pack.zip>

This script will:
- Extract the given zip to a temporary directory.
- Convert all zh_cn.json under assets/**/lang/ to zh_tw.json.
- Re-pack the directory as <original_name>_zh_tw.zip next to the original zip.

Notes:
- Existing zh_tw.json files will be overwritten.
- Keys/structure are preserved; only string values are converted.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any
from zipfile import ZipFile, ZIP_DEFLATED


def get_converter():
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


def convert_obj(obj: Any, convert_str) -> Any:
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


def process_assets_root(root: Path) -> bool:
    """
    Process a single extracted resource pack directory.

    Args:
        root: Path to the resource pack root directory (the directory that contains 'assets').

    Returns:
        True if any zh_cn.json files were converted, False otherwise.
    """

    assets_root = root / "assets"
    if not assets_root.is_dir():
        print(f"錯誤：找不到 '{assets_root}' 資料夾，此目錄可能不是合法的資源包根目錄。")
        return False

    convert_str = get_converter()
    used_opencc = convert_str("測試") != "測試"

    zh_cn_files = sorted(assets_root.rglob("zh_cn.json"))
    if not zh_cn_files:
        print(f"提示：在 '{assets_root}' 底下沒有找到 zh_cn.json，略過。")
        return False

    total = 0
    for zh_cn_path in zh_cn_files:
        try:
            with zh_cn_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            print(f"[SKIP] Failed to read '{zh_cn_path}': {exc}")
            continue

        converted = convert_obj(data, convert_str)

        zh_tw_path = zh_cn_path.with_name("zh_tw.json")
        try:
            with zh_tw_path.open("w", encoding="utf-8") as f:
                json.dump(converted, f, ensure_ascii=False, indent=2)
            print(f"[OK] {zh_cn_path} -> {zh_tw_path}")
            total += 1
        except Exception as exc:
            print(f"[SKIP] Failed to write '{zh_tw_path}': {exc}")

    print()
    print(f"完成：共轉換 {total} 個 zh_cn.json 為 zh_tw.json。")
    if not used_opencc:
        print(
            "警告：未安裝 opencc-python-reimplemented，文字實際上未轉為繁體（台灣）。\n"
            "請先使用 'pip install opencc-python-reimplemented' 安裝後再執行，"
            "以取得正確的簡體 -> 繁體（台灣）轉換效果。"
        )

    return total > 0


def create_zip_from_directory(source_root: Path, output_zip: Path) -> None:
    """
    Create a zip archive from the given directory.

    Args:
        source_root: Directory to be zipped.
        output_zip: Output zip file path.
    """

    with ZipFile(output_zip, "w", ZIP_DEFLATED) as zf:
        for path in source_root.rglob("*"):
            if path.is_file():
                rel_path = path.relative_to(source_root)
                zf.write(path, rel_path.as_posix())


def main() -> None:
    # CLI: expect one argument, the path to the resource pack zip file.
    if len(sys.argv) != 2:
        print("用法：python convert_zh_cn_to_zh_tw.py <resource_pack.zip>")
        print("說明：此工具會解壓縮 zip -> 轉換 zh_cn.json -> 重新壓縮為 *_zh_tw.zip。")
        sys.exit(1)

    zip_path = Path(sys.argv[1]).resolve()

    if not zip_path.is_file():
        print(f"錯誤：找不到檔案 '{zip_path}'.")
        sys.exit(1)
    if zip_path.suffix.lower() != ".zip":
        print(f"錯誤：'{zip_path.name}' 不是 .zip 檔案。")
        sys.exit(1)

    # Create a temporary directory to extract the zip.
    temp_dir = Path(tempfile.mkdtemp(prefix="zh_tw_resource_pack_"))
    extracted_root = temp_dir

    print(f"解壓縮：{zip_path} -> {extracted_root}")
    try:
        with ZipFile(zip_path, "r") as zf:
            zf.extractall(extracted_root)
    except Exception as exc:
        print(f"錯誤：解壓縮 '{zip_path}' 失敗：{exc}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        sys.exit(1)

    try:
        converted = process_assets_root(extracted_root)
        if not converted:
            print("未進行任何轉換，將仍然建立 *_zh_tw.zip 以保留結構。")

        output_zip = zip_path.with_name(zip_path.stem + "_zh_tw.zip")
        print(f"重新壓縮為：{output_zip}")
        create_zip_from_directory(extracted_root, output_zip)
        print("完成：已建立轉換後的資源包 zip。")
    finally:
        # Always clean up temporary directory.
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
