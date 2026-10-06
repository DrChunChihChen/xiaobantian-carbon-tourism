"""辦公室碳冒險：CASE #005 總務採購風暴：電腦設備與廢棄物的生與死 (刑偵剪貼調查風格)"""
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
        "80%", "250 到 300 公斤", "兩千公里", "100 公斤", "十八公噸",
        "以租代買", "範疇三", "四到五年", "綠色採購", "循環經濟", "零廢棄", "生命週期"
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

def laptop_prop(ctx, x, y, s=1.0):
    """現代筆記型電腦 (展開)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 螢幕上蓋 (微仰角)
    rrect(ctx, -65, -75, 130, 85, 6)
    ctx.set_source_rgb(0.2, 0.22, 0.26); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.12, 0.15); ctx.set_line_width(3); ctx.stroke()
    # 螢幕顯示面
    ctx.rectangle(-57, -67, 114, 69)
    ctx.set_source_rgb(0.12, 0.45, 0.75); ctx.fill()
    ctx.rectangle(-45, -55, 50, 30); ctx.set_source_rgba(1, 1, 1, 0.35); ctx.fill()
    # 鍵盤機身底座 (梯形透視)
    ctx.move_to(-80, 20); ctx.line_to(80, 20); ctx.line_to(65, 10); ctx.line_to(-65, 10); ctx.close_path()
    ctx.set_source_rgb(0.75, 0.78, 0.82); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.35, 0.4); ctx.set_line_width(3); ctx.stroke()
    # 觸控板
    ctx.rectangle(-18, 12, 36, 6); ctx.set_source_rgb(0.65, 0.68, 0.72); ctx.fill()
    ctx.restore()

def office_chair(ctx, x, y, s=1.0):
    """人體工學辦公椅"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 椅背
    rrect(ctx, -28, -75, 56, 65, 12)
    ctx.set_source_rgb(0.2, 0.25, 0.3); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.12, 0.15); ctx.set_line_width(3); ctx.stroke()
    # 椅墊
    rrect(ctx, -34, -10, 68, 18, 6)
    ctx.set_source_rgb(0.25, 0.3, 0.35); ctx.fill()
    # 氣壓桿與五星輪底座
    ctx.rectangle(-4, 8, 8, 25); ctx.set_source_rgb(0.6, 0.65, 0.7); ctx.fill()
    ctx.move_to(-35, 33); ctx.line_to(35, 33); ctx.set_source_rgb(0.2, 0.2, 0.25); ctx.set_line_width(4); ctx.stroke()
    for wx in (-35, 0, 35):
        ctx.arc(wx, 36, 5, 0, math.pi * 2); ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.fill()
    ctx.restore()

