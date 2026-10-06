# 卡通教學影片製作套件 — 規格說明

用 Python（pycairo）逐格畫出卡通畫面，配上 Gemini TTS 旁白、自動字幕與背景音樂，輸出 MP4。
AI 名詞小辭典、AI 公司系列、AI 蒸餾事件簿都是用這套做的。

---

## 1. 檔案結構

```
videokit/
├── engine.py          核心引擎：畫面基本元件、字幕、音樂、Episode 類別、輸出 MP4
├── dc.py              共用模板（開場、路線圖、考題、結尾…）＋ AI 小博士角色
├── xd.py              小戴角色（import 後所有模板改畫小戴）
├── aj.py              山姆角色（import 後所有模板改畫山姆）
├── dsc.py             蒸餾系列的小元件（公司卡、帳號、盾牌、錄音機…），會自動載入小戴
├── example_ds2.py     完整範例：蒸餾事件簿第 2 集（13 個場景）
├── example_ds2/       範例的 script.json + 已處理好的語音 c1.pcm～c13.pcm
├── mt1/script.json    METR 系列第 1 集旁白稿（13 段，已寫好，主持人＝山姆）
└── tools/
    ├── make_payloads.py   script.json → TTS 請求檔
    ├── tts.sh             呼叫 OpenRouter 產生語音（金鑰讀 ~/.openrouter_key）
    ├── prep.sh            語音加速 1.1 倍並改名成引擎要的格式
    └── f0.py              音高檢查（抓出不小心變成女聲的段落）
```

---

## 2. 環境需求（Mac）

```bash
brew install ffmpeg cairo pkg-config
pip3 install pycairo numpy pillow
brew install --cask font-noto-sans-cjk-tc     # 字型：Noto Sans CJK TC（必要）
```

先跑 `python3 example_ds2.py auto`，產生 `example_ds2/grid.png`，就代表環境 OK。

---

## 3. 製作流程（一集）

以 `mt1` 為例：

| 步驟 | 指令 | 產出 |
|---|---|---|
| 1. 寫稿 | 編輯 `mt1/script.json` | 字串陣列，一段＝一個場景 |
| 2. 產生請求檔 | `python3 tools/make_payloads.py mt1` | `tts_mt1/mt1_1.json`… |
| 3. 生成語音 | `bash tools/tts.sh mt1` | `tts_mt1/mt1_1.pcm`… |
| 4. 檢查音高 | `python3 tools/f0.py tts_mt1/*.pcm` | 每段的中位數 Hz |
| 5. 加速＋改名 | `bash tools/prep.sh mt1` | `mt1/c1.pcm`… |
| 6. 寫畫面 | 新增 `mt1.py`（見第 5 節） | |
| 7. 預覽 | `python3 mt1.py auto` | `mt1/grid.png`（每場景 2 格縮圖） |
| 8. 指定秒數預覽 | `python3 mt1.py 12.5 40.0` | 那幾秒的畫面拼成 `mt1/grid.png` |
| 9. 輸出 | `python3 mt1.py` | MP4（約 2～4 分鐘可算完） |
| 10. 檢查 | `ffmpeg -v error -i 檔名.mp4 -f null -` | 沒有輸出＝檔案完整 |

**音高規則：** 男聲（Puck）正常中位數約 120～160 Hz。**超過 165 Hz 就重新生成那一段**，生成兩次，取比較低的那次。Gemini 偶爾會變成女聲。

---

## 4. 技術規格

| 項目 | 規格 |
|---|---|
| 影像 | 1280×720、30 fps、H.264（libx264） |
| 聲音 | TTS 原始檔為 24 kHz 單聲道 s16le PCM；輸出 AAC |
| TTS | OpenRouter `/api/v1/audio/speech`，模型 `google/gemini-3.8-flash-tts`，voice `Puck` |
| 風格指令 | 放在 `instructions` 欄位（放在 `input` 會被唸出來） |
| 語速 | `atempo=1.1` |
| 場景長度 | 自動＝該段語音長度＋前置 0.35 秒（LEAD）＋尾端 0.45 秒（TAIL） |
| 字幕 | 自動依標點斷句（，。！？：；），過長的句子會在「、」再切；在暫停處對時 |
| 背景音樂 | 自動生成，說話時自動壓低 |
| 轉場 | 圓形擦除，只用在 `wipes` 指定的場景開頭（建議：每站開頭、考題、結尾） |

---

## 5. 寫一集的畫面（`mt1.py` 骨架）

