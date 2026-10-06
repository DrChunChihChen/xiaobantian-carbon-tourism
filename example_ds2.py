from xd import *

AL = (.96, .52, .18)     # 阿里巴巴
ZP = (.42, .38, .86)     # 智譜
CL = (.84, .52, .36)     # Claude

def card(ctx, name, col, x, y, p=1.0, w=240, h=80, size=32, sub=None):
    if p <= 0: return
    ctx.save(); pop(ctx, x, y, p)
    rrect(ctx, x - w / 2, y - h / 2, w, h, 22); fillstroke(ctx, col, lw=5)
    if sub:
        text(ctx, name, x, y - 12, size, C['white']); text(ctx, sub, x, y + 22, 20, C['white'])
    else:
        text(ctx, name, x, y, size, C['white'])
    ctx.restore()

def acct(ctx, x, y, col, a=1.0, s=1.0):
    ctx.arc(x, y - 6 * s, 6 * s, 0, 2 * math.pi); ctx.set_source_rgba(*col, a); ctx.fill()
    ctx.move_to(x - 10 * s, y + 10 * s); ctx.curve_to(x - 10 * s, y - 2 * s, x + 10 * s, y - 2 * s, x + 10 * s, y + 10 * s); ctx.close_path(); ctx.fill()

def s0(ep, ctx, u, T, m): intro_scene(ep, ctx, u, T, m, "直接挖思考過程", "AI 蒸餾事件簿・第 2 集")
def s1(ep, ctx, u, T, m): roadmap_scene(ep, ctx, u, T, m, 1, [("阿里巴巴", "阿里巴巴"), ("智譜", "智譜"), ("重點\n整理", "整理")])

def s2(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, "?", "為什麼要挖思考過程？", u)
    corner(ctx, T, m)
    ta, ts, tb, tl = ep.kw(2, "推理"), ep.kw(2, "完整步驟"), ep.kw(2, "只看答案"), ep.kw(2, "學生模型")
    if panel(ctx, 90, 200, 300, 220, prog(u, tb - .3, .5)):
        text(ctx, "只有答案", 240, 240, 26, C['teal2'])
        text(ctx, "x = 3", 240, 330, 52)
        ctx.restore()
    if panel(ctx, 450, 150, 560, 400, prog(u, ta - .2, .5), fill=(1, .97, .85)):
        text(ctx, "思考過程（推理步驟）", 730, 190, 28, C['orange'])
        for k, s in enumerate(["① 先列出方程式", "② 兩邊同時減 5", "③ 再除以 2", "④ 檢查答案", "→ x = 3"]):
            q = prog(u, ts + k * .3, .3)
            text(ctx, s, 520, 250 + k * 56, 30, a=q, align='l')
        star(ctx, 960, 190, 22, C['yellow'], prog(u, tb, .3), rot=T, outline=True)
        ctx.restore()
    chip(ctx, "拿來訓練學生模型，效果特別好", 560, 600, prog(u, tl - .2, .4), C['green'], 26, C['white'])

def s3(ep, ctx, u, T, m):
    background(ctx, T, 1); station_card(ctx, u, 1, "阿里巴巴")
    if u < 1.9: return
    header(ctx, 1, "阿里巴巴（Qwen・通義）", u - 1.9)
    corner(ctx, T, m)
    tb, to = ep.kw(3, "規模最大"), ep.kw(3, "Opus")
    card(ctx, "阿里巴巴", AL, 300, 280, prog(u, 2.0, .4), w=300, h=110, size=40, sub="Qwen・通義實驗室")
    p = prog(u, tb - .2, .4)
    if p > 0:
        ctx.save(); pop(ctx, 300, 430, p)
        rrect(ctx, 130, 395, 340, 70, 35); fillstroke(ctx, C['red'], lw=4)
        text(ctx, "觀察到規模最大", 300, 430, 28, C['white'])
        ctx.restore()
    for k, s in enumerate(["Opus 4.6", "Opus 4.7"]):
        card(ctx, s, CL, 820, 230 + k * 110, prog(u, to + k * .3, .4), w=240, h=80, size=30)
    if u > to: arrow(ctx, 460, 280, 690, 280, prog(u, to, .5))
    chip(ctx, "目標：思考過程", 820, 480, prog(u, to + .8, .4), C['yellow'], 30)