def water_bottle(ctx, x, y, s=1.0):
    """一次性塑膠瓶裝水"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 瓶身
    rrect(ctx, -18, -40, 36, 80, 8)
    ctx.set_source_rgba(0.5, 0.8, 0.95, 0.6); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.5, 0.7); ctx.set_line_width(2.5); ctx.stroke()
    # 瓶蓋
    ctx.rectangle(-10, -52, 20, 12); ctx.set_source_rgb(0.15, 0.5, 0.85); ctx.fill()
    # 標籤腰帶
    ctx.rectangle(-18, -10, 36, 25); ctx.set_source_rgb(0.2, 0.65, 0.9); ctx.fill()
    # 禁用水滴符號
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(14); ctx.move_to(-12, 8); ctx.set_source_rgb(1, 1, 1); ctx.show_text("H2O")
    ctx.restore()

def circular_loop(ctx, x, y, s=1.0):
    """循環經濟綠色箭頭環"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.arc(0, 0, 45, 0, math.pi * 1.6)
    ctx.set_source_rgb(0.15, 0.65, 0.3); ctx.set_line_width(12); ctx.stroke()
    # 箭頭尖角
    ctx.move_to(0, -45); ctx.line_to(-15, -60); ctx.line_to(-15, -30); ctx.close_path()
    ctx.set_source_rgb(0.15, 0.65, 0.3); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(14); ctx.move_to(-22, 5); ctx.set_source_rgb(0.15, 0.5, 0.25); ctx.show_text("RECYCLE")
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #005 總務採購風暴大搜查", 640, 160, size=28)
        text(ctx, "每年開工，倉庫角落的設備墓場", 640, 245, 50, (0.12, 0.12, 0.15))
        text(ctx, "整批汰換的新電腦，隱藏了什麼碳排放秘密？", 640, 310, 30, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        items = ["案發現場：堆滿舊螢幕、舊主機與散架辦公桌的總務庫房", "採購盲點：只在乎用電標章，卻忽視製造與廢棄端的龐大排碳", "核心震撼：一台電腦 80% 的碳排放，出廠那一刻就註定了！"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "採購漏洞", 960, 215, ang=-0.14, s=1.05)

# 1 三條線索
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THREE CLUES 硬體生命週期線索板", 640, 75, size=26)
    t1 = 0.5; t2 = ep.kw(1, "辦公家具") - 0.8; t3 = ep.kw(1, "循環經濟") - 1.2

    cards = [
        (t1, 260, 340, -0.04, "01 製造隱形碳足跡", laptop_prop),
        (t2, 640, 330, 0.03, "02 廉價家具拋棄潮", office_chair),
        (t3, 1020, 345, -0.03, "03 以租代買新循環", circular_loop)
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
        text(ctx, "直覺迷思：電腦下班關機就沒碳排了？", 640, 210, 36, (0.85, 0.18, 0.15))
        text(ctx, "『碳排放不就是插座上的用電嗎？只要省電，兩年換一台有差嗎？』", 640, 275, 26, (0.3, 0.3, 0.35))

        # 電腦插頭圖示
        laptop_prop(ctx, 640, 350, 0.75)

        highlighter(ctx, 280, 445, 720, 45)
        text(ctx, "調查局警告：真正的碳巨獸，早在你拆開包裝前就已經誕生！", 640, 440, 26, (0.2, 0.2, 0.25))
        red_pin(ctx, 250, 180); red_pin(ctx, 1030, 180)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "致命盲點", 960, 180, ang=-0.16, s=1.1)

# 3 真相揭曉：出廠前排完 80%
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THE TWIST 調查大逆轉", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "翻開調查檔案：筆電終生碳排結構解密", 640, 195, 34, (0.85, 0.15, 0.15))

        # 比例對比卡
        rrect(ctx, 230, 240, 380, 190, 12); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🏭 採礦、晶圓代工與組裝製造", 420, 270, 22, (0.85, 0.2, 0.2))
        text(ctx, "高溫煉製、稀土開採、無塵室", 420, 310, 20, (0.4, 0.3, 0.3))
        chip(ctx, "高達 75% ~ 80% 碳排", 420, 360, 1, C['red'], 22, C['white'])

        rrect(ctx, 670, 240, 380, 190, 12); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        text(ctx, "🔌 四年日常開機辦公用電", 860, 270, 22, (0.15, 0.5, 0.25))
        text(ctx, "低功耗高效能處理器插座耗電", 860, 310, 20, (0.3, 0.35, 0.35))
        chip(ctx, "僅佔 20% ~ 25% 碳排", 860, 360, 1, C['green'], 22, C['white'])

        highlighter(ctx, 240, 465, 800, 48)
        text(ctx, "筆電 80% 碳排在出廠時就已排完！延長使用年限才是減碳關鍵！", 640, 460, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "出廠即排 80%", 960, 215, ang=-0.14, s=1.05)

# 4 第一站：製造一台筆電的代價
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 01 一台筆電的隱形製造代價", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=0.01, bg=(0.97, 0.95, 0.91))
        text(ctx, "造一台商務筆電：排碳 250 到 300 公斤", 640, 195, 34, (0.85, 0.15, 0.15))

        # 換算卡片
        rrect(ctx, 230, 240, 400, 180, 10); ctx.set_source_rgb(0.92, 0.92, 0.95); ctx.fill()
        text(ctx, "💻 單機隱含碳排放 (Embodied)", 430, 275, 22, (0.2, 0.25, 0.3))
        text(ctx, "主機板、晶片半導體與金屬外殼", 430, 315, 20, (0.35, 0.4, 0.45))
        chip(ctx, "平均 250 ~ 300 kg CO2e", 430, 360, 1, C['red'], 20, C['white'])

        rrect(ctx, 670, 240, 380, 180, 10); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🚗 等同汽車行駛里程換算", 860, 275, 22, (0.85, 0.2, 0.2))
        text(ctx, "相當於開著燃油汽車", 860, 315, 20, (0.4, 0.3, 0.3))
        text(ctx, "行駛整整 2,000 公里！", 860, 355, 28, C['red'])

        highlighter(ctx, 240, 455, 800, 48)
        text(ctx, "每買一台新筆電，就等於讓一輛汽車環島開兩整圈！", 640, 450, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "等同開 2,000 km", 960, 215, ang=-0.14, s=1.05)

# 5 第一站深入：盲目二年一換的惡果
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "IMPACT 頻繁換新的企業碳包袱", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.95, 0.91))
        text(ctx, "每兩年整批淘汰：年年背負製造碳債", 640, 195, 34, (0.15, 0.2, 0.25))

        # 對比卡
        rrect(ctx, 230, 240, 380, 170, 10); ctx.set_source_rgb(0.98, 0.93, 0.93); ctx.fill()
        text(ctx, "❌ 每 2 年換新筆電", 420, 270, 22, (0.85, 0.2, 0.2))
        text(ctx, "每人每年分攤製造碳排", 420, 310, 20, (0.4, 0.3, 0.3))
        chip(ctx, "130 kg / 年・人", 420, 355, 1, C['red'], 20, C['white'])

        rrect(ctx, 670, 240, 380, 170, 10); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
        text(ctx, "✅ 延役至 4~5 年換新", 860, 270, 22, (0.15, 0.5, 0.25))
        text(ctx, "每人每年分攤製造碳排", 860, 310, 20, (0.3, 0.35, 0.4))
        chip(ctx, "僅 55 kg / 年・人 (減半！)", 860, 355, 1, C['green'], 20, C['white'])

        highlighter(ctx, 240, 445, 800, 48)
        text(ctx, "盲目追求最新規格，讓每位員工每年多背上百公斤製造碳債！", 640, 440, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "碳排直接翻倍", 960, 215, ang=-0.14, s=1.05)

