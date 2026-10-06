import cairo, math, subprocess, wave, numpy as np, random, sys, json, os
W, H, FPS = 1280, 720, 30
FONT = "Noto Sans CJK TC"
SR = 24000
LEAD, TAIL = 0.35, 0.45
# ---------- helpers ----------
C = dict(bg=(1, .97, .925), navy=(.15, .23, .35), teal=(.30, .71, .67), teal2=(.22, .56, .53),
         orange=(1, .54, .40), yellow=(1, .84, .31), red=(.90, .35, .35), pink=(1, .66, .70),
         screen=(.88, .97, .98), blue=(.35, .60, .92), green=(.36, .74, .42), grey=(.75, .78, .82), white=(1, 1, 1))

def clamp(x, a=0, b=1): return max(a, min(b, x))
def prog(u, t0, d=0.5): return clamp((u - t0) / d)
def ease_out(x): return 1 - (1 - x) ** 3
def back(x):
    c1 = 1.9; c3 = c1 + 1
    return 0 if x <= 0 else 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2

def rrect(ctx, x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0); ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi); ctx.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    ctx.close_path()

def fillstroke(ctx, fill, stroke=C['navy'], lw=5, a=1):
    ctx.set_source_rgba(*fill, a); ctx.fill_preserve()
    ctx.set_source_rgba(*stroke, a); ctx.set_line_width(lw); ctx.stroke()

def text(ctx, s, x, y, size, col=C['navy'], bold=True, align='c', a=1):
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(size)
    e = ctx.text_extents(s)
    dx = {'c': -e.x_advance / 2, 'l': 0, 'r': -e.x_advance}[align]
    ctx.move_to(x + dx, y + size * 0.36); ctx.set_source_rgba(*col, a); ctx.show_text(s); ctx.new_path()
    return e.x_advance

def pop(ctx, cx, cy, p):
    s = back(p); ctx.translate(cx, cy); ctx.scale(max(s, 0.001), max(s, 0.001)); ctx.translate(-cx, -cy)