def s4(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "每個請求都加一段固定指令", u)
    corner(ctx, T, m)
    tf, tt = ep.kw(4, "固定的指令"), ep.kw(4, "特定的標籤")
    if panel(ctx, 70, 170, 380, 300, prog(u, .3, .5)):
        text(ctx, "送出的請求", 260, 210, 26, C['teal2'])
        rrect(ctx, 100, 250, 320, 80, 14); fillstroke(ctx, C['white'], lw=3)
        text(ctx, "任務：寫一段程式…", 260, 290, 24)
        q = prog(u, tf - .2, .5)
        if q > 0:
            ctx.save(); ctx.translate(0, -40 * (1 - ease_out(q)))
            rrect(ctx, 100, 350, 320, 80, 14); fillstroke(ctx, C['yellow'], lw=4, a=q)
            text(ctx, "＋ 固定指令", 260, 378, 26, a=q); text(ctx, "「先寫出思考過程」", 260, 410, 20, C['teal2'], a=q)
            ctx.restore()
        ctx.restore()
    p = prog(u, tf + .8, .4)
    if p > 0:
        arrow(ctx, 460, 320, 540, 320, p)
        card(ctx, "Claude", CL, 630, 320, p, w=160, h=90, size=30)
        arrow(ctx, 720, 320, 800, 320, prog(u, tt - .3, .4))
    if panel(ctx, 810, 170, 340, 330, prog(u, tt - .2, .5)):
        rrect(ctx, 830, 200, 300, 160, 12); fillstroke(ctx, (1, .92, .8), lw=3)
        text(ctx, "【思考】", 980, 225, 24, C['orange'])
        for k in range(3):
            ctx.rectangle(850, 255 + k * 30, 260 - k * 40, 10); ctx.set_source_rgb(*C['orange']); ctx.fill()
        rrect(ctx, 830, 380, 300, 100, 12); fillstroke(ctx, C['white'], lw=3)
        text(ctx, "【回答】", 980, 405, 24)
        ctx.rectangle(850, 435, 220, 10); ctx.set_source_rgb(*C['grey']); ctx.fill()
        ctx.restore()
        chip(ctx, "思考被寫進特定標籤", 980, 560, prog(u, tt + .5, .4), C['red'], 24, C['white'])

def s5(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "思考紀錄 → 訓練資料", u)
    corner(ctx, T, m)
    ts, tf, tq = ep.kw(5, "存下來"), ep.kw(5, "SFT"), ep.kw(5, "Qwen")
    stepchain(ctx, ["思考\n紀錄", "整理成\nSFT 資料", "訓練\nQwen"], [ts, tf, tq], u, y=310, x0=220, x1=900, r=86, size=26)
    for k, v in enumerate(["3.5", "3.6", "3.7"]):
        card(ctx, "Qwen " + v, AL, 700 + k * 160 - 120, 480, prog(u, tq + .6 + k * .25, .4), w=140, h=60, size=24)

def s6(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "兩大批假帳號", u)
    corner(ctx, T, m)
    t1, tp, tb, t2, th, ta = [ep.kw(6, k) for k in ["第一批", "住宅代理", "被封鎖", "第二批", "高峰", "累計"]]
    for pool in range(2):
        x0 = 90 + pool * 480
        t0 = t1 if pool == 0 else t2
        q = prog(u, t0 - .3, .5)
        if q <= 0: continue
        banned = pool == 0 and u > tb
        rrect(ctx, x0, 150, 420, 280, 22); fillstroke(ctx, (.95, .95, .97) if not banned else (.92, .88, .88), lw=4, a=q)
        text(ctx, f"帳號池 {pool + 1}" + ("（近 5,000 個）" if pool == 0 else ""), x0 + 210, 180, 24, a=q)
        for k in range(60):
            r_, c_ = k // 12, k % 12
            if prog(u, t0 - .3 + k * .01, .2) <= 0: continue
            acct(ctx, x0 + 32 + c_ * 33, 225 + r_ * 42, (.6, .6, .65) if banned else ([C['teal'], C['blue'], C['pink']][k % 3]), 1)
        if banned:
            g = prog(u, tb, .4)
            ctx.move_to(x0 + 40, 180); ctx.line_to(x0 + 380, 420); ctx.move_to(x0 + 380, 180); ctx.line_to(x0 + 40, 420)
            ctx.set_source_rgba(*C['red'], g); ctx.set_line_width(14); ctx.stroke()
            text(ctx, "封鎖！", x0 + 210, 300, 44, C['red'], a=g)
    if u > t2: arrow(ctx, 520, 290, 560, 290, prog(u, t2 - .2, .4), C['orange'], 6)
    for k, s in enumerate(["住宅代理", "一次性信箱", "虛擬信用卡"]):
        chip(ctx, s, 170 + k * 170, 480, prog(u, tp + k * .3, .4), C['yellow'], 22)
    chip(ctx, "高峰：一天近 300 萬次", 820, 480, prog(u, th - .2, .4), C['red'], 24, C['white'])
    chip(ctx, "5～7 月累計：超過 1.51 億次", 700, 560, prog(u, ta - .2, .4), C['orange'], 28, C['white'])

