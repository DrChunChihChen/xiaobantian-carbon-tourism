import dc
from dsc import *

JK = (1.0, .78, .25); JK2 = (.92, .62, .12); HR = (.38, .32, .70)

def ajie(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True, look=0.0):
    """山姆: original host — spiky indigo hair, yellow jacket, headphones"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 100, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 4.2)) * 12
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.05); ctx.translate(0, -200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    for sd in (-1, 1):
        ctx.move_to(sd * 26, 200); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(.22, .22, .28); ctx.set_line_width(24); ctx.stroke()
        rrect(ctx, sd * 28 - 22 + sd * 6, 228, 46, 20, 10); fillstroke(ctx, C['red'], lw=4)
    # jacket
    ctx.move_to(-62, 86); ctx.curve_to(-78, 150, -80, 190, -76, 206); ctx.line_to(76, 206); ctx.curve_to(80, 190, 78, 150, 62, 86)
    ctx.curve_to(30, 72, -30, 72, -62, 86); ctx.close_path(); fillstroke(ctx, JK, lw=5)
    # inner tee + zipper
    ctx.move_to(-18, 82); ctx.line_to(18, 82); ctx.line_to(10, 206); ctx.line_to(-10, 206); ctx.close_path(); fillstroke(ctx, C['white'], lw=4)
    ctx.move_to(0, 90); ctx.line_to(0, 206); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
    for sd in (-1, 1):
        rrect(ctx, sd * 50 - 14, 160, 28, 22, 5); fillstroke(ctx, JK2, lw=3)
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(28); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*JK); ctx.set_line_width(19); ctx.stroke()
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
    # headphones around neck
    ctx.new_path(); ctx.arc(0, 70, 58, 0.15 * math.pi, 0.85 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(12); ctx.stroke()
    ctx.new_path(); ctx.arc(0, 70, 58, 0.15 * math.pi, 0.85 * math.pi); ctx.set_source_rgb(.35, .38, .48); ctx.set_line_width(6); ctx.stroke()
    for sd in (-1, 1):
        rrect(ctx, sd * 54 - 16, 76, 32, 38, 12); fillstroke(ctx, C['teal'], lw=4)
    # head
    for sd in (-1, 1):
        ctx.arc(sd * 84, 4, 15, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    ctx.arc(0, -6, 82, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=5)
    # spiky hair
    ctx.move_to(-88, -10)
    spikes = [(-96, -70), (-70, -60), (-74, -128), (-40, -88), (-24, -150), (6, -98), (30, -152), (44, -92), (80, -126), (74, -62), (98, -66)]
    px, py = -88, -10
    for (sx, sy) in spikes:
        ctx.line_to(sx, sy)
    ctx.line_to(88, -10); ctx.curve_to(60, -40, 20, -48, 0, -46); ctx.curve_to(-30, -48, -60, -40, -88, -10); ctx.close_path()
    fillstroke(ctx, HR, lw=5)
    ctx.move_to(-20, -60); ctx.line_to(-8, -100); ctx.move_to(30, -64); ctx.line_to(36, -104)
    ctx.set_source_rgb(.55, .5, .85); ctx.set_line_width(5); ctx.stroke()
    # eyes: big ovals
    blink = (t % 3.5) < 0.13
    for ex_ in (-30, 30):
        ctx.save(); ctx.translate(ex_ + look * 6, 4); ctx.scale(1, 0.12 if blink else 1.25)
        ctx.arc(0, 0, 11, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink: ctx.arc(4, -4, 4, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        ctx.restore()
        ctx.move_to(ex_ - 16, -22); ctx.line_to(ex_ + 14, -26 if ex_ < 0 else -18)
        ctx.set_source_rgb(*HR); ctx.set_line_width(7); ctx.stroke()
    ctx.move_to(0, 12); ctx.line_to(-6, 24); ctx.line_to(4, 26); ctx.set_source_rgb(.8, .55, .45); ctx.set_line_width(4); ctx.stroke()
    for ex_ in (-52, 52):
        ctx.arc(ex_, 32, 11, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], .7); ctx.fill()
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 46); ctx.scale(1, (4 + 18 * mouth) / 13); ctx.arc(0, 0, 13, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill()
    else:
        if happy:
            ctx.move_to(-16, 38); ctx.curve_to(-6, 50, 10, 50, 18, 34)
        else: ctx.arc(0, 58, 12, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(92, -40 + dy); ctx.curve_to(76, -12 + dy, 80, 0 + dy, 92, 0 + dy); ctx.curve_to(104, 0 + dy, 108, -12 + dy, 92, -40 + dy); fillstroke(ctx, (.55, .80, 1), lw=3)
    ctx.restore()

dc.doctor = ajie

if __name__ == "__main__":
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    background(ctx, 0, 1)
    ajie(ctx, 300, 330, 1.0, 0.5, 0)
    ajie(ctx, 700, 330, 1.0, 1.7, 0.6, wave=True, point=True)
    ajie(ctx, 1080, 400, 0.6, 2.2, 0, sweat=True, happy=False)
    surf.write_to_png(__file__.replace(".py", ".png"))
