from cfx import *

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "總整理：兩副眼鏡", "碳導遊小綠・第 7 集（完）")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("兩副眼鏡\n對照", "兩副眼鏡對照"), ("數據與\n係數", "係數怎麼選"), ("報告和\n查證", "報告和查證")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        random.seed(5); ctx.move_to(300, 330)
        for k in range(40):
            ctx.line_to(300 + 150 * math.sin(k * 1.7 + u), 330 + 110 * math.cos(k * 2.3 + u * .7))
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    boss_scene(ep, ctx, u, T, m, 2, "老闆的煩惱", "腦袋有點打結了！", "打結", props, sweat=True)

ROWS = [("依據", "ISO 14064-1", "ISO 14067"), ("看什麼", "整家公司・一年", "一位旅客・一趟"), ("怎麼分", "範疇一、二、三", "原料→服務→廢棄")]

def compare(ctx, u, tl, tr, tl_rows=None, tr_rows=None):
    x0, y0 = 90, 140
    p = prog(u, tl - .3, .45)
    if p <= 0: return
    ctx.save(); pop(ctx, 540, 340, p)
    rrect(ctx, x0, y0, 900, 80, 24); fillstroke(ctx, C['navy'], lw=0)
    A, B = x0 + 430, x0 + 735
    glasses(ctx, A - 125, y0 + 40, 0.3, C['teal']); text(ctx, "組織碳盤查", A + 10, y0 + 40, 28, C['white'])
    q = prog(u, tr - .3, .45)
    if q > 0:
        glasses(ctx, B - 125, y0 + 40, 0.3, C['orange'])
        text(ctx, "服務碳足跡", B + 10, y0 + 40, 28, C['white'], a=q)
    for k, (lab, a, b) in enumerate(ROWS):
        y = y0 + 100 + k * 100
        rrect(ctx, x0, y, 900, 84, 20); fillstroke(ctx, C['white'], lw=4)
        chip(ctx, lab, x0 + 110, y + 42, 1, COLS[k], 26)
        pa = prog(u, (tl_rows[k] if tl_rows else tl) - .2, .4)
        text(ctx, a, A, y + 42, 26, a=pa)
        pb = prog(u, (tr_rows[k] if tr_rows else tr) - .2, .4)
        text(ctx, b, B, y + 42, 26, C['orange'], a=pb)
    ctx.restore()

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "一張表就能分清楚", u)
    corner(ctx, T, m, wave=True)
    compare(ctx, u, ep.kw(3, "一張表"), 99, [99, 99, 99], [99, 99, 99])

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "兩副眼鏡對照")
    if u < 1.9: return
    header(ctx, 1, "公司眼鏡", u - 1.9)
    corner(ctx, T, m)
    compare(ctx, u, 2.0, 99, [ep.kw(4, "ISO 14064-1"), ep.kw(4, "整家公司一年"), ep.kw(4, "範疇一、二、三")], [99, 99, 99])

def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "旅程眼鏡", u)
    corner(ctx, T, m)
    tl = [-1, -1, -1]
    compare(ctx, u, -1, ep.kw(5, "旅程眼鏡"), tl, [ep.kw(5, "ISO 14067"), ep.kw(5, "一位旅客"), ep.kw(5, "原料取得")])

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "數據和係數怎麼選")
    if u < 1.9: return
    header(ctx, 2, "數據：一級優先", u - 1.9)
    corner(ctx, T, m)
    t1, t2, tp = ep.kw(6, "一級數據"), ep.kw(6, "二級數據"), ep.kw(6, "優先用")
    if panel(ctx, 90, 150, 440, 400, prog(u, max(2.0, t1 - .3), .45)):
        rrect(ctx, 90, 150, 440, 70, 24); fillstroke(ctx, C['green'], lw=5)
        text(ctx, "一級數據：現場實際取得", 310, 185, 28, C['white'])
        receipt(ctx, 220, 380, 0.75); bill(ctx, 410, 380, 0.6)
        ctx.restore()
    if panel(ctx, 590, 150, 440, 400, prog(u, t2 - .3, .45)):
        rrect(ctx, 590, 150, 440, 70, 24); fillstroke(ctx, C['grey'], lw=5)
        text(ctx, "二級數據：資料庫・文獻", 810, 185, 28)
        doc_icon(ctx, 810, 380, 0.9, "資料庫")
        ctx.restore()
    sticker(ctx, "能用一級，就優先用！", 560, 570, u, tp - .2, C['orange'], 28)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "係數選用順序", u)
    corner(ctx, T, m, point=True)
    steps = [("① 自己或供應商提供", ep.kw(7, "自己或供應商"), C['green']),
             ("② 政府公告：環境部產品碳足跡資訊網", ep.kw(7, "政府公告"), C['yellow']),
             ("③ 國際資料庫", ep.kw(7, "國際資料庫"), C['grey'])]
    for k, (s_, t0, col) in enumerate(steps):
        p = prog(u, t0 - .3, .45)
        if p <= 0: continue
        y = 190 + k * 120; x = 120 + k * 60
        ctx.save(); ctx.translate(-200 * (1 - ease_out(p)), 0)
        rrect(ctx, x, y - 45, 820 - k * 60, 90, 28); fillstroke(ctx, col, lw=5)
        text(ctx, s_, x + 30, y, 30, align='l')
        ctx.restore()
    src(ctx, "觀光署《旅行業遊程碳足跡計算指引》8.3 係數選用原則", u, 1.0)