def s7(ep, ctx, u, T, m):
    background(ctx, T, 1); header(ctx, 1, "不只蒸餾：還拿來做研發", u)
    corner(ctx, T, m)
    tr, ta = ep.kw(7, "強化學習"), ep.kw(7, "模型架構")
    card(ctx, "Claude", CL, 600, 220, prog(u, .3, .4), w=200, h=90, size=34)
    for k, (s, t0, col) in enumerate([("強化學習訓練環境", tr, C['teal']), ("模型架構研究", ta, C['blue'])]):
        x = 380 + k * 440
        q = prog(u, t0 - .2, .4)
        if q <= 0: continue
        arrow(ctx, 600, 270, x, 370, q, lw=5)
        ctx.save(); pop(ctx, x, 430, q)
        rrect(ctx, x - 170, 380, 340, 100, 24); fillstroke(ctx, col, lw=5)
        text(ctx, s, x, 430, 30, C['white'])
        ctx.restore()

def s8(ep, ctx, u, T, m):
    background(ctx, T, 2); station_card(ctx, u, 2, "智譜")
    if u < 1.9: return
    header(ctx, 2, "智譜（Z.ai）", u - 1.9)
    corner(ctx, T, m)
    tz, ta, to, tc = ep.kw(8, "Z.ai"), ep.kw(8, "兩百七十三"), ep.kw(8, "Opus 4.8"), ep.kw(8, "七十七萬")
    card(ctx, "智譜", ZP, 300, 230, prog(u, 2.0, .4), w=260, h=100, size=40, sub="海外品牌 Z.ai")
    q = prog(u, ta - .2, .5)
    if q > 0:
        for k in range(24):
            a = k / 24 * 2 * math.pi + u * .8
            on = int(u * 4) % 24 == k
            acct(ctx, 300 + 130 * math.cos(a), 450 + 70 * math.sin(a), C['orange'] if on else (.6, .62, .7), q, 1.1)
        text(ctx, "輪流使用", 300, 440, 24, a=q); text(ctx, "273 個假帳號", 300, 470, 24, C['red'], a=q)
    card(ctx, "Opus 4.8", CL, 820, 230, prog(u, to - .2, .4), w=220, h=80, size=30)
    if u > to: arrow(ctx, 440, 230, 700, 230, prog(u, to, .5))
    if panel(ctx, 640, 330, 380, 180, prog(u, tc - .3, .5), fill=(1, .97, .85)):
        text(ctx, "10 天內", 830, 370, 26, C['teal2'])
        text(ctx, "77 萬次", 830, 430, 50, C['orange'])
        text(ctx, "經過清洗流程", 830, 480, 22)
        ctx.restore()

