# Mekanism 新手教學與玩法筆記

## 先看這裡（前 30 分鐘）
**目標：讓第一條「粉碎 → 富集 → 熔煉」跑起來，並學會側面設定。**

1) 用 JEI/REI 找到並做出（名稱依版本可能略不同）：
- **熱力發電機 / 風力機 / 生物發電機**（任一穩定電力來源）
- **Energy Cube**（能量緩衝，先做 Basic）
- **Crusher（粉碎機）** + **Enrichment Chamber（富集室）**

2) 先做一個「測試台」：電力來源 → Energy Cube → 兩台機器 → 箱子。

3) 每台機器都先確認三件事（最常卡）：
- **Side Config（側面輸入/輸出）**：哪一面吃料？哪一面吐料？
- **Auto-Eject / Eject（自動輸出）**：有沒有開？
- **Redstone Control（紅石控制）**：是不是被設成需要紅石訊號才動？

> Mekanism 真的「學會一台」就會一路通；先做小測試台，比一次鋪十台再除錯快非常多。

---

## 這模組到底強在哪
- **礦物處理倍化**：常見從 2 倍開始，後面可走更高階化學鏈（依版本/整合包設定）。
- **Factory（工廠化）**：同類機器可升級成多工版本，一台同時處理多組輸入，省空間也好佈線。
- **完整傳輸系統**：物品/流體/氣體/能量都有對應管線（不同版本命名略異）。
- **側面配置是靈魂**：所有機器都能把每一面設定成輸入/輸出/禁用，物流乾淨到像在寫電路圖。
- **中後期省時間神器**：Digital Miner、QIO（依版本/整合包是否有啟用）。

---

## 核心觀念（學這幾個就夠你玩到中後期）
### 1) Side Config：先看顏色/圖示，再接管線
- **輸入/輸出不是「猜」**：每一面都能被指定功能。
- 建議習慣：
  - 物品輸入固定走同一側（例如左）
  - 物品輸出固定走另一側（例如右）
  - 能量永遠從背面接

### 2) Eject / Auto Output：機器不會自己把東西丟出去（除非你叫它丟）
- 你用管線接了，但機器沒吐：先找 **Eject**。
- 有些機器也有「拉取」選項（不同版本/管線）：**推（Eject）**跟**拉（Pull）**至少要成立一個。

### 3) Redstone Control：九成「機器不動」都在這裡
- 設成 **Ignored**（忽略紅石）最不會誤踩坑。

### 4) 升級（Upgrades）優先順序（新手常用）
- **Energy**（省電）→ **Speed**（加速）→ **Muffling**（降噪，若你受不了聲音）
- 高速前，先確保供電穩：不然就是一直閃、效率反而差。

---

## 進度清單（照做不容易走歪）
- [ ] 找到或取得 **Osmium（滲鋨）**（多數配方核心資源）
- [ ] 第一套電力（任一發電）+ **Basic Energy Cube**
- [ ] **Crusher** + **Enrichment Chamber**：做出穩定的 2x 礦處理
- [ ] 先把「鐵、銅、金」固定導入同一條處理線（養成產線思維）
- [ ] 做出基礎管線並理解差異：
  - [ ] 物品傳輸（Item）
  - [ ] 能量傳輸（Energy）
  - [ ] 流體傳輸（Fluid）
  - [ ] 氣體/化學品傳輸（Gas/Chemical）
- [ ] 開始用 **Factory** 取代多台同類機器（省空間 + 好維護）
- [ ] 需要特定稀有資源時再上 **Digital Miner**（避免早期過度投資）
- [ ]（有 QIO 的包）建置 QIO 倉儲/物流，收斂全基地材料流

---

## 常見問題（先看這區再問）
### Q1：機器有電、有材料，但就是不加工
- 檢查 **Redstone Control** 是否要求紅石訊號
- 檢查輸入那一面是否在 **Side Config** 被設成「輸入」
- 檢查配方是否需要「氣體/流體/額外材料」（尤其是進階倍化）

### Q2：我接了管線但東西不走/不吐
- 先確認 **Eject/Auto Output**
- 管線本身可能有：
  - **Pull（拉取）**模式沒開
  - **優先度/Priority** 被別路搶走
  - **顏色/頻道** 不一致（有些版本有）

### Q3：產線很快就塞住（輸出滿了/副產物卡住）
- 做「**副產物專用出口**」：例如額外的箱子或垃圾桶（視整合包）
- 把輸出分流：主產物回倉庫、副產物進加工或暫存

### Q4：耗電暴增、機器忽快忽慢
- 先上 **Energy Upgrade** 或增加發電/能量緩衝
- 供電不穩時上 Speed 只會更痛苦

---

## 值得先做的代表性方塊/系統（用 JEI/REI 搜尋最快）
- Enrichment Chamber（富集室）
- Crusher（粉碎機）
- Metallurgic Infuser（金屬注入器，許多零件會用到）
- Energy Cube（能量方塊）
- 各類 Transmitter（物品/能量/流體/氣體）
- Factory（機器工廠化升級）
- Digital Miner（數位採礦機）

![Mekanism Digital Miner 主介面示意（官方 wiki 圖）](https://wiki.aidancbrady.com/w/images/aidancbrady/9/92/DGGUI1.png)

*圖：Digital Miner 的主介面（來源：官方 wiki）。重點是設定掃描範圍/篩選條件與 Start/Stop；把它接進物流時一樣要留意 Auto-Eject/輸出端。*

---

## 相關連結（優先看官方）
- 官方 Wiki（總覽）：<https://wiki.aidancbrady.com/wiki/Mekanism>
- 官方 Wiki：Digital Miner：<https://wiki.aidancbrady.com/wiki/Digital_Miner>
- Modrinth：<https://modrinth.com/mod/mekanism>
- GitHub：<https://github.com/mekanism/Mekanism>

## 任務書對應（FTB Quests）

任務書章節：`mekanism`（建議在任務書搜尋此章節名或關鍵字）

本章常見任務節點（節錄）：
- 消音 升級模組
- 碎片,到礦簇,到礦粉,到錠
- 機器升級
- 辭典
- 終極級
- 熱力發電機
- 紅黃綠青 與顏料
- 粉碎 植物 以獲得 生物燃料
- 富集倉
- 等級 安裝器

> 來源：`minecraft/config/ftbquests/quests/lang/zh_tw/chapters/`

## 資料來源
- <https://wiki.aidancbrady.com/wiki/Mekanism>
- <https://wiki.aidancbrady.com/wiki/Digital_Miner>
- <https://wiki.aidancbrady.com/w/images/aidancbrady/9/92/DGGUI1.png>
- <https://modrinth.com/mod/mekanism>
