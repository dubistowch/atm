# FTB Chunks 玩家指南（宣告保護、強制載入、地圖與路標）

FTB Chunks 提供三大能力：
1) **宣告（Claim）區塊**：保護你的建築/資源不被其他玩家破壞
2) **強制載入（Chunk Loading / Force Load）**：讓區域在你離線時仍保持載入（是否允許取決於伺服器設定）
3) **小地圖 + 全螢幕地圖**：路標（Waypoints）、死亡點（Death points）

並且它會 **整合 FTB Teams**：隊伍/盟友會影響誰能在你的宣告區塊內建造與互動。

---

## 1) 如何打開「宣告/載入」用的區塊地圖？

官方指引：
- 打開背包（Inventory）後，點選 **藍色調的地圖圖示（blue tinted map icon）** → 進入區塊地圖（chunk map）
- 在區塊地圖左上角會看到 **藍色的 i 圖示**：點它可打開官方內建教學（in-game guide）

---

## 2) 宣告（Claim）與取消宣告（Unclaim）

### 2.1 宣告區塊
1. 打開區塊地圖
2. 在你要宣告的區塊上 **點一下** 就能宣告
3. 也可以 **按住滑鼠拖曳**，一次宣告多個區塊

### 2.2 取消宣告
1. 打開區塊地圖
2. 對已宣告的區塊 **右鍵** 取消宣告
3. 也可以 **右鍵拖曳**，一次取消多個區塊

---

## 3) 強制載入（Force Load）與取消載入

> 強制載入的操作方式幾乎與宣告相同，但使用 Shift 組合鍵。

### 3.1 強制載入區塊
1. 打開區塊地圖
2. 對目標區塊 **Shift + 點擊** 以載入
3. 也可以 **Shift + 拖曳** 一次載入多個區塊
4. 被強制載入的區塊會顯示 **綠色線條（green lines）** 作為辨識

### 3.2 取消載入
1. 打開區塊地圖
2. 對已載入的區塊 **Shift + 右鍵** 取消載入
3. 也可以 **Shift + 右鍵拖曳** 一次取消多個

---

## 4) 隊伍、盟友、以及「誰能在我家動手」

FTB Chunks 會整合 **FTB Teams**：
- 同隊玩家通常能在你宣告的區塊內存取/建造
- 你也可以把其他玩家/隊伍設為 **Allies（盟友）**

因此遇到「朋友不能互動/不能放置/不能破壞」時，最優先檢查：
1. 你們是否在同一個 FTB Team
2. 若不同隊，是否已設為 Ally
3. 隊伍對宣告區塊的互動/放置/破壞等權限是否被關閉（由 FTB Teams 控制）

---

## 5) 地圖與路標（Minimap / Fullscreen Map / Waypoints）

### 5.1 全螢幕地圖怎麼開？
官方文件提到全螢幕地圖「預設」可以用某個按鍵開啟；但不同整合包可能更改綁定。
請到 **Options → Controls** 搜尋：`FTB Chunks` / `map`，以你的實際綁定為準。

在全螢幕地圖中，點選地圖介面上的 **藍色 i 圖示**，可以看到鍵盤/滑鼠操作參考（官方提到有 keyboard/mouse reference）。

### 5.2 小地圖設定（gear icon）
在全螢幕地圖左下角點 **齒輪（gear icon）** 可以開啟設定 GUI，調整小地圖相關設定。

### 5.3 小地圖資訊列（Minimap Info Settings）
你可以調整小地圖下方顯示的額外資訊，例如：
- 當前生態域（biome）
- 座標（coordinates）
- 時間（time of day）
- FPS

### 5.4 建立路標（Waypoints）
官方流程：
1. 開啟全螢幕地圖
2. 在地圖上對你要的位置 **右鍵**
3. 點選 **Add Waypoint**
4. 設定名稱、顏色、維度與座標
5. 點 **Accept** 完成

### 5.5 死亡點（Death points）
死亡時會自動建立死亡點，用於標記你死亡位置，方便找回物品。

---

## 6) 指令（多為管理員用途）

FTB Chunks 的官方指令頁多為管理員工具（通常需要 OP）。例如：
- `/ftbchunks admin bypass_protection`
- `/ftbchunks admin claim_as <team name> ...`
- `/ftbchunks admin unclaim_everything`
- `/ftbchunks admin unload_everything`

> 玩家若想調整「可宣告/可載入上限」或遇到限制，通常要找管理員處理。

---

## 7) 設定檔（Config）位置與如何編輯

官方文件重點：
- client/server 設定檔位置：
  - `<instance>/config/ftbchunks-client.snbt`
  - `<instance>/config/ftbchunks-server.snbt`
- 整合包更新可能覆蓋：可以用 local / world serverconfig 的「覆寫檔」保存調整
- 在全螢幕地圖中：
  - 左下角齒輪（client config）
  - 右下角紫色齒輪（server config）

---

## 8) 常見情境與排查

### 情境 A：同居了，但朋友不能用機器/開門
按順序排查：
1. 是否同隊或 Ally
2. 檢查 FTB Teams 對你宣告區塊的互動/放置/破壞等權限設定

### 情境 B：我可以宣告，但不能強制載入
可能是伺服器針對「宣告數量」與「可載入數量」分開限制；需要管理員調整額度。

### 情境 C：找不到宣告/載入教學
回到區塊地圖左上角 **藍色 i**，官方內建教學在那裡。

---

## Sources（官方文件）
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/>
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/claiming-loading/>
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/maps-waypoints/>
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/commands/>
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/config/>
