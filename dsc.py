from xd import *

AL = (.96, .52, .18)     # 阿里巴巴
ZP = (.42, .38, .86)     # 智譜
CL = (.84, .52, .36)     # Claude / Anthropic
MS = (.20, .24, .34)     # Moonshot
DS = (.25, .45, .85)     # DeepSeek
XM = (1.0, .45, .15)     # 小米
ST = (.30, .62, .78)     # 商湯
MM = (.85, .30, .45)     # MiniMax
OA = (.22, .24, .27)     # OpenAI
GO = (.26, .52, .96)     # Google
GREY = (.55, .58, .64)

def card(ctx, name, col, x, y, p=1.0, w=240, h=80, size=32, sub=None, tcol=None):
    if p <= 0: return
    tcol = tcol or C['white']
    ctx.save(); pop(ctx, x, y, p)
    rrect(ctx, x - w / 2, y - h / 2, w, h, 22); fillstroke(ctx, col, lw=5)
    if sub:
        text(ctx, name, x, y - 13, size, tcol); text(ctx, sub, x, y + 22, 20, tcol)
    else:
        text(ctx, name, x, y, size, tcol)
    ctx.restore()

def acct(ctx, x, y, col, a=1.0, s=1.0):
    ctx.arc(x, y - 6 * s, 6 * s, 0, 2 * math.pi); ctx.set_source_rgba(*col, a); ctx.fill()
    ctx.move_to(x - 10 * s, y + 10 * s); ctx.curve_to(x - 10 * s, y - 2 * s, x + 10 * s, y - 2 * s, x + 10 * s, y + 10 * s); ctx.close_path(); ctx.fill()

def user(ctx, x, y, col=C['teal'], s=1.0, a=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.arc(0, -30, 18, 0, 2 * math.pi); fillstroke(ctx, SKIN, lw=3, a=a)
    ctx.move_to(-26, 22); ctx.curve_to(-26, -12, 26, -12, 26, 22); ctx.close_path(); fillstroke(ctx, col, lw=3, a=a)
    ctx.restore()

def shield(ctx, x, y, s, col):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.move_to(0, -70); ctx.curve_to(40, -50, 60, -55, 62, -50); ctx.curve_to(62, 20, 40, 55, 0, 75)
    ctx.curve_to(-40, 55, -62, 20, -62, -50); ctx.curve_to(-60, -55, -40, -50, 0, -70); ctx.close_path()
    fillstroke(ctx, col, lw=5); ctx.restore()

def dashed(ctx, x1, y1, x2, y2, col, a=1.0, lw=5):
    ctx.save(); ctx.set_dash([12, 8]); ctx.move_to(x1, y1); ctx.line_to(x2, y2)
    ctx.set_source_rgba(*col, a); ctx.set_line_width(lw); ctx.stroke(); ctx.restore()

def recorder(ctx, x, y, s=1.0, t=0.0, a=1.0):
    """small tape recorder with blinking REC dot"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -44, -28, 88, 56, 10); fillstroke(ctx, (.3, .32, .38), lw=3, a=a)
    for sd in (-1, 1):
        ctx.arc(sd * 20, 0, 12, 0, 2 * math.pi); fillstroke(ctx, (.85, .85, .88), lw=3, a=a)
    if (t * 2) % 1 < .6:
        ctx.arc(30, -18, 6, 0, 2 * math.pi); ctx.set_source_rgba(*C['red'], a); ctx.fill()
    ctx.restore()

def lock(ctx, x, y, s=1.0, col=C['yellow']):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.new_path(); ctx.arc(0, -14, 18, math.pi, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(7); ctx.stroke()
    rrect(ctx, -26, -14, 52, 40, 8); fillstroke(ctx, col, lw=4)
    ctx.arc(0, 4, 5, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
    ctx.restore()

def doc(ctx, x, y, col=C['white'], s=1.0, a=1.0):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -30, -38, 60, 76, 6); fillstroke(ctx, col, lw=3, a=a)
    for k in range(4):
        ctx.rectangle(-20, -24 + k * 14, 40 if k < 3 else 24, 5); ctx.set_source_rgba(*C['grey'], a); ctx.fill()
    ctx.restore()
