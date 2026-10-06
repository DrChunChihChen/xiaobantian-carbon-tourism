from cfx import *
SRC = "範例數據與係數：觀光署《旅行業遊程碳足跡計算指引》第八章；電力改用 114 年度 0.466"

def calc_table(ctx, u, rows, total, t_total, hl=None, t_hl=99):
    """rows: (item, qty, factor, result, t0)"""
    x0, y0 = 90, 140
    cols = [(x0, 200, "排放項目"), (x0 + 200, 200, "數據"), (x0 + 400, 270, "排放係數"), (x0 + 670, 200, "排放量 kg")]
    rrect(ctx, x0, y0, 870, 56, 18); fillstroke(ctx, C['navy'], lw=0)
    for x, w, lab in cols: text(ctx, lab, x + w / 2, y0 + 28, 24, C['white'])
    for k, (a, b, c, d, t0) in enumerate(rows):
        p = prog(u, t0 - .3, .4)
        if p <= 0: continue
        y = y0 + 70 + k * 74
        ctx.save(); ctx.translate(-200 * (1 - ease_out(p)), 0)
        fill = C['yellow'] if (hl == k and u > t_hl) else C['white']
        rrect(ctx, x0, y, 870, 62, 16); fillstroke(ctx, fill, lw=4)
        for j, ((x, w, _), s) in enumerate(zip(cols, (a, b, c, d))):
            text(ctx, s, x + w / 2, y + 31, 30 if j == 3 else 26, C['red'] if j == 3 else C['navy'])
        ctx.restore()
    q = prog(u, t_total - .3, .45)
    if q > 0:
        y = y0 + 70 + len(rows) * 74 + 6
        ctx.save(); pop(ctx, x0 + 770, y + 32, q)
        rrect(ctx, x0 + 560, y, 310, 66, 33); fillstroke(ctx, C['orange'], lw=5)
        text(ctx, f"合計 {total}", x0 + 715, y + 33, 32, C['white'])
        ctx.restore()

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "動手算一趟旅程", "碳導遊小綠・第 6 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("計算\n公式", "計算公式"), ("五種服務\n逐一算", "五種服務"), ("找出\n熱點", "碳排熱點")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        doc_icon(ctx, 300, 330, 1.2, "碳足跡")
        for k in range(3): text(ctx, "？", 180 + k * 120, 170 + (k % 2) * 30, 56, C['red'])
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "會不會很複雜？", "很複雜", props)

def formula4(ctx, u, ts, y=320):
    labs = [("數據", C['yellow']), ("排放係數", C['teal']), ("GWP", C['blue']), ("排放量", C['orange'])]
    xs = [170, 430, 690, 950]
    for k, ((lab, col), t0) in enumerate(zip(labs, ts)):
        p = prog(u, t0 - .2, .4)
        if p <= 0: continue
        ctx.save(); pop(ctx, xs[k], y, p)
        rrect(ctx, xs[k] - 95, y - 50, 190, 100, 30); fillstroke(ctx, col, lw=5)
        text(ctx, lab, xs[k], y, 34, C['navy'] if k == 0 else C['white'])
        ctx.restore()
        if k: text(ctx, "＝" if k == 3 else "×", (xs[k - 1] + xs[k]) / 2, y, 46, a=p)

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "只有一行公式", u)
    corner(ctx, T, m, point=True)
    ts = [ep.kw(3, "數據"), ep.kw(3, "排放係數"), ep.kw(3, "全球暖化潛勢"), ep.kw(3, "排放量")]
    formula4(ctx, u, ts)

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "計算公式")
    if u < 1.9: return
    header(ctx, 1, "三個元素", u - 1.9)
    corner(ctx, T, m)
    cards = [("數據", "用了多少", "例：3 公升柴油", C['yellow'], ep.kw(4, "3 公升柴油")),
             ("排放係數", "每單位排多少碳", "例：柴油 3.32 kg／公升", C['teal'], ep.kw(4, "每單位排多少碳")),
             ("GWP", "全球暖化潛勢", "換算成 CO2 當量（範例＝1）", C['blue'], ep.kw(4, "全球暖化潛勢"))]
    for k, (a, b, c, col, t0) in enumerate(cards):
        if not panel(ctx, 80 + k * 330, 160, 300, 360, prog(u, max(2.0, t0 - .4), .45)): continue
        x = 230 + k * 330
        rrect(ctx, 80 + k * 330, 160, 300, 80, 24); fillstroke(ctx, col, lw=5)
        text(ctx, a, x, 200, 36, C['navy'] if k == 0 else C['white'])
        text(ctx, b, x, 300, 30)
        text(ctx, c, x, 400, 21, C['teal2'])
        ctx.restore()

def s5(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "五種服務逐一算")
    if u < 1.9: return
    header(ctx, 2, "① 門市據點", u - 1.9)
    corner(ctx, T, m)
    rows = [("A4 影印紙", "1 包", "3.6", "3.600", max(2.0, ep.kw(5, "影印紙"))),
            ("電", "1 度", "0.466", "0.466", ep.kw(5, "一度電")),
            ("生活垃圾", "1 公斤", "0.36", "0.360", ep.kw(5, "一公斤垃圾"))]
    calc_table(ctx, u, rows, "4.4 kg", ep.kw(5, "4.4"))
    src(ctx, SRC, u, 2.4)

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "② 運輸服務", u)
    corner(ctx, T, m)
    rows = [("瓶裝水", "2 瓶", "0.121", "0.242", ep.kw(6, "兩瓶水")),
            ("柴油", "3 公升", "3.32", "9.960", ep.kw(6, "3 公升柴油")),
            ("生活垃圾", "1 公斤", "0.36", "0.360", ep.kw(6, "一公斤垃圾"))]
    calc_table(ctx, u, rows, "10.6 kg", ep.kw(6, "10.6"), hl=1, t_hl=ep.kw(6, "將近 10 公斤") - .2)
    src(ctx, SRC, u, .4)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "③ 餐飲服務", u)
    corner(ctx, T, m)
    rows = [("豬肉", "0.5 公斤", "37.1", "18.550", ep.kw(7, "半公斤豬肉")),
            ("天然氣", "0.5 立方公尺", "2.63", "1.315", ep.kw(7, "天然氣")),
            ("生活垃圾", "1 公斤", "0.36", "0.360", ep.kw(7, "一公斤垃圾"))]
    calc_table(ctx, u, rows, "20.2 kg", ep.kw(7, "20.2"))
    src(ctx, SRC, u, .4)

