"""碳導遊小綠・特輯：帶團實戰減碳招式！省下一百公斤的低碳旅行秘笈"""
from cfx import *

# ==================== 特輯專屬繪圖元件 ====================

def hsr(ctx, x, y, s=1.0, u=0):
    """高鐵 700T 流線車頭"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 車軌
    ctx.move_to(-160, 56); ctx.line_to(160, 56); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(6); ctx.stroke()
    for k in range(9):
        xx = -140 + k * 35
        ctx.move_to(xx, 52); ctx.line_to(xx - 10, 62); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(4); ctx.stroke()
    # 車身本體 (白色空氣動力車頭)
    ctx.move_to(-140, 48); ctx.line_to(60, 48)
    ctx.curve_to(120, 48, 150, 30, 160, 16)
    ctx.curve_to(140, -10, 100, -24, 40, -32)
    ctx.line_to(-140, -32); ctx.close_path()
    fillstroke(ctx, C['white'], lw=5)
    # 橘色經典腰帶 (台灣高鐵招牌橘)
    ctx.move_to(-140, 16); ctx.line_to(70, 16)
    ctx.curve_to(110, 16, 135, 10, 150, 14)
    ctx.line_to(142, 26); ctx.curve_to(110, 26, 70, 26, -140, 26); ctx.close_path()
    fillstroke(ctx, C['orange'], lw=2)
    # 黑色車窗帶
    rrect(ctx, -130, -22, 120, 24, 6); fillstroke(ctx, C['navy'], lw=3)
    for k in range(3):
        rrect(ctx, -120 + k * 38, -18, 26, 16, 4); fillstroke(ctx, C['screen'], lw=2)
    # 駕駛艙流線窗
    ctx.move_to(20, -14); ctx.line_to(65, -14); ctx.curve_to(80, -6, 70, 0, 35, 0); ctx.close_path()
    fillstroke(ctx, C['navy'], lw=2)
    # 車輪
    for sd in (-90, -10):
        ctx.arc(sd, 48, 14, 0, 2 * math.pi); fillstroke(ctx, (.3, .3, .35), lw=3)
        ctx.arc(sd, 48, 5, 0, 2 * math.pi); ctx.set_source_rgb(*C['grey']); ctx.fill()
    # 速度線
    for k in range(3):
        f = (u * 2.5 + k / 3) % 1
        ctx.move_to(-160 - f * 40, -10 + k * 18); ctx.line_to(-200 - f * 50, -10 + k * 18)
        ctx.set_source_rgba(*C['teal2'], 1 - f); ctx.set_line_width(4); ctx.stroke()
    ctx.restore()

def sedan(ctx, x, y, s=1.0, u=0):
    """自用小客車"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 車身
    ctx.move_to(-80, 20); ctx.line_to(-80, 0); ctx.curve_to(-75, -20, -50, -22, -35, -24)
    ctx.line_to(-20, -50); ctx.curve_to(-10, -58, 20, -58, 35, -50)
    ctx.line_to(55, -22); ctx.curve_to(75, -20, 80, 0, 80, 20); ctx.close_path()
    fillstroke(ctx, C['red'], lw=5)
    # 車窗
    ctx.move_to(-18, -46); ctx.line_to(28, -46); ctx.line_to(45, -24); ctx.line_to(-28, -24); ctx.close_path()
    fillstroke(ctx, C['screen'], lw=3)
    ctx.move_to(-2, -46); ctx.line_to(-2, -24); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
    # 輪子
    for sd in (-46, 46):
        ctx.arc(sd, 22, 16, 0, 2 * math.pi); fillstroke(ctx, C['navy'], lw=3)
        ctx.arc(sd, 22, 6, 0, 2 * math.pi); ctx.set_source_rgb(*C['grey']); ctx.fill()
    # 排氣黑煙
    if u > 0:
        smoke(ctx, -85, 15, u, a=0.8)
    ctx.restore()

