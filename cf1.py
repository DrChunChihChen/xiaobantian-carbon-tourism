from xl import *

def quiet_lu(ctx, T, **kw):  # 小綠 in corner, not talking
    xiaolu(ctx, 1150, 545, 0.42, T, 0, **kw)

def src(ctx, s, u, t0=0.6):
    q = prog(u, t0, .4)
    if q > 0: text(ctx, s, 640, 612, 18, C['teal2'], a=q)

# 0 intro
def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "旅行社也要算碳？", "碳導遊小綠・第 1 集")

# 1 roadmap
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("旅遊業的\n碳有多少", "旅遊業的碳有多少"), ("算碳的\n兩副眼鏡", "兩副眼鏡"), ("一度電\n排多少碳", "一度電")])

# 2 阿德 asks (boss voice)
def s2(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "?", "老闆的疑問", u)
    shop(ctx, 330, 330, 1.0)
    tf, tc, tq = ep.kw(2, "工廠"), ep.kw(2, "煙囪"), ep.kw(2, "哪來的碳")
    q = prog(u, tf - .2, .4)
    if q > 0:
        ctx.save(); pop(ctx, 330, 530, q)
        rrect(ctx, 270, 490, 60, 70, 4); fillstroke(ctx, C['grey'], lw=4)
        rrect(ctx, 300, 450, 22, 50, 3); fillstroke(ctx, C['grey'], lw=4)
        ctx.restore()
        mark(ctx, 380, 500, False, prog(u, tc, .3), r=24)
    boss(ctx, 780, 380, 0.95, T, m, puzzled=True)
    speech(ctx, "我又沒有煙囪，哪來的碳？", 760, 150, prog(u, tq - .4, .4), size=30)
    quiet_lu(ctx, T)

# 3 小綠 answers: four sources
def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "其實到處都在排碳", u)
    corner(ctx, T, m, point=True)
    tb, ta, th, tr = ep.kw(3, "遊覽車"), ep.kw(3, "門市冷氣"), ep.kw(3, "飯店"), ep.kw(3, "餐廳")
    items = [(tb, 210, "遊覽車：燒柴油"), (ta, 470, "門市：冷氣用電"), (th, 730, "飯店"), (tr, 960, "餐廳")]
    for k, (t0, x, lab) in enumerate(items):
        p = prog(u, t0 - .2, .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 300, p)
        if k == 0: bus(ctx, x, 300, 0.9); smoke(ctx, x - 100, 300, u)
        elif k == 1: ac_unit(ctx, x, 270, 0.8, u)
        elif k == 2: hotel(ctx, x, 300, 0.9)
        else: bowl(ctx, x, 320, 1.0, u)
        ctx.restore()
        chip(ctx, lab, x, 450, p, [C['yellow'], C['teal'], C['pink'], C['orange']][k], 24)
    sticker(ctx, "都在排碳！", 600, 540, u, tr + .5, C['red'], 32)

# 4 station 1: 8%
def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "旅遊業的碳有多少")
    if u < 1.9: return
    header(ctx, 1, "旅遊 ≈ 全球排放 8%", u - 1.9)
    corner(ctx, T, m)
    t189, t8 = ep.kw(4, "189"), ep.kw(4, "8%")
    # globe + 189 countries
    p = prog(u, 2.0, .45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 340, p)
        ctx.arc(330, 340, 150, 0, 2 * math.pi); fillstroke(ctx, C['blue'], lw=6)
        for (dx, dy, r) in [(-50, -60, 50), (60, 20, 60), (-40, 70, 34), (70, -80, 26)]:
            ctx.arc(330 + dx, 340 + dy, r, 0, 2 * math.pi); ctx.set_source_rgb(*C['green']); ctx.fill()
        ctx.restore()
        chip(ctx, "189 個國家", 330, 535, prog(u, t189, .4), C['yellow'], 28)
    # donut 8%
    tg = ep.kw(4, "全球旅遊")
    q = prog(u, tg - .2, max(.6, t8 - tg + .2))
    if q > 0:
        cx, cy, R = 800, 330, 140
        ctx.set_line_width(56)
        ctx.arc(cx, cy, R, 0, 2 * math.pi); ctx.set_source_rgb(*C['grey']); ctx.stroke()
        a0 = -math.pi / 2; a1 = a0 + 2 * math.pi * 0.08 * ease_out(q)
        ctx.arc(cx, cy, R, a0, a1); ctx.set_source_rgb(*C['orange']); ctx.stroke()
        ctx.new_path()
        text(ctx, f"{8 * ease_out(q):.0f}%", cx, cy - 10, 70, C['orange'])
        text(ctx, "旅遊相關排放", cx, cy + 50, 26)
    src(ctx, "資料：Lenzen et al. (2018), Nature Climate Change；觀光署《旅行業遊程碳足跡計算指引》", u, 2.2)

