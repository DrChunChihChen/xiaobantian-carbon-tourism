"""碳導遊系列共用：更多小圖示與場景模板"""
from xl import *

def quiet_lu(ctx, T, **kw):
    xiaolu(ctx, 1150, 545, 0.42, T, 0, **kw)

def src(ctx, s, u, t0=0.6, y=612):
    q = prog(u, t0, .4)
    if q > 0: text(ctx, s, 600, y, 18, C['teal2'], a=q)

def boss_scene(ep, ctx, u, T, m, sc, title, bubble_text, key, props=None, bg=3, puzzled=True, wave=False, sweat=False):
    """阿德老闆說話的場景（阿德配音）；props(ctx,u,T) 畫左側道具"""
    background(ctx, T, bg); header(ctx, "?", title, u)
    if props: props(ctx, u, T)
    boss(ctx, 800, 380, 0.95, T, m, puzzled=puzzled, wave=wave, sweat=sweat)
    speech(ctx, bubble_text, 780, 150, prog(u, ep.kw(sc, key) - .4, .4), size=28)
    quiet_lu(ctx, T)

def pump(ctx, x, y, s=1.0, col=C['red'], label="柴油"):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -50, -90, 100, 180, 14); fillstroke(ctx, col, lw=5)
    rrect(ctx, -34, -70, 68, 50, 8); fillstroke(ctx, C['screen'], lw=3)
    text(ctx, label, 0, -45, 20, C['navy'])
    rrect(ctx, -60, 86, 120, 18, 6); fillstroke(ctx, C['grey'], lw=3)
    ctx.move_to(50, -40); ctx.curve_to(90, -40, 90, 40, 70, 60); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(8); ctx.stroke()
    rrect(ctx, 58, 50, 24, 36, 6); fillstroke(ctx, C['navy'], lw=2)
    ctx.restore()