def balance_scale(ctx, x, y, s=1.0, tilt=0.0):
    """天平秤：tilt 傾斜弧度（負值代表左邊重向下傾斜）"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 底座與中柱
    ctx.move_to(-60, 110); ctx.line_to(60, 110); ctx.line_to(40, 95); ctx.line_to(-40, 95); ctx.close_path()
    fillstroke(ctx, C['grey'], lw=4)
    rrect(ctx, -10, -30, 20, 128, 6); fillstroke(ctx, (.45, .48, .55), lw=4)
    ctx.arc(0, -30, 16, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=4)
    # 橫梁
    ctx.save(); ctx.translate(0, -30); ctx.rotate(tilt)
    rrect(ctx, -170, -8, 340, 16, 6); fillstroke(ctx, (.35, .38, .44), lw=3)
    lx, rx = -150, 150
    ctx.arc(lx, 0, 8, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=2)
    ctx.arc(rx, 0, 8, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=2)
    ctx.restore()
    # 秤盤
    rad = tilt
    p1x, p1y = -150 * math.cos(rad), -30 - 150 * math.sin(rad)
    p2x, p2y = 150 * math.cos(rad), -30 + 150 * math.sin(rad)
    for px, py in [(p1x, p1y), (p2x, p2y)]:
        ctx.move_to(px, py); ctx.line_to(px - 45, py + 90); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
        ctx.move_to(px, py); ctx.line_to(px + 45, py + 90); ctx.stroke()
        ctx.save(); ctx.translate(px, py + 90); ctx.scale(1, 0.28)
        ctx.arc(0, 0, 58, 0, 2 * math.pi); ctx.restore(); fillstroke(ctx, (.85, .88, .92), lw=4)
    ctx.restore()

def steak_dish(ctx, x, y, s=1.0, u=0):
    """厚切煎牛排"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.45); ctx.arc(0, 0, 90, 0, 2 * math.pi); ctx.restore()
    fillstroke(ctx, C['white'], lw=5)
    ctx.save(); ctx.scale(1, 0.55)
    ctx.move_to(-50, -10); ctx.curve_to(-50, -50, 30, -50, 50, -20)
    ctx.curve_to(65, 10, 20, 50, -20, 40); ctx.curve_to(-55, 30, -55, 10, -50, -10); ctx.close_path()
    ctx.restore(); fillstroke(ctx, (.55, .20, .15), lw=4)
    for k in range(3):
        ctx.move_to(-25 + k * 22, -18); ctx.line_to(-5 + k * 22, 14)
        ctx.set_source_rgb(.30, .10, .08); ctx.set_line_width(5); ctx.stroke()
    if u > 0:
        for k in range(3):
            f = (u * 0.8 + k / 3) % 1
            ctx.move_to(-20 + k * 20, -25 - f * 35); ctx.curve_to(-12 + k * 20, -35 - f * 35, -28 + k * 20, -45 - f * 35, -20 + k * 20, -55 - f * 35)
            ctx.set_source_rgba(.6, .6, .65, 1 - f); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()

def veggie_dish(ctx, x, y, s=1.0):
    """在地當季時蔬與豆製品"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.45); ctx.arc(0, 0, 90, 0, 2 * math.pi); ctx.restore()
    fillstroke(ctx, C['white'], lw=5)
    for dx, dy in [(-35, -10), (-15, -22), (5, -15)]:
        ctx.arc(dx, dy, 18, 0, 2 * math.pi); fillstroke(ctx, (.28, .68, .36), lw=3)
    ctx.arc(36, -8, 16, 0, 2 * math.pi); fillstroke(ctx, C['red'], lw=3)
    leaf(ctx, 36, -24, 0.8, C['green'])
    rrect(ctx, -26, 4, 30, 24, 4); fillstroke(ctx, (1, .94, .75), lw=3)
    ctx.arc(18, 14, 12, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=3)
    ctx.restore()

def hotel_bed(ctx, x, y, s=1.0):
    """飯店大床"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -90, -80, 180, 80, 10); fillstroke(ctx, (.55, .38, .25), lw=4)
    rrect(ctx, -85, -20, 170, 90, 14); fillstroke(ctx, C['white'], lw=4)
    rrect(ctx, -85, 15, 170, 55, 10); fillstroke(ctx, (.40, .75, .55), lw=3)
    for sd in (-46, 46):
        rrect(ctx, sd - 32, -40, 64, 34, 8); fillstroke(ctx, C['white'], lw=3)
    rrect(ctx, -24, 26, 48, 30, 6); fillstroke(ctx, C['yellow'], lw=2.5)
    leaf(ctx, 0, 41, 0.8, C['green'])
    ctx.restore()

