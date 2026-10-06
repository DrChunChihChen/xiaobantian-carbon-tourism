from cfx import *

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "範疇三：上下游的碳", "碳導遊小綠・第 4 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("範疇三\n有哪些", "範疇三有哪些"), ("為什麼\n最大", "為什麼最大"), ("自有車\nvs 外包車", "外包車")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        hotel(ctx, 220, 330, 1.1); bowl(ctx, 420, 380, 1.1, u)
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "飯店餐廳的碳也跟我有關？", "跟我有關", props)

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "範疇三＝價值鏈上下游的間接排放", u)
    corner(ctx, T, m, point=True)
    tv, tu, tb = ep.kw(3, "價值鏈"), ep.kw(3, "上下游"), ep.kw(3, "因為你的生意")
    p = prog(u, tv - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 540, 330, p); shop(ctx, 540, 360, 0.75); ctx.restore()
    q = prog(u, tu - .2, .45)
    if q > 0:
        ctx.save(); pop(ctx, 180, 330, q)
        hotel(ctx, 140, 280, 0.6); bus(ctx, 210, 420, 0.5); plane(ctx, 230, 230, 0.5)
        ctx.restore()
        chip(ctx, "上游：合作廠商", 190, 520, q, C['teal'], 24, C['white'])
        arrow(ctx, 300, 340, 400, 340, q)
        ctx.save(); pop(ctx, 880, 330, q)
        person(ctx, 850, 320, C['orange'], 1.4); trash(ctx, 940, 340, 0.8)
        ctx.restore()
        chip(ctx, "下游：旅客・廢棄物", 890, 520, q, C['pink'], 24)
        arrow(ctx, 690, 340, 790, 340, q)
    sticker(ctx, "不在你家，卻因你而生", 540, 170, u, tb - .2, C['orange'], 26)
    chip(ctx, "一樣要算進你的盤查", 540, 590, prog(u, ep.kw(3, "一樣要算") - .2, .4), C['red'], 26, C['white'])

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "範疇三有哪些")
    if u < 1.9: return
    header(ctx, 1, "兩套常見的分類", u - 1.9)
    corner(ctx, T, m)
    t15, t36 = ep.kw(4, "15 個類別"), ep.kw(4, "類別三")
    if panel(ctx, 70, 150, 450, 400, prog(u, max(2.0, t15 - .4), .45)):
        text(ctx, "溫室氣體盤查議定書", 295, 195, 28, C['teal2'])
        text(ctx, "GHG Protocol", 295, 235, 22)
        for k in range(15):
            q = prog(u, t15 + k * .06, .2)
            x, y = 122 + (k % 5) * 70, 290 + (k // 5) * 70
            rrect(ctx, x, y, 56, 56, 12); fillstroke(ctx, COLS[k % 6], lw=3, a=q)
            text(ctx, str(k + 1), x + 28, y + 28, 22, a=q)
        text(ctx, "範疇三：15 類", 295, 520, 30, a=prog(u, t15, .4))
        ctx.restore()
    if panel(ctx, 560, 150, 430, 400, prog(u, t36 - .5, .45)):
        text(ctx, "ISO 14064-1", 775, 200, 32, C['teal2'])
        for k, lab in enumerate(["類別 1：直接", "類別 2：輸入能源", "類別 3～6：其他間接"]):
            col = C['yellow'] if k == 2 else C['white']
            rrect(ctx, 600, 245 + k * 90, 350, 70, 20); fillstroke(ctx, col, lw=4)
            text(ctx, lab, 775, 280 + k * 90, 26)
        ctx.restore()

def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "旅行社常見的範疇三", u)
    corner(ctx, T, m)
    items = [("飯店", 170, 250, "飯店"), ("餐廳", 400, 250, "餐廳"), ("外包遊覽車", 640, 250, "外包遊覽車"), ("航空公司", 880, 250, "航空"),
             ("員工通勤", 280, 450, "員工通勤"), ("出差", 520, 450, "出差"), ("廢棄物", 760, 450, "廢棄物")]
    for k, (key, x, y, lab) in enumerate(items):
        p = prog(u, ep.kw(5, key) - .3, .4)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, y, p)
        ctx.arc(x, y - 10, 70, 0, 2 * math.pi); fillstroke(ctx, C['white'], lw=4)
        if k == 0: hotel(ctx, x, y - 10, 0.55)
        elif k == 1: bowl(ctx, x, y, 0.65, u)
        elif k == 2: bus(ctx, x, y - 14, 0.45, col=C['orange'])
        elif k == 3: plane(ctx, x, y - 10, 0.5)
        elif k == 4: person(ctx, x - 20, y - 6, C['teal'], 1.0); person(ctx, x + 22, y - 6, C['blue'], 1.0)
        elif k == 5: plane(ctx, x, y - 10, 0.45, col=C['teal'])
        else: trash(ctx, x, y - 14, 0.75)
        ctx.restore()
        text(ctx, lab, x, y + 84, 26, a=p)

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "為什麼最大")
    if u < 1.9: return
    header(ctx, 2, "供應鏈排放：占 6～8 成", u - 1.9)
    corner(ctx, T, m)
    t = ep.kw(6, "6 到 8 成")
    p = prog(u, max(2.0, t - 1.0), 1.2)
    if p > 0:
        x0, y0, w, h = 140, 270, 860, 90
        rrect(ctx, x0, y0, w, h, 20); fillstroke(ctx, C['white'], lw=5)
        g = w * 0.7 * ease_out(p)
        if g > 30:
            rrect(ctx, x0 + w - g, y0, g, h, 20); fillstroke(ctx, C['teal'], lw=5)
        text(ctx, "範疇一＋二", x0 + 130, y0 + 45, 28)
        text(ctx, "範疇三：供應鏈", x0 + w - g / 2, y0 + 45, 30, C['white'], a=p)
        text(ctx, "60%～80%", x0 + w - g / 2, y0 + 140, 56, C['teal2'], a=prog(u, t - .2, .4))
    src(ctx, "資料：BCG 全球企業碳盤查調查（2021，製造業），數位時代報導", u, t)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "旅行社也很類似（示意）", u)
    corner(ctx, T, m)
    ts, tb = ep.kw(7, "小部分"), ep.kw(7, "合作廠商")
    cx, cy, R = 380, 330, 170
    p = prog(u, .3, .6)
    if p > 0:
        ctx.move_to(cx, cy); ctx.arc(cx, cy, R * ease_out(p), -math.pi / 2, -math.pi / 2 + 2 * math.pi * .15); ctx.close_path(); fillstroke(ctx, C['yellow'], lw=5)
        ctx.move_to(cx, cy); ctx.arc(cx, cy, R * ease_out(p), -math.pi / 2 + 2 * math.pi * .15, 3 * math.pi / 2); ctx.close_path()
        fillstroke(ctx, C['teal'] if u > tb - .2 else C['grey'], lw=5)
        ctx.new_path()
    chip(ctx, "自家門市電・自家車油", 820, 250, prog(u, ts - .3, .4), C['yellow'], 26)
    chip(ctx, "合作廠商的排放", 820, 380, prog(u, tb - .3, .4), C['teal'], 32, C['white'])
    text(ctx, "比例為示意，實際依各公司盤查結果", 820, 460, 20, C['teal2'], a=prog(u, tb, .4))

