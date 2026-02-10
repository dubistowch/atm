# AE2：終端機與自動合成入門（ME 終端、樣板終端、分子裝配室、匯入/匯出）

> 本篇定位：帶你做出「能用的第一套」AE2：
> - 有 **ME 終端機** 可以搜尋拿取物品
> - 有 **樣板終端（Pattern Encoding Terminal）** 可以做出合成樣板
> - 用 **Pattern Provider + Molecular Assembler** 完成最基本的自動合成
> - 會用 **Import/Export** 把 AE2 跟外部機器串起來
>
> 配方提醒：AE2 配方與你整合包的能源/礦處理息息相關，請以 **JEI/REI** 為準。

---

## 你會用到的模組／前置

- **Applied Energistics 2（AE2）**
- （建議）**JEI/REI**：編碼樣板時可以直接拖配方、或從配方頁一鍵編碼（依整合包 UI）
- 一種能源來源（能把電送進 AE2 的 Energy Acceptor 或等價方塊）

資料來源（流程與概念）：AE2 官方 Players Guide（1.20.1 版章節，內容同樣適用於大多數近代版本的概念）。

---

## 目標與準備

### 目標
1. 先搭出「可用的 ME 倉儲 + 終端」
2. 再加上「能自動合成 crafting recipe」的一小組 Pattern Provider + Molecular Assembler
3. 最後懂得用 Import/Export Bus 串外部機器

### 準備
- 你已經完成 AE2 前期：拿到 Certus、Fluix、Processors、線材、基本電力（細節可看官方 Getting Started）
- 至少 1 顆 Storage Cell + 1 個 ME Drive（或先用 ME Chest 也行）

---

## 步驟教學（照做版）

### 步驟 1：先完成「最小可用」ME 網路 + 終端
（官方 Getting Started 提供一個很標準的最小清單，這裡用新手語翻譯成操作流程）

1. 放下 **ME Drive**（或 ME Chest）。
2. 接上電力：
   - 放 **Energy Acceptor**（或你版本等價的能量輸入方塊）
   - 用你整合包的發電模組把電接進來
3. 用 AE2 線材把 Drive 與 Energy Acceptor 串起來。
4. 在線材上裝一個 **ME Terminal**（建議直接做 **ME Crafting Terminal**，官方也建議盡快升級）。
5. 把 Storage Cell 插進 ME Drive。
6. 打開終端機，試著把背包物品丟進去、再搜尋拿出來。

> 終端機「放反」是常見新手錯誤：AE2 Players Guide 特別提到終端可能裝反導致沒連到網路。

### 步驟 2：學會終端機常用操作（提升手感）
依照官方 Terminals 條目：
- 左鍵拿一疊、右鍵拿半疊
- 你可以調整排序、顯示「已儲存/可合成」等
- 有些操作會用到你綁定的「Pick Block（通常中鍵）」來叫出合成數量介面（以你鍵位為準）

建議設定：
1. 打開終端，先把排序設成你習慣的（名稱/數量/模組）。
2. 學會用搜尋欄（AE2 最大的價值之一）。

### 步驟 3：做樣板終端（Pattern Encoding Terminal），開始做第一張樣板
1. 做出並放好 **Pattern Encoding Terminal**（它是一種終端，會掛在線材上）。
2. 準備 **Blank Pattern**。
3. 在樣板終端選「Crafting」模式：
   - 從 JEI/REI 把配方材料拖進格子（或用一鍵編碼功能）
   - 檢查「Substitutions（替代材料）」：
     - 新手建議不要亂開，除非你確定允許任何木材/任何染料等
4. 按下編碼（Encode），得到「已編碼樣板」。

### 步驟 4：用 Pattern Provider + Molecular Assembler 做最小自動合成
官方觀點（很重要）：
- **Molecular Assembler** 的主要用途，就是貼著 **Pattern Provider** 來跑合成樣板。

照做：
1. 放一台 **Pattern Provider**，貼著它放 **Molecular Assembler**（面貼面）。
2. 確認它們都有連到你的 AE2 網路（線材/頻道依你進度）。
3. 把剛剛編碼好的「Crafting Pattern」塞進 Pattern Provider。
4. 回到 ME 終端搜尋該物品：
   - 應該會顯示可合成
   - 下單少量測試（例如 1～8 個）
5. 觀察：材料會從網路送到組裝室合成，成品會回到網路。

> 官方分子裝配室條目也提醒：某些 Optifine 可能破壞「推送到相鄰容器」行為，導致自動合成怪怪的。

### 步驟 5：把 AE2 接到外部機器（匯入/匯出最入門）
這裡用最常見的「丟進去加工 → 把產物拉回來」思路：

1. 找一台外部機器（熔爐、粉碎機、任意機器）。
2. 在它的輸入側放 **ME Export Bus**：
   - 過濾你要送出去的材料（例如礦）
3. 在它的輸出側放 **ME Import Bus**：
   - 把產物拉回 ME 網路
4. 先不要追求完美：
   - 先讓流程跑得起來
   - 再考慮加速卡、紅石控制、或改用 Pattern Provider 做更乾淨的 processing autocraft

---

## 常見坑與排查

1. **終端機打開但看不到東西/顯示離線**
   - 終端可能裝反（官方 Terminals 提醒）
   - 線材沒接到 Drive/能量輸入

2. **可以存取但不能自動合成**
   - 沒有 Pattern Provider + Molecular Assembler
   - 樣板沒有放進 Provider
   - 材料沒有進 ME 網路

3. **合成卡住、CPU 一直轉**
   - 缺材料、或材料被其它任務占用
   - 樣板用了替代材料但系統選不到你真正有的那種

4. **頻道（Channels）不夠**
   - 先用最少設備、少量線路
   - 中期再上 ME Controller、Smart Cable 看通道走向

---

## 相關連結

- AE2 Players Guide（1.20.1）：Getting Started（流星、press、第一套 ME 系統）
  - <https://guide.appliedenergistics.org/1.20.1/getting-started>
- AE2 Players Guide：Terminals（終端機 UI、Pattern Encoding Terminal、Pattern Access Terminal 等）
  - <https://guide.appliedenergistics.org/1.20.1/items-blocks-machines/terminals>
- AE2 Players Guide：Pattern Provider（自動合成/加工跟世界互動的核心方塊）
  - <https://guide.appliedenergistics.org/1.20.1/items-blocks-machines/pattern_provider>
- AE2 Players Guide：Molecular Assembler（與 Pattern Provider 搭配完成合成）
  - <https://guide.appliedenergistics.org/1.20.1/items-blocks-machines/molecular_assembler>

## 資料來源
- <https://guide.appliedenergistics.org/>
- <https://modrinth.com/mod/ae2>
