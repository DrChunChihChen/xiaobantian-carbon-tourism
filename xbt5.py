"""小半天旅遊系列・第 5 集：歲月沉澱的人文綠洲——石馬公園與半天竹藝
主持人：小半天在地青年導遊・阿天 (A-Tian)
"""
from atian import *

# ---------- 專屬櫻花與竹藝繪圖元件 ----------

def draw_sakura_petal(ctx, x, y, s, ang, col=C['pink']):
    """櫻花花瓣"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(ang)
    ctx.move_to(0, -12); ctx.curve_to(10, -6, 10, 6, 0, 12); ctx.curve_to(-10, 6, -10, -6, 0, -12); ctx.close_path()
    fillstroke(ctx, col, stroke=(0.85, 0.45, 0.55), lw=1.5)
    ctx.restore()

def draw_sakura_park_bg(ctx, t):
    """石馬公園粉紅櫻花與綠意草坡背景"""
    pat = cairo.LinearGradient(0, 0, 0, H)
    pat.add_color_stop_rgb(0.0, 0.82, 0.92, 0.98)   # 晴朗蔚藍天
    pat.add_color_stop_rgb(0.55, 0.98, 0.92, 0.95)  # 櫻花粉白空氣感
    pat.add_color_stop_rgb(1.0, 0.65, 0.85, 0.65)   # 公園綠草坪
    ctx.set_source(pat); ctx.paint()

    # 左右盛開的粉紅河津櫻樹冠
    ctx.save()
    for cx, cy, r in [(140, 240, 140), (280, 200, 110), (1080, 220, 130), (1200, 260, 110)]:
        ctx.arc(cx, cy, r, 0, 2 * math.pi)
        fillstroke(ctx, (1.0, 0.76, 0.84), stroke=C['navy'], lw=4)
        for i in range(4):
            ctx.arc(cx - r * 0.3 + i * 26, cy + math.sin(i) * 20, r * 0.4, 0, 2 * math.pi)
            fillstroke(ctx, (1.0, 0.85, 0.90), stroke=C['navy'], lw=2.5)
    ctx.restore()

    # 漫天飄散的粉紅櫻花花瓣
    random.seed(77)
    for i in range(12):
        px = (random.random() * W + t * (25 + i * 6)) % (W + 60) - 30
        py = (random.random() * H + t * (20 + i * 4)) % (H + 60) - 30
        draw_sakura_petal(ctx, px, py, 0.8 + (i % 3) * 0.2, t * 2.5 + i, col=(1.0, 0.72, 0.82))

def draw_bamboo_charcoal(ctx, cx, cy, s=1.0):
    """竹炭黑金意象：黑亮高溫竹炭棒與竹醋液"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    # 3 根斜靠的竹炭筒
    for idx, (ox, ang) in enumerate([(-25, -0.2), (0, 0.05), (25, 0.25)]):
        ctx.save(); ctx.translate(ox, 0); ctx.rotate(ang)
        rrect(ctx, -14, -65, 28, 130, 8); fillstroke(ctx, (0.18, 0.18, 0.20), stroke=C['navy'], lw=3.5)
        # 高溫竹炭亮澤反光線
        ctx.move_to(-4, -55); ctx.line_to(-4, 55); ctx.set_source_rgba(0.65, 0.68, 0.75, 0.7); ctx.set_line_width(3); ctx.stroke()
        ctx.restore()
    # 金黃火花/黑金能量標記
    star(ctx, 42, -45, 14, C['yellow'], 1, outline=True)
    ctx.restore()

def draw_bamboo_rice(ctx, cx, cy, s=1.0, t=0.0):
    """傳統熱騰騰竹筒飯與鮮甜冬筍"""
    ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s)
    # 斜切孟宗竹筒
    rrect(ctx, -65, -15, 130, 48, 10); fillstroke(ctx, (0.35, 0.65, 0.38), stroke=C['navy'], lw=4)
    # 飽滿米飯（糯米與花生香菇）
    rrect(ctx, -55, -28, 110, 22, 6); fillstroke(ctx, (0.98, 0.95, 0.85), stroke=C['navy'], lw=3)
    # 裊裊香氣蒸氣
    for ox in [-25, 0, 25]:
        sy = -45 + math.sin(t * 3.5 + ox) * 6
        ctx.move_to(ox, -32); ctx.curve_to(ox - 6, sy, ox + 6, sy - 14, ox, sy - 28)
        ctx.set_source_rgba(0.85, 0.88, 0.92, 0.7); ctx.set_line_width(3.5); ctx.stroke()
    # 一旁的飽滿竹筍（冬筍）
    ctx.save(); ctx.translate(75, 8)
    ctx.move_to(-16, 20); ctx.line_to(16, 20); ctx.line_to(0, -32); ctx.close_path()
    fillstroke(ctx, (0.82, 0.68, 0.40), stroke=C['navy'], lw=3)
    ctx.restore()
    ctx.restore()