def robot(ctx, x, y, s, t, mouth=0.0, wave=False, sweat=False, look=0.0, happy=True):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # shadow
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 245 / 0.18, 95, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, .10); ctx.fill(); ctx.restore()
    bob = -abs(math.sin(t * 4.2)) * 14
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.06); ctx.translate(0, -200)
    # arms
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for side in (-1, 1):
        if side == 1 and wave:
            ang = -1.05 + 0.45 * math.sin(t * 9)
        else:
            ang = side * 0.35 + math.pi / 2 + (0.05 * math.sin(t * 2) if side == -1 else 0)
            if side == 1: ang = math.pi / 2 - 0.35
        sx, sy = side * 78, 125
        ex, ey = sx + math.cos(ang) * 70 * (1 if side == 1 else 1), sy + math.sin(ang) * 70
        if side == -1: ex, ey = sx - math.cos(0.35) * 50 - 15, sy + 62
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(16); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['teal2']); ctx.set_line_width(8); ctx.stroke()
        ctx.arc(ex, ey, 14, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=4)
    # body
    rrect(ctx, -80, 88, 160, 125, 32); fillstroke(ctx, C['teal'])
    ctx.arc(0, 145, 22, 0, 2 * math.pi); fillstroke(ctx, C['orange'], lw=4)
    ctx.arc(0, 145, 8, 0, 2 * math.pi); ctx.set_source_rgba(1, 1, 1, .5 + .5 * math.sin(t * 5)); ctx.fill()
    # antenna
    ay = -128 + math.sin(t * 4) * 5
    ctx.move_to(0, -88); ctx.line_to(0, ay); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()
    ctx.arc(0, ay, 13, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], lw=4)
    # head
    rrect(ctx, -112, -90, 224, 178, 44); fillstroke(ctx, C['teal'])
    rrect(ctx, -86, -64, 172, 124, 32); fillstroke(ctx, C['screen'], lw=4)
    # bow
    ctx.save(); ctx.translate(78, -88); ctx.rotate(0.35 + 0.08 * math.sin(t * 5))
    for sd in (-1, 1):
        ctx.move_to(0, 0); ctx.curve_to(sd * 30, -26, sd * 46, -6, sd * 42, 8); ctx.curve_to(sd * 38, 22, sd * 18, 18, 0, 0)
        fillstroke(ctx, (1, .45, .62), lw=4)
    ctx.arc(0, 0, 9, 0, 2 * math.pi); fillstroke(ctx, (1, .70, .80), lw=4)
    ctx.restore()
    # eyes
    blink = (t % 3.3) < 0.13
    for ex in (-36, 36):
        ctx.save(); ctx.translate(ex + look * 8, -14)
        ctx.scale(1, 0.12 if blink else 1)
        ctx.arc(0, 0, 14, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink:
            ctx.arc(5, -5, 4.5, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
            ctx.arc(-5, 5, 2.2, 0, 2 * math.pi); ctx.fill()
        ctx.restore()
    for ex in (-58, 58):
        ctx.arc(ex, 16, 11, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], .8); ctx.fill()
    # mouth
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 26); ctx.scale(1, (4 + 20 * mouth) / 14)
        ctx.arc(0, 0, 14, 0, 2 * math.pi); ctx.restore(); ctx.set_source_rgb(*C['navy']); ctx.fill()
    else:
        if happy: ctx.arc(0, 18, 16, 0.15 * math.pi, 0.85 * math.pi)
        else: ctx.arc(0, 40, 14, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(112, -60 + dy); ctx.curve_to(95, -30 + dy, 100, -18 + dy, 112, -18 + dy)
        ctx.curve_to(124, -18 + dy, 129, -30 + dy, 112, -60 + dy)
        fillstroke(ctx, (.55, .80, 1), lw=3)
    ctx.restore()

def bubble(ctx, x, y, w, h, tailx, taily, fill=C['white']):
    rrect(ctx, x, y, w, h, 26)
    fillstroke(ctx, fill)
    ctx.move_to(tailx - 18, y + h - 3); ctx.line_to(tailx, taily); ctx.line_to(tailx + 18, y + h - 3)
    ctx.set_source_rgb(*fill); ctx.fill_preserve(); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()
    ctx.move_to(tailx - 15, y + h - 3); ctx.line_to(tailx + 15, y + h - 3); ctx.set_source_rgb(*fill); ctx.set_line_width(7); ctx.stroke()

BGS = [(1, .92, .95), (.90, .95, 1), (1, .96, .82), (.89, .99, .92), (.95, .92, 1), (1, .93, .88)]
DOTS = [(1, .72, .82), (.70, .84, 1), (1, .85, .45), (.62, .90, .72), (.80, .72, 1), (1, .78, .60)]
def background(ctx, t, sc=0):
    ctx.set_source_rgb(*BGS[sc]); ctx.paint()
    # scrolling polka dots
    off = (t * 30) % 80
    ctx.set_source_rgba(*DOTS[sc], .45)
    for gy in range(-1, 11):
        for gx in range(-1, 18):
            x = gx * 80 + off + (40 if gy % 2 else 0); y = gy * 80 + off * 0.5
            ctx.arc(x, y, 7, 0, 2 * math.pi); ctx.fill()
    # floating stars/confetti
    random.seed(3)
    for i in range(16):
        x = (random.random() * W + t * (20 + i * 3)) % (W + 80) - 40
        y = (random.random() * H + math.sin(t * 1.5 + i) * 20)
        col = random.choice([C['yellow'], C['teal'], C['orange'], C['pink'], C['blue']])
        star(ctx, x, y, 6 + random.random() * 8, col, .55, rot=t * (1 + i % 3))

def star(ctx, x, y, r, col, a=1, rot=0.0, outline=False):
    ctx.save(); ctx.translate(x, y); ctx.rotate(rot)
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.45
        ang = -math.pi / 2 + k * math.pi / 5
        (ctx.move_to if k == 0 else ctx.line_to)(math.cos(ang) * rr, math.sin(ang) * rr)
    ctx.close_path(); ctx.set_source_rgba(*col, a)
    if outline:
        ctx.fill_preserve(); ctx.set_source_rgba(*C['navy'], a); ctx.set_line_width(3); ctx.stroke()
    else: ctx.fill()
    ctx.restore()

def burst(ctx, cx, cy, u, t0, R=160, n=10):
    q = (u - t0) / 0.7
    if not (0 < q < 1): return
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue']]
    for k in range(n):
        ang = k * 2 * math.pi / n + 0.3
        d = R * ease_out(q)
        star(ctx, cx + math.cos(ang) * d, cy + math.sin(ang) * d, 14 * (1 - q) + 3, cols[k % 5], 1 - q, rot=q * 3, outline=True)

def sticker(ctx, s, x, y, u, t0, col=C['orange'], size=34, rot=-0.12, dur=99):
    p = prog(u, t0, .45)
    if p <= 0 or u > t0 + dur: return
    ctx.save(); pop(ctx, x, y, p); ctx.translate(x, y); ctx.rotate(rot + 0.05 * math.sin(u * 6)); ctx.translate(-x, -y)
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(size)
    w = ctx.text_extents(s).x_advance
    rrect(ctx, x - w / 2 - 22, y - size * 0.75, w + 44, size * 1.5, size * 0.75); fillstroke(ctx, col, lw=5)
    text(ctx, s, x, y, size, C['white'])
    ctx.restore()
    burst(ctx, x, y, u, t0, R=110, n=8)

EPTAG = [""]
def header(ctx, num, title, u):
    p = ease_out(prog(u, 0, .5))
    ctx.save(); ctx.translate(-300 * (1 - p), 0)
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(28)
    rrect(ctx, 40, 32, 88 + ctx.text_extents(title).x_advance, 58, 29); fillstroke(ctx, C['navy'], lw=0)
    ctx.arc(72, 61, 20, 0, 2 * math.pi); ctx.set_source_rgb(*C['yellow']); ctx.fill()
    text(ctx, str(num), 72, 60, 24, C['navy'])
    text(ctx, title, 104, 60, 28, C['white'], align='l')
    ctx.restore()

# ---------- icons ----------
def icon_book(ctx, x, y, s=1):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -34, -26, 34, 52, 6); fillstroke(ctx, C['orange'], lw=4)
    rrect(ctx, 0, -26, 34, 52, 6); fillstroke(ctx, C['yellow'], lw=4)
    ctx.restore()
