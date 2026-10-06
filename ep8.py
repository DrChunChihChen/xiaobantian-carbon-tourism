"""碳導遊小綠・EP8：買碳權就能零碳？旅行社的淨零真相 (1930s 復古橡皮管直式短影音風格)"""
import engine
# 設定為直式 9:16 短影音格式
engine.W = 720
engine.H = 1280
from engine import *
from rubberhose import *

# 復古橡皮管風格圓形遮罩色票 (米褐、復古綠、紅)
engine.WIPE = [(0.28, 0.62, 0.40), (0.85, 0.22, 0.18), (0.35, 0.22, 0.14), (0.28, 0.62, 0.40)]

def run(name, tag, scenes, out, wipes=None):
    ep = Episode(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), tag)
    ep.scenes = scenes; ep.wipes = wipes
    ep.run(out, sys.argv)

def vertical_sub(ctx, s):
    """直式影片專用字幕：置中偏底部 (y=1160)，黑底圓角膠囊，關鍵詞鮮黃高亮"""
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(30)
    ext = ctx.text_extents(s)
    w = ext.width
    rrect(ctx, 360 - w / 2 - 24, 1140, w + 48, 52, 16)
    ctx.set_source_rgba(0.10, 0.10, 0.12, 0.92); ctx.fill()

    highlights = ["零碳旅行團", "漂綠", "碳權", "一公噸", "減碳階梯", "自主減碳", "ISO 14068", "免死金牌", "補考抵換", "大問題", "大地雷"]
    found_hl = None
    for h in highlights:
        if h in s:
            found_hl = h
            break

    if not found_hl:
        text(ctx, s, 360, 1166, 30, C['white'])
    else:
        parts = s.split(found_hl, 1)
        w0 = ctx.text_extents(parts[0]).x_advance
        wh = ctx.text_extents(found_hl).x_advance
        start_x = 360 - w / 2
        if parts[0]:
            text(ctx, parts[0], start_x + w0 / 2, 1166, 30, C['white'])
        text(ctx, found_hl, start_x + w0 + wh / 2, 1166, 30, (1.0, 0.88, 0.22))
        if parts[1]:
            w1 = ctx.text_extents(parts[1]).x_advance
            text(ctx, parts[1], start_x + w0 + wh + w1 / 2, 1166, 30, C['white'])

engine.subtitle = vertical_sub

# ==================== 專屬道具元件 ====================

def retro_scale(ctx, x, y, s=1.0, tilt=0.0):
    """復古黃銅天平"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 底座與中柱
    ctx.rectangle(-50, 110, 100, 20); ctx.set_source_rgb(0.4, 0.35, 0.25); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
    ctx.rectangle(-8, -25, 16, 135); ctx.set_source_rgb(0.75, 0.65, 0.3); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    ctx.arc(0, -25, 14, 0, 2 * math.pi); ctx.set_source_rgb(0.9, 0.8, 0.35); ctx.fill()
    # 橫梁
    ctx.save(); ctx.translate(0, -25); ctx.rotate(tilt)
    ctx.rectangle(-140, -6, 280, 12); ctx.set_source_rgb(0.75, 0.65, 0.3); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    for sd in (-125, 125):
        ctx.arc(sd, 0, 6, 0, 2 * math.pi); ctx.set_source_rgb(0.9, 0.8, 0.35); ctx.fill()
    ctx.restore()
    # 左右秤盤 (鉛垂垂掛)
    rad = tilt
    p1x, p1y = -125 * math.cos(rad), -25 - 125 * math.sin(rad)
    p2x, p2y = 125 * math.cos(rad), -25 + 125 * math.sin(rad)
    for px, py in [(p1x, p1y), (p2x, p2y)]:
        ctx.move_to(px, py); ctx.line_to(px - 35, py + 80); ctx.set_source_rgb(0.2, 0.2, 0.22); ctx.set_line_width(2.5); ctx.stroke()
        ctx.move_to(px, py); ctx.line_to(px + 35, py + 80); ctx.stroke()
        ctx.save(); ctx.translate(px, py + 80); ctx.scale(1, 0.3)
        ctx.arc(0, 0, 48, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(0.85, 0.75, 0.4); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()

def retro_cert(ctx, x, y, s=1.0):
    """復古花邊碳權證書"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.rectangle(-130, -90, 260, 180)
    ctx.set_source_rgb(0.97, 0.95, 0.88); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()
    # 內框花邊
    ctx.rectangle(-118, -78, 236, 156)
    ctx.set_source_rgb(0.35, 0.22, 0.14); ctx.set_line_width(2.5); ctx.stroke()
    # 證書文字
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24); ctx.move_to(-70, -40)
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.show_text("CARBON CREDIT")
    ctx.set_font_size(18); ctx.move_to(-55, -15)
    ctx.set_source_rgb(0.4, 0.4, 0.45); ctx.show_text("國際核發減量憑證")
    # 數額
    rrect(ctx, -85, 8, 170, 40, 8); ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill()
    ctx.set_font_size(22); ctx.move_to(-65, 36)
    ctx.set_source_rgb(1, 1, 1); ctx.show_text("1 tCO2e 額度")
    # 紅色火漆蠟封印章
    ctx.arc(80, 50, 24, 0, 2 * math.pi)
    ctx.set_source_rgb(0.85, 0.2, 0.15); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(2.5); ctx.stroke()
    ctx.arc(80, 50, 16, 0, 2 * math.pi); ctx.set_source_rgb(0.95, 0.85, 0.25); ctx.fill()
    ctx.restore()