# 6 第二站：廉價密集板家具與雜物
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 02 辦公家具與雜物的短命悲歌", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.012, bg=(0.96, 0.95, 0.91))
        text(ctx, "快時尚家具與一次性耗材：焚化爐黑洞", 640, 190, 34, (0.85, 0.15, 0.15))

        losses = [
            ("🪑 廉價密集板辦公桌椅", "使用 3~5 年即變形損壞，無法維修直送焚化爐"),
            ("💧 會議室整箱瓶裝水與塑膠杯", "每場會議產生數十個空瓶，塑料生命週期高排碳"),
            ("🖊️ 隨手丟棄的拋棄式原子筆與耗材", "低價大量採購，缺乏回收循環，造成隱形範疇三漏斗")
        ]
        for i, (l_t, l_d) in enumerate(losses):
            yy = 250 + i * 54
            rrect(ctx, 220, yy - 18, 840, 44, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, l_t, 460, yy + 6, 21, (0.2, 0.25, 0.3))
            text(ctx, l_d, 820, yy + 6, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 240, 465, 800, 45)
        text(ctx, "總務隨手採購的廉價消耗品，正是企業永續的最大盲區！", 640, 460, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 155); red_pin(ctx, 1070, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "採購大黑洞", 960, 215, ang=-0.14, s=1.05)

# 7 範疇三排放真相
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SCOPE 3 企業範疇三供應鏈排放真相", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 400, ang=0.015, bg=(0.98, 0.96, 0.93))
        text(ctx, "採購物品與設備：佔企業碳足跡 70%！", 640, 195, 34, (0.2, 0.2, 0.25))

        # 瓶裝水與椅子圖示
        water_bottle(ctx, 350, 330, 0.8)

        rrect(ctx, 470, 240, 550, 170, 10); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
        text(ctx, "📦 範疇三 (Scope 3) 資本財與採購", 740, 270, 22, (0.1, 0.4, 0.7))
        text(ctx, "多數企業只盤查辦公室用電 (範疇二)", 740, 305, 20, (0.3, 0.35, 0.4))
        text(ctx, "卻漏算了採購供應鏈高達 70% 的製造碳排！", 740, 340, 20, (0.85, 0.2, 0.2))
        chip(ctx, "供應鏈採購是真正核心", 740, 375, 1, C['red'], 18, C['white'])

        highlighter(ctx, 250, 445, 780, 45)
        text(ctx, "不改採購習慣，任何企業碳中和宣示都只是口號！", 640, 440, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "範疇三核心", 960, 215, ang=-0.14, s=1.05)