# 5 survey: 9% / 86%
def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "會算的公司不多", u)
    corner(ctx, T, m, sweat=True)
    t9, t86, ts = ep.kw(5, "9%"), ep.kw(5, "86%"), ep.kw(5, "企業調查")
    if panel(ctx, 80, 140, 470, 420, prog(u, .3, .45)):
        text(ctx, "完整算過範疇 1–3", 315, 185, 30)
        hl = prog(u, t9 - .2, .4)
        for k in range(11):
            ok = k == 5 and hl > 0
            person(ctx, 135 + (k % 6) * 70, 280 + (k // 6) * 110, C['green'] if ok else C['grey'], 1.1, 1.0 if ok else .6)
        text(ctx, "9%", 315, 500, 64, C['green'], a=hl)
        ctx.restore()
    if panel(ctx, 600, 140, 420, 420, prog(u, t86 - .4, .45)):
        text(ctx, "還在用試算表手動記", 810, 185, 30)
        for k in range(3):
            x0, y0 = 690 + k * 30, 240 + k * 30
            rrect(ctx, x0, y0, 180, 130, 8); fillstroke(ctx, C['white'], lw=4)
            for i in range(4):
                ctx.move_to(x0, y0 + 26 * (i + 1)); ctx.line_to(x0 + 180, y0 + 26 * (i + 1))
            for j in range(3):
                ctx.move_to(x0 + 45 * (j + 1), y0); ctx.line_to(x0 + 45 * (j + 1), y0 + 130)
            ctx.set_source_rgb(*C['green']); ctx.set_line_width(2); ctx.stroke()
        text(ctx, "86%", 810, 500, 64, C['red'])
        ctx.restore()
    src(ctx, "資料：BCG 全球企業碳盤查調查（2021），數位時代報導", u, t9)

# 6 station 2: two glasses
def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "算碳的兩副眼鏡")
    if u < 1.9: return
    header(ctx, 2, "兩副眼鏡", u - 1.9)
    corner(ctx, T, m)
    t1, to, t2, tf = ep.kw(6, "第一副"), ep.kw(6, "組織碳盤查"), ep.kw(6, "第二副"), ep.kw(6, "服務碳足跡")
    for k, (t0, tn, x, col, look, name, iso) in enumerate([(t1, to, 300, C['teal'], "看：整家公司・一年", "組織碳盤查", "ISO 14064-1"),
                                                           (t2, tf, 800, C['orange'], "看：一位旅客・一趟", "服務碳足跡", "ISO 14067")]):
        p = prog(u, max(2.0, t0 - .3), .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 230, p); glasses(ctx, x, 230, 1.0, col); ctx.restore()
        text(ctx, look, x, 330, 30, a=p)
        q = prog(u, tn - .2, .4)
        if q > 0:
            ctx.save(); pop(ctx, x, 440, q)
            rrect(ctx, x - 190, 395, 380, 120, 26); fillstroke(ctx, col, lw=5)
            text(ctx, name, x, 435, 42, C['white']); text(ctx, iso, x, 485, 24, C['white'])
            ctx.restore()

# 7 scopes 1/2/3
def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "公司眼鏡：範疇一、二、三", u)
    corner(ctx, T, m)
    ts = [ep.kw(7, "範疇一"), ep.kw(7, "範疇二"), ep.kw(7, "範疇三")]
    data = [("範疇 1", "自家排的", "自家遊覽車柴油", C['orange']), ("範疇 2", "買來的電", "門市冷氣用電", C['yellow']), ("範疇 3", "上下游的碳", "飯店・餐廳・航空", C['teal'])]
    for k, (t0, (sc, a, b, col)) in enumerate(zip(ts, data)):
        x = 90 + k * 315
        if not panel(ctx, x, 140, 290, 420, prog(u, t0 - .3, .45)): continue
        rrect(ctx, x, 140, 290, 70, 24); fillstroke(ctx, col, lw=5)
        text(ctx, sc, x + 145, 175, 34)
        text(ctx, a, x + 145, 250, 34, C['navy'])
        cx, cy = x + 145, 370
        if k == 0: bus(ctx, cx, cy, 0.8); smoke(ctx, cx - 92, cy, u)
        elif k == 1:
            ac_unit(ctx, cx, cy - 20, 0.75, u)
        else:
            hotel(ctx, cx - 70, cy, 0.55); bowl(ctx, cx + 10, cy + 20, 0.55, u); plane(ctx, cx + 80, cy - 40, 0.45)
        text(ctx, b, x + 145, 510, 26, C['teal2'])
        ctx.restore()

