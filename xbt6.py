"""小半天旅遊系列・第 6 集：兩天一夜漫遊仙境——小半天低碳全攻略（系列完結特輯）
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ---------- 專屬行程規劃與低碳綠色繪圖元件 ----------

def draw_mist_cluster(ctx, cx, cy, rx, ry, alpha=0.85):
    """柔和蓬鬆白雲"""
    ctx.save(); ctx.set_source_rgba(1.0, 1.0, 1.0, alpha); ctx.new_path()
    ctx.arc(cx, cy, ry, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx - rx * 0.45, cy + ry * 0.1, ry * 0.78, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx + rx * 0.45, cy + ry * 0.1, ry * 0.78, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx - rx * 0.22, cy - ry * 0.32, ry * 0.68, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx + rx * 0.22, cy - ry * 0.32, ry * 0.68, 0, 2 * math.pi); ctx.fill()
    ctx.restore()

def draw_grand_scenic_bg(ctx, t):
    """小半天山巒與星空/晨嵐漸層全景"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.70, 0.85, 0.96)
    pat.add_color_stop_rgb(0.55, 0.85, 0.94, 0.88)
    pat.add_color_stop_rgb(1.0, 0.78, 0.90, 0.80)
    ctx.set_source(pat); ctx.paint()

    # 遠景雲海
    for ox, oy, rx, ry in [(240, 480, 200, 50), (640, 470, 240, 55), (1040, 490, 220, 50)]:
        drift = math.sin(t * 1.5 + ox) * 20
        draw_mist_cluster(ctx, ox + drift, oy, rx, ry, alpha=0.75)

    # 近景山坡與茶林剪影
    ctx.save()
    ctx.move_to(0, 560); ctx.curve_to(360, 520, 720, 600, 1280, 540); ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    fillstroke(ctx, (0.28, 0.58, 0.40), stroke=C['navy'], lw=4)
    ctx.restore()

    # 飄舞竹葉
    random.seed(91)
    for i in range(8):
        lx = (random.random() * W + t * (25 + i * 7)) % (W + 60) - 30
        ly = (random.random() * H + t * (18 + i * 4)) % (H + 60) - 30
        draw_leaf_particle(ctx, lx, ly, 0.8, t * 2.0 + i)

def draw_leaf_particle(ctx, x, y, s, ang):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(ang)
    ctx.move_to(0, -14); ctx.curve_to(12, -8, 12, 8, 0, 14); ctx.curve_to(-12, 8, -12, -8, 0, -14); ctx.close_path()
    fillstroke(ctx, C['green'], stroke=C['navy'], lw=2)
    ctx.restore()

def draw_itinerary_node(ctx, x, y, time_tag, spot_name, col):
    """行程時間軸站點"""
    ctx.save(); ctx.translate(x, y)
    ctx.arc(0, 0, 24, 0, 2 * math.pi); fillstroke(ctx, col, stroke=C['navy'], lw=3.5)
    star(ctx, 0, 0, 10, C['white'], 1)
    chip(ctx, time_tag, 0, -42, 1, (0.25, 0.28, 0.32), 18, tcol=C['white'])
    text(ctx, spot_name, 0, 46, 20, C['navy'], bold=True)
    ctx.restore()


# ==================== 場景定義 (s0 ~ s5) ====================