def s8(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "範疇三最難算", u)
    corner(ctx, T, m, sweat=True)
    th, ts, td = ep.kw(8, "別人手上"), ep.kw(8, "供應商"), ep.kw(8, "資料庫")
    for k, x in enumerate([200, 400, 600]):
        p = prog(u, th - .3 + k * .15, .4)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 260, p)
        [hotel, lambda c, a, b, s: bowl(c, a, b + 20, s, u), lambda c, a, b, s: bus(c, a, b, s * .6, col=C['orange'])][k](ctx, x, 260, 0.7)
        ctx.restore()
        text(ctx, "？", x + 60, 180, 50, C['red'], a=p)
    chip(ctx, "① 請供應商提供數據", 300, 470, prog(u, ts - .2, .4), C['yellow'], 28)
    chip(ctx, "② 用資料庫係數推估", 760, 470, prog(u, td - .2, .4), C['teal'], 28, C['white'])

def s9(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "自有車 vs 外包車")
    if u < 1.9: return
    header(ctx, 3, "誰的車，決定在哪一層", u - 1.9)
    corner(ctx, T, m)
    t1, tr, t3 = ep.kw(9, "範疇一"), ep.kw(9, "租車"), ep.kw(9, "範疇三")
    for k, (t0, x, lab, sc, col, bcol) in enumerate([(t1, 300, "綠野自有", "範疇一", C['orange'], C['teal']),
                                                      (tr, 800, "向客運公司租", "範疇三", C['teal'], C['orange'])]):
        p = prog(u, max(2.0, t0 - .6), .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 300, p); bus(ctx, x, 290, 1.0, col=bcol); ctx.restore()
        chip(ctx, lab, x, 410, p, C['white'], 28)
        q = prog(u, (t1 if k == 0 else t3) - .2, .4)
        chip(ctx, sc, x, 500, q, col, 36, C['white'])

def s10(ep, ctx, u, T, m):
    def props(ctx, u, T):
        bus(ctx, 300, 300, 1.1)
        chip(ctx, "擁有者？", 300, 440, 1, C['yellow'], 30)
    boss_scene(ep, ctx, u, T, m, 10, "原來如此", "誰擁有，就決定在哪一層！", "誰擁有", props, puzzled=False, wave=True)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "旅程眼鏡：不管車是誰的", u)
    corner(ctx, T, m)
    tn, tt, td = ep.kw(11, "不管車是誰的"), ep.kw(11, "運輸服務"), ep.kw(11, "最大的差別")
    bus(ctx, 220, 230, 0.7, col=C['teal']); chip(ctx, "自有", 220, 320, 1, C['white'], 22)
    bus(ctx, 220, 450, 0.7, col=C['orange']); chip(ctx, "外包", 220, 540, 1, C['white'], 22)
    p = prog(u, tn - .2, .5)
    if p > 0:
        arrow(ctx, 330, 230, 560, 340, p); arrow(ctx, 330, 450, 560, 360, p)
        glasses(ctx, 760, 210, 0.6, C['orange'])
    chip(ctx, "運輸服務", 760, 350, prog(u, tt - .2, .4), C['orange'], 40, C['white'])
    sticker(ctx, "兩副眼鏡最大的差別", 700, 480, u, td - .2, C['pink'], 28)

def s12(ep, ctx, u, T, m):
    rows = [("範疇三", "上下游的碳", ep.kw(12, "上下游的碳")),
            ("最大塊", "常常是最大的一塊", ep.kw(12, "最大的一塊")),
            ("車是誰的", "決定範疇，不影響足跡", ep.kw(12, "車是誰的"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 4 集重點", "下集：碳足跡的邊界怎麼畫", rows)

run("cf4", "碳導遊小綠 EP4", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP4_範疇三上下游的碳.mp4", wipes={2, 4, 6, 9, 12})
