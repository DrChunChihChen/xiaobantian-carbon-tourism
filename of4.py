"""辦公室碳冒險：CASE #004 雲端機房與 AI 算力真相 (刑偵剪貼調查風格)"""
import engine
from engine import *
from scrapbook import *

# 調查風格色票與設定
engine.WIPE = [(0.12, 0.12, 0.14), (0.82, 0.18, 0.15), (0.12, 0.12, 0.14), (0.82, 0.18, 0.15)]

def run(name, tag, scenes, out, wipes=None):
    ep = Episode(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), tag)
    ep.scenes = scenes; ep.wipes = wipes
    ep.run(out, sys.argv)

def custom_sub(ctx, s):
    """黑底圓角長條字幕，重點詞高亮黃色"""
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(32)
    ext = ctx.text_extents(s)
    w = ext.width
    rrect(ctx, 640 - w / 2 - 28, 648, w + 56, 52, 14)
    ctx.set_source_rgba(0.08, 0.08, 0.10, 0.94); ctx.fill()

    highlights = [
        "十倍", "五百公噸", "七噸", "2 到 4 克", "五瓦特", "上百萬度",
        "生成式 AI", "雲端硬碟", "冷卻水系統", "RE100", "數位囤積", "綠色算力"
    ]
    found_hl = None
    for h in highlights:
        if h in s:
            found_hl = h
            break

    if not found_hl:
        text(ctx, s, 640, 674, 32, C['white'])
    else:
        parts = s.split(found_hl, 1)
        w0 = ctx.text_extents(parts[0]).x_advance
        wh = ctx.text_extents(found_hl).x_advance
        start_x = 640 - w / 2
        if parts[0]:
            text(ctx, parts[0], start_x + w0 / 2, 674, 32, C['white'])
        text(ctx, found_hl, start_x + w0 + wh / 2, 674, 32, (1.0, 0.88, 0.20))
        if parts[1]:
            w1 = ctx.text_extents(parts[1]).x_advance
            text(ctx, parts[1], start_x + w0 + wh + w1 / 2, 674, 32, C['white'])

engine.subtitle = custom_sub

# ==================== 專屬道具繪製 ====================

def ai_chip(ctx, x, y, s=1.0):
    """AI GPU 算力晶片"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 綠色 PCB 電路板
    rrect(ctx, -70, -70, 140, 140, 8)
    ctx.set_source_rgb(0.08, 0.35, 0.2); ctx.fill_preserve()
    ctx.set_source_rgb(0.04, 0.18, 0.1); ctx.set_line_width(4); ctx.stroke()
    # 金手指接點
    for i in range(12):
        ctx.rectangle(-55 + i * 10, 62, 6, 8); ctx.set_source_rgb(0.95, 0.8, 0.2); ctx.fill()
    # 核心金屬散熱上蓋
    rrect(ctx, -45, -45, 90, 90, 4)
    ctx.set_source_rgb(0.2, 0.22, 0.25); ctx.fill_preserve()
    ctx.set_source_rgb(0.7, 0.75, 0.8); ctx.set_line_width(2); ctx.stroke()
    # 晶片字樣
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(18); ctx.move_to(-32, -5); ctx.set_source_rgb(0.2, 0.8, 0.4); ctx.show_text("AI GPU")
    ctx.set_font_size(12); ctx.move_to(-25, 20); ctx.set_source_rgb(0.8, 0.8, 0.8); ctx.show_text("400W TDP")
    ctx.restore()

def lightbulb_prop(ctx, x, y, s=1.0):
    """5W 發光燈泡"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 燈泡外框與發光黃球
    ctx.arc(0, -20, 40, 0, math.pi * 2)
    ctx.set_source_rgba(1.0, 0.9, 0.2, 0.85); ctx.fill_preserve()
    ctx.set_source_rgb(0.85, 0.7, 0.1); ctx.set_line_width(3); ctx.stroke()
    # 燈泡金屬螺口底座
    ctx.rectangle(-20, 20, 40, 25); ctx.set_source_rgb(0.6, 0.65, 0.7); ctx.fill()
    ctx.arc(0, 45, 12, 0, math.pi); ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.fill()
    # 發光光暈射線
    for a in range(0, 360, 45):
        rad = math.radians(a)
        ctx.move_to(math.cos(rad) * 48, -20 + math.sin(rad) * 48)
        ctx.line_to(math.cos(rad) * 62, -20 + math.sin(rad) * 62)
        ctx.set_source_rgba(1.0, 0.85, 0.2, 0.7); ctx.set_line_width(3); ctx.stroke()
    # 瓦數標籤
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16); ctx.move_to(-12, -14); ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.show_text("5W")
    ctx.restore()