```python
from aj import *          # 主持人＝山姆；改 from xd import * 就是小戴

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "標題", "AI 安全事件簿・第 1 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("第一站\n名稱", "稿中關鍵字"), ...])

def s2(ep, ctx, u, T, m):
    background(ctx, T, 1)                      # 第三個參數＝背景色組 0～5
    station_card(ctx, u, 1, "站名")             # 每站開頭的大標題卡（前 1.9 秒）
    if u < 1.9: return
    header(ctx, 1, "左上角小標題", u - 1.9)
    corner(ctx, T, m)                          # 右下角主持人（會跟著說話動嘴）
    t = ep.kw(2, "稿中某個詞")                  # 這個詞被唸到的秒數
    chip(ctx, "標籤", 600, 300, prog(u, t, .4), C['yellow'], 28)

# ... s3 ~ s11 ...
def s12(ep, ctx, u, T, m):
    rows = [("左標", "右側說明", ep.kw(12, "關鍵字")), ...]   # 3～4 列
    outro_doc(ep, ctx, u, T, m, 12, "第 1 集重點", "副標", rows)

run("mt1", "AI 安全事件簿 1", [s0, s1, ..., s12], "輸出檔名.mp4", wipes={2, 5, 8, 12})
```

**場景函式參數**

| 參數 | 意義 |
|---|---|
| `ep` | Episode 物件 |
| `ctx` | cairo 畫布（1280×720） |
| `u` | 進入此場景後的秒數 |
| `T` | 全片秒數（給呼吸、眨眼等動畫用） |
| `m` | 0～1 的嘴巴開合量（跟著語音音量） |

**時間對齊：** `ep.kw(場景編號, "字串")` 依字數比例，推估該字串在旁白中被唸到的時間（會提前 0.25 秒）。
- 字串必須**原封不動**出現在該段稿裡，否則會報錯。
- 只會找第一次出現的位置。例如找「要寫」可能先對到「不要寫」，所以字串要取得夠獨特。

**畫面安全區：** 內容放在 y＝120～600。下方 640～700 是字幕；右下角約 x 1050～1260、y 430～640 是主持人。

---

## 6. 常用元件速查

| 函式 | 用途 |
|---|---|
| `prog(u, t0, d)` | 0→1 進度（從 t0 開始，花 d 秒），所有動畫的基礎 |
| `ease_out(x)`、`back(x)` | 緩動曲線 |
| `text(ctx, s, x, y, size, col, align='c'/'l', a=透明度)` | 文字 |
| `chip(ctx, s, x, y, p, 底色, size, 字色)` | 圓角標籤 |
| `panel(ctx, x, y, w, h, p, fill)` | 彈出面板；回傳 True 時，畫完要 `ctx.restore()` |
| `card(ctx, 名稱, 顏色, x, y, p, w, h, size, sub=副標)` | 公司或物件卡片（dsc.py） |
| `arrow(ctx, x1, y1, x2, y2, p, col, lw)` | 會延伸的箭頭 |
| `stepchain(ctx, labels, times, u, ...)` | 流程圓圈串（A → B → C） |
| `rows_list(ctx, u, rows, ...)` | 由左滑入的條列 |
| `mark(ctx, x, y, ok, p)` | 打勾或打叉 |
| `star`、`burst`、`sticker`、`speech` | 星星、放射特效、貼紙、對話泡泡 |
| `quiz_q(ep, ctx, u, T, m, sc, 題目行, 選項)` / `quiz_a(..., 正解index, 解說)` | 考題兩場景 |
| `user`、`acct`、`doc`、`lock`、`shield`、`recorder`、`dashed` | 小圖示（dsc.py） |
| 顏色 `C['navy'/'teal'/'yellow'/'orange'/'red'/'pink'/'blue'/'green'/'grey'/'white']` | 色票 |

---

## 7. 注意事項

- **字型缺字：** ✗ ↻ ⚙ 會變方塊，打叉請用 ×。✓ → ↑ ↓ ≈ ≠ ①②③ 可以用。不確定的符號先預覽。
- **Cairo 怪線：** 畫完弧形或文字後出現多餘的線，就在下一筆之前加 `ctx.new_path()`。
- **save/restore 要成對：** `panel()` 回傳 True 時一定要 `ctx.restore()`。
- **長度為 0 的圖形：** 寬度乘上進度變成 0 時，外框會畫成一條直線，記得加 `if g > .01:`。
- **金鑰：** API 金鑰只放在 `~/.openrouter_key`，不要寫進程式或貼到任何地方。回傳 401 "API key expired" 就是需要換新的金鑰。
- **檢查清單：** 音高 OK → `grid.png` 每格看過（文字不重疊、沒有壓到主持人或字幕）→ 輸出 → ffmpeg 解碼沒有錯誤。

---

## 8. METR 系列現況

- `mt1/script.json`：第 1 集旁白，13 段，已寫好（結尾是「我是山姆，下集見！」）。
- 主持人：`aj.py`（山姆，原創造型）。
- 第 1 集的畫面檔 `mt1.py`，以及第 2、3 集的稿和畫面，需要另外撰寫。
