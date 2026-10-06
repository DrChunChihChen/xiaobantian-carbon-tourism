from cfx import *

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "範疇二：買來的電", "碳導遊小綠・第 3 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("範疇二\n是什麼", "範疇二是什麼"), ("係數\n怎麼用", "係數怎麼用"), ("分到\n每位旅客", "每位旅客")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        shop(ctx, 300, 360, 0.9); ac_unit(ctx, 300, 170, 0.6, u)
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "用電也會排碳喔？", "用電也會排碳", props)

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "電在別處排碳", u)
    corner(ctx, T, m, point=True)
    tp, ti = ep.kw(3, "發電廠"), ep.kw(3, "間接排放")
    shop(ctx, 820, 360, 0.85)
    p = prog(u, tp - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 260, 360, p); plant(ctx, 260, 380, 1.0, u); ctx.restore()
        chip(ctx, "燒煤、燒天然氣", 260, 520, p, C['grey'], 24)
        q = prog(u, tp + .6, .6)
        ctx.move_to(380, 360); ctx.line_to(380 + (300 * q), 360); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()
        if q > .2: bolt(ctx, 380 + 300 * q * .5, 330, .6)
    chip(ctx, "間接排放", 560, 220, prog(u, ti - .2, .4), C['orange'], 34, C['white'])

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "範疇二是什麼")
    if u < 1.9: return
    header(ctx, 1, "範疇二＝外購能源的間接排放", u - 1.9)
    corner(ctx, T, m)
    te, th, tm = ep.kw(4, "外購的電力"), ep.kw(4, "熱或蒸汽"), ep.kw(4, "最主要的")
    items = [(te, 250, "電力", C['yellow']), (th, 560, "熱", C['orange']), (th + .4, 860, "蒸汽", C['blue'])]
    for k, (t0, x, lab, col) in enumerate(items):
        p = prog(u, max(2.0, t0 - .3), .45)
        if p <= 0: continue
        big = (k == 0 and u > tm)
        ctx.save(); pop(ctx, x, 320, p * (1.15 if big else 1))
        ctx.arc(x, 320, 100, 0, 2 * math.pi); fillstroke(ctx, col, lw=6)
        if k == 0: bolt(ctx, x, 310, 1.0, C['white'])
        elif k == 1:
            ctx.move_to(x, 260); ctx.curve_to(x + 50, 310, x + 30, 370, x, 370); ctx.curve_to(x - 30, 370, x - 50, 310, x, 260); fillstroke(ctx, C['red'], lw=4)
        else:
            for j in range(3): ctx.arc(x - 30 + j * 30, 320 - (j % 2) * 16, 26, 0, 2 * math.pi); fillstroke(ctx, C['white'], lw=3)
        ctx.restore()
        text(ctx, lab, x, 460, 34, a=p)
    sticker(ctx, "旅行社最主要：電", 760, 170, u, tm - .2, C['pink'], 30)

def s5(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "係數怎麼用")
    if u < 1.9: return
    header(ctx, 2, "排放量＝用電度數 × 電力排碳係數", u - 1.9)
    corner(ctx, T, m)
    ta, tb = ep.kw(5, "活動數據"), ep.kw(5, "電費單")
    formula(ctx, u, [max(2.0, ta), ta + .5, ta + 1.0], labels=("用電度數", "排放係數", "排放量"))
    p = prog(u, tb - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 230, 450, p); bill(ctx, 230, 450, 0.7); ctx.restore()

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "114 年度電力排碳係數", u)
    corner(ctx, T, m)
    ta, tb, tg = ep.kw(6, "0.467"), ep.kw(6, "0.466"), ep.kw(6, "綠電")
    for k, (t0, x, val, lab, col) in enumerate([(ta, 320, "0.467", "全國平均", C['grey']), (tb, 780, "0.466", "產業盤查用", C['yellow'])]):
        p = prog(u, t0 - .3, .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 320, p)
        rrect(ctx, x - 190, 200, 380, 240, 34); fillstroke(ctx, col, lw=6)
        text(ctx, lab, x, 250, 32)
        text(ctx, val, x, 330, 80, C['red'] if k else C['navy'])
        text(ctx, "kg CO2e／度", x, 400, 26)
        ctx.restore()
    sticker(ctx, "產業買了比較多綠電", 780, 500, u, tg - .2, C['green'], 26)
    src(ctx, "資料：經濟部能源署 114 年度電力排碳係數（表燈非營業用戶 0.471）", u, tb)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "綠野旅行社門市：一年用電", u)
    corner(ctx, T, m, point=True)
    tv, t56 = ep.kw(7, "1 萬 2 千度"), ep.kw(7, "5.6")
    bill(ctx, 220, 330, 0.9)
    shown = 12000 * ease_out(prog(u, tv - .3, 1.0))
    if shown > 0:
        rrect(ctx, 380, 270, 280, 100, 22); fillstroke(ctx, C['navy'], lw=4)
        text(ctx, f"{shown:,.0f} 度", 520, 320, 40, C['yellow'])
    chip(ctx, "× 0.466", 740, 320, prog(u, tv + 1.0, .4), C['teal'], 34, C['white'])
    q = prog(u, t56 - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 970, 320, q)
        ctx.arc(970, 320, 110, 0, 2 * math.pi); fillstroke(ctx, C["orange"], lw=6)
        text(ctx, "≈ 5.6", 970, 300, 52, C["white"]); text(ctx, "公噸 CO2e", 970, 352, 24, C['white'])
        ctx.restore()
    chip(ctx, "12,000 × 0.466 ＝ 5,592 kg", 600, 520, prog(u, t56 + .5, .4), C['white'], 24)