# 8 journey chain
def s8(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 2, "旅程眼鏡：一位旅客的碳足跡", u)
    corner(ctx, T, m)
    keys = ["門市報名", "搭車", "吃飯", "住宿", "玩樂", "垃圾"]
    times = [ep.kw(8, k) for k in keys]
    person(ctx, 120, 210, C['orange'], 1.4, prog(u, ep.kw(8, "一位旅客"), .4))
    stepchain(ctx, ["報名", "搭車", "吃飯", "住宿", "玩樂", "垃圾"], times, u, y=330, x0=150, x1=1010, r=56, size=26)
    tf = ep.kw(8, "通通加起來")
    q = prog(u, tf - .2, .45)
    if q > 0:
        for i in range(6):
            x = 150 + i * (1010 - 150) / 5
            arrow(ctx, x, 392, 580, 470, q, C['teal2'], 4)
    chip(ctx, "這趟旅程的碳足跡（每人）", 580, 505, prog(u, tf + .5, .4), C['orange'], 30, C['white'])
    chip(ctx, "功能單位：一人次旅行服務", 580, 580, prog(u, tf + 1.2, .4), C['white'], 22)

# 9 station 3: 0.466
def s9(ep, ctx, u, T, m):
    background(ctx, T, 5); station_card(ctx, u, 3, "一度電排多少碳")
    if u < 1.9: return
    header(ctx, 3, "電力排碳係數", u - 1.9)
    corner(ctx, T, m)
    te, tv = ep.kw(9, "經濟部能源署"), ep.kw(9, "0.466")
    chip(ctx, "經濟部能源署・114 年度・產業盤查用", 560, 190, prog(u, max(2.0, te - .2), .4), C['white'], 26)
    p = prog(u, tv - .4, .5)
    if p > 0:
        ctx.save(); pop(ctx, 560, 360, p)
        rrect(ctx, 160, 270, 800, 180, 36); fillstroke(ctx, C['yellow'], lw=6)
        # bolt
        ctx.move_to(250, 300); ctx.line_to(215, 370); ctx.line_to(245, 370); ctx.line_to(225, 425); ctx.line_to(290, 345); ctx.line_to(258, 345); ctx.line_to(280, 300); ctx.close_path()
        fillstroke(ctx, C['orange'], lw=4)
        text(ctx, "1 度電", 390, 360, 46)
        text(ctx, "→", 510, 360, 46)
        text(ctx, "0.466", 660, 345, 72, C['red'])
        text(ctx, "kg CO2e", 850, 375, 32)
        ctx.restore()
        burst(ctx, 660, 345, u, tv, R=200, n=12)
    src(ctx, "註：全國平均 0.467；表燈非營業用戶 0.471（kg CO2e/度）", u, tv + 1.0)

# 10 20 kWh x 0.466
def s10(ep, ctx, u, T, m):
    background(ctx, T, 5); header(ctx, 3, "算算看：門市冷氣一天", u)
    corner(ctx, T, m, point=True)
    t20, t93, tk = ep.kw(10, "20 度"), ep.kw(10, "9.3"), ep.kw(10, "數字一乘")
    ac_unit(ctx, 260, 250, 1.0, u)
    shown = 20 * ease_out(prog(u, t20 - .4, 1.0))
    if shown > 0:
        rrect(ctx, 160, 400, 200, 90, 18); fillstroke(ctx, C['navy'], lw=4)
        text(ctx, f"{shown:.0f} 度", 260, 445, 44, C['yellow'])
    p = prog(u, t20 + .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 760, 330, p)
        rrect(ctx, 460, 260, 600, 140, 30); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "20 × 0.466 ＝", 640, 330, 44)
        q = prog(u, t93 - .2, .4)
        if q > 0: text(ctx, "9.3 kg", 920, 330, 52, C['red'], a=q)
        ctx.restore()
    sticker(ctx, "碳看得見了！", 760, 500, u, tk, C['green'], 34)

# 11 阿德 (boss voice)
def s11(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "同一台車，兩種看法", u)
    tb = ep.kw(11, "遊覽車")
    bus(ctx, 560, 320, 1.2, T)
    glasses(ctx, 300, 200, 0.7, C['teal']); text(ctx, "公司：範疇 1 或 3", 300, 270, 26, a=prog(u, tb, .4))
    glasses(ctx, 820, 200, 0.7, C['orange']); text(ctx, "旅程：運輸服務", 820, 270, 26, a=prog(u, tb, .4))
    boss(ctx, 230, 430, 0.7, T, m, wave=True)
    sticker(ctx, "原來如此！", 560, 470, u, ep.kw(11, "都看得到") - .2, C['pink'], 28)
    quiet_lu(ctx, T, wave=True)

# 12 outro
def s12(ep, ctx, u, T, m):
    rows = [("8%", "旅遊約占全球排放", ep.kw(12, "8%")),
            ("兩副眼鏡", "公司盤查 vs 旅程足跡", ep.kw(12, "兩副眼鏡")),
            ("0.466", "每度電 kg CO2e", ep.kw(12, "0.466"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 1 集重點", "下集：範疇一，自家排的碳", rows)

run("cf1", "碳導遊小綠 EP1", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP1_旅行社也要算碳.mp4", wipes={2, 4, 6, 9, 12})
