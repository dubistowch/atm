# FTB Teams 玩家指南（組隊、邀請、權限、盟友）

FTB Teams 是 FTB 的「隊伍管理」模組：你可以建立隊伍、邀請玩家、管理隊伍設定與權限等。
若同時安裝 **FTB Chunks**，FTB Teams 也會影響你在「已宣告（Claimed）的區塊」內，別人能不能破壞/放置/互動等行為。

---

## 1) FTB Teams 能做什麼？

依官方文件，FTB Teams 主要功能包含：
- 建立 / 管理 / 刪除隊伍
- 邀請（Invites）
- 隊伍權限與設定（Permissions & Settings）
  - 加入方式：**Free to Join** vs **Invite Only**
  - 隊伍描述（Description）
- 隊伍聊天（Team chat）：可透過指令或遊戲內 GUI
- 較完整的管理 GUI
- 隊伍顏色、隊伍名稱
- **Allies（盟友）**
  - 適合「想信任但不想拉進隊伍」或「對方已在別隊」的情境
- （若有 FTB Chunks）可控制已宣告區塊中的：
  - Mob griefing（生物破壞）
  - Block breaking（破壞方塊）
  - Block placing（放置方塊）
  - Block interaction（方塊互動）

---

## 2) 如何開啟/找到 Teams 介面？

不同整合包可能把入口放在不同 UI 按鈕上；如果你找不到按鍵或按鈕：
- 到 **Options → Controls** 搜尋：`Teams` / `FTB Teams`
- 或先用指令（見下方指令速查）

> 本文不假設你的整合包綁了哪個快捷鍵；請以 Controls 內的實際綁定為準。

---

## 3) 核心概念（玩家最常用到）

### 3.1 Team（隊伍）
隊伍是一個「共享身份」：隊伍成員通常會共享某些整合內容（尤其常見的是和 FTB Chunks 的領地/宣告權限連動）。

### 3.2 加入方式：Free to Join vs Invite Only
- **Free to Join**：允許玩家自由加入（是否可用取決於伺服器/整合包設定）
- **Invite Only**：需要邀請才能加入

### 3.3 Allies（盟友）
盟友是「被信任、但不是隊伍成員」的玩家/隊伍。
常見用途：
- 你想讓朋友進你家幫忙，但不想共享所有隊伍內容
- 對方已在另一個隊伍，不想退出原隊

---

## 4) 與 FTB Chunks 的連動（領地宣告權限）

若你有安裝 **FTB Chunks**，FTB Teams 會讓你控制「在你宣告的區塊內」哪些行為被允許，例如：
- 生物破壞（Mob griefing）
- 方塊破壞（Block breaking）
- 方塊放置（Block placing）
- 方塊互動（Block interaction）

因此當你遇到「朋友在我家不能開門/不能按按鈕/不能使用機器/不能放方塊」這類問題，第一個檢查方向通常是：
1. 你們是否在**同一個 FTB Team**
2. 若不想同隊，是否已把對方設為 **Ally**
3. 隊伍的宣告區塊權限是否把互動/放置/破壞關掉了

---

## 5) 指令速查（官方列出）

> 是否能用、能用到哪個子指令，可能受伺服器權限（OP / 權限模組）限制。

- `/ftbteams list [team-type]`：列出所有隊伍
- `/ftbteams party <party_options>`：以指令方式管理隊伍（建立/加入/邀請/離開等）
- `/ftbteams msg <message>`：隊伍聊天訊息
- `/ftbteams info [team]`：顯示隊伍資訊
- `/ftbteams server <create|delete|settings>`：伺服器隊伍管理（通常需要 OP）
- `/ftbteams force-disband <team>`：強制解散隊伍（通常需要 OP）

---

## 6) 什麼是 Server Team（伺服器隊伍）？

官方定義：**Server Team** 是由伺服器建立並管理的隊伍。
它通常搭配 **FTB Chunks**，用於伺服器層級的區塊保護、宣告區域管理等。

重要特性（玩家視角）：
- 不是玩家自己建的隊伍
- 玩家通常**不能**加入/被邀請加入/自行退出
- 它是「純伺服器管理用途」的隊伍

---

## 7) 伺服器限制玩家建隊/加入/邀請：常見原因與權限節點

官方文件指出：如果伺服器或整合包想禁止玩家建立/管理自己的隊伍，可以用像 **FTB Ranks** 這類權限管理模組，去拒絕以下指令權限：
- `command.ftbteams.party.create`
- `command.ftbteams.party.join`
- `command.ftbteams.party.invite`
- `command.ftbteams.party.leave`

玩家若遇到「不能建隊/不能邀請/不能加入/不能離開」，多半就是伺服器有做權限控管；需要請管理員確認。

---

## 8) 常見情境與排查（玩家 / 伺服器）

### 情境 A：我要跟朋友一起住、一起宣告領地
建議：建立同一個 FTB Team，讓對方加入；宣告的區塊通常就能以隊伍為單位共享/管理（具體仍取決於 FTB Chunks 與隊伍權限設定）。

### 情境 B：我想讓朋友來幫忙，但不想他成為隊伍成員
建議：使用 **Allies（盟友）**；讓對方有需要的存取權，但不必共享完整隊伍身分。

### 情境 C：朋友「看得到基地、但不能互動/不能開門/不能放置」
按順序排查：
1. 確認你們是否同隊；若不同隊，是否設為 Ally
2. 檢查隊伍對宣告區塊的權限：互動/放置/破壞/Mob griefing 是否被禁用
3. 若你在伺服器：請管理員確認是否有額外權限系統（例如 FTB Ranks）在擋

---

## Sources（官方文件）
- <https://docs.feed-the-beast.com/mod-docs/mods/suite/Teams/>