def iso_shield(ctx, x, y, s=1.0):
    """金色 ISO 守護盾牌"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(0, -90); ctx.line_to(75, -60); ctx.line_to(65, 30)
    ctx.curve_to(55, 75, 0, 100, 0, 100)
    ctx.curve_to(0, 100, -55, 75, -65, 30); ctx.line_to(-75, -60); ctx.close_path()
    ctx.set_source_rgb(0.95, 0.82, 0.28); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24); ctx.move_to(-25, -15)
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.show_text("ISO")
    ctx.set_font_size(22); ctx.move_to(-40, 20)
    ctx.show_text("14068")
    ctx.restore()

# ==================== 場景定義 (S0 ～ S12) ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    tq, tm_ = ep.kw(0, "大問題"), ep.kw(0, "花錢消滅")
    # 小綠在畫面中間偏左下
    retro_xiaolu(ctx, 230, 780, 1.25, T, m, wave=True)
    # 復古主題黑板 (上方)
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 360, p)
        retro_blackboard(ctx, 360, 360, 600, 340, title="碳導遊小綠・第 8 集")
        ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(44); ctx.move_to(160, 360)
        ctx.set_source_rgb(1.0, 0.88, 0.25); ctx.show_text("買碳權就能零碳？")
        ctx.set_font_size(28); ctx.move_to(220, 420)
        ctx.set_source_rgb(0.95, 0.95, 0.92); ctx.show_text("旅行社的淨零真相")
        ctx.restore()
    # 飛走帶翅膀的金幣？
    q = prog(u, tm_ - 0.2, 0.4)
    if q > 0:
        ctx.save(); pop(ctx, 520, 660, q)
        ctx.arc(520, 660, 36, 0, 2 * math.pi); ctx.set_source_rgb(0.95, 0.82, 0.25); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
        text(ctx, "$", 520, 672, 36, (0.1, 0.1, 0.12))
        shout_bubble(ctx, "花錢就搞定？", 540, 580, 180, 60)
        ctx.restore()

# 1 路線圖
def s1(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    t1, t2, t3 = ep.kw(1, "碳權與碳抵換"), ep.kw(1, "減碳第一"), ep.kw(1, "避開漂綠")
    retro_xiaolu(ctx, 160, 960, 1.0, T, m, point=True)
    # 黑板上列出 3 站
    retro_blackboard(ctx, 360, 430, 620, 680, title="TODAY'S 3 STATIONS")
    stations = [("① 什麼是碳權與碳抵換？", t1, (0.95, 0.85, 0.25)),
                 ("② 減碳第一，抵換墊後", t2, (0.45, 0.85, 0.55)),
                 ("③ 避開「漂綠」陷阱", t3, (0.95, 0.45, 0.40))]
    for k, (name, t0, col) in enumerate(stations):
        p = prog(u, t0 - 0.2, 0.45)
        if p > 0:
            yy = 260 + k * 180
            ctx.save(); pop(ctx, 360, yy, p)
            rrect(ctx, 100, yy - 50, 520, 100, 20)
            ctx.set_source_rgba(*col, 0.25); ctx.fill_preserve()
            ctx.set_source_rgb(*col); ctx.set_line_width(3.5); ctx.stroke()
            text(ctx, name, 360, yy + 10, 32, col)
            ctx.restore()

# 2 老闆發問 (阿德配音)
def s2(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    t28, tz = ep.kw(2, "28 公斤"), ep.kw(2, "零碳旅行團")
    # 左側老闆抓頭困惑
    retro_boss(ctx, 270, 780, 1.25, T, m, puzzled=True)
    # 浮現困惑對話框
    q = prog(u, t28 - 0.3, 0.4)
    if q > 0:
        ctx.save(); pop(ctx, 450, 430, q)
        shout_bubble(ctx, "買 28 kg 碳權抵銷，\n宣傳「零碳旅行團」？", 450, 430, 380, 140)
        ctx.restore()
    # 小綠在右下微笑聆聽
    retro_xiaolu(ctx, 580, 860, 0.85, T, 0)

# 3 小綠解答：小心漂綠地雷！
def s3(ep, ctx, u, T, m):
    action_rays(ctx, 360, 580, u)
    tg = ep.kw(3, "漂綠")
    retro_xiaolu(ctx, 230, 800, 1.25, T, m, point=True)
    retro_boss(ctx, 540, 820, 1.1, T, 0, puzzled=True)
    # 巨大漂綠地雷
    p = prog(u, tg - 0.3, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 360, p)
        # 黑色炸彈
        ctx.arc(360, 360, 100, 0, 2 * math.pi)
        ctx.set_source_rgb(0.12, 0.12, 0.15); ctx.fill_preserve()
        ctx.set_source_rgb(0.85, 0.2, 0.15); ctx.set_line_width(6); ctx.stroke()
        # 點火引信
        ctx.move_to(360, 260); ctx.curve_to(390, 220, 370, 190, 410, 180)
        ctx.set_source_rgb(0.4, 0.3, 0.2); ctx.set_line_width(6); ctx.stroke()
        ctx.arc(410, 180, 10, 0, 2 * math.pi); ctx.set_source_rgb(1.0, 0.8, 0.2); ctx.fill()
        text(ctx, "漂綠陷阱", 360, 345, 38, (1, 1, 1))
        text(ctx, "GREENWASHING", 360, 395, 20, (0.85, 0.2, 0.15))
        ctx.restore()

# 4 第一站：什麼是碳權與抵換？
def s4(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    retro_blackboard(ctx, 360, 260, 620, 260, title="第一站：什麼是碳抵換？")
    tt, tf = ep.kw(4, "植樹造林"), ep.kw(4, "風力發電")
    # 天平傾角
    p = prog(u, 0.2, 0.5)
    tilt = -0.18 * (1 - ease_out(prog(u, tt - 0.2, 0.6)))
    retro_scale(ctx, 360, 580, 1.35, tilt=tilt)
    # 左側：旅行社排碳 (灰色氣泡)
    text(ctx, "自家行程排碳", 200, 680, 24, (0.85, 0.2, 0.15))
    # 右側：造林與風電專案
    q = prog(u, tt - 0.2, 0.4)
    if q > 0:
        text(ctx, "投資植樹與綠能", 520, 680, 24, (0.28, 0.62, 0.40))
        shout_bubble(ctx, "吸收抵扣！", 520, 480, 180, 60)
    retro_xiaolu(ctx, 160, 960, 1.0, T, m, wave=True)

# 5 第一站續：一公噸碳權憑證
def s5(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    t1, tc = ep.kw(5, "一公噸"), ep.kw(5, "碳權")
    retro_blackboard(ctx, 360, 240, 620, 220, title="國際認證碳信用 (Carbon Credit)")
    # 巨大證書彈出
    p = prog(u, t1 - 0.3, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 560, p)
        retro_cert(ctx, 360, 560, 1.4)
        ctx.restore()
    # 底部說明文字
    q = prog(u, tc - 0.2, 0.4)
    if q > 0:
        rrect(ctx, 80, 760, 560, 90, 16)
        ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
        text(ctx, "一單位碳權 ＝ 減少 1,000 kg CO2e", 360, 810, 28, (0.1, 0.1, 0.12))
    retro_xiaolu(ctx, 180, 990, 0.9, T, m)

# 6 第二站：減碳階梯原則
def s6(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    retro_blackboard(ctx, 360, 220, 620, 180, title="第二站：減碳階梯原則")
    ts1, ts2, ts3 = ep.kw(6, "第一步是盤查"), ep.kw(6, "自主減碳"), ep.kw(6, "才能用抵換")

    # 三階木質樓梯
    steps = [
        ("① 完整碳盤查 (Measure)", 780, ts1, (0.85, 0.75, 0.3)),
        ("② 自主實質減量 90% (Reduce)", 620, ts2, (0.28, 0.62, 0.40)),
        ("③ 殘餘碳額抵換 10% (Offset)", 460, ts3, (0.85, 0.2, 0.15))
    ]
    for name, yy, t0, col in steps:
        p = prog(u, t0 - 0.25, 0.45)
        if p > 0:
            ctx.save(); pop(ctx, 360, yy, p)
            rrect(ctx, 90, yy - 45, 540, 90, 16)
            ctx.set_source_rgba(*col, 0.2); ctx.fill_preserve()
            ctx.set_source_rgb(*col); ctx.set_line_width(4); ctx.stroke()
            text(ctx, name, 360, yy + 8, 30, (0.1, 0.1, 0.12))
            ctx.restore()

    shout_bubble(ctx, "不能直接跳關！", 500, 360, 220, 60)
    retro_xiaolu(ctx, 160, 980, 0.95, T, m, point=True)

# 7 第二站續：便宜碳權的漂綠危機
def s7(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    tb, t18, tg = ep.kw(7, "繼續怠速"), ep.kw(7, "18 度"), ep.kw(7, "標準的漂綠")
    retro_blackboard(ctx, 360, 260, 620, 280, title="不良示範：假淨零真漂綠")
    text(ctx, "• 遊覽車全程怠速不熄火", 360, 260, 28, (0.95, 0.95, 0.92))
    text(ctx, "• 門市冷氣開 18 度吹整天", 360, 310, 28, (0.95, 0.95, 0.92))
    text(ctx, "• 卻花小錢買劣質碳權抵換", 360, 360, 28, (0.95, 0.85, 0.25))

    # 大紅叉與印章
    p = prog(u, tg - 0.3, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 360, 580, p)
        rrect(ctx, 100, 520, 520, 120, 20)
        ctx.set_source_rgb(0.85, 0.15, 0.15); ctx.fill()
        text(ctx, "× 劣質假淨零：漂綠！", 360, 585, 38, (1, 1, 1))
        ctx.restore()

    retro_boss(ctx, 520, 800, 1.15, T, 0, puzzled=True)
    retro_xiaolu(ctx, 200, 800, 1.15, T, m, point=True)

# 8 第三站：ISO 14068 標準守護
def s8(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    tiso, tc = ep.kw(8, "ISO 14068"), ep.kw(8, "不能只靠買碳權")
    retro_blackboard(ctx, 360, 240, 620, 220, title="第三站：ISO 14068 國際標準")
    # 金色盾牌
    p = prog(u, tiso - 0.3, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 540, p)
        iso_shield(ctx, 360, 540, 1.4)
        ctx.restore()
    # 承諾底牌
    q = prog(u, tc - 0.2, 0.4)
    if q > 0:
        rrect(ctx, 80, 720, 560, 110, 18)
        ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
        text(ctx, "碳中和必須承諾「持續實質減量」", 360, 765, 26, (0.1, 0.1, 0.12))
        text(ctx, "絕對不得純靠購買碳權宣稱！", 360, 805, 26, (0.85, 0.2, 0.15))
    retro_xiaolu(ctx, 160, 990, 0.9, T, m)

# 9 第三站續：三大合格檢核卡
def s9(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    t1, t2, t3 = ep.kw(9, "額外性"), ep.kw(9, "永久性"), ep.kw(9, "不可重複計算")
    retro_blackboard(ctx, 360, 200, 620, 140, title="優質碳權三大黃金檢驗")

    checks = [
        ("① 額外性 (Additionality)", "沒這筆錢，減量專案就不會發生", t1),
        ("② 永久性 (Permanence)", "碳封存必須穩定，不會隨便流失", t2),
        ("③ 防重複 (No Double Count)", "序號唯一註銷，絕不可一女二嫁", t3)
    ]
    for k, (title, sub, t0) in enumerate(checks):
        p = prog(u, t0 - 0.25, 0.45)
        if p > 0:
            yy = 400 + k * 160
            ctx.save(); pop(ctx, 360, yy, p)
            rrect(ctx, 80, yy - 60, 560, 120, 18)
            ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
            ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.set_line_width(4); ctx.stroke()
            text(ctx, title, 360, yy - 15, 28, (0.1, 0.1, 0.12))
            text(ctx, sub, 360, yy + 25, 22, (0.4, 0.4, 0.45))
            # 綠色打勾
            ctx.arc(580, yy, 22, 0, 2 * math.pi); ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill()
            text(ctx, "✓", 580, yy + 8, 28, (1, 1, 1))
            ctx.restore()
    retro_xiaolu(ctx, 160, 990, 0.85, T, m)

# 10 聰明的旅行社做法
def s10(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    te, th, tr = ep.kw(10, "電動遊覽車"), ep.kw(10, "環保旅宿"), ep.kw(10, "高品質抵換")
    retro_blackboard(ctx, 360, 220, 620, 180, title="旅行社淨零正道四部曲")

    items = [
        ("🚌 換乘電動或大眾運具", te, 430),
        ("🏨 嚴選環保標章旅宿", th, 550),
        ("🌱 全團自備備品不塑", tr - 0.3, 670),
        ("📜 最後採購認證碳權抵換", tr, 790)
    ]
    for lab, t0, yy in items:
        p = prog(u, t0 - 0.2, 0.45)
        if p > 0:
            ctx.save(); pop(ctx, 360, yy, p)
            rrect(ctx, 100, yy - 45, 520, 90, 16)
            ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill()
            text(ctx, lab, 360, yy + 8, 28, (1, 1, 1))
            ctx.restore()
    retro_xiaolu(ctx, 160, 980, 0.95, T, m, wave=True)

# 11 老闆頓悟 (阿德配音)
def s11(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    tm_, ts = ep.kw(11, "免死金牌"), ep.kw(11, "補考抵換")
    # 老闆頭頂大燈泡！
    retro_boss(ctx, 360, 780, 1.3, T, m, happy=True, wave=True)
    # 巨大金牌打叉「碳權 ≠ 免死金牌」
    p = prog(u, tm_ - 0.3, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 360, p)
        rrect(ctx, 120, 280, 480, 160, 24)
        ctx.set_source_rgb(0.95, 0.85, 0.25); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()
        text(ctx, "碳權 不是 免死金牌！", 360, 345, 36, (0.85, 0.15, 0.15))
        text(ctx, "先流汗減碳，最後才能補考", 360, 400, 26, (0.2, 0.2, 0.25))
        ctx.restore()
    shout_bubble(ctx, "完全懂了！", 520, 600, 200, 60)

# 12 結尾總結
def s12(ep, ctx, u, T, m):
    vintage_room(ctx, u)
    t1, t2, t3, tend = ep.kw(12, "一噸減量"), ep.kw(12, "先減量才能抵換"), ep.kw(12, "ISO 14068"), ep.kw(12, "我是小綠")
    retro_blackboard(ctx, 360, 200, 620, 140, title="今天記住三件事")

    notes = [
        ("① 碳權 ＝ 1 噸減量認證憑證", t1),
        ("② 減碳階梯 ＝ 先自主減量，再抵換", t2),
        ("③ 遠離漂綠 ＝ 遵守 ISO 14068", t3)
    ]
    for k, (s_, t0) in enumerate(notes):
        p = prog(u, t0 - 0.2, 0.45)
        if p > 0:
            yy = 390 + k * 140
            ctx.save(); pop(ctx, 360, yy, p)
            rrect(ctx, 80, yy - 50, 560, 100, 18)
            ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
            ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
            text(ctx, s_, 360, yy + 10, 28, (0.1, 0.1, 0.12))
            ctx.restore()

    # 小綠揮手告別
    retro_xiaolu(ctx, 360, 920, 1.25, T, m, wave=True)
    if u > tend:
        shout_bubble(ctx, "我是小綠，下集見！", 530, 800, 260, 70)

# 執行
run("ep8", "碳導遊小綠 EP8",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12],
    "碳導遊小綠_EP8_買碳權就能零碳.mp4",
    wipes={2, 4, 6, 8, 10, 12})
