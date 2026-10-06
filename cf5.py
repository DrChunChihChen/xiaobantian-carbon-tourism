from cfx import *

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "碳足跡的邊界怎麼畫", "碳導遊小綠・第 5 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("功能單位\n生命週期", "功能單位和生命週期"), ("算 vs\n不算", "哪些要算"), ("截斷\n原則", "截斷原則")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        for k in range(8):
            person(ctx, 140 + (k % 4) * 90, 270 + (k // 4) * 120, COLS[k % 6], 1.3)
        chip(ctx, "整團", 275, 520, 1, C['yellow'], 28)
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "整團加起來就好？", "整團加起來", props)

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "要算到每一個人", u)
    corner(ctx, T, m, point=True)
    tp, tf = ep.kw(3, "每一個人"), ep.kw(3, "公平比較")
    for k in range(8):
        hl = k == 0 and u > tp
        person(ctx, 140 + (k % 4) * 90, 270 + (k // 4) * 120, C['orange'] if hl else C['grey'], 1.3, 1 if hl or u < tp else .45)
    chip(ctx, "÷ 人數", 275, 520, prog(u, tp, .4), C['yellow'], 28)
    q = prog(u, tf - .3, .45)
    if q > 0:
        for j, (lab, val, col) in enumerate([("A 行程", "每人 38 kg", C['teal']), ("B 行程", "每人 25 kg", C['pink'])]):
            ctx.save(); pop(ctx, 800, 240 + j * 150, q)
            rrect(ctx, 640, 190 + j * 150, 320, 100, 26); fillstroke(ctx, col, lw=5)
            text(ctx, lab, 720, 240 + j * 150, 30, C['white']); text(ctx, val, 870, 240 + j * 150, 28, C['white'])
            ctx.restore()
        text(ctx, "（數字為示意）", 800, 500, 20, C['teal2'], a=q)

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "功能單位和生命週期")
    if u < 1.9: return
    header(ctx, 1, "功能單位", u - 1.9)
    corner(ctx, T, m)
    t = ep.kw(4, "一人次旅行服務")
    person(ctx, 280, 330, C['orange'], 2.6, prog(u, 2.0, .4))
    big_title(ctx, "一人次旅行服務", 700, 330, u, max(2.1, t - .3), 52, sub="功能單位（觀光署指引）", w=560)

def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "生命週期三階段", u)
    corner(ctx, T, m)
    stages = [("原料取得", "食材・飯店備品", C['orange'], ep.kw(5, "原料取得")),
              ("服務", "車輛柴油・飯店用電", C['blue'], ep.kw(5, "服務階段")),
              ("廢棄處理", "垃圾・污水", C['yellow'], ep.kw(5, "廢棄處理"))]
    for k, (a, b, col, t0) in enumerate(stages):
        p = prog(u, t0 - .3, .45)
        if p <= 0: continue
        x = 100 + k * 330
        ctx.save(); ctx.translate(-80 * (1 - ease_out(p)), 0)
        ctx.move_to(x, 200); ctx.line_to(x + 290, 200); ctx.line_to(x + 330, 260); ctx.line_to(x + 290, 320); ctx.line_to(x, 320)
        if k: ctx.line_to(x + 40, 260)
        ctx.close_path(); fillstroke(ctx, col, lw=5)
        text(ctx, a, x + 165, 260, 36, C['white'] if k < 2 else C['navy'])
        rrect(ctx, x + 10, 360, 290, 110, 22); fillstroke(ctx, C['white'], lw=4)
        text(ctx, b, x + 155, 415, 24)
        ctx.restore()

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "哪些要算")
    if u < 1.9: return
    header(ctx, 2, "要算：門市＋旅程中的四種服務", u - 1.9)
    corner(ctx, T, m)
    keys = [("門市據點", "門市據點"), ("運輸", "運輸"), ("餐飲", "餐飲"), ("住宿", "住宿"), ("遊樂活動", "遊樂活動")]
    for k, (key, lab) in enumerate(keys):
        p = prog(u, max(2.0, ep.kw(6, key) - .3), .4)
        if p <= 0: continue
        x = 140 + k * 200
        ctx.save(); pop(ctx, x, 320, p)
        rrect(ctx, x - 85, 230, 170, 200, 26); fillstroke(ctx, C['white'], lw=5)
        text(ctx, lab, x, 290, 30)
        ctx.restore()
        mark(ctx, x, 380, True, p, r=30)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "不算：三種情況", u)
    corner(ctx, T, m)
    items = [("額外付費", "旅客自費項目", "例：自己買的點心"),
             ("故宮", "不因人數增加排放的景點", "例：故宮、陽明山"),
             ("建築", "建築與基礎設施的建造", "")]
    for k, (key, a, b) in enumerate(items):
        p = prog(u, ep.kw(7, key) - .3, .45)
        if p <= 0: continue
        y = 190 + k * 130
        ctx.save(); ctx.translate(-300 * (1 - ease_out(p)), 0)
        rrect(ctx, 120, y - 50, 860, 100, 30); fillstroke(ctx, C['white'], lw=5)
        mark(ctx, 180, y, False, 1, r=28)
        text(ctx, a, 230, y - (14 if b else 0), 32, align='l')
        if b: text(ctx, b, 232, y + 26, 22, C['teal2'], align='l')
        ctx.restore()

