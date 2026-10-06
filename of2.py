"""辦公室碳冒險：CASE #002 印表機裡的無紙化幽靈 (刑偵剪貼調查風格)"""
import engine
from engine import *
from scrapbook import *

# 調查風格色票與設定
engine.WIPE = [(0.12, 0.12, 0.14), (0.82, 0.18, 0.15), (0.12, 0.12, 0.14), (0.82, 0.18, 0.15)]

def run(name, tag, scenes, out, wipes=None):
    ep = Episode(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), tag)
    ep.scenes = scenes; ep.wipes = wipes
    ep.run(out, sys.argv)

def custom_sub(ctx, s):
    """黑底圓角長條字幕，重點詞高亮黃色"""
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(32)
    ext = ctx.text_extents(s)
    w = ext.width
    rrect(ctx, 640 - w / 2 - 28, 648, w + 56, 52, 14)
    ctx.set_source_rgba(0.08, 0.08, 0.10, 0.94); ctx.fill()

    highlights = ["5.4 公斤", "五千公升", "五十萬張", "五公噸", "45%", "3 公斤", "電子簽章", "瞬間歸零", "八公噸碳", "十噸碳排", "無紙化", "碎紙機", "碳粉匣"]
    found_hl = None
    for h in highlights:
        if h in s:
            found_hl = h
            break

    if not found_hl:
        text(ctx, s, 640, 674, 32, C['white'])
    else:
        parts = s.split(found_hl, 1)
        w0 = ctx.text_extents(parts[0]).x_advance
        wh = ctx.text_extents(found_hl).x_advance
        start_x = 640 - w / 2
        if parts[0]:
            text(ctx, parts[0], start_x + w0 / 2, 674, 32, C['white'])
        text(ctx, found_hl, start_x + w0 + wh / 2, 674, 32, (1.0, 0.88, 0.20))
        if parts[1]:
            w1 = ctx.text_extents(parts[1]).x_advance
            text(ctx, parts[1], start_x + w0 + wh + w1 / 2, 674, 32, C['white'])

engine.subtitle = custom_sub

# ==================== 專屬道具繪製 ====================

