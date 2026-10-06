from cfx import *

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "範疇一：自家排的碳", "碳導遊小綠・第 2 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("範疇一\n有哪些", "範疇一有哪些"), ("怎麼算", "怎麼算"), ("換戴\n旅程眼鏡", "旅程眼鏡")])

def s2(ep, ctx, u, T, m):
    def props(ctx, u, T):
        bus(ctx, 300, 260, 1.0); bus(ctx, 300, 430, 1.0)
        chip(ctx, "綠野自有", 300, 540, 1, C['yellow'], 24)
    boss_scene(ep, ctx, u, T, m, 2, "老闆的疑問", "自己的遊覽車算範疇一嗎？", "範疇一嗎", props)

def s3(ep, ctx, u, T, m):
    background(ctx, T, 3); header(ctx, "!", "範疇一＝直接排放", u)
    corner(ctx, T, m, point=True)
    ta, td = ep.kw(3, "擁有或控制"), ep.kw(3, "直接排出來")
    shop(ctx, 300, 330, 0.9); bus(ctx, 620, 380, 0.8)
    q = prog(u, ta - .2, .4)
    if q > 0:
        ctx.save(); ctx.set_dash([14, 10]); rrect(ctx, 140, 180, 640, 330, 30); ctx.set_source_rgba(*C['teal2'], q); ctx.set_line_width(5); ctx.stroke(); ctx.restore()
        chip(ctx, "公司自己擁有或控制", 460, 170, q, C['teal'], 26, C['white'])
    if u > td - .2:
        smoke(ctx, 520, 370, u); smoke(ctx, 520, 330, u + .4)
    chip(ctx, "直接排出溫室氣體", 860, 300, prog(u, td - .2, .4), C['orange'], 28, C['white'])

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "範疇一有哪些")
    if u < 1.9: return
    header(ctx, 1, "燃料燃燒", u - 1.9)
    corner(ctx, T, m)
    t1, t2, t3 = ep.kw(4, "自有遊覽車"), ep.kw(4, "公務車"), ep.kw(4, "瓦斯")
    for k, (t0, x, lab, col) in enumerate([(t1, 220, "自有遊覽車：柴油", C['yellow']), (t2, 560, "公務車：汽油", C['pink']), (t3, 880, "員工廚房：瓦斯", C['teal'])]):
        p = prog(u, max(2.0, t0 - .3), .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 320, p)
        if k == 0: bus(ctx, x, 320, 0.9); smoke(ctx, x - 100, 320, u)
        elif k == 1: bus(ctx, x, 320, 0.6, col=C['blue']); smoke(ctx, x - 66, 330, u)
        else: stove(ctx, x, 350, 1.2, u)
        ctx.restore()
        chip(ctx, lab, x, 470, p, col, 26)

def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "容易被忘記：逸散排放", u)
    corner(ctx, T, m, sweat=True)
    tl, tr, t6 = ep.kw(5, "逸散排放"), ep.kw(5, "冷媒漏出來"), ep.kw(5, "677")
    p = prog(u, tl - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 260, 300, p)
        ac_unit(ctx, 230, 220, 0.8, u); fridge(ctx, 230, 420, 0.8)
        ctx.restore()
    if u > tr - .2: gas_puffs(ctx, 330, 220, u); gas_puffs(ctx, 290, 400, u + .3)
    q = prog(u, t6 - .6, .5)
    if q > 0:
        ctx.save(); pop(ctx, 760, 330, q)
        rrect(ctx, 530, 230, 460, 200, 30); fillstroke(ctx, C['yellow'], lw=6)
        text(ctx, "R-32 冷媒漏 1 公斤", 760, 280, 32)
        text(ctx, "≈ 677 kg CO2e", 760, 360, 52, C['red'])
        ctx.restore()
    src(ctx, "GWP 依 IPCC AR5（環境部溫室氣體排放係數管理表）", u, t6)

def s6(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "怎麼算")
    if u < 1.9: return
    header(ctx, 2, "排放量＝活動數據 × 排放係數", u - 1.9)
    corner(ctx, T, m)
    ta, tf, tr = ep.kw(6, "活動數據"), ep.kw(6, "排放係數"), ep.kw(6, "加油發票")
    formula(ctx, u, [max(2.0, ta), tf, tf + .5])
    p = prog(u, tr - .3, .45)
    if p > 0:
        ctx.save(); pop(ctx, 230, 470, p); receipt(ctx, 230, 470, 0.85); ctx.restore()
        arrow(ctx, 230, 360, 230, 330, p)

def s7(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "1 公升柴油燒掉會排多少？", u)
    corner(ctx, T, m, point=True)
    te, t26 = ep.kw(7, "環境部"), ep.kw(7, "2.6")
    pump(ctx, 260, 330, 1.2)
    p = prog(u, te, .45)
    if p > 0:
        ctx.save(); pop(ctx, 720, 330, p)
        rrect(ctx, 450, 240, 560, 180, 34); fillstroke(ctx, C['white'], lw=6)
        text(ctx, "1 公升柴油", 580, 330, 36)
        text(ctx, "→", 715, 330, 40)
        q = prog(u, t26 - .2, .4)
        text(ctx, "約 2.6 kg CO2", 870, 330, 40, C['red'], a=q)
        ctx.restore()
        burst(ctx, 870, 330, u, t26, R=160)
    src(ctx, "燃燒排放係數：環境部溫室氣體排放係數管理表（IPCC 74,100 kg CO2/TJ）", u, t26 + .4)

