"""小半天旅遊系列・第 3 集：隱世雙瀑的沁涼奇蹟——德興瀑布與避暑秘境
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ---------- 專屬飛瀑與水文繪圖元件 ----------

def draw_waterfall_bg(ctx, t):
    """深山溪谷清涼背景：高聳岩壁、山泉水氣"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.70, 0.88, 0.96)   # 天青
    pat.add_color_stop_rgb(0.55, 0.42, 0.70, 0.78)  # 瀑布水嵐
    pat.add_color_stop_rgb(1.0, 0.22, 0.45, 0.40)   # 碧綠深潭色
    ctx.set_source(pat); ctx.paint()

    # 左右峽谷峭壁剪影
    ctx.save()
    ctx.move_to(0, 0); ctx.line_to(220, 0); ctx.curve_to(260, 240, 180, 520, 240, 720); ctx.line_to(0, 720); ctx.close_path()
    fillstroke(ctx, (0.42, 0.45, 0.48), stroke=C['navy'], lw=4)
    ctx.move_to(1280, 0); ctx.line_to(1060, 0); ctx.curve_to(1020, 240, 1100, 520, 1040, 720); ctx.line_to(1280, 720); ctx.close_path()
    fillstroke(ctx, (0.42, 0.45, 0.48), stroke=C['navy'], lw=4)
    ctx.restore()

    # 飄散的微細水霧粒子
    random.seed(99)
    for i in range(16):
        wx = (random.random() * W + math.sin(t * 2 + i) * 20)
        wy = (H - (t * (30 + i * 5) + i * 40) % (H + 40))
        ctx.arc(wx, wy, 3 + (i % 3) * 2, 0, 2 * math.pi)
        ctx.set_source_rgba(1.0, 1.0, 1.0, 0.55 + 0.3 * math.sin(t * 3 + i)); ctx.fill()

def draw_grand_waterfall(ctx, cx, cy, w, h, t=0.0):
    """德興瀑布大雙層飛瀑：上層傾瀉、中段階梯、下層奔騰入深潭"""
    ctx.save(); ctx.translate(cx, cy)
    # 岩壁巨石背景
    rrect(ctx, -w / 2, -h / 2, w, h, 20); fillstroke(ctx, (0.48, 0.50, 0.52), stroke=C['navy'], lw=5)
    
    # 上層瀑布水流
    flow1_w = w * 0.36
    rrect(ctx, -flow1_w / 2, -h / 2, flow1_w, h * 0.45, 6)
    fillstroke(ctx, (0.75, 0.92, 1.0), stroke=C['navy'], lw=2.5)

    # 下層瀑布水流（更寬更壯觀）
    flow2_w = w * 0.52
    rrect(ctx, -flow2_w / 2, -h * 0.1, flow2_w, h * 0.52, 8)
    fillstroke(ctx, (0.78, 0.94, 1.0), stroke=C['navy'], lw=2.5)

    # 飛瀑白色激流線條（高速流動）
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for k in range(5):
        lx = -flow2_w / 2 + 15 + k * (flow2_w - 30) / 4
        f = (t * 4.5 + k * 0.25) % 1.0
        ctx.move_to(lx, -h * 0.08 + f * (h * 0.48)); ctx.line_to(lx, -h * 0.08 + f * (h * 0.48) + 24)
        ctx.set_source_rgba(1.0, 1.0, 1.0, 0.9); ctx.set_line_width(5); ctx.stroke()

    # 潭底激浪與白花漩渦
    pool_y = h / 2 - 20
    ctx.save(); ctx.scale(1, 0.28)
    ctx.arc(0, pool_y / 0.28, w * 0.58, 0, 2 * math.pi)
    fillstroke(ctx, (0.22, 0.65, 0.58), stroke=C['navy'], lw=8)
    ctx.restore()

    for i in range(5):
        sw_r = 20 + ((t * 2.5 + i * 0.4) % 1.0) * 35
        ctx.arc(-w * 0.25 + i * (w * 0.5 / 4), pool_y - 8, sw_r * 0.4, 0, 2 * math.pi)
        ctx.set_source_rgba(1.0, 1.0, 1.0, 0.7); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()

