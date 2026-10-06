"""碳導遊系列角色：小綠（主持，綠帽導遊＋小旗子）、阿德老闆（配角）＋旅遊小圖示"""
import dc
from dc import *

VEST = (.30, .66, .42); VEST2 = (.22, .52, .33); CAP = (.26, .62, .38); HAIRG = (.24, .16, .12)
PANTS = (.82, .72, .55)
POLO = (.38, .55, .85); POLO2 = (.28, .43, .70)

def leaf(ctx, x, y, s, col=C['green']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(-0.6)
    ctx.move_to(0, -14); ctx.curve_to(12, -8, 12, 8, 0, 14); ctx.curve_to(-12, 8, -12, -8, 0, -14); ctx.close_path()
    fillstroke(ctx, col, lw=2.5)
    ctx.move_to(0, -10); ctx.line_to(0, 12); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(2); ctx.stroke()
    ctx.restore()

def flag(ctx, hx, hy, t, ang=-1.45, L=170, d=1):
    """pole from hand (hx,hy) at angle ang; triangular fluttering flag with CO₂ counter"""
    ex, ey = hx + math.cos(ang) * L, hy + math.sin(ang) * L
    ctx.move_to(hx, hy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(9); ctx.stroke()
    ctx.move_to(hx, hy); ctx.line_to(ex, ey); ctx.set_source_rgb(.85, .70, .45); ctx.set_line_width(5); ctx.stroke()
    f = math.sin(t * 7) * 8
    ctx.move_to(ex, ey); ctx.curve_to(ex + d * 40, ey - 6 + f, ex + d * 70, ey + 6 - f, ex + d * 104, ey + 26 + f * .5)
    ctx.curve_to(ex + d * 70, ey + 40 + f, ex + d * 40, ey + 54 - f, ex + d * 4, ey + 62); ctx.close_path()
    fillstroke(ctx, C['yellow'], lw=4)
    text(ctx, "CO2", ex + d * 40, ey + 28 + f * .3, 22, C['navy'])
    ctx.arc(ex, ey - 4, 8, 0, 2 * math.pi); fillstroke(ctx, C['orange'], lw=3)

def xiaolu(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True, look=0.0):
    """小綠: original host — young tour guide, green cap & vest, holds a little CO₂ flag"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 95, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 4.2)) * 12
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.05); ctx.translate(0, -200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    # ponytail (behind head, swinging on the right)
    sw = math.sin(t * 3.0) * 0.15
    ctx.save(); ctx.translate(74, -44); ctx.rotate(-0.2 + sw)
    ctx.move_to(-6, 0); ctx.curve_to(60, -10, 80, 70, 46, 130); ctx.curve_to(40, 100, 10, 60, -10, 30); ctx.close_path()
    fillstroke(ctx, HAIRG, lw=5)
    ctx.arc(2, 8, 10, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=3)
    ctx.restore()
    # legs
    for sd in (-1, 1):
        ctx.move_to(sd * 26, 196); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(28); ctx.stroke()
        ctx.move_to(sd * 26, 196); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(*PANTS); ctx.set_line_width(20); ctx.stroke()
        rrect(ctx, sd * 28 - 22 + sd * 6, 228, 46, 20, 10); fillstroke(ctx, C['orange'], lw=4)
    # shirt body
    ctx.move_to(-58, 86); ctx.curve_to(-72, 150, -74, 186, -70, 206); ctx.line_to(70, 206); ctx.curve_to(74, 186, 72, 150, 58, 86)
    ctx.curve_to(30, 72, -30, 72, -58, 86); ctx.close_path(); fillstroke(ctx, C['white'], lw=5)
    # vest (two front panels, V-neck)
    for sd in (-1, 1):
        ctx.move_to(sd * 58, 86); ctx.curve_to(sd * 72, 150, sd * 74, 186, sd * 70, 206); ctx.line_to(sd * 12, 206)
        ctx.line_to(sd * 8, 120); ctx.line_to(sd * 30, 78); ctx.close_path(); fillstroke(ctx, VEST, lw=5)
    leaf(ctx, -36, 132, 1.0, C['yellow'])
    rrect(ctx, 26, 156, 34, 24, 6); fillstroke(ctx, VEST2, lw=3)
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(26); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['white']); ctx.set_line_width(17); ctx.stroke()
        ctx.arc(ex, ey, 12, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    if wave:
        ang = -2.3 + 0.4 * math.sin(t * 9); hx, hy = -60 + math.cos(ang) * 74, 106 + math.sin(ang) * 74
        flag(ctx, hx, hy, t, ang=-2.1 + 0.3 * math.sin(t * 9), L=120, d=-1)
        arm(-60, 106, hx, hy)
    else:
        hx, hy = -86, 160
        flag(ctx, hx, hy, t, ang=-1.95, L=210, d=-1)
        arm(-60, 106, hx, hy)
    if point:
        ex, ey = 128, 44 + math.sin(t * 3) * 6
        arm(60, 106, ex, ey)
        star(ctx, ex + 28, ey - 26, 14, C['yellow'], 1, rot=t * 2, outline=True)
    else:
        arm(60, 106, 82, 170)
    # hair behind face (shoulder length)
    ctx.move_to(-92, -20); ctx.curve_to(-100, 40, -96, 70, -76, 84); ctx.line_to(76, 84); ctx.curve_to(96, 70, 100, 40, 92, -20)
    ctx.curve_to(80, -110, -80, -110, -92, -20); ctx.close_path(); fillstroke(ctx, HAIRG, lw=5)
    # head
    ctx.arc(0, -6, 80, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=5)
    # hair top + bangs
    ctx.move_to(-82, -6); ctx.curve_to(-86, -70, -40, -96, 0, -96); ctx.curve_to(40, -96, 86, -70, 82, -6)
    ctx.curve_to(66, -34, 40, -44, 14, -40); ctx.curve_to(0, -30, -20, -26, -36, -40); ctx.curve_to(-56, -36, -72, -24, -82, -6); ctx.close_path()
    fillstroke(ctx, HAIRG, lw=5)
    # cap
    ctx.move_to(-78, -48); ctx.curve_to(-74, -118, 74, -118, 78, -48); ctx.close_path(); fillstroke(ctx, CAP, lw=5)
    ctx.move_to(-84, -48); ctx.curve_to(-40, -40, 60, -38, 128, -30); ctx.curve_to(110, -56, 60, -58, 78, -48); ctx.close_path()
    fillstroke(ctx, VEST2, lw=5)
    ctx.arc(0, -108, 7, 0, 2 * math.pi); fillstroke(ctx, VEST2, lw=3)
    leaf(ctx, -10, -78, 1.15, C['yellow'])
    # eyes + lashes
    blink = (t % 3.3) < 0.13
    for ex_ in (-30, 30):
        ctx.save(); ctx.translate(ex_ + look * 6, 8); ctx.scale(1, 0.12 if blink else 1)
        ctx.arc(0, 0, 12, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink: ctx.arc(4, -4, 4.5, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        ctx.restore()
        sd = -1 if ex_ < 0 else 1
        ctx.move_to(ex_ + sd * 10, 0); ctx.line_to(ex_ + sd * 16, -4); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
        ctx.move_to(ex_ - 13, -22); ctx.curve_to(ex_ - 5, -28, ex_ + 5, -28, ex_ + 13, -22); ctx.set_source_rgb(*HAIRG); ctx.set_line_width(4.5); ctx.stroke()
    for ex_ in (-52, 52):
        ctx.arc(ex_, 34, 12, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], .75); ctx.fill()
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 44); ctx.scale(1, (4 + 18 * mouth) / 13); ctx.arc(0, 0, 13, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill_preserve(); ctx.new_path()
    else:
        if happy: ctx.arc(0, 34, 15, 0.15 * math.pi, 0.85 * math.pi)
        else: ctx.arc(0, 56, 12, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(92, -40 + dy); ctx.curve_to(76, -12 + dy, 80, 0 + dy, 92, 0 + dy); ctx.curve_to(104, 0 + dy, 108, -12 + dy, 92, -40 + dy); fillstroke(ctx, (.55, .80, 1), lw=3)
    ctx.restore()

dc.doctor = xiaolu

def boss(ctx, x, y, s, t, mouth=0.0, happy=True, sweat=False, puzzled=False, wave=False):
    """阿德老闆: round, glasses, blue polo, a bit bald"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 105, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 3.6 + 1)) * 8
    ctx.translate(0, bob)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    for sd in (-1, 1):
        ctx.move_to(sd * 32, 196); ctx.line_to(sd * 34, 234); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(30); ctx.stroke()
        ctx.move_to(sd * 32, 196); ctx.line_to(sd * 34, 234); ctx.set_source_rgb(.30, .30, .36); ctx.set_line_width(22); ctx.stroke()
        rrect(ctx, sd * 34 - 24 + sd * 6, 228, 50, 20, 10); fillstroke(ctx, (.35, .22, .15), lw=4)
    # belly polo
    ctx.move_to(-66, 84); ctx.curve_to(-104, 130, -100, 196, -78, 206); ctx.line_to(78, 206); ctx.curve_to(100, 196, 104, 130, 66, 84)
    ctx.curve_to(30, 70, -30, 70, -66, 84); ctx.close_path(); fillstroke(ctx, POLO, lw=5)
    ctx.move_to(-26, 80); ctx.line_to(0, 104); ctx.line_to(26, 80); ctx.set_source_rgb(*C['white']); ctx.set_line_width(10); ctx.stroke()
    for k in range(2): ctx.arc(0, 118 + k * 18, 4, 0, 2 * math.pi); ctx.set_source_rgb(*C['white']); ctx.fill()
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(28); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*POLO); ctx.set_line_width(19); ctx.stroke()
        ctx.arc(ex, ey, 13, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    if puzzled:
        arm(70, 100, 70, 10)   # scratching head side
    elif wave:
        ang = -2.0 + 0.4 * math.sin(t * 9); arm(70, 100, 70 - math.cos(ang) * 70, 100 + math.sin(ang) * 70)
    else:
        arm(70, 100, 98, 168)
    arm(-70, 100, -98, 168)
    # head
    for sd in (-1, 1):
        ctx.arc(sd * 82, 6, 15, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=4)
    ctx.arc(0, -4, 80, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=5)
    # side hair only (bald top) + shine
    for sd in (-1, 1):
        ctx.move_to(sd * 80, 10); ctx.curve_to(sd * 86, -30, sd * 70, -56, sd * 46, -66); ctx.curve_to(sd * 58, -40, sd * 66, -20, sd * 68, 10); ctx.close_path()
        fillstroke(ctx, (.35, .33, .36), lw=4)
    ctx.arc(-28, -58, 10, 0, 2 * math.pi); ctx.set_source_rgba(1, 1, 1, .7); ctx.fill()
    # glasses
    for ex_ in (-30, 30):
        rrect(ctx, ex_ - 22, -12, 44, 34, 10); ctx.set_source_rgba(.85, .95, 1, .5); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
        blink = (t % 3.7) < 0.13
        ctx.save(); ctx.translate(ex_, 5); ctx.scale(1, .12 if blink else 1); ctx.arc(0, 0, 8, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill()
    ctx.move_to(-8, 4); ctx.line_to(8, 4); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(4); ctx.stroke()
    # eyebrows
    for ex_ in (-30, 30):
        tilt = (0.25 if ex_ < 0 else -0.25) if puzzled else 0
        ctx.move_to(ex_ - 16, -24 + tilt * 30); ctx.line_to(ex_ + 16, -24 - tilt * 30); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()
    # mustache
    ctx.move_to(-26, 38); ctx.curve_to(-14, 26, -4, 30, 0, 34); ctx.curve_to(4, 30, 14, 26, 26, 38); ctx.curve_to(10, 42, -10, 42, -26, 38); ctx.close_path()
    ctx.set_source_rgb(.30, .28, .30); ctx.fill()
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 54); ctx.scale(1, (4 + 16 * mouth) / 12); ctx.arc(0, 0, 12, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill_preserve(); ctx.new_path()
    else:
        if happy: ctx.arc(0, 46, 13, 0.15 * math.pi, 0.85 * math.pi)
        else: ctx.arc(0, 64, 10, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(-96, -40 + dy); ctx.curve_to(-112, -12 + dy, -108, 0 + dy, -96, 0 + dy); ctx.curve_to(-84, 0 + dy, -80, -12 + dy, -96, -40 + dy); fillstroke(ctx, (.55, .80, 1), lw=3)
    ctx.restore()

# ---------------- icons ----------------
def bus(ctx, x, y, s=1.0, t=0, col=C['teal']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -110, -60, 220, 110, 24); fillstroke(ctx, col, lw=5)
    for k in range(4):
        rrect(ctx, -94 + k * 46, -46, 38, 36, 8); fillstroke(ctx, C['screen'], lw=3)
    ctx.rectangle(-110, 6, 220, 10); ctx.set_source_rgb(*C['white']); ctx.fill()
    for sd in (-1, 1):
        ctx.arc(sd * 62, 52, 20, 0, 2 * math.pi); fillstroke(ctx, C['navy'], lw=3, stroke=C['navy'])
        ctx.arc(sd * 62, 52, 8, 0, 2 * math.pi); ctx.set_source_rgb(*C['grey']); ctx.fill()
    ctx.restore()

def smoke(ctx, x, y, u, a=1.0):
    for k in range(3):
        f = (u * .8 + k / 3) % 1
        ctx.arc(x - f * 60, y - f * 50, 10 + f * 22, 0, 2 * math.pi); ctx.set_source_rgba(.6, .62, .66, a * (1 - f) * .8); ctx.fill()

def ac_unit(ctx, x, y, s=1.0, u=0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -110, -40, 220, 80, 18); fillstroke(ctx, C['white'], lw=5)
    for k in range(3):
        ctx.move_to(-90, 14 + k * 8); ctx.line_to(90, 14 + k * 8); ctx.set_source_rgb(*C['grey']); ctx.set_line_width(3); ctx.stroke()
    ctx.arc(80, -18, 6, 0, 2 * math.pi); ctx.set_source_rgb(*C['green']); ctx.fill()
    for k in range(3):
        f = (u * .9 + k / 3) % 1
        ctx.move_to(-60 + k * 60, 50 + f * 50); ctx.curve_to(-50 + k * 60, 60 + f * 50, -70 + k * 60, 70 + f * 50, -60 + k * 60, 80 + f * 50)
        ctx.set_source_rgba(.45, .75, 1, 1 - f); ctx.set_line_width(5); ctx.stroke()
    ctx.restore()

def hotel(ctx, x, y, s=1.0, col=C['pink']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -60, -90, 120, 180, 10); fillstroke(ctx, col, lw=5)
    for i in range(4):
        for j in range(3):
            rrect(ctx, -44 + j * 32, -74 + i * 34, 22, 22, 4); fillstroke(ctx, C['yellow'], lw=2.5)
    rrect(ctx, -16, 56, 32, 34, 4); fillstroke(ctx, C['navy'], lw=2)
    ctx.restore()

def bowl(ctx, x, y, s=1.0, u=0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    for k in range(3):
        f = (u * .7 + k / 3) % 1
        ctx.move_to(-24 + k * 24, -30 - f * 30); ctx.curve_to(-14 + k * 24, -40 - f * 30, -34 + k * 24, -50 - f * 30, -24 + k * 24, -60 - f * 30)
        ctx.set_source_rgba(.6, .62, .66, 1 - f); ctx.set_line_width(4); ctx.stroke()
    ctx.move_to(-70, -16); ctx.curve_to(-70, 50, 70, 50, 70, -16); ctx.close_path(); fillstroke(ctx, C['orange'], lw=5)
    ctx.move_to(-20, -40); ctx.line_to(60, -60); ctx.move_to(-10, -36); ctx.line_to(66, -50); ctx.set_source_rgb(.6, .4, .25); ctx.set_line_width(5); ctx.stroke()
    ctx.restore()

def plane(ctx, x, y, s=1.0, col=C['blue']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(-80, 0); ctx.curve_to(-80, -16, 60, -16, 80, 0); ctx.curve_to(60, 16, -80, 16, -80, 0); fillstroke(ctx, C['white'], lw=5)
    ctx.move_to(-10, -6); ctx.line_to(-40, -60); ctx.line_to(-20, -60); ctx.line_to(30, -6); ctx.close_path(); fillstroke(ctx, col, lw=4)
    ctx.move_to(-10, 6); ctx.line_to(-40, 60); ctx.line_to(-20, 60); ctx.line_to(30, 6); ctx.close_path(); fillstroke(ctx, col, lw=4)
    ctx.move_to(-70, -4); ctx.line_to(-86, -36); ctx.line_to(-74, -36); ctx.line_to(-56, -6); ctx.close_path(); fillstroke(ctx, col, lw=4)
    ctx.restore()

def shop(ctx, x, y, s=1.0, name="綠野旅行社"):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -150, -80, 300, 170, 12); fillstroke(ctx, (1, .97, .88), lw=5)
    for k in range(6):
        ctx.move_to(-150 + k * 50, -80); ctx.line_to(-150 + k * 50 + 50, -80); ctx.line_to(-150 + k * 50 + 50, -50)
        ctx.curve_to(-150 + k * 50 + 38, -36, -150 + k * 50 + 12, -36, -150 + k * 50, -50); ctx.close_path()
        fillstroke(ctx, VEST if k % 2 else C['white'], lw=3)
    rrect(ctx, -110, -128, 220, 46, 12); fillstroke(ctx, VEST2, lw=4)
    text(ctx, name, 0, -105, 26, C['white'])
    rrect(ctx, -120, -10, 140, 80, 8); fillstroke(ctx, C['screen'], lw=4)
    rrect(ctx, 50, -10, 70, 100, 6); fillstroke(ctx, C['orange'], lw=4)
    ctx.restore()

def glasses(ctx, x, y, s=1.0, col=C['teal']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    for sd in (-1, 1):
        ctx.arc(sd * 58, 0, 46, 0, 2 * math.pi); ctx.set_source_rgba(.85, .95, 1, .7); ctx.fill_preserve()
        ctx.set_source_rgb(*col); ctx.set_line_width(12); ctx.stroke_preserve(); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
    ctx.move_to(-14, -6); ctx.curve_to(-6, -16, 6, -16, 14, -6); ctx.set_source_rgb(*col); ctx.set_line_width(10); ctx.stroke()
    for sd in (-1, 1):
        ctx.move_to(sd * 104, -8); ctx.line_to(sd * 134, -20); ctx.set_source_rgb(*col); ctx.set_line_width(10); ctx.stroke()
    ctx.restore()

def person(ctx, x, y, col, s=1.0, a=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.arc(0, -30, 16, 0, 2 * math.pi); ctx.set_source_rgba(*col, a); ctx.fill_preserve(); ctx.set_source_rgba(*C['navy'], a); ctx.set_line_width(3); ctx.stroke()
    ctx.move_to(-24, 26); ctx.curve_to(-24, -12, 24, -12, 24, 26); ctx.close_path(); ctx.set_source_rgba(*col, a); ctx.fill_preserve()
    ctx.set_source_rgba(*C['navy'], a); ctx.stroke(); ctx.restore()

if __name__ == "__main__":
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    background(ctx, 0, 1)
    xiaolu(ctx, 220, 330, 1.0, 0.5, 0)
    xiaolu(ctx, 560, 330, 1.0, 1.7, 0.6, wave=True, point=True)
    boss(ctx, 900, 330, 1.0, 0.5, 0.5, puzzled=True, sweat=True)
    xiaolu(ctx, 1150, 545, 0.42, 2.2, 0)
    surf.write_to_png("xl.png")