def icon_web(ctx, x, y, s=1):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.arc(0, 0, 30, 0, 2 * math.pi); fillstroke(ctx, C['blue'], lw=4)
    ctx.save(); ctx.scale(0.45, 1); ctx.arc(0, 0, 30, 0, 2 * math.pi); ctx.restore()
    ctx.move_to(-30, 0); ctx.line_to(30, 0); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()
def icon_code(ctx, x, y, s=1):
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -36, -28, 72, 56, 10); fillstroke(ctx, C['navy'], lw=4)
    text(ctx, "</>", 0, 0, 28, C['green'])
    ctx.restore()


def card(ctx, cx, cy, p, label, draw):
    if p <= 0: return
    ctx.save(); pop(ctx, cx, cy, p)
    rrect(ctx, cx - 95, cy - 110, 190, 220, 28); fillstroke(ctx, C['white'], lw=5)
    draw(cx, cy - 25)
    text(ctx, label, cx, cy + 65, 30)
    ctx.restore()


def make_music(audio, TOTAL, outpath, seed=0):
    np.random.seed(seed)
    sr = SR; n = int(TOTAL * sr) + sr
    mus = np.zeros(n, np.float32)
    bpm = 116; beat = 60 / bpm
    prog_ = [[60, 64, 67, 72], [55, 59, 62, 67], [57, 60, 64, 69], [53, 57, 60, 65]]  # C G Am F
    def pluck(freq, dur, amp):
        L = int(dur * sr); tt = np.arange(L) / sr
        w = (np.sin(2 * np.pi * freq * tt) + 0.35 * np.sin(4 * np.pi * freq * tt) + 0.15 * np.sin(6 * np.pi * freq * tt))
        return (w * np.exp(-tt * 6) * amp).astype(np.float32)
    def hz(mn): return 440 * 2 ** ((mn - 69) / 12)
    pat = [0, 2, 1, 3, 2, 1, 3, 2]
    t = 0.0; bar = 0
    while t < TOTAL:
        ch = prog_[bar % 4]
        # bass
        for bb in range(4):
            i0 = int((t + bb * beat) * sr); x = pluck(hz(ch[0] - 24), beat * 0.9, 0.5)
            mus[i0:i0 + len(x)] += x[:max(0, n - i0)]
        for k in range(8):
            i0 = int((t + k * beat / 2) * sr); x = pluck(hz(ch[pat[k]]), beat, 0.28)
            mus[i0:i0 + len(x)] += x[:max(0, n - i0)]
        # shaker
        for k in range(8):
            i0 = int((t + k * beat / 2) * sr); L = int(0.05 * sr)
            x = (np.random.randn(L) * np.exp(-np.arange(L) / sr * 60) * (0.10 if k % 2 else 0.05)).astype(np.float32)
            mus[i0:i0 + L] += x[:max(0, n - i0)]
        t += 4 * beat; bar += 1
    mus /= np.abs(mus).max() + 1e-6
    fade = np.ones(n, np.float32); fl = int(1.0 * sr); fade[-fl:] = np.linspace(1, 0, fl)
    mus *= fade
    # duck under voice
    voice = audio[:n] / 32767.0
    vol = np.convolve(np.abs(voice), np.ones(2400) / 2400, mode="same")
    duck = 0.16 - 0.08 * np.clip(vol / (vol.max() * 0.3 + 1e-6), 0, 1)
    out = voice * 0.95 + mus * duck
    out = out / max(1.0, np.abs(out).max())
    with wave.open(outpath, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((out * 32767).astype(np.int16).tobytes())

def subtitle(ctx, s):
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(34)
    w = ctx.text_extents(s).x_advance
    rrect(ctx, 640 - w / 2 - 28, 648, w + 56, 54, 27); ctx.set_source_rgba(*C['navy'], .85); ctx.fill()
    text(ctx, s, 640, 674, 34, C['white'])


# ---------- episode machinery ----------
import re as _re
def weight(s):
    s = s.replace("60%", "百分之六十").replace("25%", "百分之二十五")
    s = _re.sub(r"[A-Za-z][A-Za-z\-]*", lambda mm: "字" * max(1, round(len(mm.group(0)) / 2.6)), s)
    return sum(0 if c in " 「」～" else (0.6 if c in "，。、：！？；" else 1) for c in s)

def auto_subs(s, maxlen=19):
    parts, cur = [], ""
    for ch in s:
        if ch in "」』）" and not cur.strip() and parts:
            parts[-1] += ch; continue
        cur += ch
        if ch in "，。！？：；":
            parts.append(cur); cur = ""
    if cur.strip(): parts.append(cur)
    fixed = []
    for p in parts:
        while len(p.strip()) > 22 and "、" in p[6:-3]:
            cut = [i for i, c in enumerate(p) if c == "、" and 6 <= i <= 21]
            if not cut: break
            i = cut[-1] + 1; fixed.append(p[:i]); p = p[i:]
        fixed.append(p)
    parts = fixed
    out = []
    for p in parts:
        p = p.strip()
        if out and len(out[-1]) + len(p) <= maxlen and not out[-1].endswith(("。", "！", "？")):
            out[-1] += p
        else:
            out.append(p)
    return out

def pauses(a):
    h = SR // 100
    en = np.array([np.sqrt(np.mean(a[i*h:(i+1)*h] ** 2)) for i in range(len(a) // h)])
    thr = np.percentile(en, 90) * 0.08
    quiet = en < thr; res = []; i = 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]: j += 1
            if j - i >= 12: res.append((i + j) / 2 / 100)
            i = j
        else: i += 1
    return res

WIPE = [C['orange'], C['pink'], C['blue'], C['yellow'], C['green'], C['orange'], C['pink']]

class Episode:
    def __init__(self, d, tag, subs=None):
        self.d = d; EPTAG[0] = tag
        self.SPOKEN = json.load(open(f"{d}/script.json"))
        n = len(self.SPOKEN)
        self.SUBS = subs or [auto_subs(s) for s in self.SPOKEN]
        self.clips, self.durs = [], []
        for i in range(n):
            a = np.fromfile(f"{d}/c{i+1}.pcm", dtype="<i2").astype(np.float32)
            idx = np.where(np.abs(a) > 400)[0]
            a = a[max(0, idx[0] - 1200): idx[-1] + 2400]
            self.clips.append(a); self.durs.append(len(a) / SR)
        self.starts = []; t = 0.0
        for i, dd in enumerate(self.durs):
            self.starts.append(t); t += LEAD + dd + (TAIL if i < n - 1 else 1.6)
        self.TOTAL = t
        au = np.zeros(int(t * SR) + SR, np.float32)
        for s0, a in zip(self.starts, self.clips):
            i0 = int((s0 + LEAD) * SR); au[i0:i0 + len(a)] += a
        self.audio = au
        hop = SR // FPS
        env = np.array([np.sqrt(np.mean(au[i*hop:(i+1)*hop] ** 2)) for i in range(len(au) // hop)])
        self.env = np.clip(env / (np.percentile(env[env > 0], 95) + 1e-6), 0, 1)
        P = [pauses(a) for a in self.clips]
        self.SUBT = []
        for sc in range(n):
            ws = [weight(c) for c in self.SUBS[sc]]; tot = sum(ws); acc = 0; b = []
            for wg in ws[:-1]:
                acc += wg; tt = self.durs[sc] * acc / tot
                c = [p for p in P[sc] if abs(p - tt) < 0.7]
                b.append(min(c, key=lambda p: abs(p - tt)) if c else tt)
            self.SUBT.append(b)
        self.scenes = []
        self.wipes = None

    def kw(self, sc, phrase, nth=0):
        s = self.SPOKEN[sc]; idx = -1
        for _ in range(nth + 1): idx = s.index(phrase, idx + 1)
        return max(0.2, LEAD + self.durs[sc] * weight(s[:idx]) / weight(s) - 0.25)

    def sub_at(self, sc, u):
        x = u - LEAD
        if x < -0.1 or x > self.durs[sc] + 0.3: return None
        for c, b in zip(self.SUBS[sc], self.SUBT[sc]):
            if x < b: return c
        return self.SUBS[sc][-1]

    def render(self, T, ctx):
        fi = int(T * FPS); m = float(self.env[fi]) if fi < len(self.env) else 0
        sc = 0
        for i, st in enumerate(self.starts):
            if T >= st: sc = i
        u = T - self.starts[sc]
        ctx.save(); self.scenes[sc](self, ctx, u, T, m); ctx.restore()
        if EPTAG[0]:
            ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(20)
            w = ctx.text_extents(EPTAG[0]).x_advance
            rrect(ctx, W - 40 - w - 32, 40, w + 32, 40, 20); ctx.set_source_rgba(1, 1, 1, .85); ctx.fill_preserve()
            ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
            text(ctx, EPTAG[0], W - 40 - w / 2 - 16, 60, 20)
        sub = self.sub_at(sc, u)
        if sub: subtitle(ctx, sub)
        n = len(self.starts)
        use_in = self.wipes is None or sc in self.wipes
        use_out = self.wipes is None or (sc + 1) in self.wipes
        if sc > 0 and u < 0.45 and use_in:
            q = ease_out(u / 0.45)
            ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
            ctx.rectangle(0, 0, W, H); ctx.arc(640, 360, 800 * q, 0, 2 * math.pi)
            ctx.set_source_rgb(*WIPE[sc % len(WIPE)]); ctx.fill(); ctx.set_fill_rule(cairo.FILL_RULE_WINDING)
        if sc < n - 1 and use_out:
            end = self.starts[sc + 1] - self.starts[sc]
            if u > end - 0.3:
                q = ease_out((u - (end - 0.3)) / 0.3)
                ctx.arc(640, 360, 800 * q, 0, 2 * math.pi); ctx.set_source_rgb(*WIPE[(sc + 1) % len(WIPE)]); ctx.fill()
        if T < 0.3:
            ctx.set_source_rgba(1, 1, 1, 1 - T / 0.3); ctx.paint()
        if T > self.TOTAL - 0.5:
            ctx.set_source_rgba(1, 1, 1, clamp((T - (self.TOTAL - 0.5)) / 0.5)); ctx.paint()

    def run(self, out, argv):
        if len(argv) > 1:
            from PIL import Image
            ts = argv[1:] if argv[1] != "auto" else [str(round(s + LEAD + d * f, 1)) for s, d in zip(self.starts, self.durs) for f in (0.3, 0.85)]
            ims = []
            for tt in ts:
                surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
                self.render(float(tt), ctx); surf.write_to_png(f"{self.d}/prev.png")
                ims.append(Image.open(f"{self.d}/prev.png").convert("RGB").resize((640, 360)))
            rows = (len(ims) + 1) // 2
            g = Image.new("RGB", (1280, 360 * rows), "white")
            for i, im in enumerate(ims): g.paste(im, ((i % 2) * 640, (i // 2) * 360))
            g.save(f"{self.d}/grid.png"); print(ts, [round(x, 1) for x in self.durs], round(self.TOTAL, 1)); return
        make_music(self.audio, self.TOTAL, f"{self.d}/mix.wav", seed=len(out))
        nf = int(self.TOTAL * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", f"{self.d}/mix.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium",
                               "-c:a", "aac", "-b:a", "160k", "-shortest", out], stdin=subprocess.PIPE)
        surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
        for i in range(nf):
            ctx.save(); self.render(i / FPS, ctx); ctx.restore(); surf.flush()
            ff.stdin.write(bytes(surf.get_data()))
        ff.stdin.close(); ff.wait(); print("done", out, nf / FPS)

# ---------- extra reusable pieces ----------
def outro_common(ep, ctx, u, T, m, sc, big, line, chips=None, bye="掰掰～"):
    background(ctx, T, 5)
    random.seed(11)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(60):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        y = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        x = x0 + math.sin(u * 3 + k) * 20
        ctx.save(); ctx.translate(x, y); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()
    ctx.save(); pop(ctx, 290, 360, prog(u, 0, .6)); robot(ctx, 290, 320, 0.95, T, m, wave=True); ctx.restore()
    pp = prog(u, .3, .6)
    ctx.save(); pop(ctx, 850, 230, pp); text(ctx, big, 850, 200, 64, C['orange']); text(ctx, line, 850, 285, 34); ctx.restore()
    burst(ctx, 850, 220, u, .3, R=300, n=14)
    if chips:
        n = len(chips); wd = 138 if n > 4 else 170
        for i, (lab, t0) in enumerate(chips):
            x = 850 + (i - (n - 1) / 2) * (wd + 12)
            p = prog(u, t0, .4)
            if p <= 0: continue
            ctx.save(); pop(ctx, x, 430, p)
            rrect(ctx, x - wd / 2, 395, wd, 70, 35); fillstroke(ctx, [C['yellow'], C['teal'], C['pink'], C['blue'], C['green']][i % 5])
            text(ctx, lab, x, 430, 28, C['navy']); ctx.restore()
    if bye:
        t0 = ep.kw(sc, "掰掰") if "掰掰" in ep.SPOKEN[sc] else 99
        sticker(ctx, bye, 1080, 560, u, t0, C['pink'], 38)

def chip(ctx, s, x, y, p, col, size=30, tcol=C['navy'], padx=24):
    if p <= 0: return
    ctx.save(); pop(ctx, x, y, p)
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(size)
    w = ctx.text_extents(s).x_advance
    rrect(ctx, x - w / 2 - padx, y - size * 0.85, w + 2 * padx, size * 1.7, size * 0.85); fillstroke(ctx, col)
    text(ctx, s, x, y, size, tcol); ctx.restore()

def big_title(ctx, s, x, y, u, t0, size=60, sub=None, col=C['yellow'], w=None):
    p = prog(u, t0, .6)
    if p <= 0: return
    ctx.save(); pop(ctx, x, y, p)
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(size)
    ww = w or ctx.text_extents(s).x_advance + 100
    hh = size * 2.2 + (40 if sub else 0)
    rrect(ctx, x - ww / 2, y - hh / 2, ww, hh, 30); fillstroke(ctx, col, lw=6)
    text(ctx, s, x, y - (18 if sub else 0), size)
    if sub: text(ctx, sub, x, y + size * 0.75, 28, C['teal2'])
    ctx.restore()
    burst(ctx, x, y, u, t0 + .1, R=ww * 0.6, n=14)

def mark(ctx, x, y, ok, p, r=26):
    if p <= 0: return
    ctx.save(); pop(ctx, x, y, p)
    ctx.arc(x, y, r, 0, 2 * math.pi); fillstroke(ctx, C['green'] if ok else C['red'], lw=4)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_source_rgb(1, 1, 1); ctx.set_line_width(r * 0.28)
    if ok:
        ctx.move_to(x - r * .45, y); ctx.line_to(x - r * .1, y + r * .38); ctx.line_to(x + r * .5, y - r * .38)
    else:
        ctx.move_to(x - r * .4, y - r * .4); ctx.line_to(x + r * .4, y + r * .4); ctx.move_to(x + r * .4, y - r * .4); ctx.line_to(x - r * .4, y + r * .4)
    ctx.stroke(); ctx.restore()

def chatbox(ctx, x, y, w, s, shown, T, size=34):
    rrect(ctx, x, y, w, 80, 40); fillstroke(ctx, C['white'], lw=5)
    t = s[:shown]
    adv = text(ctx, t, x + 34, y + 40, size, align='l')
    if (T * 2) % 1 < .6:
        ctx.rectangle(x + 38 + adv, y + 20, 4, 40); ctx.set_source_rgb(*C['navy']); ctx.fill()
    ctx.arc(x + w - 40, y + 40, 24, 0, 2 * math.pi); fillstroke(ctx, C['orange'], lw=4)
    text(ctx, "↑", x + w - 40, y + 38, 26, C['white'])

def typed(u, t0, s, cps=9):
    return int(clamp((u - t0) * cps / max(1, len(s))) * len(s) + (0.999 if u > t0 else 0))

def speech(ctx, s, x, y, p, tail='l', size=28, fill=C['white'], col=C['navy']):
    if p <= 0: return
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD); ctx.set_font_size(size)
    w = ctx.text_extents(s).x_advance + 50; h = size * 2
    ctx.save(); pop(ctx, x, y, p)
    tx = x - w / 2 + 40 if tail == 'l' else x + w / 2 - 40
    bubble(ctx, x - w / 2, y - h / 2, w, h, tx, y + h / 2 + 22, fill=fill)
    text(ctx, s, x, y, size, col); ctx.restore()