def copier_machine(ctx, x, y, s=1.0):
    """大型落地多功能影印機"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 機身下半 (紙匣底座)
    ctx.rectangle(-70, 0, 140, 100)
    ctx.set_source_rgb(0.92, 0.92, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.25); ctx.set_line_width(4); ctx.stroke()
    for i in range(2):
        ctx.rectangle(-60, 15 + i * 40, 120, 30); ctx.set_source_rgb(0.85, 0.85, 0.88); ctx.fill()
        rrect(ctx, -15, 25 + i * 40, 30, 8, 3); ctx.set_source_rgb(0.4, 0.4, 0.45); ctx.fill()
    # 機身上半 (操作台與進紙托盤)
    ctx.rectangle(-75, -60, 150, 60)
    ctx.set_source_rgb(0.96, 0.96, 0.98); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.25); ctx.set_line_width(4); ctx.stroke()
    # 觸控螢幕
    ctx.rectangle(20, -50, 45, 35); ctx.set_source_rgb(0.2, 0.5, 0.85); ctx.fill()
    # 自動雙面送稿器 (頂蓋)
    ctx.rectangle(-60, -90, 100, 30); ctx.set_source_rgb(0.88, 0.88, 0.92); ctx.fill()
    # 出紙托盤上堆滿的白紙
    for k in range(4):
        ctx.rectangle(-95, -20 - k * 6, 40, 6); ctx.set_source_rgb(1, 1, 1); ctx.fill()
        ctx.set_source_rgb(0.7, 0.7, 0.7); ctx.set_line_width(1); ctx.stroke()
    ctx.restore()

def shredder_machine(ctx, x, y, s=1.0):
    """辦公室碎紙機 (吞進整疊廢紙)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 碎紙桶身 (透明可見紙條)
    ctx.rectangle(-60, -30, 120, 120)
    ctx.set_source_rgb(0.25, 0.25, 0.28); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
    # 桶內滿滿碎紙條
    for k in range(12):
        xx = -45 + (k % 6) * 16
        yy = 10 + (k // 6) * 35
        ctx.rectangle(xx, yy, 6, 25); ctx.set_source_rgb(0.95, 0.95, 0.92); ctx.fill()
    # 碎紙機頭
    ctx.rectangle(-68, -75, 136, 45); ctx.set_source_rgb(0.85, 0.85, 0.88); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
    # 進紙入料口
    ctx.rectangle(-45, -70, 90, 8); ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill()
    # 正在被碎掉的紙張
    ctx.rectangle(-35, -100, 70, 32); ctx.set_source_rgb(1, 1, 1); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(10); ctx.move_to(-25, -82); ctx.set_source_rgb(0.8, 0.2, 0.2); ctx.show_text("機密報告")
    ctx.restore()

def paper_ream(ctx, x, y, s=1.0):
    """一包 500 張 A4 影印紙"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 厚厚一疊紙身
    ctx.rectangle(-70, -45, 140, 90)
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.set_line_width(4); ctx.stroke()
    # 藍色外包裝紙腰帶
    ctx.rectangle(-70, -20, 140, 40); ctx.set_source_rgb(0.2, 0.5, 0.85); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16); ctx.move_to(-55, 6); ctx.set_source_rgb(1, 1, 1); ctx.show_text("A4 COPY PAPER")
    ctx.set_font_size(12); ctx.move_to(-30, 24); ctx.show_text("500 SHEETS")
    ctx.restore()

def toner_cartridge(ctx, x, y, s=1.0):
    """雷射印表機碳粉匣"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.rectangle(-80, -35, 160, 70)
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill_preserve()
    ctx.set_source_rgb(0.35, 0.35, 0.40); ctx.set_line_width(4); ctx.stroke()
    # 感光滾筒綠光
    ctx.rectangle(-70, 15, 140, 12); ctx.set_source_rgb(0.2, 0.85, 0.45); ctx.fill()
    # 碳粉警示黃標
    ctx.rectangle(-40, -25, 80, 24); ctx.set_source_rgb(0.95, 0.8, 0.2); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12); ctx.move_to(-30, -9); ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.show_text("TONER BLACK")
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    tp, tc = ep.kw(0, "無紙化"), ep.kw(0, "影印機")
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #002 辦公室紙張大搜查", 640, 160, size=28)
        text(ctx, "印表機裡的無紙化幽靈", 640, 245, 54, (0.12, 0.12, 0.15))
        text(ctx, "紙張真的被消滅了嗎？", 640, 310, 32, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        items = ["案發現場：影印室與多功能事務機", "日常現象：開會人手一份印紙、當天直接進碎紙機", "嫌疑目標：口頭上的無紙化，背地裡的大量伐木與碳排"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    q = prog(u, tc - 0.2, 0.35)
    if q > 0:
        ctx.save(); pop(ctx, 920, 220, q)
        red_stamp(ctx, "浪費確鑿", 920, 220, ang=-0.16, s=1.1)
        ctx.restore()

# 1 三條線索
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THREE CLUES 紙張調查線索板", 640, 75, size=26)
    t1, t2, t3 = ep.kw(1, "一包 A4 紙"), ep.kw(1, "會議簡報"), ep.kw(1, "紙張浪費")

    cards = [
        (t1, 260, 340, -0.04, "01 一包紙的代價", paper_ream),
        (t2, 640, 330, 0.03, "02 碎紙機黑洞", shredder_machine),
        (t3, 1020, 345, -0.03, "03 電子簽章革命", None)
    ]
    pins = []
    for t0, xx, yy, ang, lab, draw_fn in cards:
        p = prog(u, t0 - 0.3, 0.45)
        if p > 0:
            ctx.save(); pop(ctx, xx, yy, p)
            polaroid(ctx, xx, yy, 260, 320, ang=ang, label=lab)
            if draw_fn:
                ctx.save(); ctx.translate(xx, yy - 20); ctx.rotate(ang)
                draw_fn(ctx, 0, 0, 0.75)
                ctx.restore()
            else:
                rrect(ctx, xx - 60, yy - 70, 120, 90, 12); ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill()
                text(ctx, "E-Sign", xx, yy - 30, 24, (1, 1, 1))
                text(ctx, "✓ 線上核決", xx, yy - 5, 18, (1, 1, 1))
            red_pin(ctx, xx, yy - 145)
            ctx.restore()
        pins.append((xx, yy - 145))

    if u > t2 - 0.1:
        red_string(ctx, pins[0][0], pins[0][1], pins[1][0], pins[1][1], sag=35, p=prog(u, t2 - 0.1, 0.4))
    if u > t3 - 0.1:
        red_string(ctx, pins[1][0], pins[1][1], pins[2][0], pins[2][1], sag=35, p=prog(u, t3 - 0.1, 0.4))

# 2 迷思：天然木頭沒碳排？
def s2(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "COMMON MYTH 紙張天然環保？", 380, 85, size=24)
    tw, tq = ep.kw(2, "天然木頭"), ep.kw(2, "哪有什麼碳排放")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 380, 380, ang=-0.03, label="辦公桌上堆積成山的文件")
        copier_machine(ctx, 330, 330, 0.9)
        red_pin(ctx, 330, 180)
        ctx.restore()

    q = prog(u, tw - 0.2, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 850, 350, q)
        torn_paper(ctx, 850, 350, 480, 340, ang=0.03, bg=(0.97, 0.96, 0.92))
        text(ctx, "常見誤區告白", 850, 240, 32, (0.15, 0.15, 0.2))
        text(ctx, "「紙張是木頭做的天然材質，", 850, 305, 26, (0.3, 0.3, 0.35))
        text(ctx, "開會多印個二十份，", 850, 345, 26, (0.3, 0.3, 0.35))
        text(ctx, "事後回收就好，能有什麼碳排？」", 850, 385, 24, (0.3, 0.3, 0.35))
        ctx.restore()

    k = prog(u, tq - 0.2, 0.35)
    if k > 0:
        ctx.save(); pop(ctx, 850, 470, k)
        ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(68)
        ctx.move_to(850 - 150, 490)
        ctx.set_source_rgb(0.9, 0.15, 0.15); ctx.show_text("真沒事？")
        ctx.restore()

# 3 震撼真相：5.4 kg ＋ 5,000 公升水！
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THE COST OF PAPER 紙張代價", 640, 85, size=26)
    t54, tw = ep.kw(3, "5.4 公斤"), ep.kw(3, "五千公升")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 400, ang=0.01, bg=(0.97, 0.96, 0.90))
        text(ctx, "製造一包普通 A4 影印紙 (500 張)", 640, 210, 32, (0.3, 0.3, 0.35))

        q = prog(u, t54 - 0.3, 0.45)
        if q > 0:
            highlighter(ctx, 220, 350, 420, 75)
            text(ctx, "5.4 kg CO2e", 430, 335, 52, (0.85, 0.15, 0.15))
            text(ctx, "碳排相當於開車 25 公里", 430, 385, 22, (0.3, 0.3, 0.35))

            highlighter(ctx, 660, 350, 420, 75, (0.4, 0.8, 1.0, 0.45))
            text(ctx, "5,000 L 耗水", 870, 335, 52, (0.1, 0.45, 0.85))
            text(ctx, "相當於一人連續洗澡一個月", 870, 385, 22, (0.3, 0.3, 0.35))

        text(ctx, "紙張看似純白無暇，背後浸泡著驚人的高溫電力與水資源！", 640, 450, 26, (0.4, 0.4, 0.45))
        ctx.restore()

    if u > tw + 0.2:
        red_stamp(ctx, "高耗水耗能", 920, 270, ang=-0.16, s=1.1)

