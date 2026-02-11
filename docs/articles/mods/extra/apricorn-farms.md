# ATM10 杏果（Apricorn）農場整理（前期 / 中期 / 後期）

> 影片來源：<https://youtu.be/FTk22eRyOZI>
>
> 背景：ATM10（beta）目前常見的作物加速（如各種 growth accelerator / garden cloche / 部分儀式）對杏果不一定生效，因此需要改用「可右鍵採收」或「互動/點擊」類機制來自動化。

---

## 章節 1｜前期：拿到芽（sprout）＋穩定低成本產線

### 1.1 基礎取得方式（先搞懂）
- 杏果樹上「成熟的杏果」可 **右鍵** 採收 → 掉落杏果。
- 採收時有機率掉 **sprout（芽）**（影片提到約 12.5%）。
- 芽可：
  - 種地上長成樹（之後可再右鍵採收更多杏果）
  - 或 **右鍵貼在杏果樹葉上**（像可可豆那樣貼上去）

### 1.2 用 Pasture Block + Pickup（Cobble Workers）被動刷芽
目標：不需要跑圖就能慢慢把各色芽湊齊。

**做法：**
1) 製作並放置 **Pasture Block**。
2) 召喚具有 **Pickup** 能力的寶可夢在 Pasture Block 範圍內活動（影片示範用 Zigzagoon）。
3) 在 Pasture Block 旁放 **一般木箱（普通 chest）** 作為輸出容器。

**注意（影片提醒的 bug）：**
- Pasture Block 可能 **不認** 部分模組箱（例如某些升級箱/鐵箱/進階箱），導致物品被丟到地上。
- 解法：
  - 先用 **普通 chest** 接輸出
  - 再用漏斗/管線轉進你的進階倉儲系統。

**優缺點：**
- 優點：便宜、早期可用、可順便產一堆雜物。
- 缺點：效率偏被動，適合「起步湊芽」。

### 1.3 Hopper Botany Pot（漏斗植物盆）— 早期最穩保底
目標：簡單、全自動產杏果（速度慢但穩）。

**核心方塊：**
- **Hopper Botany Pot**（材質很多種，影片推薦：
  - 基礎（陶土）
  - Stone Brick
  - **Deepslate Brick（作者最愛，因為不用燒深板岩卵石）**）

**擺法：**
1) Hopper Botany Pot 放在箱子/抽屜上方（讓掉落物自動輸出）。
2) 上槽放 **Apricorn sprout**。
3) 下槽放 **Dirt**。
4) 放入一把 **Hoe（鋤頭）**。

**加速技巧（必抄）：**
- 在盆裡對 Dirt **右鍵鋤一下** → 變 farmland，免費 **+10% 生長速度**。
- 影片提到一個很關鍵的「工具不會壞」技巧：
  - 做 **Stone Hoe** 後轉成 **Silent Gear 版本**（耐久掉到 1 不會破）
  - 等於可以永久放在盆裡使用。
- Hoe 上 **Efficiency** 附魔可再加快生長（影片示範有效）。

---

## 章節 2｜中期：機器化採收牆（效率起飛）

> 這章節開始，核心概念是：杏果本質上是「右鍵採收」的作物 → 用「範圍互動/點擊」去自動化。

### 2.1 Bug Type 自動採收（Cobble Workers）
目標：蟲系寶可夢會幫你採杏果並放進箱子。

**做法概念：**
1) 種/催生杏果樹（或把芽貼在葉子上排牆）。
2) 召喚 **Bug type** 寶可夢在附近。
3) 放箱子讓採收物進箱。

**缺點：**
- AI 可能卡卡的、採收頻率不夠穩定。

### 2.2 Just Dire Things：Advanced Clicker + Item Collector（重點）
目標：做一面杏果牆，讓機器範圍內自動採收＋自動撿取。

**需要：**
- **Advanced Clicker**（Just Dire Things）
- **Item Collector**（Just Dire Things）
- 電力（RF/FE）

**擺法/設定流程（照影片操作邏輯）：**
1) 先把杏果「貼牆」或排成可採收的牆面。
2) 放置 Advanced Clicker，打開 **Render Area**。
3) 用 **Offset** 對準牆面中心，再調整半徑把整面牆框進去。
4) Item Collector 放在箱子上方，並把它的範圍/Offset 設成 **跟 Clicker 一模一樣**（確保掉落物都能撿）。
5) 設定速度到 **1 tick**（影片示範可用左右鍵調整）。

**加速選項：**
- 可往 Clicker 供應骨粉（可行但消耗很大）。
- 更強的作法（影片強推）：
  - 放入「不會壞」的 **Silent Gear Stone Hoe**
  - 並附魔 **Nature’s Blessing**
  - 讓 Clicker 在採收同時大量促生，產量會非常誇張。

**影片提到的量級：**
- 中期版本測到約 **125 杏果 / 秒**（非常足夠）。

---

## 章節 3｜後期：Ars Nouveau 終局大範圍（上千 / 秒）

> 後期做法本質上是「中期方案的放大版」：把採收/促生範圴擴到更大、並用更方便的方式一鍵鋪場。

### 3.1 法術書升級（增加 glyph slot）
- 影片提到升級到：Allthemodium / Vibranium / Unobtainium 等級
- glyph slots 最高可到 **20 格**（範圍、AoE 能堆更大）

### 3.2 快速鋪場技巧：Place Block 一鍵放葉子/芽
作者教了一個很實用的建場方式：
1) 先把原本用來採收/促生的法術 **複製**（Ctrl+C / Ctrl+V）。
2) 把複製版改成結尾放 **Place Block** glyph。
3) 用紅石訊號觸發 turret，一次把整面牆需要的 **Apricorn Leaves** 放好。
4) 再用同樣方式一鍵把 **sprout** 放滿（不用手動一個個擺）。

### 3.3 影片提到的終局產量
- 最大化後，作者展示約 **1,125 杏果 / 秒** 的產量等級。

---

## 建議路線（懶人包）
- 前期：Pasture Block + Pickup 湊芽 → Botany Pot 做保底產線
- 中期：直接做 Advanced Clicker + Item Collector（再加 Nature’s Blessing）
- 後期：Ars Nouveau 升級擴大範圍 + Place Block 一鍵鋪場 → 上千/秒
