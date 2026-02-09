# All The Mons 繁體中文 (台灣) 轉換工具操作教學

本文件介紹如何使用專案中的 Python 腳本將簡體中文 (`zh_cn`) 內容轉換為繁體中文（台灣，`zh_tw`）。

## 1. 環境準備

在開始之前，請確保已安裝 Python 3.8+，並建立虛擬環境與安裝必要套件：

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows)
./venv/Scripts/activate

# 安裝 OpenCC (高品質簡轉繁套件)
pip install opencc-python-reimplemented
```

---

## 2. 工具說明與用法

### A. 資源包轉換 (`convert_zh_cn_to_zh_tw.py`)
用於處理 `.zip` 格式的 Minecraft 資源包。它會解壓縮 zip，將內部的 `zh_cn.json` 轉換為 `zh_tw.json`，然後重新封裝。

*   **用法**: `python convert_zh_cn_to_zh_tw.py <資源包路徑.zip>`
*   **範例**:
    ```bash
    python convert_zh_cn_to_zh_tw.py target/resourcepacks/1.21.1.zip
    python convert_zh_cn_to_zh_tw.py target/resourcepacks/All-the-Mons-0.10.0-beta-補漢材質包-1.21.1.zip
    ```

### B. 目錄內 JSON 轉換 (`convert_zh_cn_to_zh_tw_in_dir.py`)
遞迴搜尋指定目錄下所有的 `zh_cn.json` 檔案，並在同目錄下產生對應的 `zh_tw.json`。

*   **用法**: `python convert_zh_cn_to_zh_tw_in_dir.py <目錄路徑>`
*   **範例**:
    ```bash
    python convert_zh_cn_to_zh_tw_in_dir.py target/kubejs/assets/
    ```

### C. FTB Quests 專用轉換 (`convert_ftbquests_zh_cn_to_zh_tw.py`)
專門處理 FTB Quests 的 `.snbt` 格式語系檔。會轉換 `lang/zh_cn.snbt` 以及 `lang/zh_cn/` 目錄下的所有子檔案。

*   **用法**: `python convert_ftbquests_zh_cn_to_zh_tw.py <ftbquests目錄路徑>`
*   **範例**:
    ```bash
    python convert_ftbquests_zh_cn_to_zh_tw.py target/config/ftbquests
    ```

### D. 通用檔案轉換 (`convert_to_zh_tw_general.py`)
適用於普通 JSON、JS 或 TXT 檔案。它會直接修改原始檔案（原地替換），將檔案中所有雙引號或單引號內的簡體字轉換為繁體。

*   **用法**: `python convert_to_zh_tw_general.py <檔案或目錄路徑>`
*   **範例**:
    ```bash
    # 轉換 Mystical Customization 設定
    python convert_to_zh_tw_general.py target/config/mysticalcustomization
    # 轉換 KubeJS 腳本內容
    python convert_to_zh_tw_general.py target/kubejs
    ```

### E. LLM AI 翻譯 (`translate_en_to_zh_tw_llm.py`)
使用本地 LLM (如 LM Studio) 進行高品質的英翻中。這對於翻譯原始模組的英文語系檔非常有用。

*   **前置作業**:
    1. 開啟 **LM Studio** 並載入模型 (推薦 Llama-3-8B)。
    2. 啟動 **Local Server** (預設 `localhost:1234`)。
    3. 安裝 OpenAI 套件: `pip install openai`
*   **用法**: `python translate_en_to_zh_tw_llm.py <英文語系檔.json>`
*   **說明**: 該腳本會發送內容至本地 AI 並產生 `en_to_zh_tw.json`。

---

## 3. 注意事項
*   **OpenCC**: 必須安裝 `opencc-python-reimplemented` 才能獲得正確的台灣用語轉換（如 `内存` -> `記憶體`）。
*   **覆蓋**: 這些腳本通常會覆蓋已存在的 `zh_tw` 檔案，執行前請確保有備份。
*   **編碼**: 所有檔案均使用 `UTF-8` 編碼處理。