# 4 第一站：一包紙的製造旅程
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "01 造紙背後的重工業代價", 280, 80, size=24)
    th, te = ep.kw(4, "耗水大戶"), ep.kw(4, "大量能源")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 920, 400, ang=-0.01, bg=(0.97, 0.96, 0.92))
        text(ctx, "一張 A4 紙的排碳重污染旅程", 640, 210, 32, (0.15, 0.15, 0.2))

        steps = [("森林伐木", "原始林與原生木開採"),
                 ("化學漂白", "氯氣與高腐蝕蒸煮"),
                 ("高溫乾燥", "巨型煤炭燃氣鍋爐"),
                 ("全球運輸", "跨洋貨櫃柴油航運")]
        for k, (title, sub) in enumerate(steps):
            xx = 230 + k * 180
            rrect(ctx, xx - 80, 270, 160, 120, 16)
            ctx.set_source_rgb(0.92, 0.92, 0.95); ctx.fill_preserve()
            ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(3); ctx.stroke()
            text(ctx, title, xx, 315, 24, (0.1, 0.1, 0.12))
            text(ctx, sub, xx, 355, 14, (0.45, 0.45, 0.50))

        highlighter(ctx, 240, 455, 800, 40)
        text(ctx, "造紙業是全球排碳第五大工業，每一張紙都是高耗能產物！", 640, 450, 26, (0.85, 0.15, 0.15))
        ctx.restore()