# ==================== 場景定義 (s0 ~ s5) ====================

# ----- s0: 開場 -----
def s0(ep, ctx, u, T, m):
    draw_sakura_park_bg(ctx, T)

    p_lu = ease_out(prog(u, 0.0, 0.7))
    x_lu = -120 + 330 * p_lu
    atian(ctx, x_lu, 340, 0.92, T, m, wave=True)
    sticker(ctx, "哈囉！", 150, 110, u, 0.3, C['pink'], 38, dur=3.5)

    t_card = 1.8
    p_card = prog(u, t_card, 0.6)
    if p_card > 0:
        cx, cy = 760, 290
        ctx.save(); pop(ctx, cx, cy, p_card)
        card_w, card_h = 740, 260
        rrect(ctx, cx - card_w / 2 + 10, cy - card_h / 2 + 12, card_w, card_h, 32)
        ctx.set_source_rgba(0.22, 0.15, 0.18, 0.18); ctx.fill()

        # 櫻花粉與竹金漸層底
        pat = cairo.LinearGradient(0, cy - card_h / 2, 0, cy + card_h / 2)
        pat.add_color_stop_rgb(0.0, 1.0, 0.88, 0.92)
        pat.add_color_stop_rgb(1.0, 1.0, 0.75, 0.65)
        rrect(ctx, cx - card_w / 2, cy - card_h / 2, card_w, card_h, 32)
        ctx.set_source(pat); ctx.fill_preserve()
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(6); ctx.stroke()

        sub_text = "小半天旅遊系列・第 5 集"
        sub_w = 340; sub_h = 42
        rrect(ctx, cx - sub_w / 2, cy - card_h / 2 + 28, sub_w, sub_h, 21)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
        text(ctx, sub_text, cx, cy - card_h / 2 + 50, 22, (0.85, 0.35, 0.45), bold=True)

        text(ctx, "歲月沉澱的人文綠洲", cx, cy + 8, 42, C['navy'], bold=True)
        text(ctx, "石馬公園與半天竹藝傳奇", cx, cy + 66, 48, (0.65, 0.22, 0.32), bold=True)
        ctx.restore()
        burst(ctx, cx, cy, u, t_card + 0.1, R=420, n=16)

    t_sakura = ep.kw(0, "石馬公園")
    p_sakura = prog(u, t_sakura - 0.2, 0.4)
    if p_sakura > 0:
        chip(ctx, "一年開兩次花河津櫻", 600, 480, p_sakura, C['pink'], 28, tcol=C['navy'])
        star(ctx, 465, 480, 10, C['yellow'], p_sakura, rot=T * 2, outline=True)

    t_craft = ep.kw(0, "竹藝傳奇")
    p_craft = prog(u, t_craft - 0.2, 0.45)
    if p_craft > 0:
        chip(ctx, "竹編工藝與竹炭黑金", 920, 480, p_craft, C['teal'], 28, tcol=C['white'])
        star(ctx, 790, 480, 10, C['yellow'], p_craft, rot=-T * 2, outline=True)


# ----- s1: 路線圖導覽 -----
def s1(ep, ctx, u, T, m):
    stations = [
        ("粉紅奇蹟\n石馬公園", "石馬公園"),
        ("竹編工藝\n竹炭黑金", "竹炭黑金"),
        ("竹鄉美食\n冬筍竹筒飯", "幸福滋味")
    ]
    roadmap_scene(ep, ctx, u, T, m, 1, stations)