def s9(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "讓 Claude 反過來幫忙", u)
    corner(ctx, T, m)
    tb, tj, tn = ep.kw(9, "丟回給"), ep.kw(9, "裁判"), ep.kw(9, "批改")
    nodes = [("偷來的\n思考紀錄", 230, 300, .3, (.9, .9, .92)), ("Claude\n清洗・整理", 560, 300, tb, CL), ("Claude 當裁判\n打分・篩選", 890, 300, tj, CL)]
    for i, (lab, x, y, t0, col) in enumerate(nodes):
        q = prog(u, t0 - .2, .4)
        if q <= 0: continue
        if i: arrow(ctx, x - 250, y, x - 150, y, q)
        ctx.save(); pop(ctx, x, y, q)
        rrect(ctx, x - 140, y - 70, 280, 140, 26); fillstroke(ctx, col, lw=5)
        for k, part in enumerate(lab.split("\n")): text(ctx, part, x, y - 18 + k * 40, 28, C['white'] if i else C['navy'])
        ctx.restore()
    if u > tj + .5:
        for k in range(3):
            mark(ctx, 820 + k * 70, 420, k != 1, prog(u, tj + .5 + k * .2, .3), r=22)
    p = prog(u, tn - .3, .5)
    if p > 0:
        ctx.save(); pop(ctx, 560, 540, p)
        rrect(ctx, 240, 505, 640, 70, 35); fillstroke(ctx, C['yellow'], lw=4)
        text(ctx, "就像請老師批改偷來的筆記", 560, 540, 30)
        ctx.restore()

def shield(ctx, x, y, s, col):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(0, -70); ctx.curve_to(40, -50, 60, -55, 62, -50); ctx.curve_to(62, 20, 40, 55, 0, 75)
    ctx.curve_to(-40, 55, -62, 20, -62, -50); ctx.curve_to(-60, -55, -40, -50, 0, -70); ctx.close_path()
    fillstroke(ctx, col, lw=5); ctx.restore()

def s10(ep, ctx, u, T, m):
    background(ctx, T, 2); header(ctx, 2, "想蒸餾資安能力", u)
    corner(ctx, T, m)
    tc, tf, tb, to = ep.kw(10, "資安能力"), ep.kw(10, "Fable"), ep.kw(10, "擋下"), ep.kw(10, "Opus 4.6")
    card(ctx, "智譜", ZP, 180, 330, prog(u, tc - .2, .4), w=180, h=90, size=34)
    p = prog(u, tf - .2, .4)
    if p > 0:
        shield(ctx, 700, 250, 1.1, C['green'])
        text(ctx, "Fable", 700, 245, 30, C['white']); text(ctx, "防護最強", 700, 350, 24, C['green'])
        # attack arrow and bounce
        if u < tb:
            g = clamp((u - tf) / max(.3, tb - tf))
            arrow(ctx, 280, 320, 280 + 330 * g, 280, 1, C['red'], 6)
        else:
            q = prog(u, tb, .5)
            arrow(ctx, 280, 320, 610, 280, 1, (.8, .8, .8), 6)
            chip(ctx, "被擋下・效果變差", 520, 200, q, C['red'], 22, C['white'])
    q = prog(u, to - .2, .5)
    if q > 0:
        arrow(ctx, 280, 350, 530, 490, q, C['red'], 6)
        card(ctx, "Opus 4.6", CL, 640, 490, q, w=200, h=70, size=28)
        card(ctx, "另一家美國模型", (.5, .55, .62), 880, 490, prog(u, to + .4, .4), w=240, h=70, size=26)
        text(ctx, "改找防護較弱的", 760, 575, 24, C['red'], a=q)

def s11(ep, ctx, u, T, m):
    background(ctx, T, 3); station_card(ctx, u, 3, "重點整理")
    if u < 1.9: return
    header(ctx, 3, "兩家手法的共同點", u - 1.9)
    corner(ctx, T, m)
    rows = [("目標", "鎖定思考過程", ep.kw(11, "都鎖定"), C['yellow']), ("掩護", "大量假帳號躲避偵測", ep.kw(11, "假帳號"), C['pink']),
            ("反過來", "讓 Claude 整理和打分", ep.kw(11, "反過來"), C['teal'])]
    rows_list(ctx, u, rows, x=120, y=200, gap=100, w=880, size=30)
    chip(ctx, "防護較強的模型，比較難被蒸餾", 560, 530, prog(u, ep.kw(11, "防護較強") - .2, .4), C['green'], 28, C['white'])

def s12(ep, ctx, u, T, m):
    rows = [("注意", "Anthropic 單方面的報告", ep.kw(12, "單方面")), ("被點名方", "不一定同意這些說法", ep.kw(12, "不一定同意")),
            ("下一集", "Moonshot・DeepSeek", ep.kw(12, "下一集"))]
    outro_doc(ep, ctx, u, T, m, 12, "第 2 集重點", "直接挖思考過程", rows)

run("example_ds2", "AI 蒸餾事件簿 2", [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12], "example_ds2.mp4", wipes={3, 8, 11, 12})
