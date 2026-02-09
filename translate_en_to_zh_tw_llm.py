import json
import os
import re
import sys
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Error: 'openai' library not found. Please install it using 'pip install openai'.")
    sys.exit(1)

# LM Studio 預設 API 設定
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

SYSTEM_PROMPT = """You are a professional Minecraft mod translator. 
Translate the following English text into Traditional Chinese (Taiwan, zh_tw).
Rules:
1. Use Taiwan localization terms (e.g., 'Optimization' -> '最佳化', 'Registry' -> '註冊', 'Inbound' -> '輸入').
2. Keep the original format, codes (like §c, %s), and symbols.
3. Only output the translated text. No explanations.
4. If it's a mod name or technical ID that shouldn't be translated, keep it as is.
"""

def translate_text(text: str) -> str:
    # 略過空字串或不含英文字母的字串
    if not text.strip() or not re.search('[a-zA-Z]', text):
        return text

    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def process_json(file_path: Path):
    print(f"Processing {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 遞迴處理 JSON
        def translate_recursive(obj, current_count=[0], total_count=0):
            if isinstance(obj, dict):
                return {k: translate_recursive(v, current_count, total_count) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [translate_recursive(i, current_count, total_count) for i in obj]
            elif isinstance(obj, str):
                current_count[0] += 1
                if total_count > 0:
                    print(f"[{current_count[0]}/{total_count}] Translating...", end='\r')
                return translate_text(obj)
            return obj

        # 先計算總量以便顯示進度
        def count_strings(obj):
            if isinstance(obj, dict): return sum(count_strings(v) for v in obj.values())
            if isinstance(obj, list): return sum(count_strings(i) for i in obj)
            if isinstance(obj, str): return 1
            return 0
        
        total = count_strings(data)
        translated_data = translate_recursive(data, total_count=total)
        print(f"\nTranslation finished ({total} strings).")
        
        # 另存為 zh_tw.json
        output_path = file_path.parent / "en_to_zh_tw.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)
        print(f"Saved to {output_path}")

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translate_en_to_zh_tw_llm.py <path_to_en_us.json>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    if path.is_file():
        process_json(path)
    else:
        print("Please provide a valid JSON file.")