def s8(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "綠野旅行社：自有遊覽車一年", u)
    corner(ctx, T, m)
    tv, t78 = ep.kw(8, "3 萬公升"), ep.kw(8, "78 公噸")
    bus(ctx, 200, 230, 0.75); bus(ctx, 200, 380, 0.75)
    shown = 30000 * ease_out(prog(u, tv - .3, 1.0))
    if shown > 0:
        rrect(ctx, 360, 260, 300, 100, 22); fillstroke(ctx, C['navy'], lw=4)
        text(ctx, f"{shown:,.0f} 公升", 510, 310, 40, C['yellow'])
    chip(ctx, "× 2.6", 740, 310, prog(u, tv + 1.0, .4), C['teal'], 36, C['white'])
    q = prog(u, t78 - .3, .45)
    if q > 0:
        ctx.save(); pop(ctx, 920, 310, q)
        ctx.arc(920, 310, 110, 0, 2 * math.pi); fillstroke(ctx, C['orange'], lw=6)
        text(ctx, "≈ 78", 920, 290, 56, C['white']); text(ctx, "公噸 CO2", 920, 345, 26, C['white'])
        ctx.restore()
    chip(ctx, "30,000 × 2.606 ＝ 78,180 kg", 560, 520, prog(u, t78 + .5, .4), C['white'], 24)

def s9(ep, ctx, u, T, m):
    def props(ctx, u, T):
        ctx.arc(300, 330, 130, 0, 2 * math.pi); fillstroke(ctx, C['orange'], lw=6)
        text(ctx, "78", 300, 310, 90, C['white']); text(ctx, "公噸", 300, 390, 34, C['white'])
    boss_scene(ep, ctx, u, T, m, 9, "嚇一跳", "比我想的多好多！", "多好多", props, puzzled=False, sweat=True)

def s10(ep, ctx, u, T, m):
    background(ctx, T, 4); station_card(ctx, u, 3, "換戴旅程眼鏡")
    if u < 1.9: return
    header(ctx, 3, "同一桶柴油，兩個係數", u - 1.9)
    corner(ctx, T, m)
    tt, t3 = ep.kw(10, "運輸服務"), ep.kw(10, "3.32")
    for k, (x, col, title, val, sub, t0) in enumerate([(300, C['teal'], "公司眼鏡・範疇一", "2.6", "只算燃燒", 2.0),
                                                        (800, C['orange'], "旅程眼鏡・碳足跡", "3.32", "開採→煉製→運送→燃燒", t3)]):
        p = prog(u, max(2.0, t0 - .3), .45)
        if p <= 0: continue
        ctx.save(); pop(ctx, x, 340, p)
        glasses(ctx, x, 190, 0.6, col)
        rrect(ctx, x - 210, 250, 420, 230, 30); fillstroke(ctx, C['white'], lw=5)
        rrect(ctx, x - 210, 250, 420, 60, 26); fillstroke(ctx, col, lw=5)
        text(ctx, title, x, 280, 28, C['white'])
        text(ctx, val, x, 370, 72, col)
        text(ctx, "kg CO2／公升" if k == 0 else "kg CO2e／公升", x, 425, 22)
        text(ctx, sub, x, 458, 22, C['teal2'])
        ctx.restore()
    src(ctx, "3.32：觀光署《旅行業遊程碳足跡計算指引》範例（柴油，公路運輸，2021）", u, t3 + .5)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 4); header(ctx, 3, "數字不一樣，是眼鏡不一樣", u)
    corner(ctx, T, m)
    t1, t2, t3 = ep.kw(11, "排出來的那一刻"), ep.kw(11, "整個生命週期"), ep.kw(11, "眼鏡不一樣")
    labs = ["開採", "煉製", "運送", "燃燒"]
    stepchain(ctx, labs, [0.3, 0.5, 0.7, 0.9], u, y=300, x0=200, x1=860, r=60, size=28)
    p = prog(u, t1 - .2, .4)
    if p > 0:
        ctx.save(); ctx.set_dash([12, 8]); ctx.arc(860, 300, 80, 0, 2 * math.pi); ctx.set_source_rgba(*C['teal2'], p); ctx.set_line_width(6); ctx.stroke(); ctx.restore()
        chip(ctx, "範疇一", 860, 190, p, C['teal'], 28, C['white'])
    q = prog(u, t2 - .2, .5)
    if q > 0:
        rrect(ctx, 120, 400, 820 * ease_out(q), 26, 13); fillstroke(ctx, C['orange'], lw=3)
        chip(ctx, "碳足跡：整個生命週期", 530, 470, q, C['orange'], 28, C['white'])
    sticker(ctx, "眼鏡不一樣！", 600, 570, u, t3 - .2, C['pink'], 30)

def s12(ep, ctx, u, T, m):
    rows = [("範疇一", "自家排的", ep.kw(12, "自家排的")),
            ("公式", "活動數據 × 排放係數", ep.kw(12, "活動數據")),
            ("2.6 kg", "每公升柴油燃燒排放", ep.kw(12, "2.6"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 2 集重點", "下集：範疇二，買來的電", rows)

run("cf2", "碳導遊小綠 EP2", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "碳導遊小綠_EP2_範疇一自家排的碳.mp4", wipes={2, 4, 6, 10, 12})