def draw_twin_waterfalls(ctx, cx, cy, s=1.0, t=0.0):
    """小半天雙瀑意象：雙柱平行垂落於深綠峽谷"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    rrect(ctx, -140, -100, 280, 200, 18); fillstroke(ctx, (0.35, 0.45, 0.38), stroke=C['navy'], lw=4)
    # 左瀑
    rrect(ctx, -75, -95, 38, 170, 6); fillstroke(ctx, (0.80, 0.94, 1.0), stroke=C['navy'], lw=2.5)
    # 右瀑
    rrect(ctx, 35, -95, 38, 170, 6); fillstroke(ctx, (0.80, 0.94, 1.0), stroke=C['navy'], lw=2.5)
    # 底部水潭
    rrect(ctx, -110, 55, 220, 36, 12); fillstroke(ctx, (0.24, 0.62, 0.55), stroke=C['navy'], lw=3)
    text(ctx, "小半天雙瀑", 0, -60, 22, C['white'], bold=True)
    ctx.restore()


# ==================== 場景定義 (s0 ~ s6) ====================

# ----- s0: 開場 -----
def s0(ep, ctx, u, T, m):
    draw_waterfall_bg(ctx, T)

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

        # 沁涼冰藍漸層底
        pat = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat.add_color_stop_rgb(0.0, 0.88, 0.96, 1.0)
        pat.add_color_stop_rgb(1.0, 0.65, 0.88, 0.96)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        sub_text = "小半天旅遊系列・第 3 集"
        sub_w = 340; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, C['blue'], bold=True)

        text(ctx, "隱世雙瀑的沁涼奇蹟", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "德興瀑布與避暑秘境", cx, cy + 66, 48, (0.15, 0.45, 0.65), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_fall = ep.kw(0, "避暑勝地")
    p_fall = prog(u, t_fall - 0.2, 0.4)
    if p_fall > 0:
        chip(ctx, "南投避暑首選秘境", 600, 480, p_fall, C['teal'], 28, tcol=C['white'])
        star(ctx, 475, 480, 10, C['yellow'], p_fall, rot=T * 2, outline=True)

    t_twin = ep.kw(0, "德興瀑布")
    p_twin = prog(u, t_twin - 0.2, 0.45)
    if p_twin > 0:
        chip(ctx, "壯觀二十米雙層飛瀑", 920, 480, p_twin, C['blue'], 28, tcol=C['white'])
        star(ctx, 790, 480, 10, C['yellow'], p_twin, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("雙層飛瀑\n落差二十米", "雙層飛瀑"),
        ("壺穴奇景\n碧綠深潭", "壺穴"),
        ("負離子\n天然冷氣房", "負離子")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站：德興瀑布景觀 -----
def s2(ep, ctx, u, T, m):
    draw_waterfall_bg(ctx, T)
    station_card(ctx, u, 1, "德興瀑布景觀")
    if u < 1.9: return
    header(ctx, 1, "內樹皮坑溪源頭：高達二十公尺雙層飛瀑", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 中央大瀑布特寫
    p_fall = prog(u, 2.1, 0.5)
    if p_fall > 0:
        ctx.save(); pop(ctx, 580, 340, p_fall)
        draw_grand_waterfall(ctx, 580, 330, w=480, h=300, t=T)
        ctx.restore()

    t_loud = ep.kw(2, "白練奔騰")
    p_loud = prog(u, t_loud - 0.2, 0.4)
    if p_loud > 0:
        chip(ctx, "白練奔騰・水聲如雷澎湃壯觀", 580, 520, p_loud, C['blue'], 28, tcol=C['white'])


# ----- s3: 第 2 站：壺穴與碧綠深潭 -----
def s3(ep, ctx, u, T, m):
    background(ctx, T, 1)
    station_card(ctx, u, 2, "壺穴與碧綠深潭")
    if u < 1.9: return
    header(ctx, 2, "萬年溪水雕琢：天然巨石壺穴與翡翠深潭", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側地質景觀卡
    p_geo = prog(u, 2.1, 0.5)
    if p_geo > 0:
        ctx.save(); pop(ctx, 330, 330, p_geo)
        rrect(ctx, 160, 160, 340, 340, 22); fillstroke(ctx, (0.95, 0.98, 1.0), stroke=C['navy'], lw=5)
        chip(ctx, "地質奇觀", 330, 205, 1, C['teal'], 22, tcol=C['white'])
        text(ctx, "天然壺穴", 330, 275, 42, C['navy'], bold=True)
        text(ctx, "溪水夾帶砂石萬年迴旋沖刷", 330, 330, 20, (0.40, 0.42, 0.45), bold=True)
        chip(ctx, "大自然鬼斧神工的雕刻", 330, 400, 1, C['yellow'], 22)
        ctx.restore()

    # 右側碧綠深潭意象
    p_pool = prog(u, 2.5, 0.5)
    if p_pool > 0:
        ctx.save(); pop(ctx, 770, 330, p_pool)
        rrect(ctx, 560, 180, 420, 220, 24); fillstroke(ctx, (0.18, 0.65, 0.58), stroke=C['navy'], lw=5)
        # 潭水波紋
        for ox in range(600, 960, 55):
            wy = 270 + math.sin(T * 3 + ox) * 8
            ctx.arc(ox, wy, 16, 0.2 * math.pi, 0.8 * math.pi); ctx.set_source_rgba(1, 1, 1, 0.8); ctx.set_line_width(3.5); ctx.stroke()
        chip(ctx, "深澈如翡翠般碧綠潭水", 770, 440, 1, C['green'], 24, tcol=C['white'])
        ctx.restore()


# ----- s4: 第 3 站：天然冷氣房與負離子 -----
def s4(ep, ctx, u, T, m):
    draw_waterfall_bg(ctx, T)
    station_card(ctx, u, 3, "天然冷氣房")
    if u < 1.9: return
    header(ctx, 3, "氣溫驟降 3~5 度：滿滿負離子與芬多精", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 左右對照卡片
    cards = [
        ("天然冷氣房", "峽谷氣溫驟降 3 到 5 度", 380, 2.1, C['blue']),
        ("負離子森呼吸", "深呼吸一口，暑氣全消身心舒暢", 760, ep.kw(4, "負離子"), C['teal'])
    ]

    for title, desc, cx, t_c, col in cards:
        p_c = prog(u, t_c - 0.2, 0.45)
        if p_c <= 0: continue
        ctx.save(); pop(ctx, cx, 320, p_c)
        rrect(ctx, cx - 170, 180, 340, 260, 22); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
        if "冷氣" in title:
            # 溫度計圖示
            rrect(ctx, cx - 14, 215, 28, 70, 14); fillstroke(ctx, C['screen'], stroke=C['navy'], lw=3)
            ctx.arc(cx, 290, 22, 0, 2 * math.pi); fillstroke(ctx, (0.35, 0.70, 0.95), stroke=C['navy'], lw=3)
        else:
            # 滿滿負離子光環
            for i in range(5):
                ctx.arc(cx - 50 + i * 25, 255 + math.sin(u * 4 + i) * 8, 12, 0, 2 * math.pi)
                fillstroke(ctx, (0.80, 0.95, 0.85), stroke=C['green'], lw=2.5)
        chip(ctx, title, cx, 345, 1, col, 26, tcol=C['white'])
        text(ctx, desc, cx, 395, 20, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()


# ----- s5: 小半天雙瀑與安全守則 -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 3)
    header(ctx, "!", "秘境尋幽：小半天雙瀑與安全提醒", u)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側雙瀑圖示
    p_twin = prog(u, 0.4, 0.5)
    if p_twin > 0:
        ctx.save(); pop(ctx, 360, 330, p_twin)
        draw_twin_waterfalls(ctx, 360, 330, s=1.1, t=T)
        ctx.restore()

    # 右側安全叮嚀卡
    t_safe = ep.kw(5, "安全標示")
    p_safe = prog(u, t_safe - 0.2, 0.45)
    if p_safe > 0:
        ctx.save(); pop(ctx, 770, 330, p_safe)
        rrect(ctx, 580, 180, 380, 260, 20); fillstroke(ctx, C['white'], stroke=C['orange'], lw=5)
        chip(ctx, "阿天的安全叮嚀", 770, 220, 1, C['orange'], 24, tcol=C['white'])
        text(ctx, "1. 山區溪谷水深，切勿擅自下水", 770, 275, 20, C['navy'], bold=True)
        text(ctx, "2. 巨石濕滑，請穿著防滑登山鞋", 770, 315, 20, C['navy'], bold=True)
        text(ctx, "3. 遵守安全標示，平安開心遊", 770, 355, 20, C['navy'], bold=True)
        ctx.restore()


# ----- s6: 總整理與下集預告 -----
def s6(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(33)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(50):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()

    tb = LEAD + ep.durs[6] * 0.78
    atian(ctx, 220, 350, 0.95, T, m, wave=u > tb)

    # 標題
    pp = prog(u, 0.2, 0.5)
    ctx.save(); pop(ctx, 780, 115, pp)
    text(ctx, "第 3 集 重點筆記", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・德興瀑布與雙瀑秘境", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    rows = [
        ("雙層飛瀑", "高達二十米雙層白練奔騰，水聲如雷", ep.kw(6, "清涼的飛瀑"), C['blue']),
        ("壺穴深潭", "溪水萬年沖刷雕琢，翡翠碧綠水潭", ep.kw(6, "洗滌了心靈"), C['teal']),
        ("避暑秘境", "負離子芬多精天然冷氣房，舒暢身心", ep.kw(6, "凍頂烏龍茶"), C['green'])
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

    # 下集預告橫幅
    t_next = ep.kw(6, "下一集")
    p_next = prog(u, t_next - 0.2, 0.5)
    if p_next > 0:
        cx, cy = 800, 490
        ctx.save(); pop(ctx, cx, cy, p_next)
        rrect(ctx, cx - 350, cy - 34, 700, 68, 20)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        chip(ctx, "下集預告", cx - 265, cy + 1, 1, C['orange'], 22, tcol=C['white'])
        text(ctx, "百年飄香的茶金歲月！鹿谷凍頂烏龍茶傳奇", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "下集見！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5, s6]
wipes = {2, 3, 4, 6}

run("xbt3", "小半天系列 EP3", scenes, "小半天_EP3_德興瀑布與雙瀑.mp4", wipes=wipes)
