"""小半天旅遊系列・第 4 集：百年飄香的茶金歲月——小半天與凍頂烏龍茶
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ---------- 專屬茶鄉與品茗繪圖元件 ----------

def draw_tea_farm_bg(ctx, t):
    """小半天層疊高山茶園背景"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.74, 0.88, 0.96)
    pat.add_color_stop_rgb(0.55, 0.88, 0.94, 0.88)
    pat.add_color_stop_rgb(1.0, 0.76, 0.88, 0.75)
    ctx.set_source(pat); ctx.paint()

    # 遠景雲海茶山
    ctx.save()
    ctx.move_to(0, 480); ctx.curve_to(320, 360, 680, 440, 1280, 370); ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    fillstroke(ctx, (0.48, 0.72, 0.58), stroke=C['navy'], lw=4)

    # 近景一壟壟階梯圓弧茶園 (Tea Terraces)
    for row, (ry, col) in enumerate([(540, (0.32, 0.65, 0.44)), (600, (0.26, 0.58, 0.38)), (660, (0.20, 0.50, 0.32))]):
        ctx.move_to(0, ry)
        for rx in range(0, W + 80, 120):
            ctx.curve_to(rx + 30, ry - 22, rx + 90, ry - 22, rx + 120, ry)
        ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
        fillstroke(ctx, col, stroke=C['navy'], lw=4)
    ctx.restore()

    # 隨風飄曳的一心二葉嫩綠茶葉
    random.seed(66)
    for i in range(7):
        lx = (random.random() * W + t * (24 + i * 6)) % (W + 80) - 40
        ly = (random.random() * H + t * (16 + i * 4)) % (H + 60) - 30
        draw_leaf_particle(ctx, lx, ly, 0.8, t * 2.2 + i, col=(0.35, 0.75, 0.42))