# 8 第三站：循環辦公室第一招：延役升級
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 03 循環辦公室第一招：升級延役", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.96, 0.92))
        text(ctx, "模組化升級：筆電壽命延長至四到五年", 640, 195, 34, (0.15, 0.5, 0.25))

        pillars = [
            ("擴充 RAM 與 SSD", "以十分之一成本換來滿血效能", (0.2, 0.5, 0.8)),
            ("官方電池保養更換", "徹底解決續航衰退問題", C['green']),
            ("延役至 5 年汰換", "單機製造碳排直接減半！", (0.9, 0.55, 0.1))
        ]
        for k, (t_box, d_box, col) in enumerate(pillars):
            cx = 320 + k * 320
            rrect(ctx, cx - 140, 250, 280, 140, 8); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
            chip(ctx, t_box, cx, 285, 1, col, 20, C['white'])
            text(ctx, d_box, cx, 345, 18, (0.3, 0.35, 0.4))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "讓設備物盡其用，就是對地球最直接的實質保護！", 640, 435, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "壽命延長 5年", 960, 215, ang=-0.14, s=1.05)

# 9 循環第二招：以租代買 DaaS
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CIRCULAR ACTION 第二招：以租代買與循環家具", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=0.012, bg=(0.97, 0.95, 0.91))
        text(ctx, "設備即服務 (DaaS)：供應商全權回收翻新", 640, 195, 34, (0.2, 0.2, 0.25))

        actions = [
            ("🔄 導入電腦設備租賃服務 (DaaS)", "由原廠統一翻新、再利用、零件拆解零掩埋"),
            ("🪑 採購模組化與環保標章家具", "損壞只換單一零件，壽命長達十年以上"),
            ("☕ 茶水間全面設置飲水機與玻璃杯", "徹底終結會議瓶裝水，一年省下上萬瓶廢塑")
        ]
        for i, (act, ben) in enumerate(actions):
            yy = 260 + i * 50
            rrect(ctx, 220, yy - 18, 840, 40, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, act, 440, yy + 5, 21, (0.15, 0.45, 0.25))
            text(ctx, ben, 820, yy + 5, 19, (0.45, 0.45, 0.5))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "推動以租代買與循環採購，邁向真正的零廢棄辦公室！", 640, 435, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "零廢棄循環", 960, 215, ang=-0.14, s=1.05)

# 10 證物盤點
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "ANNUAL BALANCE 企業總務採購年度碳帳本", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "證物盤點：年總務採購端碳排總結算", 640, 190, 34, (0.15, 0.2, 0.25))

        rows = [
            ("💻 IT 硬體新購與製造分攤", "12 公噸 CO2e", "採購端最大排碳宗", C['red']),
            ("🪑 辦公家具頻繁汰舊換新", "4 公噸 CO2e", "短命快家具惡果", (0.9, 0.55, 0.1)),
            ("🥤 會議瓶裝水與拋棄式耗材", "2 公噸 CO2e", "微小累積的常態浪費", (0.2, 0.5, 0.8)),
        ]
        for k, (mode, amount, status, col) in enumerate(rows):
            yy = 250 + k * 56
            rrect(ctx, 230, yy - 18, 820, 45, 8); ctx.set_source_rgb(0.92, 0.93, 0.95); ctx.fill()
            text(ctx, mode, 380, yy + 7, 24, (0.2, 0.2, 0.25))
            chip(ctx, amount, 650, yy + 7, 1, col, 24, C['white'])
            text(ctx, status, 900, yy + 7, 20, col)

        highlighter(ctx, 250, 450, 780, 45)
        text(ctx, "一家中小企業採購端一年的隱形排碳，竟高達整整十八公噸！", 640, 445, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 150); red_pin(ctx, 1070, 150)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "年排高達 18 噸", 960, 215, ang=-0.14, s=1.05)

# 11 結案報告
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    tt = T
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.98, 0.96, 0.92))
        text(ctx, "CASE #005 結案行動三原則", 640, 195, 34, (0.15, 0.2, 0.25))

        habits = [
            ("① 硬體延役升級：換 SSD 電池延長壽命", "製造碳排砍半", 1.0),
            ("② 全面導入 DaaS：以租代買循環翻新", "零廢棄物掩埋", 2.5),
            ("③ 茶水間零瓶裝水：全面自備環保杯", "年省萬個塑膠瓶", tt - 0.5)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "綠色採購，是企業最具力量的減碳實踐！", 640, 450, 32, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    if u > tt - 0.3:
        red_stamp(ctx, "結案 CLOSED", 950, 200, ang=-0.16, s=1.15)

# 執行
run("of5", "辦公室碳冒險 EP5",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP5_總務設備與採購風暴.mp4",
    wipes={2, 4, 6, 8, 10, 11})