# 5 百人企業的紙張巨坑
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "01 百人企業年度紙張消耗", 280, 80, size=24)
    t100, t50, t5t = ep.kw(5, "百人企業"), ep.kw(5, "五十萬張"), ep.kw(5, "五公噸")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 400, ang=0.015, bg=(0.96, 0.95, 0.91))
        text(ctx, "假設：每人每天列印 10 張（百人規模公司）", 640, 205, 30, (0.3, 0.3, 0.35))

        # 三大計數器
        stats = [("500,000 張", "年度總用紙量 (1,000包)", t50, (0.1, 0.1, 0.12)),
                 ("54 棵大樹", "相當於砍伐成年林木", t50 + 0.3, (0.35, 0.22, 0.14)),
                 ("5.4 噸 CO2e", "光是紙張產生的排碳", t5t, (0.85, 0.15, 0.15))]
        for k, (num, sub, t_, col) in enumerate(stats):
            xx = 260 + k * 255
            rrect(ctx, xx - 110, 265, 220, 130, 18)
            ctx.set_source_rgb(0.98, 0.98, 0.96); ctx.fill_preserve()
            ctx.set_source_rgb(*col); ctx.set_line_width(4); ctx.stroke()
            text(ctx, num, xx, 315, 32, col)
            text(ctx, sub, xx, 360, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 280, 455, 720, 45)
        text(ctx, "一年花掉十幾萬紙張預算，還背上五公噸碳負債！", 640, 450, 28, (0.85, 0.15, 0.15))
        ctx.restore()

# 6 第二站：碎紙機黑洞 (45% 當天進垃圾桶)
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "02 會議廢紙・印完即丟", 260, 80, size=24)
    t45, ts = ep.kw(6, "45%"), ep.kw(6, "碎紙機")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 380, 380, ang=-0.02, label="會議結束後的垃圾桶與碎紙機")
        shredder_machine(ctx, 330, 340, 1.0)
        red_pin(ctx, 330, 180)
        ctx.restore()

    q = prog(u, t45 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 350, q)
        torn_paper(ctx, 860, 350, 520, 360, ang=0.02, bg=(0.97, 0.96, 0.91))
        text(ctx, "辦公室文件生命週期調查", 860, 220, 30, (0.15, 0.15, 0.2))

        highlighter(ctx, 640, 310, 440, 60)
        text(ctx, "45% 的列印文件", 860, 300, 36, (0.85, 0.15, 0.15))
        text(ctx, "在列印當天傍晚就進了垃圾桶！", 860, 350, 24, (0.1, 0.1, 0.1))

        text(ctx, "「印了沒看、看了就丟、改一個錯字重印十份」", 860, 415, 20, (0.45, 0.45, 0.5))
        ctx.restore()

    if u > ts + 0.2:
        red_stamp(ctx, "短命廢紙", 930, 260, ang=-0.15, s=1.1)