def cloud_folder(ctx, x, y, s=1.0):
    """雲端硬碟檔案堆積"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 雲朵身
    ctx.arc(-30, -10, 32, 0, math.pi * 2); ctx.set_source_rgb(0.3, 0.65, 0.95); ctx.fill()
    ctx.arc(25, -15, 38, 0, math.pi * 2); ctx.fill()
    ctx.arc(0, -35, 30, 0, math.pi * 2); ctx.fill()
    ctx.rectangle(-40, -10, 80, 35); ctx.fill()
    # 雲下硬碟檔案圖示
    rrect(ctx, -50, 30, 100, 35, 6)
    ctx.set_source_rgb(0.85, 0.88, 0.92); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.25, 0.3); ctx.set_line_width(3); ctx.stroke()
    ctx.arc(-30, 47, 5, 0, math.pi * 2); ctx.set_source_rgb(0.2, 0.85, 0.4); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12); ctx.move_to(-15, 52); ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.show_text("DRIVE: 99% FULL")
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #004 雲端機房與 AI 算力大搜查", 640, 160, size=28)
        text(ctx, "敲幾行字，AI 正在燃燒電力", 640, 245, 52, (0.12, 0.12, 0.15))
        text(ctx, "螢幕背後的散熱風扇，藏著多少隱形碳排放？", 640, 310, 30, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        items = ["案發現場：全球 24 小時轟鳴運轉的超大規模雲端資料中心", "科技奇蹟：生成式 AI 幾秒生成報告，耗電卻是搜尋的十倍", "嫌疑目標：無感數位囤積、未最佳化的算力調用、高能耗冷卻"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "高能耗機密", 960, 175, ang=-0.14, s=1.05)

# 1 三條線索
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THREE CLUES 雲端算力線索板", 640, 75, size=26)
    t1, t2, t3 = ep.kw(1, "大型語言模型"), ep.kw(1, "數位囤積"), ep.kw(1, "綠色運算")

    cards = [
        (t1, 260, 340, -0.04, "01 問一次 AI 代價", ai_chip),
        (t2, 640, 330, 0.03, "02 雲端硬碟囤積", cloud_folder),
        (t3, 1020, 345, -0.03, "03 機房散熱黑洞", server_rack)
    ]
    pins = []
    for t_in, cx, cy, ang, title, drawer in cards:
        p = prog(u, t_in, 0.4)
        if p > 0:
            ctx.save(); pop(ctx, cx, cy, p)
            polaroid(ctx, cx, cy, 320, 360, ang, title)
            drawer(ctx, cx, cy - 30, 0.85)
            red_pin(ctx, cx, cy - 165)
            pins.append((cx, cy - 165))
            ctx.restore()

    if len(pins) >= 2:
        red_string(ctx, pins[0][0], pins[0][1], pins[1][0], pins[1][1], sag=18)
    if len(pins) >= 3:
        red_string(ctx, pins[1][0], pins[1][1], pins[2][0], pins[2][1], sag=-15)

# 2 迷思審訊
def s2(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "INTERROGATION 迷思審訊", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 840, 380, ang=0.012, bg=(0.98, 0.96, 0.92))
        text(ctx, "直覺迷思：虛擬資料哪來的碳排放？", 640, 210, 44, (0.85, 0.18, 0.15))
        text(ctx, "『雲端輕盈如空氣、硬碟容量無限大，怎麼可能有污染？』", 640, 275, 28, (0.3, 0.3, 0.35))

        # 雲朵問號圖示
        cloud_folder(ctx, 640, 350, 0.75)

        highlighter(ctx, 280, 445, 720, 45)
        text(ctx, "調查局警告：虛擬世界的所有位元，全靠實體電力燃燒支撐！", 640, 440, 26, (0.2, 0.2, 0.25))
        red_pin(ctx, 250, 180); red_pin(ctx, 1030, 180)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "嚴重誤解", 960, 180, ang=-0.16, s=1.1)

# 3 真相揭曉：問一次 AI 耗電 10 倍
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THE TWIST 調查大逆轉", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "翻開調查檔案：問一次 AI 的能耗真相", 640, 195, 34, (0.85, 0.15, 0.15))

        # 對比卡
        rrect(ctx, 230, 240, 380, 190, 12); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        text(ctx, "🔍 傳統 Google 搜尋", 420, 270, 24, (0.15, 0.5, 0.25))
        text(ctx, "檢索索引資料庫", 420, 310, 20, (0.3, 0.35, 0.35))
        chip(ctx, "約 0.3 瓦時 (Wh)", 420, 360, 1, C['green'], 22, C['white'])

        rrect(ctx, 670, 240, 380, 190, 12); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🤖 生成式 AI 提問", 860, 270, 24, (0.85, 0.2, 0.2))
        text(ctx, "數千億參數逐字矩陣運算", 860, 310, 20, (0.35, 0.3, 0.3))
        chip(ctx, "高達 3.0 瓦時 (Wh)", 860, 360, 1, C['red'], 22, C['white'])

        highlighter(ctx, 240, 465, 800, 48)
        text(ctx, "問一次 AI 耗電約為搜尋的十倍，等於點亮 5W 燈泡一小時！", 640, 460, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "耗電暴增 10倍", 950, 175, ang=-0.14, s=1.05)

# 4 第一站：訓練模型的五百噸碳排
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 01 頂級模型背後的碳足跡", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=0.01, bg=(0.97, 0.95, 0.91))
        text(ctx, "訓練一個大型模型，機房燒掉多少電？", 640, 195, 34, (0.85, 0.15, 0.15))

        # 數據卡片
        rrect(ctx, 230, 240, 400, 180, 10); ctx.set_source_rgb(0.92, 0.92, 0.95); ctx.fill()
        text(ctx, "⚡ 頂級 LLM 訓練耗電量", 430, 275, 22, (0.2, 0.25, 0.3))
        text(ctx, "數萬張 GPU 滿載運轉數月", 430, 315, 20, (0.35, 0.4, 0.45))
        text(ctx, "＝ 突破 1,000,000+ 度電", 430, 355, 22, (0.1, 0.45, 0.8))

        rrect(ctx, 670, 240, 380, 180, 10); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🔥 相當排放量換算", 860, 275, 22, (0.85, 0.2, 0.2))
        text(ctx, "排放超過 500 公噸 CO2e", 860, 315, 20, (0.4, 0.3, 0.3))
        chip(ctx, "相當於 100 輛汽車開一年！", 860, 360, 1, C['red'], 20, C['white'])

        highlighter(ctx, 240, 455, 800, 48)
        text(ctx, "算力背後是真實且巨大的發電廠煤炭與天然氣燃燒！", 640, 450, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "五百噸碳排", 950, 175, ang=-0.14, s=1.05)

# 5 第一站深入：生成圖片與企業日常累積
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "INFERENCE 日常推論累積效應", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.95, 0.91))
        text(ctx, "一張 AI 高清圖＝2 到 4 克碳", 640, 195, 34, (0.15, 0.2, 0.25))

        # 兩種推論對比
        rrect(ctx, 230, 240, 380, 170, 10); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
        text(ctx, "📝 純文字 Prompt 回答", 420, 270, 22, (0.1, 0.4, 0.7))
        text(ctx, "每次約 0.1 ~ 0.3 克碳", 420, 310, 20, (0.3, 0.35, 0.4))
        chip(ctx, "輕量級運算", 420, 355, 1, C['green'], 20, C['white'])

        rrect(ctx, 670, 240, 380, 170, 10); ctx.set_source_rgb(0.98, 0.93, 0.93); ctx.fill()
        text(ctx, "🎨 AI 生成高清圖像 / 影片", 860, 270, 22, (0.85, 0.2, 0.2))
        text(ctx, "每次 2 ~ 4 克 (達文字的 20 倍)", 860, 310, 20, (0.4, 0.3, 0.3))
        chip(ctx, "密集重負載算力", 860, 355, 1, C['red'], 20, C['white'])

        highlighter(ctx, 240, 445, 800, 48)
        text(ctx, "全公司每天呼叫數千次 AI，一年推論排碳同樣破公噸！", 640, 440, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "算力累積驚人", 950, 175, ang=-0.14, s=1.05)

# 6 第二站：雲端硬碟數位囤積症
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 02 雲端硬碟的數位囤積症", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.012, bg=(0.96, 0.95, 0.91))
        text(ctx, "陳年未用的檔案，正在機房裡發燙", 640, 190, 34, (0.85, 0.15, 0.15))

        reasons = [
            ("📁 90% 企業資料儲存超過 90 天未再打開", "冷資料長期佔用高耗能儲存體"),
            ("🎬 未壓縮的超大 4K 影片與重複備份", "資料中心為了可靠度儲存三份副本"),
            ("🔥 即使無人讀取，伺服器與硬碟依然 24 小時通電通風", "造成無意識的長期排碳黑洞")
        ]
        for i, (r_t, r_d) in enumerate(reasons):
            yy = 250 + i * 54
            rrect(ctx, 220, yy - 18, 840, 44, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, r_t, 460, yy + 6, 21, (0.2, 0.25, 0.3))
            text(ctx, r_d, 820, yy + 6, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 240, 465, 800, 45)
        text(ctx, "數位囤積不是免錢的！它把實體電力變成了無謂的廢熱！", 640, 460, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 155); red_pin(ctx, 1070, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "數位垃圾 DIGITAL", 950, 175, ang=-0.14, s=1.05)

# 7 機房冷卻與 PUE 廢熱真相
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "COOLING CRISIS 機房冷卻與廢熱真相", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 400, ang=0.015, bg=(0.98, 0.96, 0.93))
        text(ctx, "全球資料中心耗電量：已超越多數國家！", 640, 195, 34, (0.2, 0.2, 0.25))

        # 機櫃與冷卻插圖
        server_rack(ctx, 360, 330, 0.75)

        rrect(ctx, 500, 240, 520, 170, 10); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
        text(ctx, "❄️ 機房能源使用效率 (PUE 指標)", 760, 270, 22, (0.1, 0.4, 0.7))
        text(ctx, "伺服器每消耗 1 度電運算", 760, 305, 20, (0.3, 0.35, 0.4))
        text(ctx, "冷卻空調就要額外吃掉 0.3 ~ 0.8 度電！", 760, 340, 20, (0.85, 0.2, 0.2))
        chip(ctx, "冷卻系統是吃電巨獸", 760, 375, 1, C['red'], 18, C['white'])

        highlighter(ctx, 250, 445, 780, 45)
        text(ctx, "伺服器產生的龐大廢熱，讓冷卻水系統每天瘋狂吃電！", 640, 440, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "能耗怪獸 PUE", 960, 175, ang=-0.14, s=1.05)

# 8 第三站：綠色雲端革命
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 03 綠色雲端與高效架構", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.96, 0.92))
        text(ctx, "綠色運算三大解方：從能源到架構", 640, 195, 34, (0.15, 0.5, 0.25))

        pillars = [
            ("承諾 100% 綠電", "採購 RE100 認證機房", C['green']),
            ("小型專用模型 SLM", "參數量減半、能效倍增", (0.2, 0.5, 0.8)),
            ("端點邊緣運算 Edge", "減少遠程中心伺服器負擔", (0.9, 0.55, 0.1))
        ]
        for k, (t_box, d_box, col) in enumerate(pillars):
            cx = 320 + k * 320
            rrect(ctx, cx - 140, 250, 280, 140, 8); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
            chip(ctx, t_box, cx, 285, 1, col, 20, C['white'])
            text(ctx, d_box, cx, 345, 18, (0.3, 0.35, 0.4))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "用最聰明的演算法，打造最低碳的數位服務！", 640, 435, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "綠色轉型 GREEN", 960, 175, ang=-0.14, s=1.05)

# 9 數位大掃除行動
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "ACTION 企業數位大掃除具體行動", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=0.012, bg=(0.97, 0.95, 0.91))
        text(ctx, "定期清理冷資料：省下租金更減碳", 640, 195, 34, (0.2, 0.2, 0.25))

        actions = [
            ("🧹 定期封存與清理冷資料", "釋放過期檔案與重複雲端快照"),
            ("📦 採用高效壓縮格式儲存", "將無損檔案降維壓縮，減少儲存節點"),
            ("📉 退訂冗餘備份與殭屍伺服器", "立即減少 20~40% 雲端帳單支出")
        ]
        for i, (act, ben) in enumerate(actions):
            yy = 260 + i * 50
            rrect(ctx, 220, yy - 18, 840, 40, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, act, 440, yy + 5, 21, (0.15, 0.45, 0.25))
            text(ctx, ben, 820, yy + 5, 19, (0.45, 0.45, 0.5))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "不只能省下公司雲端租金，更能實質減少大量碳排放！", 640, 435, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "省錢減碳 WIN-WIN", 960, 175, ang=-0.14, s=1.05)

# 10 證物盤點
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "ANNUAL BALANCE 企業雲端年度碳帳本", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "證物盤點：年雲端碳排放總結算", 640, 190, 34, (0.15, 0.2, 0.25))

        rows = [
            ("🤖 AI 密集算力與推論", "1.5 公噸 CO2e", "快速暴增的新怪獸", (0.9, 0.55, 0.1)),
            ("📁 陳年冷資料與備份儲存", "2.2 公噸 CO2e", "隱形慢性囤積", (0.2, 0.5, 0.8)),
            ("❄️ 機房空調冷卻系統消耗", "3.5 公噸 CO2e", "最大能耗黑洞", C['red']),
        ]
        for k, (mode, amount, status, col) in enumerate(rows):
            yy = 250 + k * 56
            rrect(ctx, 230, yy - 18, 820, 45, 8); ctx.set_source_rgb(0.92, 0.93, 0.95); ctx.fill()
            text(ctx, mode, 380, yy + 7, 24, (0.2, 0.2, 0.25))
            chip(ctx, amount, 650, yy + 7, 1, col, 24, C['white'])
            text(ctx, status, 900, yy + 7, 20, col)

        highlighter(ctx, 250, 450, 780, 45)
        text(ctx, "一家中型重度數位化企業，一年雲端排碳突破七公噸！", 640, 445, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 150); red_pin(ctx, 1070, 150)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "年排破 7 噸", 950, 175, ang=-0.14, s=1.05)

# 11 結案報告
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    tt = T
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.98, 0.96, 0.92))
        text(ctx, "CASE #004 結案行動三原則", 640, 195, 34, (0.15, 0.2, 0.25))

        habits = [
            ("① 精準調用 AI：避免無謂浪費 Prompt", "減少冗餘算力", 1.0),
            ("② 半年數位大掃除：清空陳年冷資料", "省 30% 儲存碳排", 2.5),
            ("③ 優先採購 RE100 綠電資料中心", "實質綠色轉型", tt - 0.5)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "科技不斷進步，更要擁有負責的綠色算力！", 640, 450, 32, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    if u > tt - 0.3:
        red_stamp(ctx, "結案 CLOSED", 950, 200, ang=-0.16, s=1.15)

# 執行
run("of4", "辦公室碳冒險 EP4",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP4_雲端機房與AI算力真相.mp4",
    wipes={2, 4, 6, 8, 10, 11})
