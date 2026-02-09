# Waystones 教學與玩法筆記

## 簡介（這個模組在整合包的角色）
Waystones 提供可互相傳送的「傳送石碑」玩法：玩家啟動過的 Waystone 會被記錄，之後可以透過**傳送卷軸**、可充能的**傳送石**，或直接在 Waystone 之間跳轉。它常被整合包用來取代伺服器指令 `/home`、`/warp` 的便利性，讓生存模式也能有「合理的快速移動」。

## 模組特色（條列，含 5-10 點）
- 新增 Waystone 方塊：啟動後即可作為傳送目的地。
- 可透過物品（例如 Warp Scroll、Warp Stone）或 Waystone 本體進行傳送。
- 支援「全服共用」的全球 Waystone（適合公共樞紐/主城）。
- 可選用背包/介面按鈕：在背包介面中呼叫傳送（可設定是否啟用）。
- 村莊可能生成 Waystone 結構（依整合包與世界生成設定）。
- 跨載入器：文件指出支援 NeoForge、Fabric、Forge，並需要 Balm 作為前置。

## 按鍵操作
Waystones 的互動多半在介面中完成；若整合包啟用了「背包介面傳送按鈕」，也可能提供對應按鍵或按鈕位置調整。

- 請到：**選項 → 控制**
- 搜尋：`Waystones`、`Warp`
- 若沒有看到相關鍵位，代表該版本主要以 GUI/按鈕操作為主。

## 如何設定（含常見設定檔位置/遊戲內設定入口）
- 常見設定檔位置（依版本可能不同）：
  - `config/waystones/` 或 `config/waystones-*.toml`
  - `config/balm-*.toml`（因為 Waystones 依賴 Balm，部分共用設定可能在 Balm）
- 遊戲內設定入口：
  - 可能在 **Mods** 清單中找到 Waystones 設定（若版本支援）。
- 常見可調方向（以實際版本為準）：
  - 傳送成本（經驗/道具/冷卻）、是否允許跨維度、全球 Waystone 行為、背包按鈕顯示等。

## 如何獲得模組道具（生存模式取得路線：合成、掉落、交易、探索；舉 3-6 個代表性物品）
Waystones 的代表性內容多以合成與探索取得：
- **Waystone（傳送石碑）**：可合成（多數整合包）或在村莊結構中找到（依世界生成）。
- **Warp Scroll（傳送卷軸）**：消耗型，常用於回到已啟動的 Waystone。
- **Warp Stone（傳送石）**：可充能/可重複使用的傳送道具（依版本設定）。
- **Return Scroll（回程卷軸）**：回到綁定點/最近使用點（依版本/整合包）。
- **Warp Plate（傳送板）**：可放置的傳送裝置（依版本/整合包）。

> 具體配方、是否需要經驗、冷卻時間等通常由整合包平衡決定，請以 JEI/REI 與設定檔為準。

## 好玩的點在哪（給玩家的玩法建議與小技巧）
- 每到新地點先啟動 Waystone：探索節奏會變得很流暢，死亡回收也更有效率。
- 主城/公共點用「全球 Waystone」：多人遊玩時能顯著降低集合成本（但也要注意伺服器規範）。
- 搭配 JourneyMap 路標：地圖上標好 Waystone 名稱與用途，回傳不迷路。
- 風險控管：若整合包有傳送成本，建議常備卷軸或準備經驗來源，避免卡在野外。

## 相關連結（至少 3 個）
- Modrinth（介紹/需求 Balm）：https://modrinth.com/mod/waystones
- Balm（前置）：https://modrinth.com/mod/balm
- Twelve Iterations Mods（作者/贊助頁，Modrinth 描述中提及）：https://mods.twelveiterations.com/sponsor

## 圖片
- Modrinth 發佈頁通常會有展示圖與說明，適合引用：https://modrinth.com/mod/waystones