# 7 第二站續：雷射印表機與碳粉匣
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "02 碳粉匣與加熱耗電", 260, 80, size=24)
    th, t3, tc = ep.kw(7, "高溫加熱"), ep.kw(7, "3 公斤"), ep.kw(7, "碳粉匣")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 400, 380, ang=0.02, label="黑色雷射碳粉匣")
        toner_cartridge(ctx, 330, 330, 1.2)
        red_pin(ctx, 330, 180)
        ctx.restore()

    q = prog(u, t3 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 350, q)
        torn_paper(ctx, 860, 350, 520, 360, ang=-0.02, bg=(0.96, 0.95, 0.90))
        text(ctx, "印表機隱形耗能清單", 860, 220, 30, (0.15, 0.15, 0.2))

        lines = [("碳粉匣原料與製造", "3.2 kg CO2e / 顆"),
                 ("雷射加熱定影滾筒耗電", "瞬間達 1,000 W"),
                 ("待機整天不關機", "年耗電 150 度")]
        for k, (lab, val) in enumerate(lines):
            text(ctx, lab, 720, 280 + k * 44, 22, (0.35, 0.35, 0.4), align='l')
            text(ctx, val, 1020, 280 + k * 44, 22, (0.85, 0.15, 0.15), align='r')

        highlighter(ctx, 640, 430, 440, 45)
        text(ctx, "「無紙化」口號下的高耗能假象！", 860, 425, 26, (0.85, 0.15, 0.15))
        ctx.restore()

# 8 第三站：真正的無紙化革命・電子簽章
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "03 無紙化革命・電子簽章", 280, 80, size=24)
    te, td = ep.kw(8, "電子簽章"), ep.kw(8, "數位轉型")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 920, 400, ang=-0.015, bg=(0.97, 0.96, 0.92))
        text(ctx, "假無紙化 vs 真無紙化", 640, 210, 34, (0.1, 0.1, 0.15))

        # 假無紙化 (紅框打叉)
        rrect(ctx, 220, 260, 380, 140, 16)
        ctx.set_source_rgb(0.98, 0.95, 0.95); ctx.fill_preserve()
        ctx.set_source_rgb(0.85, 0.2, 0.15); ctx.set_line_width(3); ctx.stroke()
        text(ctx, "× 假無紙化", 410, 300, 26, (0.85, 0.15, 0.15))
        text(ctx, "PDF 印出 → 人工手寫蓋章 → 掃描存檔", 410, 350, 18, (0.4, 0.4, 0.45))

        # 真無紙化 (綠框打勾)
        rrect(ctx, 680, 260, 380, 140, 16)
        ctx.set_source_rgb(0.95, 0.98, 0.95); ctx.fill_preserve()
        ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.set_line_width(3); ctx.stroke()
        text(ctx, "✓ 真無紙化：電子簽章", 870, 300, 26, (0.28, 0.62, 0.40))
        text(ctx, "符合電子簽章法，全程數位加密免列印！", 870, 350, 18, (0.4, 0.4, 0.45))

        highlighter(ctx, 260, 450, 760, 40)
        text(ctx, "導入合法電子簽章，才是徹底告別紙張的核心！", 640, 445, 28, (0.1, 0.1, 0.12))
        ctx.restore()

