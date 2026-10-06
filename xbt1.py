"""小半天旅遊系列・第 1 集：雲端上的世外桃源——小半天的由來與拓墾史
高品質製作版本 (High-Quality Enhanced Edition)
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ==================== 高品質視覺與環境動態元件 ====================

def draw_fluttering_leaf(ctx, x, y, s, ang, col=C['green'], alpha=0.85):
    """飄落的青竹葉"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(ang)
    ctx.move_to(0, -16); ctx.curve_to(14, -8, 14, 8, 0, 16); ctx.curve_to(-14, 8, -14, -8, 0, -16); ctx.close_path()
    fillstroke(ctx, col, stroke=C['navy'], lw=2.0, a=alpha)
    ctx.move_to(0, -12); ctx.line_to(0, 14); ctx.set_source_rgba(*C['navy'], alpha); ctx.set_line_width(1.5); ctx.stroke()
    ctx.restore()

def draw_mist_cluster(ctx, cx, cy, rx, ry, alpha=0.88):
    """柔和細緻蓬鬆山嵐雲團"""
    ctx.save()
    ctx.set_source_rgba(1.0, 1.0, 1.0, alpha)
    ctx.new_path()
    ctx.arc(cx, cy, ry, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx - rx * 0.45, cy + ry * 0.1, ry * 0.78, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx + rx * 0.45, cy + ry * 0.1, ry * 0.78, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx - rx * 0.22, cy - ry * 0.32, ry * 0.68, 0, 2 * math.pi); ctx.fill()
    ctx.arc(cx + rx * 0.22, cy - ry * 0.32, ry * 0.68, 0, 2 * math.pi); ctx.fill()
    ctx.restore()

def draw_flowing_mist_band(ctx, y, direction=1, t=0.0, part=0.0, alpha=0.88):
    """橫向流動山嵐（支援隨語音向兩側優雅撥開）"""
    ctx.save()
    drift = math.sin(t * 1.2 + y * 0.01) * 35
    part_dx = direction * 680 * ease_out(part)
    curr_alpha = alpha * (1.0 - part * 0.45)
    ctx.translate(part_dx + drift, 0)
    base_x = 220 if direction < 0 else 780
    for i, offset_x in enumerate([-320, -140, 40, 220, 400]):
        blob_x = base_x + offset_x
        blob_y = y + math.sin(t * 1.8 + i * 1.1) * 16
        draw_mist_cluster(ctx, blob_x, blob_y, 145, 56, curr_alpha)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.set_source_rgba(1.0, 1.0, 1.0, curr_alpha * 0.72)
    ctx.set_line_width(30)
    ctx.move_to(base_x - 400, y + 25)
    ctx.curve_to(base_x - 120, y + 42, base_x + 120, y + 8, base_x + 440, y + 30)
    ctx.stroke()
    ctx.restore()