def receipt(ctx, x, y, s=1.0, lines=("加油發票", "柴油 120 公升"), col=C['white']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(-90, -110); ctx.line_to(90, -110); ctx.line_to(90, 100)
    for k in range(6): ctx.line_to(90 - (k * 2 + 1) * 15, 112); ctx.line_to(90 - (k * 2 + 2) * 15, 100)
    ctx.close_path(); fillstroke(ctx, col, lw=4)
    for k, s_ in enumerate(lines):
        text(ctx, s_, 0, -80 + k * 40, 22 if k else 24, C['navy'] if k else C['teal2'])
    for k in range(2):
        ctx.move_to(-66, 20 + k * 26); ctx.line_to(66, 20 + k * 26); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(4); ctx.stroke()
    ctx.restore()

def stove(ctx, x, y, s=1.0, u=0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -80, -10, 160, 60, 10); fillstroke(ctx, C['grey'], lw=4)
    for k in range(5):
        f = math.sin(u * 12 + k) * 4
        ctx.move_to(-40 + k * 20, -10); ctx.curve_to(-48 + k * 20, -30, -40 + k * 20, -44 + f, -40 + k * 20, -50 + f)
        ctx.curve_to(-32 + k * 20, -36, -34 + k * 20, -24, -40 + k * 20, -10); fillstroke(ctx, C['blue'], lw=2)
    ctx.restore()

def fridge(ctx, x, y, s=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -55, -100, 110, 200, 14); fillstroke(ctx, C['white'], lw=5)
    ctx.move_to(-55, -30); ctx.line_to(55, -30); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(4); ctx.stroke()
    for yy in (-70, 10): rrect(ctx, 34, yy, 8, 30, 4); fillstroke(ctx, C['grey'], lw=2)
    ctx.restore()

def gas_puffs(ctx, x, y, u, label="冷媒", col=(.7, .85, 1)):
    for k in range(4):
        f = (u * .6 + k / 4) % 1
        ctx.arc(x + f * 120, y - f * 60 + math.sin(k) * 10, 10 + f * 16, 0, 2 * math.pi); ctx.set_source_rgba(*col, (1 - f) * .9); ctx.fill()
    text(ctx, label, x + 70, y - 70, 22, C['teal2'])

def plant(ctx, x, y, s=1.0, u=0):
    """power plant with cooling tower & chimney"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    for k in range(3):
        f = (u * .6 + k / 3) % 1
        ctx.arc(60 - f * 30, -150 - f * 70, 14 + f * 26, 0, 2 * math.pi); ctx.set_source_rgba(.6, .62, .66, (1 - f) * .8); ctx.fill()
    rrect(ctx, 46, -150, 28, 120, 4); fillstroke(ctx, C['grey'], lw=4)
    ctx.move_to(-90, 60); ctx.curve_to(-70, 0, -70, -40, -84, -90); ctx.line_to(-6, -90); ctx.curve_to(-20, -40, -20, 0, 0, 60); ctx.close_path()
    fillstroke(ctx, C['white'], lw=5)
    rrect(ctx, -20, -20, 130, 80, 6); fillstroke(ctx, C['pink'], lw=5)
    for k in range(3): rrect(ctx, -6 + k * 38, 0, 24, 24, 4); fillstroke(ctx, C['yellow'], lw=2)
    ctx.restore()

def bolt(ctx, x, y, s=1.0, col=C['yellow']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(10, -60); ctx.line_to(-30, 8); ctx.line_to(0, 8); ctx.line_to(-14, 60); ctx.line_to(34, -14); ctx.line_to(4, -14); ctx.line_to(22, -60); ctx.close_path()
    fillstroke(ctx, col, lw=4); ctx.restore()

def bulb(ctx, x, y, s=1.0, on=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    if on > 0:
        for k in range(8):
            a = k * math.pi / 4
            ctx.move_to(math.cos(a) * 62, -16 + math.sin(a) * 62); ctx.line_to(math.cos(a) * 80, -16 + math.sin(a) * 80)
        ctx.set_source_rgba(*C['yellow'], on); ctx.set_line_width(6); ctx.stroke()
    ctx.arc(0, -16, 44, 0, 2 * math.pi); fillstroke(ctx, C['yellow'] if on > .5 else C['white'], lw=5)
    rrect(ctx, -22, 26, 44, 34, 6); fillstroke(ctx, C['grey'], lw=4)
    text(ctx, "LED", 0, -16, 24, C['navy'])
    ctx.restore()

def bill(ctx, x, y, s=1.0, title="電費單", line="用電 12,000 度"):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -110, -120, 220, 240, 14); fillstroke(ctx, C['white'], lw=5)
    rrect(ctx, -110, -120, 220, 56, 14); fillstroke(ctx, C['teal'], lw=5)
    text(ctx, title, 0, -92, 26, C['white'])
    text(ctx, line, 0, -20, 24)
    for k in range(3):
        ctx.move_to(-80, 30 + k * 26); ctx.line_to(80, 30 + k * 26); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(4); ctx.stroke()
    ctx.restore()

def doc_icon(ctx, x, y, s=1.0, title="報告書", col=C['white']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(-80, -110); ctx.line_to(50, -110); ctx.line_to(80, -80); ctx.line_to(80, 110); ctx.line_to(-80, 110); ctx.close_path(); fillstroke(ctx, col, lw=5)
    text(ctx, title, 0, -70, 26)
    for k in range(5):
        ctx.move_to(-56, -26 + k * 28); ctx.line_to(56 - (k % 2) * 30, -26 + k * 28); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(5); ctx.stroke()
    ctx.restore()

def seal(ctx, x, y, s=1.0, label="查證", col=C['red'], rot=-0.2):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(rot)
    for k in range(16):
        a = k * math.pi / 8
        (ctx.move_to if k == 0 else ctx.line_to)(math.cos(a) * 60, math.sin(a) * 60)
        ctx.line_to(math.cos(a + math.pi / 16) * 50, math.sin(a + math.pi / 16) * 50)
    ctx.close_path(); fillstroke(ctx, col, lw=4)
    ctx.arc(0, 0, 38, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.set_line_width(4); ctx.stroke()
    text(ctx, label, 0, 0, 24, C['white'])
    ctx.restore()

def pig(ctx, x, y, s=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1.3, 1); ctx.arc(0, 0, 50, 0, 2 * math.pi); ctx.restore(); fillstroke(ctx, C['pink'], lw=5)
    for sd in (-1, 1):
        ctx.move_to(sd * 20, -44); ctx.line_to(sd * 34, -66); ctx.line_to(sd * 44, -38); ctx.close_path(); fillstroke(ctx, C['pink'], lw=4)
    ctx.save(); ctx.translate(46, 6); ctx.scale(1, .8); ctx.arc(0, 0, 18, 0, 2 * math.pi); ctx.restore(); fillstroke(ctx, (1, .55, .62), lw=4)
    for sd in (-1, 1): ctx.arc(46 + sd * 6, 6, 3, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
    ctx.arc(20, -14, 5, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
    for sd in (-30, 20): rrect(ctx, sd, 40, 16, 22, 5); fillstroke(ctx, C['pink'], lw=3)
    ctx.restore()

def bottle(ctx, x, y, s=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -10, -60, 20, 14, 3); fillstroke(ctx, C['blue'], lw=3)
    ctx.move_to(-10, -46); ctx.curve_to(-26, -36, -26, -20, -26, 0); ctx.line_to(-26, 56); ctx.line_to(26, 56); ctx.line_to(26, 0)
    ctx.curve_to(26, -20, 26, -36, 10, -46); ctx.close_path(); fillstroke(ctx, (.80, .92, 1), lw=4)
    ctx.restore()

def trash(ctx, x, y, s=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(-40, -30); ctx.line_to(-32, 60); ctx.line_to(32, 60); ctx.line_to(40, -30); ctx.close_path(); fillstroke(ctx, C['grey'], lw=4)
    rrect(ctx, -50, -46, 100, 16, 6); fillstroke(ctx, C['grey'], lw=4)
    ctx.restore()

def paper(ctx, x, y, s=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    for k in range(3):
        rrect(ctx, -40 + k * 6, -50 + k * 6, 80, 100, 6); fillstroke(ctx, C['white'], lw=3)
    ctx.restore()

def bar_h(ctx, x, y, w, h, frac, col, p=1.0):
    rrect(ctx, x, y, w, h, h / 2); fillstroke(ctx, (.92, .93, .95), lw=3)
    g = w * frac * ease_out(p)
    if g > h: rrect(ctx, x, y, g, h, h / 2); fillstroke(ctx, col, lw=3)

def formula(ctx, u, ts, y=250, labels=("活動數據", "排放係數", "排放量"), cols=(C['yellow'], C['teal'], C['orange'])):
    xs = [230, 560, 890]
    for k in range(3):
        p = prog(u, ts[k] - .2, .4)
        if p <= 0: continue
        ctx.save(); pop(ctx, xs[k], y, p)
        rrect(ctx, xs[k] - 130, y - 50, 260, 100, 30); fillstroke(ctx, cols[k], lw=5)
        text(ctx, labels[k], xs[k], y, 34, C['white'] if k else C['navy'])
        ctx.restore()
        if k: text(ctx, "×" if k == 1 else "＝", (xs[k - 1] + xs[k]) / 2, y, 50, a=p)

