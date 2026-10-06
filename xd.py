import dc
from dc import *

HOOD = (.36, .72, .56); HOOD2 = (.26, .58, .45); CURL = (.30, .20, .14)

def xiaodai(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True, look=0.0):
    """小戴: original host — curly hair, green hoodie"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 100, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 4.2)) * 12
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.05); ctx.translate(0, -200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    # legs: jeans + sneakers
    for sd in (-1, 1):
        ctx.move_to(sd * 26, 200); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(.30, .40, .62); ctx.set_line_width(24); ctx.stroke()
        rrect(ctx, sd * 28 - 22 + sd * 6, 228, 46, 20, 10); fillstroke(ctx, C['white'], lw=4)
    # hoodie body
    ctx.move_to(-62, 86); ctx.curve_to(-78, 150, -80, 190, -76, 206); ctx.line_to(76, 206); ctx.curve_to(80, 190, 78, 150, 62, 86)
    ctx.curve_to(30, 72, -30, 72, -62, 86); ctx.close_path(); fillstroke(ctx, HOOD, lw=5)
    # pocket + strings
    rrect(ctx, -40, 150, 80, 40, 12); fillstroke(ctx, HOOD2, lw=4)
    for sd in (-1, 1):
        ctx.move_to(sd * 12, 92); ctx.line_to(sd * 14, 132); ctx.set_source_rgb(1, 1, 1); ctx.set_line_width(4); ctx.stroke()
        ctx.arc(sd * 14, 134, 4, 0, 2 * math.pi); ctx.fill()
    # hood collar
    ctx.move_to(-46, 84); ctx.curve_to(-30, 104, 30, 104, 46, 84); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(28); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*HOOD); ctx.set_line_width(19); ctx.stroke()
        ctx.arc(ex, ey, 13, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    if wave:
        ang = -2.3 + 0.4 * math.sin(t * 9); arm(-64, 108, -64 + math.cos(ang) * 72, 108 + math.sin(ang) * 72)
    else:
        arm(-64, 108, -84, 170)
    if point:
        ex, ey = 128, 44 + math.sin(t * 3) * 6
        arm(64, 108, ex, ey)
        star(ctx, ex + 28, ey - 26, 14, C['yellow'], 1, rot=t * 2, outline=True)
    else:
        arm(64, 108, 86, 170)
    # head
    for sd in (-1, 1):
        ctx.arc(sd * 84, 4, 15, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    ctx.arc(0, -6, 82, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=5)
    # curly hair: clusters of small circles over the top
    random.seed(21)
    curls = []
    for k in range(17):
        a = math.pi * (1.02 + k * 0.96 / 16)
        r = 84 + 6 * math.sin(k * 1.7)
        curls.append((math.cos(a) * r, -10 + math.sin(a) * r * 1.05, 24 + 4 * math.sin(k * 2.3)))
    for k in range(7):
        curls.append((-54 + k * 18, -86 - 8 * math.sin(k * 1.3), 22))
    for (cx, cy, r) in curls:
        ctx.new_sub_path(); ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.set_source_rgb(*C['navy']); ctx.set_line_width(10); ctx.stroke_preserve(); ctx.set_source_rgb(*CURL); ctx.fill()
    for (cx, cy, r) in curls[::2]:
        ctx.new_path(); ctx.arc(cx, cy, r * .5, 3.6, 5.6); ctx.set_source_rgb(.48, .34, .24); ctx.set_line_width(4); ctx.stroke()
    ctx.new_path()
    # eyes (no glasses)
    blink = (t % 3.3) < 0.13
    for ex_ in (-30, 30):
        ctx.save(); ctx.translate(ex_ + look * 6, 6); ctx.scale(1, 0.12 if blink else 1)
        ctx.arc(0, 0, 11, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink: ctx.arc(4, -4, 4, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        ctx.restore()
        ctx.move_to(ex_ - 14, -18); ctx.curve_to(ex_ - 6, -24, ex_ + 6, -24, ex_ + 14, -18); ctx.set_source_rgb(*CURL); ctx.set_line_width(6); ctx.stroke()
    for ex_ in (-52, 52):
        ctx.arc(ex_, 34, 11, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], .7); ctx.fill()
    # freckles
    for fx, fy in [(-58, 18), (-48, 24), (48, 24), (58, 18)]:
        ctx.arc(fx, fy, 2.5, 0, 2 * math.pi); ctx.set_source_rgb(.75, .5, .35); ctx.fill()
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

dc.doctor = xiaodai      # all shared templates now draw 小戴

if __name__ == "__main__":
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    background(ctx, 0, 1)
    xiaodai(ctx, 300, 330, 1.0, 0.5, 0)
    xiaodai(ctx, 700, 330, 1.0, 1.7, 0.6, wave=True, point=True)
    xiaodai(ctx, 1080, 400, 0.6, 2.2, 0, sweat=True, happy=False)
    surf.write_to_png(__file__.replace(".py", ".png"))
