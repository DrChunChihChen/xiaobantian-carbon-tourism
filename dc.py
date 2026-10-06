import sys, os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from engine import *

SKIN = (1, .86, .72); HAIR = (.20, .16, .22)
COAT = (.98, .98, 1.0); COAT2 = (.80, .84, .90)
COLS = [C['pink'], C['yellow'], C['teal'], C['blue'], C['orange'], C['green']]
QC, KC, VC = (1, .55, .62), (1, .80, .30), (.30, .71, .67)

def doctor(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True, look=0.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 100, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 4.2)) * 12
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.05); ctx.translate(0, -200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    for sd in (-1, 1):
        ctx.move_to(sd * 26, 200); ctx.line_to(sd * 28, 236); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(20); ctx.stroke()
        rrect(ctx, sd * 28 - 22 + sd * 6, 228, 44, 20, 10); fillstroke(ctx, (.95, .45, .35), lw=4)
    # lab coat
    ctx.move_to(-60, 86); ctx.curve_to(-76, 150, -84, 192, -80, 212); ctx.line_to(80, 212); ctx.curve_to(84, 192, 76, 150, 60, 86)
    ctx.curve_to(30, 74, -30, 74, -60, 86); ctx.close_path(); fillstroke(ctx, COAT, lw=5)
    # shirt + tie
    ctx.move_to(-22, 82); ctx.line_to(0, 140); ctx.line_to(22, 82); ctx.close_path(); fillstroke(ctx, (.55, .75, .95), lw=4)
    ctx.move_to(-7, 92); ctx.line_to(7, 92); ctx.line_to(10, 128); ctx.line_to(0, 140); ctx.line_to(-10, 128); ctx.close_path(); fillstroke(ctx, C['orange'], lw=3)
    for sd in (-1, 1):
        ctx.move_to(sd * 22, 82); ctx.line_to(sd * 46, 84); ctx.line_to(sd * 20, 150); ctx.close_path(); fillstroke(ctx, COAT2, lw=4)
    rrect(ctx, 26, 156, 36, 30, 5); fillstroke(ctx, COAT2, lw=3)
    ctx.move_to(36, 150); ctx.line_to(36, 170); ctx.set_source_rgb(*C['blue']); ctx.set_line_width(5); ctx.stroke()
    ctx.move_to(48, 150); ctx.line_to(48, 168); ctx.set_source_rgb(*C['red']); ctx.set_line_width(5); ctx.stroke()
    # arms
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(26); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*COAT); ctx.set_line_width(17); ctx.stroke()
        ctx.arc(ex, ey, 13, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    if wave:
        ang = -2.3 + 0.4 * math.sin(t * 9); arm(-64, 108, -64 + math.cos(ang) * 72, 108 + math.sin(ang) * 72)
    else:
        arm(-64, 108, -84, 172)
    if point:
        ex, ey = 130, 40 + math.sin(t * 3) * 6
        arm(64, 108, ex, ey)
        ctx.move_to(ex, ey); ctx.line_to(ex + 70, ey - 60); ctx.set_source_rgb(.55, .33, .18); ctx.set_line_width(7); ctx.stroke()
        star(ctx, ex + 76, ey - 66, 16, C['yellow'], 1, rot=t * 2, outline=True)
    else:
        arm(64, 108, 86, 172)
    # head
    for sd in (-1, 1):
        ctx.arc(sd * 86, 0, 16, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    ctx.arc(0, -10, 86, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=5)
    # hair: fluffy top with an antenna tuft
    ctx.move_to(-90, -20)
    for k, (hx, hy) in enumerate([(-92, -70), (-60, -104), (-20, -112), (20, -112), (60, -104), (92, -70)]):
        ctx.curve_to(hx - 10, hy - 18, hx + 18, hy - 22, hx + 14, hy)
    ctx.line_to(90, -20); ctx.curve_to(70, -60, 40, -66, 0, -62); ctx.curve_to(-40, -66, -70, -60, -90, -20); ctx.close_path()
    fillstroke(ctx, HAIR, lw=5)
    ctx.move_to(0, -112); ctx.curve_to(10, -150, 40, -150, 34, -128 + math.sin(t * 5) * 4); ctx.set_source_rgb(*HAIR); ctx.set_line_width(8); ctx.stroke()
    # glasses
    blink = (t % 3.1) < 0.13
    for ex_ in (-34, 34):
        ctx.save(); ctx.translate(ex_ + look * 6, -2); ctx.scale(1, 0.12 if blink else 1)
        ctx.arc(0, 0, 12, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink: ctx.arc(4, -5, 4.5, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        ctx.restore()
        ctx.arc(ex_, -2, 27, 0, 2 * math.pi); ctx.set_source_rgba(.8, .93, 1, .25); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    ctx.move_to(-8, -4); ctx.curve_to(-4, -12, 4, -12, 8, -4); ctx.set_line_width(5); ctx.stroke()
    for ex_ in (-54, 54):
        ctx.arc(ex_, 32, 11, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], .75); ctx.fill()
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 44); ctx.scale(1, (4 + 18 * mouth) / 13); ctx.arc(0, 0, 13, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill()
    else:
        if happy: ctx.arc(0, 34, 15, 0.15 * math.pi, 0.85 * math.pi)
        else: ctx.arc(0, 56, 12, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(92, -40 + dy); ctx.curve_to(76, -12 + dy, 80, 0 + dy, 92, 0 + dy); ctx.curve_to(104, 0 + dy, 108, -12 + dy, 92, -40 + dy); fillstroke(ctx, (.55, .80, 1), lw=3)
    ctx.restore()

def corner(ctx, T, m, **kw):
    doctor(ctx, 1150, 545, 0.42, T, m, **kw)

def panel(ctx, x, y, w, h, p, fill=C['white'], lw=5, r=24):
    if p <= 0: return False
    ctx.save(); pop(ctx, x + w / 2, y + h / 2, p)
    rrect(ctx, x, y, w, h, r); fillstroke(ctx, fill, lw=lw)
    return True

def arrow(ctx, x1, y1, x2, y2, p=1.0, col=C['navy'], lw=6):
    if p <= 0: return
    x2 = x1 + (x2 - x1) * ease_out(p); y2 = y1 + (y2 - y1) * ease_out(p)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(x1, y1); ctx.line_to(x2, y2); ctx.set_source_rgb(*col); ctx.set_line_width(lw); ctx.stroke()
    ang = math.atan2(y2 - y1, x2 - x1)
    for sd in (-1, 1):
        ctx.move_to(x2, y2); ctx.line_to(x2 - 16 * math.cos(ang + sd * 0.5), y2 - 16 * math.sin(ang + sd * 0.5)); ctx.stroke()

def token(ctx, s, x, y, col=C['white'], size=32, a=1.0, h=62):
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(size)
    w = max(ctx.text_extents(s).x_advance + 26, h)
    ctx.save(); ctx.push_group()
    rrect(ctx, x - w / 2, y - h / 2, w, h, 14); fillstroke(ctx, col, lw=4)
    text(ctx, s, x, y, size)
    ctx.pop_group_to_source(); ctx.paint_with_alpha(a); ctx.restore()
    return w

def vec(ctx, x, y, col, lab, p=1.0, n=4, seed=0):
    """small vector: row of cells + label"""
    if p <= 0: return
    random.seed(seed)
    ctx.save(); pop(ctx, x, y, p)
    for i in range(n):
        v = .3 + .7 * random.random()
        rrect(ctx, x - n * 13 + i * 26, y - 22, 22, 44, 5); ctx.set_source_rgba(*col, .35 + .65 * v); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
    text(ctx, lab, x, y + 44, 24)
    ctx.restore()

def station_card(ctx, u, num, title, dur=1.6):
    """chapter title card overlay at the start of a chapter"""
    if u > dur + .4: return
    q = ease_out(prog(u, 0.1, .35)) * (1 - prog(u, dur, .4))
    if q <= 0: return
    ctx.save(); ctx.translate(0, -60 * (1 - q))
    ctx.push_group()
    rrect(ctx, 290, 250, 700, 200, 40); fillstroke(ctx, C['navy'], stroke=C['navy'], lw=0)
    ctx.arc(390, 350, 58, 0, 2 * math.pi); ctx.set_source_rgb(*C['yellow']); ctx.fill()
    text(ctx, str(num), 390, 348, 60)
    text(ctx, f"第 {num} 站", 470, 305, 30, C['yellow'], align='l')
    text(ctx, title, 470, 380, 52, C['white'], align='l')
    ctx.pop_group_to_source(); ctx.paint_with_alpha(q); ctx.restore()

def outro_doc(ep, ctx, u, T, m, sc, big, line, rows=None):
    background(ctx, T, 5)
    random.seed(11)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(60):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()
    tb = LEAD + ep.durs[sc] * 0.8
    doctor(ctx, 230, 330, 0.9, T, m, wave=u > tb)
    pp = prog(u, .2, .5)
    ctx.save(); pop(ctx, 800, 150, pp); text(ctx, big, 800, 130, 56, C['orange']); text(ctx, line, 800, 195, 30); ctx.restore()
    if rows:
        for k, (a, b, t0) in enumerate(rows):
            p = prog(u, t0 - .2, .4)
            if p <= 0: continue
            y = (290 + k * 105) if len(rows) <= 3 else (262 + k * 92)
            ctx.save(); ctx.translate(-300 * (1 - ease_out(p)), 0)
            rrect(ctx, 460, y - 42, 700, 84, 42); fillstroke(ctx, C['white'], lw=5)
            chip(ctx, a, 600, y, 1, cols[k], 30)
            text(ctx, "→ " + b, 760, y, 32, align='l')
            ctx.restore()
    sticker(ctx, "下集見！" if "下集" in ep.SPOKEN[sc] or "下一集" in ep.SPOKEN[sc] else "下次見！", 1100, 610, u, tb, C['pink'], 32)

def run(name, tag, scenes, out, wipes=None):
    ep = Episode(os.path.join(HERE, name), tag)
    ep.scenes = scenes; ep.wipes = wipes
    ep.run(os.path.join(HERE, out), sys.argv)

if __name__ == "__main__":
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    background(ctx, 0, 1)
    doctor(ctx, 300, 330, 1.0, 0.5, 0)
    doctor(ctx, 700, 330, 1.0, 1.7, 0.6, wave=True, point=True)
    doctor(ctx, 1080, 400, 0.6, 2.2, 0, sweat=True, happy=False)
    surf.write_to_png(os.path.join(HERE, "doc.png"))

# ================= shared templates for dictionary episodes =================
def intro_scene(ep, ctx, u, T, m, title, sub):
    background(ctx, T, 0)
    p = ease_out(prog(u, 0, .8))
    doctor(ctx, -150 + 440 * p, 330, 1.0, T, m, wave=u > .8)
    sticker(ctx, "哈囉！", 170, 110, u, .8, C['pink'], 38, dur=3)
    big_title(ctx, title, 860, 300, u, 1.2, 46, sub=sub, w=620)

def roadmap_scene(ep, ctx, u, T, m, sc, stations):
    """stations: list of (label with \\n, key phrase in SPOKEN[sc])"""
    background(ctx, T, 0)
    doctor(ctx, 170, 470, 0.6, T, m, point=True)
    n = len(stations); y = 300; x0, x1 = 360, 1140
    ctx.move_to(x0, y); ctx.line_to(x1, y); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(14); ctx.stroke()
    ctx.move_to(x0, y); ctx.line_to(x1, y); ctx.set_source_rgb(*C['teal']); ctx.set_line_width(8); ctx.stroke()
    for i, (lab, key) in enumerate(stations):
        x = x0 + i * (x1 - x0) / max(1, n - 1)
        p = prog(u, ep.kw(sc, key) - .2, .4)
        ctx.save(); pop(ctx, x, y, max(p, .001))
        ctx.arc(x, y, 34, 0, 2 * math.pi); fillstroke(ctx, COLS[i % 6], lw=6); text(ctx, str(i + 1), x, y, 32)
        for k, part in enumerate(lab.split("\n")): text(ctx, part, x, y + 70 + k * 34, 28)
        ctx.restore()
    if "考題" in ep.SPOKEN[sc]:
        chip(ctx, "＋ 考題", 1140, 480, prog(u, ep.kw(sc, "考題") - .2, .4), C['red'], 28, C['white'])

def quiz_q(ep, ctx, u, T, m, sc, question_lines, options):
    background(ctx, T, 5)
    header(ctx, "?", "考題時間", u)
    if panel(ctx, 100, 120, 1080, 190, prog(u, 0.2, .5), fill=(1, .97, .85)):
        for k, s in enumerate(question_lines):
            text(ctx, s, 140, 175 + k * 50, 32, align='l')
        ctx.restore()
    for k, s in enumerate(options):
        p = prog(u, 1.0 + k * .25, .35)
        x = 150 + (k % 2) * 480; y = 380 + (k // 2) * 100
        if p <= 0: continue
        ctx.save(); pop(ctx, x + 200, y, p)
        rrect(ctx, x, y - 38, 420, 76, 38); fillstroke(ctx, C['white'], lw=5)
        ctx.arc(x + 40, y, 24, 0, 2 * math.pi); fillstroke(ctx, COLS[k], lw=4); text(ctx, "ABCD"[k], x + 40, y, 26)
        text(ctx, s, x + 80, y, 30, align='l')
        ctx.restore()
    doctor(ctx, 1160, 560, 0.4, T, m, point=False)
    # countdown ring
    tq = ep.durs[sc] + LEAD - 1.2
    if u > tq:
        q = prog(u, tq, 1.0)
        ctx.new_path(); ctx.arc(1160, 380, 36, -math.pi / 2, -math.pi / 2 + 2 * math.pi * q); ctx.set_source_rgb(*C['red']); ctx.set_line_width(8); ctx.stroke()
        text(ctx, "想想看", 1160, 380, 18, C['red'])

def quiz_a(ep, ctx, u, T, m, sc, question_lines, options, correct, why):
    background(ctx, T, 5)
    header(ctx, "?", "考題時間", 9)
    if panel(ctx, 100, 120, 1080, 190, 1, fill=(1, .97, .85)):
        for k, s in enumerate(question_lines):
            text(ctx, s, 140, 175 + k * 50, 32, align='l')
        ctx.restore()
    q = prog(u, 0.3, .4)
    for k, s in enumerate(options):
        x = 150 + (k % 2) * 480; y = 380 + (k // 2) * 100
        right = k == correct
        a = 1 - .6 * q if not right else 1
        rrect(ctx, x, y - 38, 420, 76, 38); fillstroke(ctx, C['green'] if (right and q > 0) else C['white'], lw=5 if not right else 7, a=a)
        ctx.arc(x + 40, y, 24, 0, 2 * math.pi); fillstroke(ctx, COLS[k], lw=4, a=a); text(ctx, "ABCD"[k], x + 40, y, 26, a=a)
        text(ctx, s, x + 80, y, 30, C['white'] if (right and q > 0) else C['navy'], align='l', a=a)
        if right: mark(ctx, x + 390, y - 30, True, q, r=26)
    if right_burst := True:
        k = correct; burst(ctx, 150 + (k % 2) * 480 + 210, 380 + (k // 2) * 100, u, .3, R=260)
    chip(ctx, why, 640, 590, prog(u, 1.2, .4), C['yellow'], 26)
    doctor(ctx, 1160, 560, 0.4, T, m, wave=True)

def stepchain(ctx, labels, times, u, y=330, x0=150, x1=1130, r=62, size=24):
    n = len(labels); dx = (x1 - x0) / max(1, n - 1)
    for i in range(n - 1):
        p = prog(u, times[i + 1] - .3, .4)
        if p > 0 and u > times[i]:
            arrow(ctx, x0 + i * dx + r + 8, y, x0 + (i + 1) * dx - r - 8, y, p, lw=5)
    for i, lab in enumerate(labels):
        p = prog(u, times[i] - .1, .45)
        if p <= 0: continue
        x = x0 + i * dx
        ctx.save(); pop(ctx, x, y, p)
        ctx.arc(x, y, r, 0, 2 * math.pi); fillstroke(ctx, COLS[i % 6], lw=5)
        parts = lab.split("\n")
        for k, part in enumerate(parts):
            text(ctx, part, x, y + (k - (len(parts) - 1) / 2) * (size + 4), size)
        ctx.restore()

def rows_list(ctx, u, rows, x=140, y=180, gap=100, w=920, size=32):
    """rows: (badge, text, t0, color)"""
    for k, (badge, s, t0, col) in enumerate(rows):
        p = prog(u, t0 - .15, .45)
        if p <= 0: continue
        yy = y + k * gap
        ctx.save(); ctx.translate(-300 * (1 - ease_out(p)), 0)
        rrect(ctx, x, yy - 40, w, 80, 26); fillstroke(ctx, C['white'], lw=5)
        chip(ctx, badge, x + 90, yy, 1, col, 26, padx=14)
        text(ctx, s, x + 190, yy, size, align='l')
        ctx.restore()

def term_card(ctx, u, t0, x, y, term, en, lines, col=C['yellow'], w=520, h=None):
    h = h or (130 + 44 * len(lines))
    if panel(ctx, x - w / 2, y - h / 2, w, h, prog(u, t0 - .2, .45), fill=C['white']):
        rrect(ctx, x - w / 2, y - h / 2, w, 76, 24); fillstroke(ctx, col, lw=5)
        text(ctx, term, x, y - h / 2 + 38, 34)
        if en: text(ctx, en, x, y - h / 2 + 100, 22, C['teal2'])
        for k, s in enumerate(lines):
            text(ctx, s, x, y - h / 2 + 140 + k * 44, 28)
        ctx.restore()
