# Industrial Foregoing 新手教學與玩法筆記

## 簡介
Industrial Foregoing（IF）是一個很「工具箱」的自動化模組：你缺木材、缺作物、缺皮革、缺經驗、缺某種流體……它幾乎都能用對應機器把流程自動化。

在整合包裡它通常是中期主力：機器直覺、用 FE 供能、接上管線與倉儲就能變成穩定產線。

## 模組特色
- 大量以 FE 驅動的實用機器，專注解決「原版做起來很麻煩」的自動化。
- 作物/樹場/動物/怪物等農場型機器選項多。
- 常見有橡膠（Latex）相關流程，很多配方會用到。
- 提供大容量儲存（黑洞系列）作為農場輸出的緩衝。
- 後期常見 Infinity 系列工具（依整合包是否啟用）。

## 按鍵操作
IF 主要在機器 GUI 裡操作，通常沒有必備快捷鍵。

- 打開「選項 → 控制設定」，搜尋：
  - `Industrial Foregoing`
  - `Foregoing`

## 遊戲內設定與調整
1) **先學會看機器 GUI：工作條件與輸入輸出**
- IF 的機器多半有幾個共同點：
  - 需要 FE
  - 可能需要特定耗材/流體
  - 有工作範圍或工作面向
- 你每次覺得機器「不動」時，優先檢查：
  - 有沒有電
  - 有沒有輸入
  - 輸出端是不是滿了

2) **用 JEI/REI 找到你的「第一條最有感產線」**
- 新手最常從橡膠線開始（Latex → 橡膠材料），因為很多機器零件會用到。
- 也可以反過來：你目前最缺什麼，就先做那條。

3) **黑洞儲存當緩衝，避免農場爆倉**
- 作物/樹場一旦跑起來產量很大，若沒有緩衝很容易：
  - 箱子滿 → 機器停機
  - 物流塞住 → 整條線卡死
- 先接大容量容器當緩衝，再接入主倉庫最穩。

4) **Mod 設定畫面（若有）**
- 依整合包與版本可能不同：
  - `ESC` → **Mods** → Industrial Foregoing → `Config/設定`（若有）
  - 找不到就先不用管；玩家端多數情況不需要動。

> 補充（只留短註）：機器耗電、範圍、黑名單等細節通常在設定檔；一般玩家不建議自行改動以免和整合包平衡衝突。

## 如何獲得模組道具
典型「入門 → 擴展」路線（配方以 JEI/REI 為準）：

- **橡膠/乳膠路線（常見入門關鍵）**
  - Tree Fluid Extractor 類：對原木抽取 Latex
  - Latex Processing Unit 類：用水 + 乳膠 + FE 做出橡膠材料

- **農場機器（選你最缺的先做）**
  - 播種/收割（Plant Sower/Gatherer 類）
  - 樹場（Plant/Gather 組合或專用樹機）

- **怪物與經驗（整合包若開放）**
  - Mob Crusher/Mob Duplicator 類機器（常需要流體/特定輸入）

代表性物品/方塊：
- Tree Fluid Extractor
- Latex Processing Unit
- Plant Sower / Plant Gatherer
- Mob Crusher / Mob Duplicator（若整合包有）
- Black Hole Unit / Black Hole Tank

## 好玩的點在哪
- **成就感很直接**：你缺什麼就做一台機器解決，立刻見效。
- **基地會越來越像工廠**：樹場、農田、怪物線各自獨立，最後全部回到倉庫系統。
- **玩法很彈性**：不用一次做全套；挑瓶頸補上就能大幅加速整包進度。

## 相關連結
- GitHub：<https://github.com/InnovativeOnlineIndustries/Industrial-Foregoing>
- Modrinth：<https://modrinth.com/mod/industrial-foregoing>
- CraftTweaker（若整合包用腳本改配方可參考）：<https://crafttweaker.readthedocs.io/en/latest/#Mods/Industrial_Foregoing/IndustrialForegoing/>
- 巴哈姆特（站內搜尋）：<https://forum.gamer.com.tw/search.php?kw=Industrial%20Foregoing>

## 圖片
（為避免版本差異造成連結失效，本篇不固定引用圖片；建議直接參考 Modrinth/GitHub 發佈頁）

## 安裝與前置（可略讀）
- IF 需要穩定 FE 供電與物流/倉儲配套才會「舒服」；整合包通常會一併提供其他能源/管線模組。
- 若你是管理員：機器範圍/耗能等平衡多在 config；修改前先備份。