def s8(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "報告和查證")
    if u < 1.9: return
    header(ctx, 3, "報告書＋第三方查證", u - 1.9)
    corner(ctx, T, m)
    tr, tv = ep.kw(8, "報告書"), ep.kw(8, "第三方查證")
    p = prog(u, max(2.0, tr - .3), .45)
    if p > 0:
        ctx.save(); pop(ctx, 260, 330, p); doc_icon(ctx, 260, 330, 1.3, "報告書"); ctx.restore()
        for k, (key, lab) in enumerate([("邊界", "邊界"), ("數據來源", "數據來源"), ("係數", "排放係數"), ("假設", "假設")]):
            chip(ctx, lab, 560, 200 + k * 80, prog(u, ep.kw(8, key) - .2, .4), COLS[k], 26)
    q = prog(u, tv - .3, .45)
    if q > 0:
        seal(ctx, 860, 330, 1.6 * ease_out(q) + .01, "查證")
        text(ctx, "第三方查證機構", 860, 470, 28, a=q)

def s9(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "有效期與資料保存", u)
    corner(ctx, T, m)
    t2, t6 = ep.kw(9, "兩年"), ep.kw(9, "六年")
    for k, (t0, x, big, lab, col) in enumerate([(t2, 320, "最多 2 年", "服務碳足跡有效期", C['yellow']), (t6, 790, "至少 6 年", "佐證資料保存", C['teal'])]):
        p = prog(u, t0 - .4, .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 330, p)
        rrect(ctx, x - 200, 190, 400, 280, 30); fillstroke(ctx, C['white'], lw=5)
        rrect(ctx, x - 200, 190, 400, 70, 26); fillstroke(ctx, col, lw=5)
        text(ctx, lab, x, 225, 28, C['navy'] if k == 0 else C['white'])
        text(ctx, big, x, 360, 56, C['red'])
        ctx.restore()
    src(ctx, "觀光署《旅行業遊程碳足跡計算指引》7.7、10.2", u, t6)

def s10(ep, ctx, u, T, m):
    def props(ctx, u, T):
        for k in range(3):
            ctx.save(); ctx.translate(250 + k * 18, 380 - k * 40); ctx.scale(1, .35)
            ctx.arc(0, 0, 80, 0, 2 * math.pi); ctx.restore(); fillstroke(ctx, C['yellow'], lw=5)
        text(ctx, "碳權", 286, 290, 34, C['navy'])
    boss_scene(ep, ctx, u, T, m, 10, "老闆的點子", "買碳權抵換就變少了？", "碳權", props, puzzled=False)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "碳足跡不能用抵換", u)
    corner(ctx, T, m)
    tn, ts, th = ep.kw(11, "不行喔"), ep.kw(11, "指引規定"), ep.kw(11, "從熱點下手")
    p = prog(u, tn - .2, .4)
    if p > 0:
        rrect(ctx, 140, 200, 520, 160, 30); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "抵換 → 宣稱減碳", 400, 280, 40)
        ctx.set_source_rgba(*C['red'], p); ctx.set_line_width(16); ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(170, 220); ctx.line_to(170 + 460 * p, 220 + 120 * p); ctx.stroke()
        ctx.move_to(630, 220); ctx.line_to(630 - 460 * p, 220 + 120 * p); ctx.stroke()
    chip(ctx, "指引 6.4：不得以抵換抵銷", 400, 430, prog(u, ts - .2, .4), C['yellow'], 26)
    q = prog(u, th - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 300, q); pig(ctx, 860, 280, 1.0); ctx.restore()
        chip(ctx, "真正減碳：從熱點下手", 860, 420, q, C['green'], 28, C['white'])

def s12(ep, ctx, u, T, m):
    rows = [("公司 vs 旅程", "看範疇 vs 看足跡", ep.kw(12, "公司看範疇")),
            ("一級數據", "優先使用", ep.kw(12, "優先用一級")),
            ("不能抵換", "碳足跡不能用抵換", ep.kw(12, "不能用抵換"))]
    outro_doc(ep, ctx, u, T, m, 12, "系列總整理", "謝謝跟著碳導遊小綠走完旅程", rows)

run("cf7", "碳導遊小綠 EP7", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP7_總整理.mp4", wipes={2, 4, 6, 8, 12})
