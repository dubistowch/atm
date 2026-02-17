# 沉浸工程（Immersive Engineering）入門：第一組發電、第一條電線、第一台機器

沉浸工程（Immersive Engineering，IE）是一種很有「工業感」的科技模組：它不走「一格方塊塞滿功能」的路線，而是用**電線、變壓器、電容**與**大型多方塊機器**來做出發電與加工。

如果你喜歡：
- 看得見的電線網路（不是隱形管線）
- 需要規劃擺放的多方塊機器
- 有年代感的工業風

那 IE 會是你很值得學的一條科技線。

---

## 30 秒看懂：IE 的核心概念
- **電力不是憑空到處跑**：你要用電線把電拉到該去的地方
- **電容（Capacitor）＝緩衝**：不先放電容，你會更常遇到「機器一下就停」
- **多方塊機器＝IE 的主菜**：粉碎、挖礦、加工通常都在多方塊裡
- **工程師手冊（Engineer’s Manual）是你的課本**：它會直接告訴你「這台機器怎麼拼」

---

## 前 30 分鐘：最短上手流程（照做就能開始跑）

### 步驟 1｜先做工程師手冊（最重要）
- 在 JEI/REI 搜尋：`Engineer`、`Manual`
- 做出 **Engineer’s Manual**（工程師手冊）

> 你後面要拼任何多方塊，都會靠它的圖。

### 步驟 2｜做出「電線 + 接頭 + 電容」的最小供電組
你的目標是：讓「電可以從發電端 → 走電線 → 進電容/機器」。

- 在 JEI/REI 搜：`Connector`、`Wire`、`Capacitor`
- 先做一組最低階即可（配方與等級以整合包為準）

### 步驟 3｜選一種 IE 發電（先求穩）
IE 常見的前期發電會有：
- 水車/風車（看地形）
- 生質柴油等（中後期）

你不用一次挑最強，只要先讓機器能穩定吃到電。

### 步驟 4｜接線（這裡是新手最常卡的）
- 確認你有「接線/剪線」相關工具（通常是 **Wirecutter** 一類；以 JEI/REI 為準）
- 用工具把「接頭」跟「電線」連起來

> 按鍵/操作不要猜：到 **選項 → 控制設定** 搜 `Immersive` / `Wire` / `Connector` / `Engineer`。

### 步驟 5｜做第一台加工機器（選一台最需要的）
IE 的加工通常是多方塊，你先挑一台「你現在最缺的」：
- 你缺礦處理：就先做粉碎/冶煉路線
- 你缺材料自動化：就先做輸入輸出與儲能穩定

拼法直接照 Engineer’s Manual 圖：
- [ ] 先把外框拼出來
- [ ] 再照圖放上「功能方塊」
- [ ] 最後用指定工具/操作「形成多方塊」（手冊會寫）

---

## 任務書照做：3 個新手最常用的 IE 多方塊（照圖擺、照步驟啟動）

整合包的 FTB Quests 其實把 IE 的多方塊「怎麼擺」寫得很清楚。下面我挑 3 個**最常用、而且新手最常卡**的，多做一次你就會熟。

> 圖片都是「資訊型」的擺放示意，來源是任務書內的 questpics（不是 logo）。

### 1) 粗製高爐（Crude Blast Furnace）＝最早的鋼錠來源
任務書重點：
- 把 **鐵錠** + **木炭/焦炭**丟進去燒鋼
- 燃料時間：木炭比較短、焦炭比較穩（實際以你包內說明為準）
- 需要一個 3×3×3 的結構，最後用錘子在正面啟動

![粗製高爐 步驟 1](./assets/questpics/immersive/immersive_crude1.png)
![粗製高爐 步驟 2](./assets/questpics/immersive/immersive_crude2.png)
![粗製高爐 步驟 3](./assets/questpics/immersive/immersive_crude3.png)
![粗製高爐 完成](./assets/questpics/immersive/immersive_crude.png)

### 2) 擠壓機（Squeezer）＝種子榨油/特定粉末處理
任務書重點：
- 用來從作物種子榨出油（例如植物燃油線）
- 也會拿來做一些粉末/材料的關鍵中繼（以任務與 JEI 為準）
- 結構完成後，用錘子對指定方塊啟動

![擠壓機 步驟 1](./assets/questpics/immersive/immersive_squeezer1.png)
![擠壓機 步驟 2](./assets/questpics/immersive/immersive_squeezer2.png)
![擠壓機 步驟 3](./assets/questpics/immersive/immersive_squeezer3.png)
![擠壓機 完成](./assets/questpics/immersive/immersive_squeezer.png)

### 3) 裝配器（Assembler）＝把小零件量產起來
任務書重點：
- 這台機器很多操作在 GUI 裡設定（可以放多個配方、依序執行）
- 你可以用輸送帶/管線輸入輸出（依你包內物流線）
- 結構完成後，照任務書提示用工程師錘啟動

![裝配器 步驟 1](./assets/questpics/immersive/immersive_assembler1.png)
![裝配器 步驟 2](./assets/questpics/immersive/immersive_assemble2.png)
![裝配器 步驟 3](./assets/questpics/immersive/immersive_assembler3.png)
![裝配器 完成](./assets/questpics/immersive/immersive_assembler.png)

---

## 常見卡關與排查

### Q1：我有電線，但接不起來
- 通常是少了「接線工具」或你接到錯的方塊面
- 先看 Engineer’s Manual 該方塊的章節：它會寫支援哪些面、用什麼工具

### Q2：機器看起來拼好了，但不運作
- 多方塊可能還沒「成形」：要用手冊指定的方式啟動（很多 IE 都是這樣）
- 確認電容有電、機器有吃到電

### Q3：電很不穩、機器一下就停
- 先加大電容/緩衝
- 把發電跟加工區分開（用電容當中繼）

---

## 延伸閱讀（玩家真的會用到的）
- 你能跑起第一台機器後，下一步通常是：
  - [ ] 做第二層供電（把線路整理成「主幹線 + 分支」）
  - [ ] 開始規劃第一台大型加工多方塊（例如粉碎/挖礦）
  - [ ] 研究 IE 的物品輸送方式（不同版本會有不同選項，先以包內為準）

---

## 資料來源（文件）
- Modrinth：<https://modrinth.com/mod/immersiveengineering>
- GitHub（官方）：<https://github.com/BluSunrize/ImmersiveEngineering>
- README（提到模組定位與下載）：<https://raw.githubusercontent.com/BluSunrize/ImmersiveEngineering/master/README.md>

> IE 最完整的玩家說明通常在遊戲內的 Engineer’s Manual；本篇以「新手起步流程」整理。

## 任務書對應（FTB Quests）

任務書章節：`immersive_engineering`（建議在任務書搜尋此章節名或關鍵字）

本章常見任務節點（節錄）：
- 轉輪藍圖
- 粗製高爐
- 重型盾牌
- 擠壓機
- 工程師工具箱
- 電線卷
- 普通子彈
- 保暖物品
- 精煉廠
- 分級電壓

> 來源：`minecraft/config/ftbquests/quests/lang/zh_tw/chapters/`