def eco_kit(ctx, x, y, s=1.0):
    """不塑備品組：環保隨行水壺＋竹牙刷"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -55, -45, 46, 95, 10); fillstroke(ctx, (.35, .72, .88), lw=4)
    rrect(ctx, -50, -60, 36, 16, 4); fillstroke(ctx, (.25, .55, .70), lw=3)
    leaf(ctx, -32, 5, 1.0, C['yellow'])
    ctx.save(); ctx.translate(35, 0); ctx.rotate(0.3)
    rrect(ctx, -7, -65, 14, 120, 6); fillstroke(ctx, (.78, .62, .42), lw=3)
    rrect(ctx, -8, -65, 16, 28, 4); fillstroke(ctx, C['white'], lw=2.5)
    ctx.restore()
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    intro_scene(ep, ctx, u, T, m, "帶團實戰減碳招式！", "碳導遊小綠・特輯")

# 1 路線圖
def s1(ep, ctx, u, T, m):
    roadmap_scene(ep, ctx, u, T, m, 1, [
        ("交通大對決\n高鐵省最大", "交通大對決"),
        ("吃在地旬味\n低碳好食材", "吃在地"),
        ("綠色旅宿\n不塑新密技", "綠色旅宿")
    ])

# 2 老闆提問 (阿德發音)
def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        shop(ctx, 280, 340, 0.95)
        tw = ep.kw(2, "走路")
        if u > tw - 0.2:
            rrect(ctx, 160, 480, 240, 60, 16); fillstroke(ctx, C['white'], lw=4)
            text(ctx, "要叫客人走 20 公里？", 280, 510, 22, C['red'])
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "走路吃野菜、不吹冷氣？", "走路", props, puzzled=True, sweat=True)

# 3 小綠解答迷思
def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "低碳旅行＝更精緻、更在地", u)
    corner(ctx, T, m, point=True)
    tx, tf, tl, ts = ep.kw(3, "想太多"), ep.kw(3, "吃得更鮮"), ep.kw(3, "玩得更在地"), ep.kw(3, "省下大把")
    # 左側：破除三迷思
    p = prog(u, .2, .4)
    if p > 0:
        rrect(ctx, 120, 160, 420, 380, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "常見誤區", 330, 210, 32, C['grey'])
        mis = [("只能走路苦行？", 270), ("天天吃草啃野菜？", 350), ("滿頭大汗不開冷氣？", 430)]
        for s_, yy in mis:
            text(ctx, s_, 310, yy, 26, C['navy'])
            mark(ctx, 480, yy, False, p, r=18)
    # 右側：三大亮點
    badges = [(tf, 750, 210, "吃得更鮮：在地當季旬味！", C['orange']),
              (tl, 750, 310, "玩得更深：深度低碳慢遊！", C['teal']),
              (ts, 750, 410, "省得更多：一口氣省下百公斤！", C['green'])]
    for t0, xx, yy, txt, col in badges:
        q = prog(u, t0 - .2, .45)
        if q > 0:
            ctx.save(); pop(ctx, xx, yy, q)
            chip(ctx, txt, xx, yy, 1, col, 28, C['white'], padx=20)
            ctx.restore()
    sticker(ctx, "實戰減碳秘笈！", 750, 520, u, ts + .3, C['yellow'], 34)

# 4 第一站：交通占旅程四成
def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "交通大對決")
    if u < 1.9: return
    header(ctx, 1, "交通往往占旅程碳排 40%+", u - 1.9)
    corner(ctx, T, m)
    t40, td = ep.kw(4, "四成以上"), ep.kw(4, "差距非常驚人")
    # 圓餅圖：交通占 45%
    q = prog(u, t40 - .2, .5)
    if q > 0:
        cx, cy, R = 340, 350, 130
        ctx.set_line_width(52)
        ctx.arc(cx, cy, R, 0, 2 * math.pi); ctx.set_source_rgb(*C['grey']); ctx.stroke()
        a0 = -math.pi / 2; a1 = a0 + 2 * math.pi * 0.45 * ease_out(q)
        ctx.arc(cx, cy, R, a0, a1); ctx.set_source_rgb(*C['orange']); ctx.stroke()
        ctx.new_path()
        text(ctx, f"{45 * ease_out(q):.0f}%", cx, cy - 10, 64, C['orange'])
        text(ctx, "交通排放", cx, cy + 45, 26)
    # 右側三種工具每公里排碳對比
    p = prog(u, td - .3, .45)
    if p > 0:
        rrect(ctx, 550, 160, 470, 380, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "每人每公里碳排放", 785, 210, 28)
        items = [("一人自駕開車", "170 g", 270, C['red'], sedan),
                 ("團體遊覽車", "45 g", 360, C['yellow'], bus),
                 ("台灣高鐵", "32 g", 450, C['green'], hsr)]
        for name, val, yy, col, draw_fn in items:
            chip(ctx, name, 660, yy, 1, col, 22)
            text(ctx, val, 900, yy, 28, col)
    src(ctx, "資料來源：交通部運輸研究所、台灣高鐵企業社會責任報告", u, 2.2)

# 5 第一站數據：台北高雄來回對決
def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "台北 ↔ 高雄（來回約 700 公里）", u)
    corner(ctx, T, m, point=True)
    t120, th, t25, t100 = ep.kw(5, "120"), ep.kw(5, "高鐵"), ep.kw(5, "25"), ep.kw(5, "省下將近 100")
    # 左卡：自駕 120 kg
    p1 = prog(u, .2, .45)
    if p1 > 0:
        ctx.save(); pop(ctx, 330, 330, p1)
        rrect(ctx, 130, 170, 400, 350, 24); fillstroke(ctx, C['white'], lw=5)
        sedan(ctx, 330, 250, 1.2, u)
        text(ctx, "一人開車自駕", 330, 340, 28, C['navy'])
        rrect(ctx, 180, 390, 300, 80, 16); fillstroke(ctx, C['red'], lw=3)
        text(ctx, "120 kg CO2e", 330, 435, 34, C['white'])
        ctx.restore()
    # 右卡：高鐵 25 kg
    p2 = prog(u, th - .2, .45)
    if p2 > 0:
        ctx.save(); pop(ctx, 770, 330, p2)
        rrect(ctx, 570, 170, 400, 350, 24); fillstroke(ctx, C['white'], lw=5)
        hsr(ctx, 770, 250, 1.0, u)
        text(ctx, "改搭台灣高鐵", 770, 340, 28, C['navy'])
        rrect(ctx, 620, 390, 300, 80, 16); fillstroke(ctx, C['green'], lw=3)
        text(ctx, "25 kg CO2e", 770, 435, 34, C['white'])
        ctx.restore()
    # 震撼省碳金牌
    q = prog(u, t100 - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 550, 560, q)
        chip(ctx, "每人直接省下 95 公斤碳！", 550, 560, 1, C['yellow'], 34, C['navy'], padx=28)
        ctx.restore()

# 6 第二站：牛排 vs 時蔬 天平
def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "吃在地與低碳餐")
    if u < 1.9: return
    header(ctx, 2, "進口牛肉 vs 在地時蔬", u - 1.9)
    corner(ctx, T, m)
    tb, t60, t30 = ep.kw(6, "進口牛肉"), ep.kw(6, "60"), ep.kw(6, "三十倍")
    # 天平秤 (左傾 -0.22 弧度)
    tilt = -0.22 * ease_out(prog(u, t60 - .3, .6))
    balance_scale(ctx, 550, 340, 1.25, tilt=tilt)
    # 左側牛排 (向下沉)
    p = prog(u, tb - .2, .4)
    if p > 0:
        ctx.save(); pop(ctx, 360, 350, p)
        steak_dish(ctx, 360, 340, 0.9, u)
        chip(ctx, "進口牛肉 60 kg", 360, 450, 1, C['red'], 26, C['white'])
        ctx.restore()
    # 右側時蔬 (飄揚向上)
    q = prog(u, t30 - .4, .4)
    if q > 0:
        ctx.save(); pop(ctx, 740, 240, q)
        veggie_dish(ctx, 740, 230, 0.9)
        chip(ctx, "在地時蔬 2 kg", 740, 340, 1, C['green'], 26, C['white'])
        ctx.restore()
    sticker(ctx, "相差 30 倍！", 550, 170, u, t30, C['yellow'], 36)
    src(ctx, "資料來源：Poore & Nemecek (2018), Science、環境部碳足跡資訊網", u, 2.2)

# 7 第二站實戰：菜單微調減 15kg
def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "菜單小微調，美味又減碳", u)
    corner(ctx, T, m, point=True)
    tj, tr, t15 = ep.kw(7, "在地當季"), ep.kw(7, "少一點長途空運"), ep.kw(7, "15 公斤")
    # 左側盤查卡
    if panel(ctx, 100, 160, 420, 380, prog(u, .2, .45)):
        text(ctx, "原菜單：進口空運大餐", 310, 210, 28, C['red'])
        steak_dish(ctx, 310, 300, 0.8, u)
        text(ctx, "每人餐飲約 22 kg CO2e", 310, 400, 24)
        mark(ctx, 470, 210, False, 1.0, r=18)
        ctx.restore()
    # 右側低碳升級卡
    if panel(ctx, 550, 160, 450, 380, prog(u, tj - .2, .45)):
        text(ctx, "升級：在地旬味蔬果餐", 775, 210, 28, C['green'])
        veggie_dish(ctx, 775, 300, 0.8)
        text(ctx, "每人餐飲僅約 7 kg CO2e", 775, 400, 24)
        mark(ctx, 950, 210, True, 1.0, r=18)
        ctx.restore()
    q = prog(u, t15 - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 550, 560, q)
        chip(ctx, "單日每位旅客減碳 -15 kg CO2e！", 550, 560, 1, C['teal'], 32, C['white'], padx=24)
        ctx.restore()

# 8 第三站：綠色旅宿不換床單
def s8(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "綠色旅宿與不塑旅程")
    if u < 1.9: return
    header(ctx, 3, "連續住宿不換單", u - 1.9)
    corner(ctx, T, m)
    ts, t3 = ep.kw(8, "不更換床單毛巾"), ep.kw(8, "3 公斤")
    p = prog(u, 2.0, .45)
    if p > 0:
        hotel_bed(ctx, 340, 350, 1.35)
        chip(ctx, "愛地球・連續住宿不換單", 340, 530, prog(u, ts - .2, .4), C['yellow'], 26)
    # 右側節省效益卡
    q = prog(u, t3 - .4, .45)
    if q > 0:
        rrect(ctx, 570, 170, 440, 350, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "減少洗滌與烘乾能耗", 790, 220, 28)
        items = [("省水 150 公升", 290, C['blue']),
                 ("省電 4.5 度", 360, C['yellow']),
                 ("每房每晚減碳 3 kg！", 440, C['green'])]
        for s_, yy, col in items:
            chip(ctx, s_, 790, yy, 1, col, 26, C['white'] if col != C['yellow'] else C['navy'])
    sticker(ctx, "輕鬆省 3 公斤！", 790, 560, u, t3, C['green'], 34)

# 9 第三站：自備備品與水壺
def s9(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "自備備品，向塑膠說不", u)
    corner(ctx, T, m, point=True)
    tb, tp, t2 = ep.kw(9, "自備牙刷水壺"), ep.kw(9, "一次性備品"), ep.kw(9, "2 公斤")
    # 左側：一次性垃圾 ❌
    p = prog(u, .2, .45)
    if p > 0:
        rrect(ctx, 120, 170, 400, 350, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "一次性備品", 320, 220, 28, C['red'])
        trash(ctx, 320, 310, 1.2)
        bottle(ctx, 250, 330, 0.8)
        mark(ctx, 470, 220, False, 1.0, r=18)
        text(ctx, "大量塑膠廢棄焚化", 320, 440, 24, C['grey'])
    # 右側：自備環保組 ✓
    q = prog(u, tb - .2, .45)
    if q > 0:
        rrect(ctx, 560, 170, 440, 350, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "自備環保好物", 780, 220, 28, C['green'])
        eco_kit(ctx, 780, 320, 1.2)
        mark(ctx, 950, 220, True, 1.0, r=18)
        chip(ctx, "整趟再省 2 kg CO2e！", 780, 440, 1, C['teal'], 28, C['white'])
    sticker(ctx, "不塑更輕盈！", 550, 560, u, t2, C['yellow'], 34)

# 10 阿德頓悟（老闆配音）
def s10(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "帶團實戰減碳成績單", u)
    th, tv, tb, t100 = ep.kw(10, "高鐵"), ep.kw(10, "產地時蔬"), ep.kw(10, "自備備品"), ep.kw(10, "一百公斤")
    # 左側老闆興奮按讚
    boss(ctx, 260, 390, 0.95, T, m, happy=True, wave=True)
    speech(ctx, "真的能省下一百公斤耶！", 260, 170, prog(u, t100 - .3, .4), size=28)
    # 右側計分板
    p = prog(u, .2, .45)
    if p > 0:
        rrect(ctx, 480, 160, 520, 380, 24); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "低碳遊程減碳算盤", 740, 210, 30)
        scores = [("改搭高鐵軌道", "-95 kg", th, C['green']),
                  ("在地旬味低碳餐", "-15 kg", tv, C['teal']),
                  ("不換單與自備備品", "-5 kg", tb, C['blue'])]
        for k, (name, val, t_, col) in enumerate(scores):
            yy = 270 + k * 60
            chip(ctx, name, 620, yy, prog(u, t_ - .2, .4), col, 24, C['white'] if col != C['yellow'] else C['navy'])
            text(ctx, val, 910, yy, 28, col, a=prog(u, t_ - .2, .4))
        # 分隔線與總分
        ctx.move_to(510, 450); ctx.line_to(970, 450); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(4); ctx.stroke()
        q = prog(u, t100 - .3, .4)
        if q > 0:
            text(ctx, "合計減碳：", 630, 495, 30)
            text(ctx, "115 kg CO2e！", 850, 495, 38, C['red'])
    quiet_lu(ctx, T, wave=True)

# 11 結尾總結
def s11(ep, ctx, u, T, m):
    rows = [
        ("大眾運輸", "高鐵直接省下近百公斤", ep.kw(11, "大眾運輸省最大")),
        ("吃在地", "多旬味蔬食少空運紅肉", ep.kw(11, "吃在地少紅肉")),
        ("綠色旅宿", "自備備品連續住宿不換單", ep.kw(11, "自備備品不換單"))
    ]
    outro_doc(ep, ctx, u, T, m, 11, "實戰減碳秘笈", "特輯：省下一百公斤的旅行", rows)

# 執行
run("cf8", "碳導遊小綠 特輯",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "碳導遊小綠_特輯_省下一百公斤的低碳旅行秘笈.mp4",
    wipes={2, 4, 6, 8, 10, 11})
