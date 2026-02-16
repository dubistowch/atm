# Applied Energistics 2（AE2）｜玩家向新手上路（A）

## 30 秒看懂
AE2 是把「收納 + 搜尋 + 自動合成」做成一套 **ME 網路** 的模組：你把物品塞進系統後，就像開一個超強搜尋欄——要什麼打字拿什麼；常用材料甚至可以「下單」讓它自己合成。只要你玩到中期開始量產零件，AE2 幾乎等於把整個整合包的體驗提升一個檔次。

> 這篇以「你要怎麼做出第一套能用的 ME 倉庫」為主。名稱/配方/鍵位可能因版本與整合包不同：**一律以 JEI/REI + 你遊戲內 Controls 為準**。

---

## 開始前：先用 Controls 搜尋，確定有沒有額外終端/無線鍵位
1. `ESC` → **選項** → **控制設定 (Controls)**
2. 搜尋：`Applied Energistics`、`AE2`、`ME`、`Terminal`

AE2 本體多數操作都在 GUI 裡完成，通常不需要背一堆快捷鍵；但整合包若有「無線終端」或附加模組，可能會多一些快捷鍵，先確認最省事。

---

## 從 JEI/REI 開始：你要做的「第一套可用倉庫」清單
打開 JEI/REI，先把下面這幾個物品的配方點一輪，搞清楚你缺的是哪條材料線：

- **ME Drive（磁碟機）**：放 Storage Cell 用
- **Storage Cell（儲存元件）**：真正裝物品的「硬碟」
- **ME Terminal / ME Crafting Terminal（終端 / 合成終端）**：你用來搜尋、取放物品的介面
- **Energy Acceptor（能量接收器）**（或整合包提供的等價供電方式）
- **Cables（線材）**：把上面全部連成網路

玩家向建議：
- 先做 **ME Crafting Terminal**（合成終端）會更舒服；它能用網路裡的材料自動補格子。

---

## 走最穩的路線：第一套 ME 系統怎麼擺（不含自動合成）
依官方 Players Guide 的 Getting Started 建議，最基本 ME 系統就是「供電 + 線 + Drive + Terminal」：

1) 先把 **Energy Acceptor** 接上你現有的能源（看整合包用什麼電）
2) 用 **ME Cable** 把能量接收器連到：
   - **ME Drive**（裝 Storage Cell）
   - **ME Terminal / Crafting Terminal**（你要操作的介面）
3) 把 **Storage Cell** 插進 **ME Drive**
4) 打開終端，丟幾組常用材料進去測試（圓石、木材、鐵、紅石之類）

如果你打開終端「什麼都看不到 / 顯示離線」：先直接跳到下面的「常見踩雷」。

---

## 任務書照做：AE2 章節最常考的幾個「一定要會」重點

整合包的 FTB Quests（應用能源 2 章）其實把 AE2 的核心概念拆得很清楚。你可以把它當成「讀書會重點整理」，照著做會快很多。

### 1) 先做出第一個「儲存單元」
任務書提醒：每個儲存單元容量由你放進去的「儲存元件」決定（例如 1k 元件）。

- 任務章節：**製作你的首個儲存單元**

### 2) 終端（Terminal）＝你跟 ME 網路溝通的入口
任務書把「終端」講得很直白：
- ME 終端：用統一網格介面存取網路物品
- ME 合成終端：多一個合成格，能直接用網路材料合成

- 任務章節：**終端系統**

### 3) 自動合成一定會用到「樣板」
任務書重點：
- 樣板要用 **樣板編碼終端**編碼
- 樣板可以是「普通合成」也可以是「處理配方」（把材料送進其他機器）

- 任務章節：**樣板**

### 4) 無線終端：先「綁定」到無線訪問點
任務書重點：
- 無線終端要先放進 **無線訪問點** 的插槽綁定
- 超出範圍或沒電就不能用
- 能量卡可升級內部電池容量（實際以你包內物品為準）

- 任務章節：**無線終端**

### 5) P2P（點對點）是 AE2 的黑科技：不用中繼儲存也能傳
任務書重點：
- P2P 可以傳物品/流體/能量/紅石（依你調諧的種類）
- 常需要用記憶體卡把兩端連起來

- 任務章節：**P2P通道**

> 以上文字重點來自：`ftbquests/quests/lang/zh_tw/chapters/applied_energistics_2.snbt`

---

## 終端機（Terminal）你一定會用到的 UI/操作
官方 Guide 的 Terminals 章節有幾個超實用的點，熟了體感差很多：

### 你最常用的滑鼠/按鍵習慣
- **左鍵**拿一整疊、**右鍵**拿半疊（終端列表裡點物品）
- **按住 Shift** 可以「凍結列表」：東西進出庫時，列表不會一直跳來跳去（很救命）
- 如果某物品可自動合成：
  - 你綁定的 **Pick Block（通常是滑鼠中鍵）** 會跳出下單介面，可輸入數量

### 終端常見按鈕在哪
- 左側：排序/篩選（依名稱、模組、數量；看「已儲存/可合成」等）
- 右側：通常有 View Cell 等插槽（用來過濾顯示）
- 右上角（官方提到的「槌子」圖示）：常用來開自動合成狀態/CPU 狀態（版本介面可能略不同）

### 放置終端時最容易做錯的一件事
官方 Guide 特別提醒：**終端是線材的「子零件」**，有正反面。
- 放反時你會看到「終端在那，但根本沒連上網路」的尷尬狀況。
- 你如果怎麼接線都不通，第一個就先懷疑：**終端是不是放反了**。

---

## 常見踩雷（AE2 最常見的「看起來壞了」其實都在這）
- **終端放反 / 沒接到同一條網路**：看起來像有擺好，其實沒連上。
- **供電不足**：網路會離線或部分機器不工作；先確認能量接收器真的有吃到電。
- **Storage Cell 不是放在 Drive/ME Chest**：你有做出硬碟，但沒插進去，當然什麼都存不了。
- **儲存元件不是「容量」問題，而是「類型數」也會滿**：你如果丟進去一堆雜物，可能很快就「還有空間但放不進去」。
- **Shift 點合成終端輸出要小心**：官方在 Crafting Terminal 也提醒過，Shift-Click 可能讓你一次做太多或把材料吃光。

---

## 下一步你可以做什麼（想更強再看）
- **自動合成（Autocrafting）**：樣板（Pattern）+ 組裝（Assembler）+ Crafting CPU，讓「下單就做」成為日常。
- **更完整的終端配置**：Pattern Encoding Terminal（編樣板）、Pattern Access Terminal（遠端管理 Provider 的樣板）。

---

## 資料來源（官方/權威）
- AE2 官方網站：<https://appliedenergistics.org/>
- AE2 官方 Players Guide（1.20.1 版索引）：<https://guide.appliedenergistics.org/1.20.1/index>
- Players Guide｜Getting Started：<https://guide.appliedenergistics.org/1.20.1/getting-started>
- Players Guide｜Terminals：<https://guide.appliedenergistics.org/1.20.1/items-blocks-machines/terminals>
- Modrinth（AE2）：<https://modrinth.com/mod/ae2>
- GitHub（Applied Energistics 2）：<https://github.com/AppliedEnergistics/Applied-Energistics-2>