def draw_xbt_background(ctx, t, show_leaves=True):
    """高質感背景：青嵐與天藍漸層、三重遠近山巒剪影、隨風飄舞竹葉"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.74, 0.88, 0.96)
    pat.add_color_stop_rgb(0.55, 0.86, 0.94, 0.91)
    pat.add_color_stop_rgb(1.0, 0.80, 0.92, 0.83)
    ctx.set_source(pat); ctx.paint()

    # 遠景 1：黛青深山（阿里山山脈前緣意象）
    ctx.save()
    ctx.move_to(0, 470); ctx.curve_to(260, 340, 460, 420, 690, 360)
    ctx.curve_to(910, 310, 1110, 380, 1280, 340); ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    ctx.set_source_rgba(0.50, 0.68, 0.75, 0.38); ctx.fill()

    # 中景 2：翠綠竹山茶巒
    ctx.move_to(0, 520); ctx.curve_to(220, 430, 510, 480, 790, 410)
    ctx.curve_to(990, 370, 1160, 450, 1280, 400); ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    ctx.set_source_rgba(0.38, 0.66, 0.52, 0.48); ctx.fill()

    # 近景 3：小半天台地山稜
    ctx.move_to(0, 615); ctx.curve_to(350, 585, 730, 645, 1280, 575)
    ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    ctx.set_source_rgba(0.32, 0.60, 0.44, 0.62); ctx.fill()
    ctx.restore()

    # 陽光透出的金色靈氣光點
    random.seed(42)
    for i in range(14):
        sp_x = (random.random() * W + t * (16 + i * 2)) % (W + 60) - 30
        sp_y = 100 + random.random() * 420 + math.sin(t * 1.6 + i) * 15
        star(ctx, sp_x, sp_y, 4 + (i % 3) * 2, C['yellow'], 0.65, rot=t * (1 + i % 2))

    # 隨風飄曳的嫩綠竹葉粒子
    if show_leaves:
        for i in range(7):
            lx = (random.random() * W + t * (25 + i * 8)) % (W + 80) - 40
            ly = (random.random() * H + t * (15 + i * 4)) % (H + 60) - 30
            ang = t * 1.8 + i * 1.2
            draw_fluttering_leaf(ctx, lx, ly, 0.75 + (i % 3) * 0.15, ang, col=C['green'], alpha=0.7)

def draw_bamboo_stalk(ctx, x, y, h, w=12, col=C['green']):
    """單株精緻孟宗竹（竹節凸環與層疊竹葉）"""
    ctx.save()
    segs = max(3, int(h / 38))
    seg_h = h / segs
    for i in range(segs):
        sy = y - (i + 1) * seg_h
        rrect(ctx, x - w / 2, sy + 3, w, seg_h - 4, 3)
        fillstroke(ctx, col, stroke=C['navy'], lw=2.5)
        # 立體竹節凸緣
        ctx.move_to(x - w / 2 - 3, sy + seg_h); ctx.line_to(x + w / 2 + 3, sy + seg_h)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3.2); ctx.stroke()
    # 頂部竹葉分枝
    for ang, lx, sc in [(-0.55, -16, 1.0), (0.48, 16, 0.9), (-0.2, -8, 0.75), (0.25, 10, 0.65)]:
        ctx.save(); ctx.translate(x + lx * 0.35, y - h); ctx.rotate(ang); ctx.scale(sc, sc)
        ctx.move_to(0, 0); ctx.curve_to(16, -9, 24, -2, 30, 0); ctx.curve_to(22, 7, 14, 7, 0, 0); ctx.close_path()
        fillstroke(ctx, col, stroke=C['navy'], lw=2)
        ctx.restore()
    ctx.restore()

def draw_plateau(ctx, cx, cy, w, h, t=0.0):
    """繪製山頂小台地地形（四周深壑峭壁、頂部青翠平坦、有涓涓泉瀑）"""
    ctx.save()
    # 台地下層峭壁岩體
    ctx.move_to(cx - w * 0.65, cy + h)
    ctx.line_to(cx - w * 0.46, cy + 20)
    ctx.line_to(cx + w * 0.46, cy + 20)
    ctx.line_to(cx + w * 0.65, cy + h)
    ctx.close_path()
    fillstroke(ctx, (0.56, 0.46, 0.36), stroke=C['navy'], lw=5.5)

    # 岩層節理紋理
    for dy in [32, 62, 92]:
        if dy < h - 10:
            ctx.move_to(cx - w * 0.52 + dy * 0.2, cy + dy); ctx.line_to(cx + w * 0.52 - dy * 0.2, cy + dy)
            ctx.set_source_rgba(0.40, 0.30, 0.22, 0.65); ctx.set_line_width(4); ctx.stroke()

    # 峭壁邊緣的小瀑布泉流（象徵小半天德興瀑布水脈）
    wf_x = cx + w * 0.28
    ctx.move_to(wf_x, cy + 22); ctx.line_to(wf_x + 5, cy + h - 10)
    ctx.set_source_rgba(0.75, 0.92, 1.0, 0.95); ctx.set_line_width(8); ctx.stroke()
    ctx.move_to(wf_x + 1, cy + 22); ctx.line_to(wf_x + 6, cy + h - 10)
    ctx.set_source_rgb(*C['white']); ctx.set_line_width(4); ctx.stroke()

    # 台地頂部平坦綠洲（橢圓平原）
    ctx.save(); ctx.translate(cx, cy + 16); ctx.scale(1, 0.32)
    ctx.arc(0, 0, w * 0.48, 0, 2 * math.pi)
    fillstroke(ctx, C['green'], stroke=C['navy'], lw=12)
    ctx.restore()

    # 台地上的點綴：茂密竹林、青翠茶樹叢
    draw_bamboo_stalk(ctx, cx - w * 0.30, cy + 6, 56, w=8, col=(0.26, 0.66, 0.36))
    draw_bamboo_stalk(ctx, cx - w * 0.22, cy + 9, 46, w=7, col=C['green'])
    draw_bamboo_stalk(ctx, cx + w * 0.12, cy + 7, 52, w=8, col=(0.26, 0.66, 0.36))
    
    # 圓滾滾的高山烏龍茶樹叢
    for ox in [-w * 0.08, w * 0.04]:
        ctx.arc(cx + ox, cy + 13, 14, 0, 2 * math.pi); fillstroke(ctx, (0.20, 0.50, 0.30), stroke=C['navy'], lw=2.5)

    ctx.restore()

def draw_ancient_boat(ctx, cx, cy, s=1.0, t=0.0):
    """福建渡海古帆船：起伏浪花、傳統雙紅帆"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    bob = math.sin(t * 3.5) * 7; ctx.translate(0, bob); ctx.rotate(math.sin(t * 2.5) * 0.06)
    
    # 木造船體
    ctx.move_to(-80, 10); ctx.curve_to(-55, 48, 55, 48, 85, 10); ctx.line_to(70, -12); ctx.line_to(-70, -12); ctx.close_path()
    fillstroke(ctx, (0.76, 0.50, 0.30), stroke=C['navy'], lw=4.5)
    # 主桅桿與前桅桿
    ctx.move_to(8, -12); ctx.line_to(8, -100); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()
    ctx.move_to(-38, -12); ctx.line_to(-38, -75); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(4.5); ctx.stroke()

    # 主帆（折扇朱紅帆）
    ctx.move_to(12, -22); ctx.curve_to(48, -48, 46, -82, 12, -96); ctx.line_to(12, -22); ctx.close_path()
    fillstroke(ctx, (0.86, 0.30, 0.24), stroke=C['navy'], lw=3.5)
    for yy in [-38, -56, -76]:
        ctx.move_to(12, yy); ctx.line_to(42, yy + 5); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(2.5); ctx.stroke()

    # 前帆
    ctx.move_to(-34, -20); ctx.curve_to(-12, -40, -14, -65, -34, -72); ctx.line_to(-34, -20); ctx.close_path()
    fillstroke(ctx, (0.92, 0.42, 0.32), stroke=C['navy'], lw=3)

    # 浪頭白花
    for ox in [-70, -25, 20, 65]:
        ctx.arc(ox + math.sin(t * 4 + ox) * 6, 36, 14, 0.1 * math.pi, 0.9 * math.pi)
        ctx.set_source_rgba(1, 1, 1, 0.9); ctx.set_line_width(4.5); ctx.stroke()
    ctx.restore()