def s8(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "小陷阱：工作人員", u)
    corner(ctx, T, m, sweat=True)
    ts, tt, td = ep.kw(8, "司機"), ep.kw(8, "總排放"), ep.kw(8, "分母")
    for k, lab in enumerate(["司機", "領隊", "導遊"]):
        p = prog(u, ts - .2 + k * .3, .4)
        person(ctx, 180 + k * 120, 260, [C['blue'], C['teal'], C['green']][k], 1.6, p)
        text(ctx, lab, 180 + k * 120, 340, 26, a=p)
    q = prog(u, tt - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 740, 300, q)
        rrect(ctx, 520, 190, 440, 250, 30); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "總排放（含工作人員）", 740, 260, 30)
        ctx.move_to(570, 310); ctx.line_to(910, 310); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
        text(ctx, "旅客人數", 740, 365, 30)
        ctx.restore()
        mark(ctx, 960, 260, True, q, r=22)
    r = prog(u, td - .2, .4)
    if r > 0:
        mark(ctx, 960, 365, False, r, r=22)
        chip(ctx, "工作人員不算進分母", 740, 500, r, C['pink'], 26)
    src(ctx, "觀光署《旅行業遊程碳足跡計算指引》5.5", u, td)

def s9(ep, ctx, u, T, m):
    def props(ctx, u, T):
        person(ctx, 160, 300, C['green'], 1.8)
        flag(ctx, 200, 300, T, ang=-1.3, L=110)
        for k in range(4): person(ctx, 280 + k * 70, 330, COLS[k], 1.3)
    boss_scene(ep, ctx, u, T, m, 9, "原來如此", "導遊的排放，旅客一起扛！", "一起扛", props, puzzled=False, wave=True)

def s10(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "截斷原則")
    if u < 1.9: return
    header(ctx, 3, "小於 1%，可以不算", u - 1.9)
    corner(ctx, T, m)
    t1, te = ep.kw(10, "1%"), ep.kw(10, "要說明")
    vals = [("餐飲", .50, C['orange']), ("運輸", .28, C['teal']), ("門市", .12, C['yellow']), ("住宿", .06, C['pink']), ("其他", .035, C['blue']), ("某小項", .005, C['grey'])]
    for k, (lab, v, col) in enumerate(vals):
        p = prog(u, 2.0 + k * .15, .5)
        y = 160 + k * 66
        text(ctx, lab, 210, y + 18, 24, align='c', a=p)
        bar_h(ctx, 270, y, 560, 36, max(v, .01), col, p)
    q = prog(u, t1 - .2, .4)
    if q > 0:
        ctx.save(); ctx.set_dash([10, 8]); rrect(ctx, 150, 480, 720, 60, 20); ctx.set_source_rgba(*C['red'], q); ctx.set_line_width(5); ctx.stroke(); ctx.restore()
        chip(ctx, "< 1%", 940, 510, q, C['red'], 28, C['white'])
    chip(ctx, "排除要說明", 940, 420, prog(u, te - .2, .4), C['yellow'], 26)
    text(ctx, "（比例為示意）", 550, 600, 20, C['teal2'], a=q)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "排除的加起來 ≤ 5%", u)
    corner(ctx, T, m, point=True)
    t5, t95 = ep.kw(11, "5%"), ep.kw(11, "95%")
    x0, y0, w, h = 120, 260, 860, 110
    p = prog(u, .3, .6)
    rrect(ctx, x0, y0, w, h, 26); fillstroke(ctx, C['white'], lw=5)
    g = w * .95 * ease_out(prog(u, t95 - .6, .8))
    if g > 30: rrect(ctx, x0, y0, g, h, 26); fillstroke(ctx, C['green'], lw=5)
    q = prog(u, t5 - .2, .4)
    if q > 0:
        rrect(ctx, x0 + w * .95, y0, w * .05, h, 10); fillstroke(ctx, C['grey'], lw=4)
        chip(ctx, "排除 ≤ 5%", x0 + w * .95, y0 - 50, q, C['grey'], 26)
    text(ctx, "至少涵蓋 95%", x0 + w * .45, y0 + 55, 44, C['white'], a=prog(u, t95 - .2, .4))
    src(ctx, "截斷原則：觀光署《旅行業遊程碳足跡計算指引》4.2", u, t5, y=480)

def s12(ep, ctx, u, T, m):
    rows = [("功能單位", "一人次旅行服務", ep.kw(12, "一人次旅行服務")),
            ("不算", "自費項目・固定景點", ep.kw(12, "自費項目")),
            ("截斷", "1% 與 5%", ep.kw(12, "1% 和 5%"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 5 集重點", "下集：動手算一趟旅程", rows)

run("cf5", "碳導遊小綠 EP5", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP5_碳足跡的邊界.mp4", wipes={2, 4, 6, 10, 12})
