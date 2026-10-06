"""小半天旅遊系列・第 2 集：臥虎藏龍的綠色秘境——孟宗竹海與長源圳古道
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ---------- 專屬視覺繪圖元件 ----------

def draw_fluttering_leaf(ctx, x, y, s, ang, col=C['green'], alpha=0.85):
    """飄落的青竹葉"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(ang)
    ctx.move_to(0, -16); ctx.curve_to(14, -8, 14, 8, 0, 16); ctx.curve_to(-14, 8, -14, -8, 0, -16); ctx.close_path()
    fillstroke(ctx, col, stroke=C['navy'], lw=2.0, a=alpha)
    ctx.move_to(0, -12); ctx.line_to(0, 14); ctx.set_source_rgba(*C['navy'], alpha); ctx.set_line_width(1.5); ctx.stroke()
    ctx.restore()

def draw_bamboo_canopy_bg(ctx, t):
    """深邃翠綠的孟宗竹林背景，陽光灑落林間光束"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.82, 0.94, 0.86)   # 頂部透光淡青
    pat.add_color_stop_rgb(0.6, 0.42, 0.72, 0.52)   # 中層竹林翠綠
    pat.add_color_stop_rgb(1.0, 0.24, 0.48, 0.32)   # 底層濃鬱林蔭
    ctx.set_source(pat); ctx.paint()

    # 斜射入竹林的金色陽光光柱 (Komorebi)
    ctx.save()
    for ox, w, a in [(180, 140, 0.12), (480, 180, 0.15), (860, 160, 0.14), (1120, 120, 0.10)]:
        ctx.move_to(ox, 0); ctx.line_to(ox + 80, 0); ctx.line_to(ox - 60, 720); ctx.line_to(ox - 140, 720); ctx.close_path()
        ctx.set_source_rgba(1.0, 0.96, 0.75, a + 0.04 * math.sin(t * 1.5 + ox)); ctx.fill()
    ctx.restore()

    # 背景遠處的密密麻麻細竹林剪影
    ctx.save()
    for bx in range(30, W + 40, 45):
        sw = math.sin(t * 1.8 + bx * 0.05) * 12
        ctx.move_to(bx + sw, 0); ctx.line_to(bx - sw * 0.5, 720)
        ctx.set_source_rgba(0.20, 0.42, 0.28, 0.25); ctx.set_line_width(12); ctx.stroke()
    ctx.restore()

    # 飄逸竹葉粒子
    random.seed(88)
    for i in range(8):
        lx = (random.random() * W + t * (28 + i * 7)) % (W + 80) - 40
        ly = (random.random() * H + t * (18 + i * 4)) % (H + 60) - 30
        draw_fluttering_leaf(ctx, lx, ly, 0.75 + (i % 3) * 0.15, t * 2.0 + i, col=C['green'], alpha=0.75)

def draw_bamboo_forest(ctx, x_start, count=5, h=380, spacing=60, t=0.0):
    """繪製一叢高聳挺拔的孟宗竹林"""
    for i in range(count):
        bx = x_start + i * spacing
        sway = math.sin(t * 2.2 + i * 0.8) * 10
        ctx.save()
        # 竹桿
        ctx.move_to(bx + sway, 720 - h); ctx.line_to(bx, 720)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(22); ctx.stroke()
        ctx.move_to(bx + sway, 720 - h); ctx.line_to(bx, 720)
        ctx.set_source_rgb(*[C['green'], (0.28, 0.68, 0.38), (0.22, 0.58, 0.32)][i % 3]); ctx.set_line_width(16); ctx.stroke()
        
        # 竹節
        for seg in range(6):
            sy = 720 - h + seg * (h / 6)
            ctx.arc(bx + sway * (1 - seg / 6), sy, 11, 0, 2 * math.pi)
            ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()

        # 竹葉枝
        for ang, sd in [(-0.4, -1), (0.4, 1)]:
            ctx.save(); ctx.translate(bx + sway, 720 - h + 20); ctx.rotate(ang + sway * 0.03)
            ctx.move_to(0, 0); ctx.curve_to(sd * 24, -12, sd * 36, 0, sd * 44, 4); ctx.curve_to(sd * 32, 10, sd * 18, 10, 0, 0); ctx.close_path()
            fillstroke(ctx, C['green'], stroke=C['navy'], lw=2.2)
            ctx.restore()
        ctx.restore()

def draw_water_canal(ctx, cx, cy, w, h, t=0.0):
    """長源圳清澈流水渠道（石砌渠道壁、波光粼粼甘泉水）"""
    ctx.save(); ctx.translate(cx, cy)
    # 兩側砌石堤岸
    rrect(ctx, -w / 2 - 20, -h / 2, w + 40, h, 14); fillstroke(ctx, (0.62, 0.65, 0.68), stroke=C['navy'], lw=4)
    # 清澈水體
    rrect(ctx, -w / 2, -h / 2 + 10, w, h - 20, 8); fillstroke(ctx, (0.68, 0.88, 0.98), stroke=C['navy'], lw=3.5)
    
    # 流動水波紋
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for k in range(3):
        f = (t * 1.2 + k * 0.33) % 1.0
        wy = -h / 2 + 25 + f * (h - 50)
        ctx.move_to(-w / 2 + 25, wy); ctx.curve_to(-w / 4, wy - 8, w / 4, wy + 8, w / 2 - 25, wy)
        ctx.set_source_rgba(1.0, 1.0, 1.0, 0.85); ctx.set_line_width(4.5); ctx.stroke()

    # 溪魚（台灣馬口魚小剪影）
    for fx, fy, sp in [(-60, -15, 1.5), (40, 20, 1.2)]:
        fx_t = fx + math.sin(t * sp) * 18
        ctx.save(); ctx.translate(fx_t, fy)
        ctx.move_to(-14, 0); ctx.curve_to(-6, -6, 6, -6, 14, 0); ctx.curve_to(6, 6, -6, 6, -14, 0); ctx.close_path()
        fillstroke(ctx, (0.32, 0.48, 0.55), stroke=C['navy'], lw=1.8)
        ctx.move_to(-14, 0); ctx.line_to(-20, -5); ctx.line_to(-20, 5); ctx.close_path()
        fillstroke(ctx, (0.32, 0.48, 0.55), stroke=C['navy'], lw=1.5)
        ctx.restore()
    ctx.restore()

def draw_chessboard_statue(ctx, cx, cy, s=1.0):
    """林爽文古戰場象棋意象雕塑（巨大紅黑棋子）"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    # 木質棋盤底座
    rrect(ctx, -140, -40, 280, 80, 16); fillstroke(ctx, (0.85, 0.65, 0.42), stroke=C['navy'], lw=4)
    # 楚河漢界標記
    text(ctx, "楚 河   漢 界", 0, -15, 20, (0.42, 0.28, 0.16), bold=True)
    # 紅棋「帥」
    ctx.save(); ctx.translate(-65, 10)
    ctx.arc(0, 0, 28, 0, 2 * math.pi); fillstroke(ctx, (0.95, 0.90, 0.80), stroke=(0.82, 0.25, 0.20), lw=4)
    text(ctx, "帥", 0, 2, 28, (0.82, 0.25, 0.20), bold=True)
    ctx.restore()
    # 黑棋「將」
    ctx.save(); ctx.translate(65, 10)
    ctx.arc(0, 0, 28, 0, 2 * math.pi); fillstroke(ctx, (0.95, 0.90, 0.80), stroke=C['navy'], lw=4)
    text(ctx, "將", 0, 2, 28, C['navy'], bold=True)
    ctx.restore()
    ctx.restore()