# ----- s0: 開場 -----
def s0(ep, ctx, u, T, m):
    draw_grand_scenic_bg(ctx, T)

    p_lu = ease_out(prog(u, 0.0, 0.7))
    x_lu = -120 + 330 * p_lu
    atian(ctx, x_lu, 340, 0.92, T, m, wave=True)
    sticker(ctx, "哈囉！", 150, 110, u, 0.3, C['pink'], 38, dur=3.5)

    t_card = 1.8
    p_card = prog(u, t_card, 0.6)
    if p_card > 0:
        cx, cy = 760, 290
        ctx.save(); pop(ctx, cx, cy, p_card)
        card_w, card_h = 740, 260
        rrect(ctx, cx - card_w / 2 + 10, cy - card_h / 2 + 12, card_w, card_h, 32)
        ctx.set_source_rgba(0.12, 0.22, 0.28, 0.18); ctx.fill()

        # 活力翠綠金漸層底
        pat = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat.add_color_stop_rgb(0.0, 1.0, 0.92, 0.45)
        pat.add_color_stop_rgb(1.0, 0.95, 0.76, 0.25)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        sub_text = "小半天旅遊系列・第 6 集（完結特輯）"
        sub_w = 400; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, C['teal2'], bold=True)

        text(ctx, "兩天一夜漫遊仙境", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "小半天低碳慢活全攻略", cx, cy + 66, 48, (0.18, 0.52, 0.28), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_trip = ep.kw(0, "低碳慢遊")
    p_trip = prog(u, t_trip - 0.2, 0.4)
    if p_trip > 0:
        chip(ctx, "兩天一夜經典遊程", 600, 480, p_trip, C['teal'], 28, tcol=C['white'])
        star(ctx, 475, 480, 10, C['yellow'], p_trip, rot=T * 2, outline=True)

    t_guide = ep.kw(0, "全攻略")
    p_guide = prog(u, t_guide - 0.2, 0.45)
    if p_guide > 0:
        chip(ctx, "綠色永續玩透小半天", 920, 480, p_guide, C['orange'], 28, tcol=C['white'])
        star(ctx, 790, 480, 10, C['yellow'], p_guide, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("行程規劃\n兩天一夜", "經典遊程"),
        ("夜宿雲海\n特色民宿", "特色民宿"),
        ("低碳心法\n綠色旅行", "綠色旅行")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站：第一天行程推薦 -----
def s2(ep, ctx, u, T, m):
    background(ctx, T, 1)
    station_card(ctx, u, 1, "第一天行程規劃")
    if u < 1.9: return
    header(ctx, 1, "Day 1：長源圳竹海 ➔ 竹筒飯 ➔ 德興瀑布 ➔ 茶園夕陽", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 行程軸底板
    rrect(ctx, 100, 140, 960, 420, 24); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
    # 連接線條
    ctx.move_to(220, 320); ctx.line_to(940, 320); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(8); ctx.stroke()
    ctx.move_to(220, 320); ctx.line_to(940, 320); ctx.set_source_rgb(*C['teal']); ctx.set_line_width(4); ctx.stroke()

    # 4 個行程節點
    nodes = [
        ("上午", "長源圳步道\n孟宗竹林隧道", 220, 2.1, C['green']),
        ("中午", "在地竹筒飯\n鮮筍風味餐", 460, ep.kw(2, "竹筒飯"), C['orange']),
        ("下午", "德興瀑布\n吸收負離子", 700, ep.kw(2, "德興瀑布"), C['blue']),
        ("傍晚", "高山茶園\n夕陽與雲海", 940, ep.kw(2, "雲海"), C['yellow'])
    ]

    for time_tag, spot, nx, t_n, col in nodes:
        p_n = prog(u, t_n - 0.2, 0.4)
        if p_n <= 0: continue
        ctx.save(); pop(ctx, nx, 320, p_n)
        draw_itinerary_node(ctx, nx, 320, time_tag, "", col)
        # 站點名稱卡
        rrect(ctx, nx - 90, 360, 180, 75, 12); fillstroke(ctx, (0.95, 0.98, 1.0), stroke=C['navy'], lw=2.5)
        for idx, line in enumerate(spot.split("\n")):
            text(ctx, line, nx, 388 + idx * 24, 18, C['navy'], bold=True)
        ctx.restore()


# ----- s3: 第 2 站：第二天行程推薦 -----
def s3(ep, ctx, u, T, m):
    background(ctx, T, 2)
    station_card(ctx, u, 2, "第二天行程規劃")
    if u < 1.9: return
    header(ctx, 2, "Day 2：晨光茶園 ➔ 石馬公園 ➔ 竹編 DIY ➔ 慢活品茗", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 行程軸底板
    rrect(ctx, 100, 140, 960, 420, 24); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
    ctx.move_to(220, 320); ctx.line_to(940, 320); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(8); ctx.stroke()
    ctx.move_to(220, 320); ctx.line_to(940, 320); ctx.set_source_rgb(*C['orange']); ctx.set_line_width(4); ctx.stroke()

    nodes = [
        ("清晨", "山嵐鳥鳴\n茶園晨間漫步", 220, 2.1, C['yellow']),
        ("上午", "石馬公園\n散心賞景打卡", 460, ep.kw(3, "石馬公園"), C['pink']),
        ("午後", "在地竹藝\n竹編體驗 DIY", 700, ep.kw(3, "DIY"), C['teal']),
        ("歸賦", "茶坊品茗\n採購伴手禮", 940, ep.kw(3, "凍頂烏龍"), C['green'])
    ]

    for time_tag, spot, nx, t_n, col in nodes:
        p_n = prog(u, t_n - 0.2, 0.4)
        if p_n <= 0: continue
        ctx.save(); pop(ctx, nx, 320, p_n)
        draw_itinerary_node(ctx, nx, 320, time_tag, "", col)
        rrect(ctx, nx - 90, 360, 180, 75, 12); fillstroke(ctx, (1, 0.98, 0.95), stroke=C['navy'], lw=2.5)
        for idx, line in enumerate(spot.split("\n")):
            text(ctx, line, nx, 388 + idx * 24, 18, C['navy'], bold=True)
        ctx.restore()


# ----- s4: 第 3 站：低碳慢遊守則 -----
def s4(ep, ctx, u, T, m):
    draw_grand_scenic_bg(ctx, T)
    station_card(ctx, u, 3, "低碳慢遊守則")
    if u < 1.9: return
    header(ctx, 3, "友善大地：實踐綠色永續旅行心法", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 4 大綠色心法卡片
    rules = [
        ("共乘出發", "減少碳排共享旅程", 210, 2.1, C['blue']),
        ("自備餐具", "環保水壺與餐具", 470, ep.kw(4, "自備環保"), C['green']),
        ("無痕山林", "垃圾不落地敬自然", 730, ep.kw(4, "不隨意留下"), C['orange']),
        ("支持小農", "在地鮮產當季茶筍", 990, ep.kw(4, "共同守護"), C['teal'])
    ]

    for title, desc, cx, t_r, col in rules:
        p_r = prog(u, t_r - 0.2, 0.45)
        if p_r <= 0: continue
        ctx.save(); pop(ctx, cx, 330, p_r)
        rrect(ctx, cx - 115, 190, 230, 270, 20); fillstroke(ctx, C['white'], stroke=C['navy'], lw=4.5)
        ctx.arc(cx, 260, 36, 0, 2 * math.pi); fillstroke(ctx, col, stroke=C['navy'], lw=3)
        star(ctx, cx, 260, 16, C['white'], 1)
        chip(ctx, title, cx, 345, 1, col, 22, tcol=C['white'])
        text(ctx, desc, cx, 400, 18, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()


# ----- s5: 全系列大總結 -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(66)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(60):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()

    tb = LEAD + ep.durs[5] * 0.70
    atian(ctx, 220, 350, 0.95, T, m, wave=True)

    # 標題
    pp = prog(u, 0.2, 0.5)
    ctx.save(); pop(ctx, 780, 115, pp)
    text(ctx, "小半天旅遊系列・圓滿大結尾", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・雲端上的世外桃源", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    rows = [
        ("自然仙境", "萬頃孟宗竹海、壯觀德興飛瀑、天然冷氣房", ep.kw(5, "小半天是仙境"), C['teal']),
        ("人文風土", "三百年拓墾傳奇、凍頂茶香、石馬櫻花奇蹟", ep.kw(5, "生活溫度"), C['orange']),
        ("低碳漫活", "放慢腳步深呼吸，享受綠色永續的美好生活", ep.kw(5, "六集"), C['green'])
    ]
    for k, (a, b, t0, col) in enumerate(rows):
        p = prog(u, t0 - 0.2, 0.4)
        if p <= 0: continue
        y = 215 + k * 80
        ctx.save(); ctx.translate(-250 * (1 - ease_out(p)), 0)
        rrect(ctx, 450, y - 32, 700, 66, 33)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=4)
        chip(ctx, a, 555, y + 1, 1, col, 24)
        text(ctx, b, 665, y + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    # 感謝收看橫幅
    t_end = ep.kw(5, "熱情歡迎")
    p_end = prog(u, t_end - 0.2, 0.5)
    if p_end > 0:
        cx, cy = 800, 490
        ctx.save(); pop(ctx, cx, cy, p_end)
        rrect(ctx, cx - 350, cy - 34, 700, 68, 20)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        chip(ctx, "阿天感謝您", cx - 265, cy + 1, 1, C['orange'], 22, tcol=C['white'])
        text(ctx, "南投鹿谷小半天・熱情歡迎隨時上山作客！", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "感謝收看！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5]
wipes = {2, 3, 4, 5}

run("xbt6", "小半天系列 EP6", scenes, "小半天_EP6_兩天一夜低碳全攻略.mp4", wipes=wipes)
