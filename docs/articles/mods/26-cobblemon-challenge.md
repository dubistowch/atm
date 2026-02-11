# 伺服器玩家對戰：Cobblemon Challenge 指令與玩法（/challenge）

如果你想在伺服器上「跟朋友直接來一場正式對戰」，Cobblemon 本體通常不會直接提供你要的完整 PVP 流程。

**Cobblemon Challenge** 是一個伺服器端模組：它提供 `/challenge` 相關指令，讓你可以指定「幾打幾、等級統一、要不要隊伍預覽」等規則，快速開打。

---

## 你會用到什麼
- `/challenge`：單打對戰
- `/challengedouble`：雙打對戰

> 如果你輸入後顯示 unknown command：代表伺服器沒有安裝或沒有開放該指令。

---

## 使用方式

### 1) 最常用的一行（推薦）
```
/challenge <對方ID> level 50 nopreview
```
- `level 50`：把雙方隊伍等級拉到固定等級（常用 50，公平又好玩）
- `nopreview`：不展示隊伍（想要「盲打」就加；想要正式賽制就拿掉）

### 2) 幾打幾（單打）
```
/challenge <對方ID> 1v1
/challenge <對方ID> 3v3
/challenge <對方ID> 6v6
```
- 從 `1v1` 到 `6v6` 都可

### 3) 幾打幾（雙打）
```
/challengedouble <對方ID> 2v2
/challengedouble <對方ID> 4v4
/challengedouble <對方ID> 6v6
```

---

## 團體遊玩建議（比較不會吵架）
- 打之前先講規則：
  - [ ] 要不要 preview？
  - [ ] 等級要不要統一（level 50）？
  - [ ] 幾打幾（1v1 / 3v3 / 6v6）？
- 如果是新手場：建議 `3v3 level 50`，節奏快又不會打太久。

---

## 常見問題
- **指令沒反應/unknown command**：伺服器沒裝 Cobblemon Challenge，或權限沒開。
- **對方沒收到挑戰**：可能對方關閉邀請、或在戰鬥/特定狀態下不能接受。

---

## 相關連結
- Modrinth：<https://modrinth.com/mod/cobblemon-challenge>

---

## 安裝與前置（可略讀）
- 這是伺服器端模組：一般玩家不需要自己裝。
- 若你是伺服器主：請以 Modrinth 頁面顯示的版本/loader 相容性為準。