def draw_cottage(ctx, cx, cy, s=1.0, u=0.0):
    """閩南傳統土角厝建築（煙囪緩緩冒炊煙）"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    # 煙囪裊裊炊煙
    for k in range(3):
        f = (u * 0.8 + k / 3) % 1.0
        smk_x = 42 + math.sin(f * 4) * 12
        smk_y = -35 - f * 42
        ctx.arc(smk_x, smk_y, 8 + f * 10, 0, 2 * math.pi)
        ctx.set_source_rgba(0.9, 0.92, 0.95, (1.0 - f) * 0.7); ctx.fill()

    # 牆身（夯土泥色）
    rrect(ctx, -60, -20, 120, 65, 8); fillstroke(ctx, (0.92, 0.82, 0.65), stroke=C['navy'], lw=4)
    # 大門
    rrect(ctx, -14, 8, 28, 37, 4); fillstroke(ctx, (0.55, 0.28, 0.18), stroke=C['navy'], lw=3)
    # 木框窗
    for sx in [-42, 26]:
        rrect(ctx, sx, 0, 18, 18, 3); fillstroke(ctx, C['screen'], stroke=C['navy'], lw=2.5)
    # 燕尾磚紅屋頂
    ctx.move_to(-76, -18); ctx.curve_to(-40, -48, 40, -48, 76, -18); ctx.line_to(65, -18); ctx.line_to(-65, -18); ctx.close_path()
    fillstroke(ctx, (0.85, 0.38, 0.28), stroke=C['navy'], lw=4)
    # 煙囪
    rrect(ctx, 36, -42, 14, 25, 2); fillstroke(ctx, (0.68, 0.32, 0.22), stroke=C['navy'], lw=2.5)
    ctx.restore()

def draw_clan_lantern(ctx, cx, cy, char="蘇"):
    """傳統宮燈宗祠印記（朱紅大宮燈、金黃字、下垂流蘇）"""
    ctx.save(); ctx.translate(cx, cy)
    # 燈籠頂蓋
    rrect(ctx, -50, -82, 100, 18, 6); fillstroke(ctx, (0.32, 0.20, 0.15), stroke=C['navy'], lw=3)
    # 燈身
    ctx.move_to(-46, -65); ctx.curve_to(-75, -20, -75, 25, -46, 60)
    ctx.line_to(46, 60); ctx.curve_to(75, 25, 75, -20, 46, -65); ctx.close_path()
    fillstroke(ctx, (0.88, 0.26, 0.22), stroke=C['navy'], lw=5)
    # 燈身內金黃書法字
    text(ctx, char, 0, 6, 68, C['yellow'], bold=True)
    # 燈籠底座
    rrect(ctx, -42, 60, 84, 16, 5); fillstroke(ctx, (0.32, 0.20, 0.15), stroke=C['navy'], lw=3)
    # 金黃流蘇穗
    for ox in [-18, 0, 18]:
        ctx.move_to(ox, 76); ctx.line_to(ox, 108); ctx.set_source_rgb(*C['yellow']); ctx.set_line_width(4); ctx.stroke()
        ctx.arc(ox, 110, 4, 0, 2 * math.pi); fillstroke(ctx, C['orange'], stroke=C['navy'], lw=2)
    ctx.restore()


# ==================== 場景定義 (s0 ~ s9) ====================

# ----- s0: 開場・世外桃源 -----
def s0(ep, ctx, u, T, m):
    draw_xbt_background(ctx, T)
    part = prog(u, 1.6, 1.2)
    draw_flowing_mist_band(ctx, y=240, direction=-1, t=T, part=part, alpha=0.90)
    draw_flowing_mist_band(ctx, y=410, direction=1, t=T, part=part, alpha=0.85)

    p_lu = ease_out(prog(u, 0.0, 0.7))
    x_lu = -120 + 330 * p_lu
    atian(ctx, x_lu, 340, 0.92, T, m, wave=True)
    sticker(ctx, "哈囉！", 150, 110, u, 0.3, C['pink'], 38, dur=3.5)

    t_card = 1.9
    p_card = prog(u, t_card, 0.6)
    if p_card > 0:
        cx, cy = 780, 290
        ctx.save(); pop(ctx, cx, cy, p_card)
        card_w, card_h = 720, 260
        rrect(ctx, cx - card_w / 2 + 10, cy - card_h / 2 + 12, card_w, card_h, 32)
        ctx.set_source_rgba(0.12, 0.22, 0.28, 0.16); ctx.fill()

        pat_gold = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat_gold.add_color_stop_rgb(0.0, 1.0, 0.88, 0.38)
        pat_gold.add_color_stop_rgb(1.0, 0.98, 0.73, 0.20)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat_gold); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        rrect(ctx, cx - card_w / 2 + 12, cy - card_h / 2 + 12, card_w - 24, card_h - 24, 22)
        ctx.set_source_rgba(0.92, 0.60, 0.10, 0.65); ctx.set_line_width(2.5); ctx.stroke()

        sub_text = "小半天旅遊系列・第 1 集"
        sub_w = 330; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, C['teal2'], bold=True)

        text(ctx, "雲端上的世外桃源", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "南投鹿谷・小半天", cx, cy + 66, 50, (0.75, 0.20, 0.10), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_xbt = ep.kw(0, "小半天", 1)
    p_xbt = prog(u, t_xbt - 0.2, 0.4)
    if p_xbt > 0:
        chip(ctx, "仙氣名境：小半天", 620, 480, p_xbt, C['teal'], 28, tcol=C['white'])
        star(ctx, 505, 480, 10, C['yellow'], p_xbt, rot=T * 2, outline=True)

    t_hist = ep.kw(0, "三百年")
    p_hist = prog(u, t_hist - 0.2, 0.45)
    if p_hist > 0:
        chip(ctx, "三百年拓墾傳奇", 940, 480, p_hist, C['orange'], 28, tcol=C['white'])
        star(ctx, 835, 480, 10, C['yellow'], p_hist, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("仙境地名\n半天之處", "地名"),
        ("明末風雲\n林圯拓墾", "林圯"),
        ("渡海入墾\n蘇林開拓", "蘇姓林姓")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站卡片 + 東埔蚋往東望 -----
def s2(ep, ctx, u, T, m):
    draw_xbt_background(ctx, T)
    station_card(ctx, u, 1, "為什麼叫小半天？")
    if u < 1.9: return
    header(ctx, 1, "從東埔蚋往東望：雲霧在半天", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側：古地名標牌「東埔蚋（今竹山延平）」
    p_sign = prog(u, 2.1, 0.4)
    if p_sign > 0:
        ctx.save(); pop(ctx, 280, 360, p_sign)
        # 木質地名牌立柱與牌面
        rrect(ctx, 268, 370, 24, 150, 6); fillstroke(ctx, (0.58, 0.42, 0.28), stroke=C['navy'], lw=4)
        rrect(ctx, 160, 240, 240, 130, 18); fillstroke(ctx, (0.95, 0.88, 0.76), stroke=C['navy'], lw=5)
        text(ctx, "東埔蚋", 280, 282, 34, C['navy'], bold=True)
        text(ctx, "（今竹山延平里）", 280, 324, 22, (0.55, 0.35, 0.18), bold=True)
        chip(ctx, "漢人遠眺視角", 280, 400, 1, C['yellow'], 22)
        ctx.restore()

    # 右側：雲霧深鎖的高山
    p_mtn = prog(u, 2.5, 0.5)
    if p_mtn > 0:
        ctx.save(); pop(ctx, 720, 340, p_mtn)
        # 前後雙層山稜
        ctx.move_to(440, 480); ctx.curve_to(560, 140, 780, 140, 940, 480); ctx.close_path()
        fillstroke(ctx, (0.38, 0.60, 0.48), stroke=C['navy'], lw=5)
        ctx.move_to(580, 480); ctx.curve_to(700, 190, 880, 200, 1000, 480); ctx.close_path()
        fillstroke(ctx, (0.46, 0.70, 0.56), stroke=C['navy'], lw=4)

        # 厚重山嵐雲層飄動繚繞在半山腰
        for idx, (ox, oy, rx, ry) in enumerate([(-110, 20, 135, 50), (35, 0, 155, 55), (145, 40, 125, 45)]):
            drift = math.sin(T * 1.5 + idx) * 16
            draw_mist_cluster(ctx, 720 + ox + drift, 300 + oy, rx, ry, alpha=0.92)
        ctx.restore()

    t_cloud = ep.kw(2, "雲霧籠罩")
    p_cloud = prog(u, t_cloud - 0.2, 0.4)
    if p_cloud > 0:
        chip(ctx, "山上經常雲霧籠罩", 720, 470, p_cloud, C['teal'], 28, tcol=C['white'])

    t_half = ep.kw(2, "半天之上")
    p_half = prog(u, t_half - 0.2, 0.4)
    if p_half > 0:
        chip(ctx, "看起來就像懸掛在半天之上", 720, 530, p_half, C['orange'], 28, tcol=C['white'])


# ----- s3: 撥開雲霧・登上見小台地 -----
def s3(ep, ctx, u, T, m):
    draw_xbt_background(ctx, T)
    header(ctx, 1, "登上一望：驚見群山中的小台地", u)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 雲霧向兩側散開動態
    p_part = prog(u, 0.4, 1.2)
    # 中央台地浮現
    p_plat = prog(u, 0.8, 0.6)
    if p_plat > 0:
        cx, cy = 600, 310
        ctx.save(); pop(ctx, cx, cy, p_plat)
        draw_plateau(ctx, cx, cy, w=490, h=165, t=T)
        ctx.restore()

    # 飄散的薄雲
    draw_flowing_mist_band(ctx, y=260, direction=-1, t=T, part=p_part, alpha=0.8)
    draw_flowing_mist_band(ctx, y=420, direction=1, t=T, part=p_part, alpha=0.75)

    # 命名亮點大章
    t_name = ep.kw(3, "小半天")
    p_name = prog(u, t_name - 0.2, 0.5)
    if p_name > 0:
        cx, cy = 600, 480
        ctx.save(); pop(ctx, cx, cy, p_name)
        rrect(ctx, cx - 310, cy - 40, 620, 80, 40)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        text(ctx, "半天之中・一小塊台地：命名「小半天」", cx, cy + 2, 28, C['navy'], bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_name, R=240, n=12)


# ----- s4: 第 2 站卡片 + 明永曆22年(1668) 林圯屯墾水沙連 -----
def s4(ep, ctx, u, T, m):
    background(ctx, T, 2)
    station_card(ctx, u, 2, "明末林圯拓墾風雲")
    if u < 1.9: return
    header(ctx, 2, "明永曆 22 年（西元 1668）屯墾水沙連", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 歷史檔案卷軸卡片（左側）
    p_doc = prog(u, 2.1, 0.5)
    if p_doc > 0:
        ctx.save(); pop(ctx, 330, 340, p_doc)
        # 上下卷軸軸心
        rrect(ctx, 140, 150, 380, 20, 8); fillstroke(ctx, (0.45, 0.28, 0.18), stroke=C['navy'], lw=3.5)
        rrect(ctx, 140, 490, 380, 20, 8); fillstroke(ctx, (0.45, 0.28, 0.18), stroke=C['navy'], lw=3.5)
        # 卷軸宣紙本體
        rrect(ctx, 160, 160, 340, 340, 20); fillstroke(ctx, (1, 0.96, 0.88), stroke=C['navy'], lw=5)
        
        # 卷軸印章
        rrect(ctx, 200, 190, 260, 50, 12); fillstroke(ctx, (0.85, 0.32, 0.24), stroke=C['navy'], lw=3.5)
        text(ctx, "明末・鄭成功部屬", 330, 222, 24, C['white'], bold=True)
        text(ctx, "林圯將軍", 330, 290, 44, C['navy'], bold=True)
        text(ctx, "率部開闢屯墾水沙連", 330, 340, 24, (0.42, 0.38, 0.35), bold=True)
        chip(ctx, "奠定漢人入鹿谷基石", 330, 410, 1, C['yellow'], 24)
        ctx.restore()

    # 右側：戰事衝擊歷程卡（上下並列，版面寬裕）
    t_war = ep.kw(4, "原住民")
    p_war = prog(u, t_war - 0.2, 0.45)
    if p_war > 0:
        ctx.save(); pop(ctx, 770, 240, p_war)
        rrect(ctx, 550, 185, 440, 105, 20); fillstroke(ctx, C['white'], stroke=C['red'], lw=4)
        chip(ctx, "突襲戰役", 630, 216, 1, C['red'], 20, tcol=C['white'])
        text(ctx, "林圯與百多名部屬不幸陣亡", 770, 258, 24, C['navy'], bold=True)
        ctx.restore()

    t_retreat = ep.kw(4, "斗六門")
    p_retreat = prog(u, t_retreat - 0.2, 0.45)
    if p_retreat > 0:
        ctx.save(); pop(ctx, 770, 375, p_retreat)
        rrect(ctx, 550, 320, 440, 105, 20); fillstroke(ctx, C['white'], stroke=C['orange'], lw=4)
        chip(ctx, "重整戰局", 630, 351, 1, C['orange'], 20, tcol=C['white'])
        text(ctx, "漢人軍隊暫退回斗六門", 770, 393, 24, C['navy'], bold=True)
        ctx.restore()


# ----- s5: 漢人反攻地圖推進（斗六門 ➔ 東埔蚋 ➔ 大水崛 ➔ 鹿谷） -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 1)
    header(ctx, 2, "開墾推進：漢人勢力延伸至鹿谷", u)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 復古推進古地圖面板
    rrect(ctx, 100, 130, 960, 430, 24)
    fillstroke(ctx, (0.98, 0.95, 0.88), stroke=C['navy'], lw=5)

    # 地圖背景淡水流（濁水溪、清水溪水系意象）
    ctx.save()
    ctx.move_to(120, 360); ctx.curve_to(360, 390, 580, 240, 1040, 260)
    ctx.set_source_rgba(0.70, 0.86, 0.95, 0.5); ctx.set_line_width(22); ctx.stroke()
    ctx.restore()

    # 4 個據點座標與資訊
    pts = [
        ("斗六門", "重整反攻", 220, 410, 0.5),
        ("東埔蚋", "擊潰退敵", 460, 310, ep.kw(5, "東埔蚋")),
        ("大水崛", "一路追擊", 700, 380, ep.kw(5, "大水崛")),
        ("鹿谷", "勢力延伸", 940, 260, ep.kw(5, "延伸進了鹿谷"))
    ]

    # 連接箭頭路線
    for i in range(len(pts) - 1):
        x1, y1, t1 = pts[i][2], pts[i][3], pts[i][4]
        x2, y2, t2 = pts[i + 1][2], pts[i + 1][3], pts[i + 1][4]
        p_line = prog(u, t1, max(0.4, t2 - t1))
        if p_line > 0:
            arrow(ctx, x1, y1, x2, y2, p_line, col=C['red'], lw=8)

    # 各站點地標圖章
    for name, sub, x, y, t_pt in pts:
        p_pt = prog(u, t_pt - 0.2, 0.35)
        if p_pt <= 0: continue
        ctx.save(); pop(ctx, x, y, p_pt)
        ctx.arc(x, y, 32, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=4)
        star(ctx, x, y, 16, C['orange'], 1)
        rrect(ctx, x - 75, y - 72, 150, 38, 12); fillstroke(ctx, C['white'], stroke=C['navy'], lw=3)
        text(ctx, name, x, y - 53, 22, C['navy'], bold=True)
        chip(ctx, sub, x, y + 54, 1, C['teal'], 20, tcol=C['white'])
        ctx.restore()


# ----- s6: 第 3 站卡片 + 明永曆36年(1682) 蘇姓林姓渡海入墾 -----
def s6(ep, ctx, u, T, m):
    background(ctx, T, 0)
    station_card(ctx, u, 3, "蘇姓林姓渡海入墾")
    if u < 1.9: return
    header(ctx, 3, "明永曆 36 年（西元 1682）四月", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側：渡海古帆船（福建 ➔ 台灣黑水溝）
    p_boat = prog(u, 2.1, 0.5)
    if p_boat > 0:
        ctx.save(); pop(ctx, 320, 340, p_boat)
        draw_ancient_boat(ctx, 320, 350, s=1.1, t=T)
        chip(ctx, "福建渡海渡過黑水溝", 320, 480, 1, C['blue'], 26, tcol=C['white'])
        ctx.restore()

    # 右側：蘇姓、林姓傳統大宮燈印記
    t_clan = ep.kw(6, "蘇姓")
    p_clan = prog(u, t_clan - 0.2, 0.45)
    if p_clan > 0:
        ctx.save(); pop(ctx, 770, 320, p_clan)
        draw_clan_lantern(ctx, 670, 300, char="蘇")
        chip(ctx, "蘇姓先民", 670, 435, 1, C['yellow'], 24)

        draw_clan_lantern(ctx, 860, 300, char="林")
        chip(ctx, "林姓先民", 860, 435, 1, C['yellow'], 24)
        ctx.restore()

    t_enter = ep.kw(6, "進入小半天")
    p_enter = prog(u, t_enter - 0.2, 0.4)
    if p_enter > 0:
        chip(ctx, "攜帶農具種苗・正式入墾小半天", 730, 525, p_enter, C['green'], 28, tcol=C['white'])


# ----- s7: 闢建家園・世代生根 -----
def s7(ep, ctx, u, T, m):
    background(ctx, T, 3)
    header(ctx, 3, "雲霧台地闢家園：世代安居生根", u)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 三大安居生根支柱卡片（橫排三張）
    cards = [
        ("闢建房舍", "土角厝聚落成形", 260, 0.4),
        ("引水開田", "開闢梯田與水圳", 550, ep.kw(7, "引水")),
        ("深耕茶竹", "開拓孟宗竹與茶園", 840, ep.kw(7, "茶園"))
    ]

    for title, desc, cx, t_c in cards:
        p_c = prog(u, t_c - 0.2, 0.4)
        if p_c <= 0: continue
        ctx.save(); pop(ctx, cx, 320, p_c)
        rrect(ctx, cx - 130, 180, 260, 290, 20); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
        if "房舍" in title:
            draw_cottage(ctx, cx, 260, s=0.85, u=u)
        elif "引水" in title:
            # 梯田溪流層疊灌溉
            for dy, col in [(235, C['green']), (268, (0.35, 0.65, 0.45)), (300, C['blue'])]:
                rrect(ctx, cx - 85, dy, 170, 24, 7); fillstroke(ctx, col, stroke=C['navy'], lw=2.5)
            # 水圳流動波紋
            ctx.arc(cx - 30 + math.sin(u * 5) * 8, 312, 5, 0, 2 * math.pi); ctx.set_source_rgb(*C['white']); ctx.fill()
            ctx.arc(cx + 30 + math.sin(u * 5 + 2) * 8, 312, 5, 0, 2 * math.pi); ctx.fill()
        else:
            draw_bamboo_stalk(ctx, cx - 35, 310, 68, w=9)
            draw_bamboo_stalk(ctx, cx + 25, 310, 56, w=8)
            # 可愛春筍
            ctx.move_to(cx - 5, 315); ctx.line_to(cx + 8, 315); ctx.line_to(cx + 1, 298); ctx.close_path()
            fillstroke(ctx, (0.75, 0.60, 0.35), stroke=C['navy'], lw=2)

        chip(ctx, title, cx, 360, 1, C['yellow'], 24)
        text(ctx, desc, cx, 415, 20, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()

    t_vital = ep.kw(7, "深山中繁榮")
    p_vital = prog(u, t_vital - 0.2, 0.4)
    if p_vital > 0:
        chip(ctx, "鹿谷深山中充滿生機的繁榮聚落", 550, 520, p_vital, C['orange'], 28, tcol=C['white'])


# ----- s8: 今日小半天風貌（現代觀光仙境） -----
def s8(ep, ctx, u, T, m):
    draw_xbt_background(ctx, T)
    header(ctx, "★", "今日小半天：國際知名的綠色仙境", u)
    atian(ctx, 1150, 545, 0.42, T, m, wave=True)

    # 現代三大旅遊勝景（三宮格卡片）
    spots = [
        ("孟宗竹海", "長源圳步道・竹林幽徑", 260, ep.kw(8, "孟宗竹林")),
        ("雙瀑秘境", "德興瀑布・清涼負離子", 550, ep.kw(8, "德興瀑布")),
        ("茶香漫遊", "百年凍頂烏龍・茶席慢活", 840, ep.kw(8, "放鬆心靈"))
    ]

    for title, desc, cx, t_s in spots:
        p_s = prog(u, t_s - 0.2, 0.4)
        if p_s <= 0: continue
        ctx.save(); pop(ctx, cx, 320, p_s)
        rrect(ctx, cx - 130, 180, 260, 290, 20); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)

        if "竹海" in title:
            draw_bamboo_stalk(ctx, cx - 45, 300, 75, w=10)
            draw_bamboo_stalk(ctx, cx + 15, 300, 65, w=9)
            draw_bamboo_stalk(ctx, cx + 55, 300, 80, w=10)
        elif "瀑布" in title:
            # 瀑布岩壁與水花噴泉
            rrect(ctx, cx - 55, 215, 110, 95, 10); fillstroke(ctx, (0.55, 0.58, 0.62), stroke=C['navy'], lw=3)
            rrect(ctx, cx - 22, 215, 44, 95, 6); fillstroke(ctx, C['screen'], stroke=C['blue'], lw=2.5)
            # 水花波浪
            for i in range(4):
                sp_y = 308 + math.sin(u * 8 + i) * 3
                ctx.arc(cx - 36 + i * 24, sp_y, 11, 0, 2 * math.pi); fillstroke(ctx, C['white'], stroke=C['blue'], lw=2)
        else:
            # 經典高山凍頂茶席：茶壺與茶杯＋裊裊茶香
            ctx.arc(cx, 265, 28, 0, 2 * math.pi); fillstroke(ctx, (0.68, 0.38, 0.25), stroke=C['navy'], lw=3.5)
            ctx.arc(cx - 42, 280, 12, 0, 2 * math.pi); fillstroke(ctx, C['white'], stroke=C['navy'], lw=2)
            ctx.arc(cx + 42, 280, 12, 0, 2 * math.pi); fillstroke(ctx, C['white'], stroke=C['navy'], lw=2)
            # 升騰茶香飄氣
            for st in [-10, 10]:
                sy = 225 + math.sin(u * 4 + st) * 6
                ctx.move_to(cx + st, 238); ctx.curve_to(cx + st - 8, sy, cx + st + 8, sy - 12, cx + st, sy - 24)
                ctx.set_source_rgba(0.75, 0.60, 0.45, 0.65); ctx.set_line_width(3); ctx.stroke()

        chip(ctx, title, cx, 360, 1, C['teal'], 24, tcol=C['white'])
        text(ctx, desc, cx, 415, 18, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()

    t_relax = ep.kw(8, "放鬆心靈")
    p_relax = prog(u, t_relax - 0.2, 0.4)
    if p_relax > 0:
        chip(ctx, "森呼吸・放慢腳步的世外桃源", 550, 520, p_relax, C['yellow'], 28)


# ----- s9: 總整理與下集預告 -----
def s9(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(11)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(50):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()

    tb = LEAD + ep.durs[9] * 0.78
    atian(ctx, 220, 350, 0.95, T, m, wave=u > tb)

    # 標題
    pp = prog(u, 0.2, 0.5)
    ctx.save(); pop(ctx, 780, 115, pp)
    text(ctx, "第 1 集 重點筆記", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・小半天由來與開拓史", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    # 3 列重點卡（整齊排列於 y=215, 295, 375）
    rows = [
        ("地名由來", "半天雲霧中發現平坦小台地", ep.kw(9, "半天雲霧"), C['teal']),
        ("1668 年", "林圯水沙連屯墾，勢力入鹿谷", ep.kw(9, "1668"), C['yellow']),
        ("1682 年", "蘇姓林姓渡海入墾，聚落生根", ep.kw(9, "1682"), C['pink'])
    ]
    for k, (a, b, t0, col) in enumerate(rows):
        p = prog(u, t0 - 0.2, 0.4)
        if p <= 0: continue
        y = 215 + k * 80
        ctx.save(); ctx.translate(-250 * (1 - ease_out(p)), 0)
        rrect(ctx, 450, y - 32, 700, 66, 33)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=4)
        chip(ctx, a, 555, y + 1, 1, col, 24)
        text(ctx, b, 665, y + 1, 24, C['navy'], bold=True, align='l')
        ctx.restore()

    # 下集預告橫幅（置於 y=490，不遮擋重點卡）
    t_next = ep.kw(9, "下一集")
    p_next = prog(u, t_next - 0.2, 0.5)
    if p_next > 0:
        cx, cy = 800, 490
        ctx.save(); pop(ctx, cx, cy, p_next)
        rrect(ctx, cx - 350, cy - 34, 700, 68, 20)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        chip(ctx, "下集預告", cx - 265, cy + 1, 1, C['orange'], 22, tcol=C['white'])
        text(ctx, "鑽進全台最美孟宗竹海秘境！長源圳古道漫遊", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "下集見！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
wipes = {2, 4, 6, 9}

run("xbt1", "小半天系列 EP1", scenes, "小半天_EP1_世外桃源由來.mp4", wipes=wipes)