def s8(ep, ctx, u, T, m):
    def props(ctx, u, T):
        bulb(ctx, 220, 300, 1.1, 1.0); ac_unit(ctx, 420, 260, 0.6, u)
    boss_scene(ep, ctx, u, T, m, 8, "老闆想省電", "換省電冷氣、LED 就變少？", "LED", props, puzzled=False)

def s9(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "減少範疇二的兩個方法", u)
    corner(ctx, T, m, wave=True)
    ts, tg = ep.kw(9, "節電"), ep.kw(9, "購買綠電")
    p = prog(u, ts - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 320, 320, p)
        rrect(ctx, 120, 170, 400, 330, 30); fillstroke(ctx, C['white'], lw=5)
        bulb(ctx, 320, 300, 1.0, 1.0)
        text(ctx, "① 節電", 320, 450, 36, C['teal2'])
        ctx.restore()
    q = prog(u, tg - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 780, 320, q)
        rrect(ctx, 580, 170, 400, 330, 30); fillstroke(ctx, C['white'], lw=5)
        # solar panel
        ctx.move_to(680, 340); ctx.line_to(720, 230); ctx.line_to(880, 230); ctx.line_to(860, 340); ctx.close_path(); fillstroke(ctx, C['blue'], lw=5)
        for j in range(1, 4):
            ctx.move_to(680 + 40 * j / 1.0 * .0 + 680 * 0, 0); ctx.new_path()
        for j in range(1, 3):
            ctx.move_to(720 + j * 53 - 13 * j, 230); ctx.line_to(680 + j * 60, 340); ctx.set_source_rgb(1, 1, 1); ctx.set_line_width(3); ctx.stroke()
        ctx.move_to(700, 285); ctx.line_to(870, 285); ctx.stroke()
        leaf(ctx, 900, 220, 1.6)
        text(ctx, "② 購買綠電", 780, 450, 36, C['green'])
        ctx.restore()

def s10(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "分到每位旅客")
    if u < 1.9: return
    header(ctx, 3, "旅程眼鏡：門市據點服務", u - 1.9)
    corner(ctx, T, m)
    tg, ts = ep.kw(10, "門市的電"), ep.kw(10, "門市據點服務")
    shop(ctx, 330, 340, 1.0)
    p = prog(u, max(2.0, tg - .2), .45)
    if p > 0: bolt(ctx, 520, 250, 0.8)
    q = prog(u, ts - .3, .45)
    if q > 0:
        glasses(ctx, 800, 220, 0.6, C['orange'])
        chip(ctx, "門市據點服務", 800, 330, q, C['orange'], 34, C['white'])
        chip(ctx, "也算進一趟旅程", 800, 420, q, C['white'], 26)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "依旅客人數比例分攤", u)
    corner(ctx, T, m, point=True)
    tr, tp = ep.kw(11, "比例來分攤"), ep.kw(11, "0.466 公斤")
    t0 = ep.kw(11, "旅客人數")
    if panel(ctx, 90, 150, 560, 280, prog(u, t0 - .3, .45)):
        text(ctx, "這團旅客人數", 370, 220, 34, C['orange'])
        ctx.move_to(150, 270); ctx.line_to(590, 270); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
        text(ctx, "門市一年服務總人數", 370, 320, 34)
        text(ctx, "× 門市一年用電", 370, 390, 26, C['teal2'], a=prog(u, tr, .4))
        ctx.restore()
    q = prog(u, tp - 1.2, .45)
    if q > 0:
        ctx.save(); pop(ctx, 870, 290, q)
        rrect(ctx, 700, 170, 340, 240, 30); fillstroke(ctx, C['yellow'], lw=5)
        person(ctx, 870, 240, C['orange'], 1.2)
        text(ctx, "1 度 × 0.466", 870, 320, 32)
        text(ctx, "＝ 0.466 kg", 870, 375, 36, C['red'], a=prog(u, tp - .2, .4))
        ctx.restore()
    src(ctx, "分配方法：觀光署《旅行業遊程碳足跡計算指引》7.5.2", u, tr)

def s12(ep, ctx, u, T, m):
    rows = [("範疇二", "買來的電", ep.kw(12, "買來的電")),
            ("× 0.466", "用電度數 × 排碳係數", ep.kw(12, "用電度數")),
            ("分攤", "依人數分給每位旅客", ep.kw(12, "依人數"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 3 集重點", "下集：範疇三，上下游的碳", rows)

run("cf3", "碳導遊小綠 EP3", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP3_範疇二買來的電.mp4", wipes={2, 4, 5, 10, 12})