# ----- s2: 第 1 站：石馬公園奇蹟 -----
def s2(ep, ctx, u, T, m):
    draw_sakura_park_bg(ctx, T)
    station_card(ctx, u, 1, "石馬公園櫻花奇蹟")
    if u < 1.9: return
    header(ctx, 1, "小半天入口門面：全台罕見一年開兩次花的河津櫻", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側石馬傳說與由來卡
    p_hist = prog(u, 2.1, 0.5)
    if p_hist > 0:
        ctx.save(); pop(ctx, 330, 330, p_hist)
        rrect(ctx, 160, 160, 340, 340, 22); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
        chip(ctx, "入口綠色地標", 330, 205, 1, C['teal'], 20, tcol=C['white'])
        text(ctx, "石馬公園", 330, 275, 42, C['navy'], bold=True)
        text(ctx, "相傳早年有巨石形如駿馬", 330, 330, 20, (0.42, 0.38, 0.35), bold=True)
        chip(ctx, "小半天最美的門戶客廳", 330, 400, 1, C['yellow'], 22)
        ctx.restore()

    # 右側雙花期解析卡
    p_bloom = prog(u, 2.5, 0.5)
    if p_bloom > 0:
        ctx.save(); pop(ctx, 770, 330, p_bloom)
        rrect(ctx, 560, 180, 420, 250, 22); fillstroke(ctx, (1, 0.95, 0.97), stroke=C['pink'], lw=5)
        chip(ctx, "🌸 全台唯一的雙重花期奇觀", 770, 225, 1, (0.85, 0.35, 0.45), 24, tcol=C['white'])
        text(ctx, "✦ 第一次：每年春節初春爛漫盛開", 770, 285, 22, C['navy'], bold=True)
        text(ctx, "✦ 第二次：每年九月秋風吹起再次綻放", 770, 335, 22, (0.75, 0.25, 0.35), bold=True)
        text(ctx, "✦ 數百株河津櫻染紅整座綠谷", 770, 385, 22, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()


# ----- s3: 第 2 站：竹藝與竹炭黑金 -----
def s3(ep, ctx, u, T, m):
    background(ctx, T, 2)
    station_card(ctx, u, 2, "竹藝與竹炭黑金")
    if u < 1.9: return
    header(ctx, 2, "傳統巧手編織到高溫竹炭：綠金變黑金", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m, point=True)

    # 左右對照卡片
    cards = [
        ("傳統竹編工藝", "竹簍、竹籃、竹椅生活器具", 380, 2.1, C['yellow']),
        ("現代竹炭黑金", "千度高溫精煉，除濕養生綠金", 760, ep.kw(3, "竹炭產業"), (0.25, 0.25, 0.28))
    ]

    for title, desc, cx, t_c, col in cards:
        p_c = prog(u, t_c - 0.2, 0.45)
        if p_c <= 0: continue
        ctx.save(); pop(ctx, cx, 320, p_c)
        rrect(ctx, cx - 170, 180, 340, 260, 22); fillstroke(ctx, C['white'], stroke=C['navy'], lw=5)
        if "竹編" in title:
            # 編織竹籃
            rrect(ctx, cx - 40, 225, 80, 50, 10); fillstroke(ctx, (0.85, 0.68, 0.42), stroke=C['navy'], lw=3)
            ctx.arc(cx, 220, 30, 1.0 * math.pi, 2.0 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3.5); ctx.stroke()
        else:
            draw_bamboo_charcoal(ctx, cx, 245, s=0.9)
        chip(ctx, title, cx, 345, 1, col, 24, tcol=C['white'] if col != C['yellow'] else C['navy'])
        text(ctx, desc, cx, 395, 20, (0.35, 0.35, 0.40), bold=True)
        ctx.restore()


# ----- s4: 第 3 站：竹鄉特色料理 -----
def s4(ep, ctx, u, T, m):
    draw_sakura_park_bg(ctx, T)
    station_card(ctx, u, 3, "竹鄉特色料理")
    if u < 1.9: return
    header(ctx, 3, "大自然的饋贈：鮮甜冬筍與竹筒飯", u - 1.9)
    atian(ctx, 1150, 545, 0.42, T, m)

    # 左側竹筒飯與冬筍特寫
    p_food = prog(u, 2.1, 0.5)
    if p_food > 0:
        ctx.save(); pop(ctx, 340, 330, p_food)
        draw_bamboo_rice(ctx, 340, 330, s=1.35, t=T)
        chip(ctx, "天然竹膜清甜融入米粒", 340, 460, 1, C['green'], 24, tcol=C['white'])
        ctx.restore()

    # 右側美食精華卡
    t_taste = ep.kw(4, "冬筍")
    p_taste = prog(u, t_taste - 0.2, 0.5)
    if p_taste > 0:
        ctx.save(); pop(ctx, 770, 330, p_taste)
        rrect(ctx, 560, 190, 420, 240, 22); fillstroke(ctx, C['white'], stroke=C['orange'], lw=5)
        chip(ctx, "小半天當令美味饗宴", 770, 235, 1, C['orange'], 24, tcol=C['white'])
        text(ctx, "🎍 冬筍/春筍：鮮甜脆口、排骨甘醇", 770, 290, 22, C['navy'], bold=True)
        text(ctx, "🍚 竹筒飯：慢火蒸烤、竹膜飄香", 770, 335, 22, C['navy'], bold=True)
        text(ctx, "🍵 在地茶餐：融入凍頂茶香的獨家風味", 770, 380, 22, (0.75, 0.35, 0.15), bold=True)
        ctx.restore()


# ----- s5: 總整理與下集預告 -----
def s5(ep, ctx, u, T, m):
    background(ctx, T, 5)
    random.seed(55)
    cols = [C['yellow'], C['orange'], C['pink'], C['teal'], C['blue'], C['green']]
    for k in range(50):
        x0 = random.random() * W; sp = 120 + random.random() * 160; ph = random.random() * 3
        yy = -30 + (u * sp + ph * 200) % (H + 60) if u > 0.2 else -50
        ctx.save(); ctx.translate(x0 + math.sin(u * 3 + k) * 20, yy); ctx.rotate(u * 4 + k)
        ctx.rectangle(-6, -3, 12, 6); ctx.set_source_rgb(*cols[k % 6]); ctx.fill(); ctx.restore()

    tb = LEAD + ep.durs[5] * 0.78
    atian(ctx, 220, 350, 0.95, T, m, wave=u > tb)

    # 標題
    pp = prog(u, 0.2, 0.5)
    ctx.save(); pop(ctx, 780, 115, pp)
    text(ctx, "第 5 集 重點筆記", 780, 95, 52, C['orange'], bold=True)
    text(ctx, "南投鹿谷・石馬公園與竹藝美食", 780, 145, 24, (0.35, 0.35, 0.40), bold=True)
    ctx.restore()

    rows = [
        ("櫻花奇觀", "石馬公園河津櫻，一年春秋開兩次花", ep.kw(5, "竹子的韌性"), C['pink']),
        ("竹藝黑金", "竹編生活器具，千度竹炭轉化綠色黑金", ep.kw(5, "櫻花的柔美"), C['teal']),
        ("竹鄉美味", "冬筍鮮甜脆口，竹筒飯慢烤米粒竹香", ep.kw(5, "人文風景"), C['green'])
    ]
    for k, (a, b, t0, col) in enumerate(rows):
        p = prog(u, t0 - 0.2, 0.4)
        if p <= 0: continue
        y = 215 + k * 80
        ctx.save(); ctx.translate(-250 * (1 - ease_out(p)), 0)
        rrect(ctx, 450, y - 32, 700, 66, 33)
        fillstroke(ctx, C['white'], stroke=C['navy'], lw=4)
        chip(ctx, a, 555, y + 1, 1, col, 24)
        text(ctx, b, 665, y + 1, 24, C['navy'], bold=True, align='l')
        ctx.restore()

    # 下集預告橫幅
    t_next = ep.kw(5, "下一集")
    p_next = prog(u, t_next - 0.2, 0.5)
    if p_next > 0:
        cx, cy = 800, 490
        ctx.save(); pop(ctx, cx, cy, p_next)
        rrect(ctx, cx - 350, cy - 34, 700, 68, 20)
        fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=5)
        chip(ctx, "壓軸完結", cx - 265, cy + 1, 1, C['orange'], 22, tcol=C['white'])
        text(ctx, "兩天一夜低碳慢遊！小半天全攻略特輯", cx - 185, cy + 1, 22, C['navy'], bold=True, align='l')
        ctx.restore()

    sticker(ctx, "下集見！", 1080, 595, u, tb, C['pink'], 34)


# ==================== 整合執行 ====================

scenes = [s0, s1, s2, s3, s4, s5]
wipes = {2, 3, 4, 5}

run("xbt5", "小半天系列 EP5", scenes, "小半天_EP5_石馬公園與竹藝傳奇.mp4", wipes=wipes)
