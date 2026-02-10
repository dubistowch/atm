# Cobblemon：精靈球自動化／精靈球機器製作教學（整合包自動化思路）

![模組圖示](https://cdn.modrinth.com/data/MdwFAVRL/abfca1654a2d09bab85cbffcc9869938c951ee0e_96.webp)

> 本篇是「玩法與工廠思路」：
> - Cobblemon 的球大多需要 **杏果（Apricorn）+ 金屬錠** 等材料（細節依球種不同）
> - 整合包通常會有 Create / Mekanism / Industrial Foregoing / AE2 等模組，可以把「種杏果 → 收成 → 合成球」整條線自動化
>
> 重要：不同整合包會改配方、也可能有額外的機器方塊。**我不會硬寫不存在的方塊名稱**；所有配方與可用機器請以你整合包內的 **JEI/REI** 為準。

---

## 你會用到的模組／前置

- **Cobblemon**（杏果、精靈球配方）
- （幾乎必備）**JEI/REI**：確認你版本的精靈球配方、杏果用途
- （依整合包而定，擇一或混搭）
  - **Create**：農場收成、物品輸送、（可用機械合成/工作站）做大量合成
  - **Mekanism**：物流（管線）、能量、機器自動化
  - **Industrial Foregoing**：農場機器（收成/種植）、物流
  - **Applied Energistics 2 (AE2)**：倉儲、合成樣板、自動合成

---

## 目標與準備

### 目標
建立一條「精靈球供應線」：
1. 杏果（Apricorn）自動量產
2. 金屬錠（銅/鐵/金…依球種）穩定供應
3. 依 JEI 配方自動合成某一兩種「主力球」
4. 產出自動進倉（AE2/箱子）

### 準備
- 先決定你要量產哪種球：
  - 新手最常用：**基礎球系**（例如 Poké Ball 類）
  - 中期：Great/Ultra 等（通常需要更高階金屬）
- 先確認配方：
  - 打開 JEI/REI，查你目標球的配方
  - 把所有材料列成一張清單（杏果顏色、金屬錠種類、是否需要 tumblestone 等）

參考：Cobblemon Wiki 的 Poké Ball 條目提到，許多球主要透過 crafting 取得，且不同球需要不同材料。

---

## 步驟教學（從 0 → 自動化）

### 步驟 1：先做「杏果來源」——你要的是穩定，不是漂亮
杏果是整條線的核心瓶頸，所以第一步永遠是：**先把杏果變成可持續供應**。

通用做法（不限定模組）：
1. 先在家附近種一片杏果（至少每種顏色各一排）。
2. 用任何你整合包提供的「農場/收成」手段把它變成半自動：
   - 早期：手動收成 + 箱子分類
   - 中期：Create 收成裝置 / Industrial Foregoing 農場機器（依整合包而定）
3. 把收成物集中到一個「材料總線箱」或直接進 AE2。

### 步驟 2：補上金屬錠供應（銅/鐵/金…）
精靈球常見會用到銅、鐵、金等（以 Wiki 舉例：基礎球類會用到杏果 + 銅錠；更高階球可能用鐵/金）。

建議作法：
1. 先把礦物處理線穩定（熔爐陣列、Mekanism 製程、或你整合包的礦處理）。
2. 讓「錠」輸出到同一個材料總線箱/AE2。

### 步驟 3：把配方拆成「可自動合成」的形狀
不同整合包可能有不同合成工具，但拆解思路固定：

1. **確認是工作台合成（Crafting）還是機器合成（Processing）**
   - 若 JEI 顯示是一般 Crafting：優先用 AE2/Create 的合成系統做
   - 若你整合包把球改成機器配方：就改走該機器的自動化（以 JEI 顯示為準）
2. 先挑 1 種球做通：例如你最常丟的球。
3. 做出「輸入材料箱」→「合成」→「輸出箱/倉庫」的最短迴路。

### 步驟 4A：用 AE2 做「精靈球自動合成」（最像現代工廠）
（如果你整合包有 AE2，且你已經有基礎 ME 網路）

1. 在 AE2 網路上放：
   - ME Crafting Terminal（或一般 ME Terminal 也可，但有 Crafting Terminal 更順）
   - Pattern Encoding Terminal（樣板終端）
2. 在樣板終端裡：
   - 放入 Blank Pattern
   - 以 JEI 的配方直接編碼成「Crafting pattern」
3. 放置 1 組最小自動合成模組：
   - Pattern Provider + Molecular Assembler（貼在一起）
4. 確保杏果與金屬錠都已進 ME 儲存。
5. 在終端機搜尋你的球，應該會顯示「可合成」並能下單。

> 小提醒：AE2 的自動合成很吃「材料是否有進系統」與「通道/頻道」概念；先從少量機器開始擴。

### 步驟 4B：用 Create 做「大量合成 + 輸送」
Create 的做法很多種，這裡給「最不容易踩雷」的思路：

1. 用漏斗/管道把杏果與金屬錠送到一個「合成點」。
2. 合成點可用：
   - 你整合包提供的 Create 合成方案（例如機械合成/工作站等，依整合包為準）
3. 合成後把成品用輸送帶/溜槽送進箱子或 AE2。

> 如果你不確定整合包到底讓你用哪一種 Create 合成方塊：請直接 JEI 搜尋「crafting」相關 Create 方塊，或看整合包作者的任務書/說明。

### 步驟 4C：用 Industrial Foregoing 做「農場端」再把材料丟給 AE2/管線
Industrial Foregoing 常見定位是：
- 農場端（種植/收成）很省事
- 合成端通常交給 AE2 或其它自動合成系統

做法：
1. IF 農場把杏果量產。
2. 用你整合包的物流把杏果送到 AE2 或集中箱。
3. 合成端交給 AE2（推薦）或其它模組。

---

## 常見坑與排查

1. **杏果不夠 → 球永遠卡材料**
   - 先把杏果農場擴大 2～4 倍再談「更多球種」
   - 先專注量產 1～2 種主力球

2. **配方跟網路上看到的不一樣**
   - 很正常：Cobblemon 版本、整合包配方調整都會影響
   - 永遠以 JEI/REI 為準

3. **AE2 顯示可合成，但下單就卡住**
   - 缺材料（杏果顏色不對、錠不足）
   - Pattern Provider/Assembler 沒接好、或頻道不足

4. **你想做全自動，但球在地上亂噴**
   - 先用箱子緩衝（buffer）把流程拆段
   - 先做到「穩定產出」再追求「漂亮佈線」

---

## 圖片（可靠來源才放）

- Cobblemon Wiki：Poké Ball 圖例（頁面內有各種球的模型圖，若你需要直連可從 File 取得 Special:FilePath）
  - <https://wiki.cobblemon.com/index.php/Pok%C3%A9_Ball>

（自動化流程建議自行截圖你的工廠：最能反映你整合包版本與機器配置。）

---

## 相關連結

- Cobblemon Wiki：Poké Ball（球種、取得方式、部分配方示例與版本說明）
  - <https://wiki.cobblemon.com/index.php/Pok%C3%A9_Ball>
- 本整合包指南：Create（自動化/物流概念）
  - （同資料夾既有指南）`guides/03-create.md`
- 本整合包指南：Industrial Foregoing（農場/機器自動化概念）
  - （同資料夾既有指南）`guides/08-industrial-foregoing.md`
- 本整合包指南：Applied Energistics 2（倉儲與自動合成）
  - （同資料夾既有指南）`guides/10-applied-energistics-2.md`

## 資料來源
- <https://modrinth.com/mod/cobblemon>
- <https://cdn.modrinth.com/data/MdwFAVRL/abfca1654a2d09bab85cbffcc9869938c951ee0e_96.webp>