# ==================== 場景定義 (s0 ~ s6) ====================

# ----- s0: 開場 -----
def s0(ep, ctx, u, T, m):
    draw_bamboo_canopy_bg(ctx, T)
    draw_bamboo_forest(ctx, -30, count=4, h=420, spacing=55, t=T)
    draw_bamboo_forest(ctx, 1060, count=4, h=440, spacing=55, t=T)

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
        ctx.set_source_rgba(0.10, 0.20, 0.15, 0.18); ctx.fill()

        # 嫩竹翡翠金漸層底
        pat = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat.add_color_stop_rgb(0.0, 1.0, 0.92, 0.45)
        pat.add_color_stop_rgb(1.0, 0.98, 0.78, 0.28)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        sub_text = "小半天旅遊系列・第 2 集"
        sub_w = 340; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, (0.22, 0.55, 0.35), bold=True)

        text(ctx, "臥虎藏龍的綠色秘境", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "孟宗竹海與長源圳古道", cx, cy + 66, 48, (0.18, 0.52, 0.28), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_bamboo = ep.kw(0, "綠色秘境")
    p_bamboo = prog(u, t_bamboo - 0.2, 0.4)
    if p_bamboo > 0:
        chip(ctx, "萬頃翠綠孟宗竹海", 600, 480, p_bamboo, C['teal'], 28, tcol=C['white'])
        star(ctx, 475, 480, 10, C['yellow'], p_bamboo, rot=T * 2, outline=True)

    t_canal = ep.kw(0, "長源圳")
    p_canal = prog(u, t_canal - 0.2, 0.45)
    if p_canal > 0:
        chip(ctx, "百年引水生態古道", 920, 480, p_canal, C['orange'], 28, tcol=C['white'])
        star(ctx, 800, 480, 10, C['yellow'], p_canal, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("臥虎藏龍\n萬頃竹海", "孟宗竹海"),
        ("百年傳奇\n長源圳史", "長源圳"),
        ("古戰場\n林爽文地", "林爽文")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站：孟宗竹林古道 -----
def s2(ep, ctx, u, T, m):
    draw_bamboo_canopy_bg(ctx, T)
    station_card(ctx, u, 1, "孟宗竹林古道")
    if u < 1.9: return
    header(ctx, 1, "全台最壯觀：數百公頃孟宗竹海", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左右密實大竹林
    draw_bamboo_forest(ctx, 160, count=3, h=440, spacing=65, t=T)
    draw_bamboo_forest(ctx, 820, count=3, h=450, spacing=65, t=T)

    # 中央竹林步道石階
    p_path = prog(u, 2.1, 0.5)
    if p_path > 0:
        ctx.save(); pop(ctx, 540, 360, p_path)
        for k in range(5):
            y_step = 280 + k * 45
            w_step = 240 + k * 50
            rrect(ctx, 540 - w_step / 2, y_step, w_step, 36, 12)
            fillstroke(ctx, (0.82, 0.85, 0.88), stroke=C['navy'], lw=3.5)
        chip(ctx, "長源圳竹林古道", 540, 240, 1, C['yellow'], 24)
        ctx.restore()

    t_crouch = ep.kw(2, "臥虎藏龍")
    p_crouch = prog(u, t_crouch - 0.2, 0.4)
    if p_crouch > 0:
        chip(ctx, "宛如走進電影《臥虎藏龍》世界", 540, 520, p_crouch, C['green'], 28, tcol=C['white'])


# ----- s3: 第 2 站：百年長源圳開鑿史 -----
def s3(ep, ctx, u, T, m):
    background(ctx, T, 2)
    station_card(ctx, u, 2, "百年長源圳引水史")
    if u < 1.9: return
    header(ctx, 2, "民國 12 年：先民徒手劈山鑿壁引水", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側歷史紀錄卡
    p_hist = prog(u, 2.1, 0.5)
    if p_hist > 0:
        ctx.save(); pop(ctx, 330, 330, p_hist)
        rrect(ctx, 160, 160, 340, 340, 22); fillstroke(ctx, (1, 0.97, 0.90), stroke=C['navy'], lw=5)
        chip(ctx, "日治大正 12 年（1923）", 330, 205, 1, (0.85, 0.35, 0.25), 20, tcol=C['white'])
        text(ctx, "長源圳開鑿", 330, 275, 42, C['navy'], bold=True)
        text(ctx, "解決小半天台地灌溉用水", 330, 330, 22, (0.42, 0.38, 0.35), bold=True)
        chip(ctx, "先民全憑徒手鑿開險壁", 330, 400, 1, C['yellow'], 22)
        ctx.restore()

    # 右側開鑿意象（險峻山壁與引水水圳）
    p_cliff = prog(u, 2.5, 0.5)
    if p_cliff > 0:
        ctx.save(); pop(ctx, 770, 330, p_cliff)
        draw_water_canal(ctx, 770, 330, w=380, h=160, t=T)
        chip(ctx, "活化小半天農業經濟命脈", 770, 450, 1, C['teal'], 24, tcol=C['white'])
        ctx.restore()


# ----- s4: 長源圳生態步道漫步 -----
def s4(ep, ctx, u, T, m):
    draw_bamboo_canopy_bg(ctx, T)
    header(ctx, 2, "長源圳生態步道：清溪甘泉與芬多精", u)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 中央大水圳特寫
    p_canal = prog(u, 0.4, 0.5)
    if p_canal > 0:
        draw_water_canal(ctx, 580, 290, w=540, h=180, t=T)

    # 左右立體竹海
    draw_bamboo_forest(ctx, 80, count=2, h=400, spacing=60, t=T)
    draw_bamboo_forest(ctx, 960, count=2, h=400, spacing=60, t=T)

    # 生態標籤
    t_fish = ep.kw(4, "馬口魚")
    p_fish = prog(u, t_fish - 0.2, 0.4)
    if p_fish > 0:
        chip(ctx, "台灣馬口魚與溪蝦悠游", 420, 440, p_fish, C['blue'], 26, tcol=C['white'])

    t_air = ep.kw(4, "芬多精")
    p_air = prog(u, t_air - 0.2, 0.4)
    if p_air > 0:
        chip(ctx, "漫步吸滿清甜芬多精", 740, 440, p_air, C['green'], 26, tcol=C['white'])


# ----- s5: 第 3 站：林爽文古戰場 -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 0)
    station_card(ctx, u, 3, "林爽文古戰場")
    if u < 1.9: return
    header(ctx, 3, "清乾隆 52 年：天地會抗清最後決戰", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側歷史背景
    p_hist = prog(u, 2.1, 0.5)
    if p_hist > 0:
        ctx.save(); pop(ctx, 330, 330, p_hist)
        rrect(ctx, 160, 160, 340, 340, 22); fillstroke(ctx, (1, 0.96, 0.90), stroke=C['navy'], lw=5)
        chip(ctx, "乾隆 52 年（1787）", 330, 205, 1, C['red'], 20, tcol=C['white'])
        text(ctx, "林爽文事件", 330, 275, 42, C['navy'], bold=True)
        text(ctx, "反清軍隊退守小半天深山", 330, 330, 22, (0.42, 0.38, 0.35), bold=True)
        chip(ctx, "一場悲壯而震撼的歷史決戰", 330, 400, 1, C['orange'], 22, tcol=C['white'])
        ctx.restore()

    # 右側象棋紀念雕塑意象
    t_chess = ep.kw(5, "象棋雕塑")
    p_chess = prog(u, t_chess - 0.2, 0.5)
    if p_chess > 0:
        ctx.save(); pop(ctx, 770, 330, p_chess)
        draw_chessboard_statue(ctx, 770, 320, s=1.1)
        chip(ctx, "走過烽火・回歸和平與寧靜", 770, 440, 1, C['teal'], 26, tcol=C['white'])
        ctx.restore()


# ----- s6: 總整理與下集預告 -----
def s6(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(22)
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
    text(ctx, "第 2 集 重點筆記", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・孟宗竹海與長源圳古道", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    rows = [
        ("萬頃竹海", "全台最密集孟宗竹，臥虎藏龍勝景", ep.kw(6, "長源圳"), C['teal']),
        ("百年水圳", "日治大正12年人工鑿山引水渠道", ep.kw(6, "孟宗竹海"), C['yellow']),
        ("古戰場", "清代天地會林爽文事件最後決戰地", ep.kw(6, "歷史交融"), C['pink'])
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
        text(ctx, "深山中的避暑奇蹟！德興瀑布與雙瀑秘境", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "下集見！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5, s6]
wipes = {2, 3, 5, 6}

run("xbt2", "小半天系列 EP2", scenes, "小半天_EP2_孟宗竹海長源圳.mp4", wipes=wipes)