# 9 第三站續：線上協作與公文歸零
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "03 線上公文與平板開會", 280, 80, size=24)
    tp, to, tz = ep.kw(9, "平板投影"), ep.kw(9, "線上公文"), ep.kw(9, "瞬間歸零")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 400, ang=0.01, bg=(0.97, 0.96, 0.91))
        text(ctx, "現代辦公室三大零用紙神技", 640, 210, 32, (0.12, 0.12, 0.18))

        skills = [
            ("① 平板投影無紙會議", "雲端共享即時共筆，告別厚重簡報紙本", tp),
            ("② 手機一鍵線上簽核", "公文跑件時間從三天縮短至三分鐘", to),
            ("③ 雙面黑白預設列印", "強制設為出廠預設，直接減少 50% 誤印", tz)
        ]
        for k, (title, sub, t_) in enumerate(skills):
            yy = 265 + k * 55
            black_tape(ctx, title, 440, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            text(ctx, f"→ {sub}", 750, yy, 22, (0.28, 0.62, 0.40), align='l')

        highlighter(ctx, 320, 455, 640, 45)
        text(ctx, "既快、又省、又環保，用紙量瞬間歸零！", 640, 450, 30, (0.85, 0.15, 0.15))
        ctx.restore()

# 10 證物總盤點：紙張浪費年破 8 噸
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "EVIDENCE TOTAL TALLY 紙張證物總盤點", 640, 75, size=26)
    tc, t54, t8t = ep.kw(10, "證物盤點"), ep.kw(10, "5.4 噸"), ep.kw(10, "八公噸碳")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.97, 0.96, 0.91))
        text(ctx, "中小企業 (100人) 年度紙張排碳結算", 640, 195, 32, (0.12, 0.12, 0.18))

        rows = [("紙張製造與長途運輸排放", "5.4 噸 CO2e"),
                ("雷射印表機加熱與碳粉匣", "1.8 噸 CO2e"),
                ("碎紙清運與焚化掩埋處理", "0.8 噸 CO2e")]
        for k, (name, val) in enumerate(rows):
            yy = 260 + k * 45
            text(ctx, f"• {name}", 320, yy, 26, (0.25, 0.25, 0.3), align='l')
            text(ctx, val, 960, yy, 28, (0.85, 0.15, 0.15), align='r')

        ctx.move_to(300, 395); ctx.line_to(980, 395); ctx.set_source_rgb(0.65, 0.65, 0.70); ctx.set_line_width(3); ctx.stroke()

        highlighter(ctx, 320, 440, 640, 50)
        text(ctx, "年度總浪費：高達 8.0 噸 CO2e！", 640, 435, 34, (0.85, 0.15, 0.15))
        text(ctx, "等於平白燒掉 20 萬元紙張與碳粉預算！", 640, 495, 26, (0.3, 0.3, 0.35))
        ctx.restore()

    if u > t8t + 0.2:
        red_stamp(ctx, "證物確鑿", 930, 270, ang=-0.15, s=1.1)

# 11 結案報告：告別無紙化幽靈
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CASE CLOSED 結案報告", 640, 75, size=26)
    tc, te, td, tt = ep.kw(11, "結案報告"), ep.kw(11, "電子簽章"), ep.kw(11, "預設值"), ep.kw(11, "十噸碳排")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 900, 410, ang=-0.01, bg=(0.97, 0.96, 0.92))
        text(ctx, "徹底終結紙張浪費三大招", 640, 190, 34, (0.1, 0.1, 0.15))

        habits = [
            ("① 全面啟用電子簽章公文", "減用紙 80%", te),
            ("② 印表機雙面黑白預設鎖定", "減用紙 15%", td),
            ("③ 開會平板投影＋自備筆記本", "廢紙清零", tt - 0.3)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "每年為公司省數十萬預算、為地球省下十噸碳！", 640, 450, 32, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    if u > tt - 0.2:
        red_stamp(ctx, "結案 CLOSED", 950, 200, ang=-0.16, s=1.15)

# 執行
run("of2", "辦公室碳冒險 EP2",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP2_印表機裡的無紙化幽靈.mp4",
    wipes={2, 4, 6, 8, 10, 11})