def draw_leaf_particle(ctx, x, y, s, ang, col=C['green']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(ang)
    ctx.move_to(0, -14); ctx.curve_to(12, -8, 12, 8, 0, 14); ctx.curve_to(-12, 8, -12, -8, 0, -14); ctx.close_path()
    fillstroke(ctx, col, stroke=C['navy'], lw=2)
    ctx.restore()

def draw_gaiwan_tea(ctx, cx, cy, s=1.0, t=0.0):
    """傳統沖泡蓋碗與琥珀金湯茶具（熱氣升騰）"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    # 茶托底盤
    rrect(ctx, -75, 30, 150, 20, 10); fillstroke(ctx, (0.65, 0.40, 0.28), stroke=C['navy'], lw=3.5)
    # 陶瓷茶碗身
    ctx.move_to(-60, -15); ctx.curve_to(-65, 25, 65, 25, 60, -15); ctx.close_path()
    fillstroke(ctx, (0.98, 0.98, 0.95), stroke=C['navy'], lw=4)
    # 琥珀金黃茶湯
    ctx.save(); ctx.scale(1, 0.35); ctx.arc(0, 5 / 0.35, 48, 0, 2 * math.pi)
    fillstroke(ctx, (0.98, 0.72, 0.22), stroke=C['navy'], lw=2)
    ctx.restore()
    # 斜開茶碗蓋
    ctx.save(); ctx.translate(6, -20); ctx.rotate(0.18)
    ctx.move_to(-52, 0); ctx.curve_to(-25, -28, 25, -28, 52, 0); ctx.close_path()
    fillstroke(ctx, (0.98, 0.98, 0.95), stroke=C['navy'], lw=3.5)
    ctx.arc(0, -22, 9, 0, 2 * math.pi); fillstroke(ctx, (0.65, 0.40, 0.28), stroke=C['navy'], lw=2.5)
    ctx.restore()
    # 裊裊熟果茶香升騰
    for ox, sd in [(-18, -1), (18, 1)]:
        sy = -35 + math.sin(t * 3.5 + ox) * 8
        ctx.move_to(ox, -25); ctx.curve_to(ox + sd * 14, sy, ox - sd * 14, sy - 18, ox, sy - 36)
        ctx.set_source_rgba(0.85, 0.65, 0.35, 0.75); ctx.set_line_width(4); ctx.stroke()
    ctx.restore()


# ==================== 場景定義 (s0 ~ s5) ====================

# ----- s0: 開場 -----
def s0(ep, ctx, u, T, m):
    draw_tea_farm_bg(ctx, T)

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
        ctx.set_source_rgba(0.20, 0.18, 0.10, 0.18); ctx.fill()

        # 琥珀金與茶綠漸層底
        pat = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat.add_color_stop_rgb(0.0, 1.0, 0.90, 0.50)
        pat.add_color_stop_rgb(1.0, 0.98, 0.72, 0.28)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        sub_text = "小半天旅遊系列・第 4 集"
        sub_w = 340; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, (0.75, 0.45, 0.15), bold=True)

        text(ctx, "百年飄香的茶金歲月", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "小半天與鹿谷凍頂烏龍茶", cx, cy + 66, 48, (0.65, 0.25, 0.15), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_tea = ep.kw(0, "茶金傳奇")
    p_tea = prog(u, t_tea - 0.2, 0.4)
    if p_tea > 0:
        chip(ctx, "聞名全台凍頂烏龍", 600, 480, p_tea, C['orange'], 28, tcol=C['white'])
        star(ctx, 475, 480, 10, C['yellow'], p_tea, rot=T * 2, outline=True)

    t_taste = ep.kw(0, "茶香")
    p_taste = prog(u, t_taste - 0.2, 0.45)
    if p_taste > 0:
        chip(ctx, "茶香繚繞的慢活山城", 920, 480, p_taste, C['green'], 28, tcol=C['white'])
        star(ctx, 790, 480, 10, C['yellow'], p_taste, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("百年由來\n林鳳池引茶", "百年由來"),
        ("製茶工藝\n繁複六部曲", "六步曲"),
        ("高山茶席\n甘醇喉韻", "茶生活")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站：凍頂烏龍的起源 -----
def s2(ep, ctx, u, T, m):
    background(ctx, T, 2)
    station_card(ctx, u, 1, "凍頂烏龍的起源")
    if u < 1.9: return
    header(ctx, 1, "清咸豐年間：先賢林鳳池引進武夷烏龍茶苗", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側歷史故事卡
    p_hist = prog(u, 2.1, 0.5)
    if p_hist > 0:
        ctx.save(); pop(ctx, 330, 330, p_hist)
        rrect(ctx, 160, 160, 340, 340, 22); fillstroke(ctx, (1, 0.97, 0.90), stroke=C['navy'], lw=5)
        chip(ctx, "清咸豐年間舉人", 330, 205, 1, (0.85, 0.35, 0.25), 20, tcol=C['white'])
        text(ctx, "先賢林鳳池", 330, 275, 42, C['navy'], bold=True)
        text(ctx, "從福建武夷山引進 36 株茶苗", 330, 330, 20, (0.42, 0.38, 0.35), bold=True)
        chip(ctx, "奠定鹿谷凍頂茶業基石", 330, 400, 1, C['yellow'], 22)
        ctx.restore()

    # 右側風土優勢卡
    p_terroir = prog(u, 2.5, 0.5)
    if p_terroir > 0:
        ctx.save(); pop(ctx, 770, 330, p_terroir)
        rrect(ctx, 560, 180, 420, 250, 22); fillstroke(ctx, C['white'], stroke=C['green'], lw=5)
        chip(ctx, "小半天得天獨厚的茶鄉風土", 770, 225, 1, C['green'], 24, tcol=C['white'])
        text(ctx, "✦ 終年雲霧籠罩，濕度適中", 770, 280, 22, C['navy'], bold=True)
        text(ctx, "✦ 日夜溫差大，茶多酚豐富", 770, 325, 22, C['navy'], bold=True)
        text(ctx, "✦ 孕育獨步全台的甘純喉韻", 770, 370, 22, (0.75, 0.35, 0.15), bold=True)
        ctx.restore()


# ----- s3: 第 2 站：傳統製茶工藝六部曲 -----
def s3(ep, ctx, u, T, m):
    background(ctx, T, 0)
    station_card(ctx, u, 2, "傳統製茶工藝")
    if u < 1.9: return
    header(ctx, 2, "製茶職人六部曲：慢工細活出好茶", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 4 格製茶工藝卡片橫排展示
    steps = [
        ("採茶與萎凋", "一心二葉 Sunlight", 210, 2.1, C['green']),
        ("炒青殺青", "大鐵鍋高溫保香", 470, ep.kw(3, "炒青"), C['orange']),
        ("揉捻成球", "布巾反覆裹揉", 730, ep.kw(3, "揉捻"), C['teal']),
        ("慢火炭焙", "龍眼木炭香淬鍊", 990, ep.kw(3, "烘焙"), (0.85, 0.35, 0.22))
    ]

    for title, desc, cx, t_s, col in steps:
        p_s = prog(u, t_s - 0.2, 0.45)
        if p_s <= 0: continue
        ctx.save(); pop(ctx, cx, 330, p_s)
        rrect(ctx, cx - 115, 190, 230, 270, 20); fillstroke(ctx, C['white'], stroke=C['navy'], lw=4.5)
        # 工藝小圖章
        ctx.arc(cx, 260, 36, 0, 2 * math.pi); fillstroke(ctx, col, stroke=C['navy'], lw=3)
        star(ctx, cx, 260, 16, C['white'], 1)
        chip(ctx, title, cx, 345, 1, col, 22, tcol=C['white'])
        text(ctx, desc, cx, 400, 18, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()


# ----- s4: 第 3 站：琥珀金湯與熟果香 -----
def s4(ep, ctx, u, T, m):
    draw_tea_farm_bg(ctx, T)
    station_card(ctx, u, 3, "琥珀金湯與熟果香")
    if u < 1.9: return
    header(ctx, 3, "清澈透亮琥珀金湯：回甘持久齒頰生津", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側蓋碗茶具特寫
    p_tea = prog(u, 2.1, 0.5)
    if p_tea > 0:
        ctx.save(); pop(ctx, 340, 330, p_tea)
        draw_gaiwan_tea(ctx, 340, 330, s=1.35, t=T)
        chip(ctx, "鹿谷特色熟果香與炭焙火香", 340, 460, 1, (0.85, 0.45, 0.15), 24, tcol=C['white'])
        ctx.restore()

    # 右側品茗風味解析
    t_taste = ep.kw(4, "回甘持久")
    p_taste = prog(u, t_taste - 0.2, 0.5)
    if p_taste > 0:
        ctx.save(); pop(ctx, 770, 330, p_taste)
        rrect(ctx, 560, 190, 420, 240, 22); fillstroke(ctx, C['white'], stroke=C['orange'], lw=5)
        chip(ctx, "品茶風味筆記", 770, 235, 1, C['yellow'], 24)
        text(ctx, "🍵 茶湯：晶瑩透亮、澄淨琥珀金", 770, 290, 22, C['navy'], bold=True)
        text(ctx, "🌸 香氣：濃郁熟果韻、炭焙暖香", 770, 335, 22, C['navy'], bold=True)
        text(ctx, "✨ 喉韻：溫潤醇厚、生津回甘持久", 770, 380, 22, (0.75, 0.25, 0.15), bold=True)
        ctx.restore()


# ----- s5: 總整理與下集預告 -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(44)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(50):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()

    tb = LEAD + ep.durs[5] * 0.78
    atian(ctx, 220, 350, 0.95, T, m, wave=u > tb)

    # 標題
    pp = prog(u, 0.2, 0.5)
    ctx.save(); pop(ctx, 780, 115, pp)
    text(ctx, "第 4 集 重點筆記", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・凍頂烏龍茶與茶金歲月", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    rows = [
        ("百年茶金", "咸豐年間林鳳池引進36株烏龍茶苗", ep.kw(5, "坐下來泡一壺"), C['orange']),
        ("六部工藝", "採摘萎凋、炒青揉捻、細緻炭火烘焙", ep.kw(5, "山風吹過竹海"), C['yellow']),
        ("琥珀金湯", "獨特熟果香與焙火香，生津持久回甘", ep.kw(5, "慢活美學"), C['green'])
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
    t_next = ep.kw(5, "下一集")
    p_next = prog(u, t_next - 0.2, 0.5)
    if p_next > 0:
        cx, cy = 800, 490
        ctx.save(); pop(ctx, cx, cy, p_next)
        rrect(ctx, cx - 350, cy - 34, 700, 68, 20)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        chip(ctx, "下集預告", cx - 265, cy + 1, 1, C['orange'], 22, tcol=C['white'])
        text(ctx, "歲月沉澱的人文綠洲！石馬公園櫻花與竹藝傳奇", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "下集見！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5]
wipes = {2, 3, 4, 5}

run("xbt4", "小半天系列 EP4", scenes, "小半天_EP4_凍頂烏龍茶香傳奇.mp4", wipes=wipes)