def s8(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "④⑤ 加總：每人碳足跡", u)
    corner(ctx, T, m, point=True)
    data = [("門市據點", 4.426, C['yellow'], .3), ("運輸服務", 10.562, C['teal'], .5), ("餐飲服務", 20.225, C['orange'], .7),
            ("住宿服務", 1.6095, C['pink'], ep.kw(8, "住宿服務")), ("遊樂活動", 1.234, C['blue'], ep.kw(8, "遊樂活動服務"))]
    for k, (lab, v, col, t0) in enumerate(data):
        p = prog(u, t0 - .2, .5)
        if p <= 0: continue
        y = 150 + k * 70
        text(ctx, lab, 190, y + 22, 26, a=p)
        bar_h(ctx, 280, y, 520, 44, v / 23, col, p)
        text(ctx, f"{v:.2f}", 280 + 520 * v / 23 * ease_out(p) + 50, y + 22, 24, a=p)
    tt, t38 = ep.kw(8, "38.06"), ep.kw(8, "每人 38")
    q = prog(u, tt - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 640, 545, q)
        rrect(ctx, 300, 510, 680, 72, 36); fillstroke(ctx, C['white'], lw=5)
        text(ctx, "合計 38.06", 470, 546, 32)
        text(ctx, "→ 每人 38 kg CO2e", 760, 546, 32, C['red'], a=prog(u, t38 - .2, .4))
        ctx.restore()

def s9(ep, ctx, u, T, m):
    def props(ctx, u, T):
        for k, (lab, v, col) in enumerate([("餐飲", 20.2, C['orange']), ("運輸", 10.6, C['teal'])]):
            x = 200 + k * 180; h = v * 14
            rrect(ctx, x - 50, 470 - h, 100, h, 12); fillstroke(ctx, col, lw=5)
            text(ctx, lab, x, 505, 28); text(ctx, f"{v}", x, 445 - h, 28)
    boss_scene(ep, ctx, u, T, m, 9, "等一下！", "餐飲怎麼比遊覽車還多？", "比遊覽車還多", props)

def s10(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "找出碳排熱點")
    if u < 1.9: return
    header(ctx, 3, "最大熱點：豬肉", u - 1.9)
    corner(ctx, T, m, sweat=True)
    t18, th = ep.kw(10, "18.6"), ep.kw(10, "將近一半")
    p = prog(u, 2.0, .45)
    if p > 0:
        ctx.save(); pop(ctx, 270, 320, p); pig(ctx, 270, 320, 1.6); ctx.restore()
        chip(ctx, "半公斤豬肉", 270, 460, p, C['white'], 28)
    q = prog(u, t18 - .3, .45)
    if q > 0:
        text(ctx, "18.6 kg", 270, 540, 44, C['red'], a=q)
    r = prog(u, th - .6, .8)
    if r > 0:
        cx, cy, R = 760, 320, 160
        ctx.move_to(cx, cy); ctx.arc(cx, cy, R, -math.pi / 2, 3 * math.pi / 2); ctx.close_path(); fillstroke(ctx, C['grey'], lw=5)
        ctx.move_to(cx, cy); ctx.arc(cx, cy, R, -math.pi / 2, -math.pi / 2 + 2 * math.pi * .487 * ease_out(r)); ctx.close_path(); fillstroke(ctx, C['pink'], lw=5)
        ctx.new_path()
        text(ctx, "48.7%", cx + 70, cy - 10, 40, C['navy'], a=r)
        text(ctx, "18.55 ÷ 38.06", cx, cy + R + 40, 24, C['teal2'], a=r)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "找到熱點，才知道從哪減碳", u)
    corner(ctx, T, m, wave=True)
    tf, tm, tv = ep.kw(11, "找到熱點"), ep.kw(11, "調整菜單"), ep.kw(11, "蔬食")
    p = prog(u, tf - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 300, 320, p)
        bowl(ctx, 300, 340, 1.4, u)
        ctx.arc(330, 300, 110, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(12); ctx.stroke()
        ctx.move_to(410, 380); ctx.line_to(490, 460); ctx.set_line_width(22); ctx.stroke()
        ctx.restore()
    chip(ctx, "調整菜單", 760, 260, prog(u, tm - .2, .4), C['yellow'], 34)
    q = prog(u, tv - .2, .4)
    chip(ctx, "多一點蔬食", 760, 380, q, C['green'], 34, C['white'])
    if q > 0: leaf(ctx, 900, 360, 2.0)

def s12(ep, ctx, u, T, m):
    rows = [("公式", "數據 × 係數 × GWP", ep.kw(12, "數據乘係數")),
            ("每人 38 kg", "這趟旅程的碳足跡", ep.kw(12, "38 公斤")),
            ("熱點", "餐飲（豬肉）", ep.kw(12, "熱點在餐飲"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 6 集重點", "下集：系列總整理", rows)

run("cf6", "碳導遊小綠 EP6", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP6_動手算一趟旅程.mp4", wipes={2, 4, 5, 10, 12})
