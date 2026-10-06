"""辦公室碳冒險：上班族的日常排碳帳本 (刑偵剪貼調查風格)"""
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
    """黑底圓角長條字幕，重點詞高亮黃色（完全還原參考影片）"""
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(32)
    ext = ctx.text_extents(s)
    w = ext.width
    rrect(ctx, 640 - w / 2 - 28, 648, w + 56, 52, 14)
    ctx.set_source_rgba(0.08, 0.08, 0.10, 0.94); ctx.fill()

    # 文字繪製，支援關鍵字高亮
    highlights = ["十公斤", "4.5 度", "兩公斤", "五公斤", "0.55 公斤", "2.8 公斤", "50 克", "150 克", "兩百公斤", "一噸碳", "案發現場", "隱形排碳怪獸"]
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
        # 前段白字
        if parts[0]:
            text(ctx, parts[0], start_x + w0 / 2, 674, 32, C['white'])
        # 高亮黃字
        text(ctx, found_hl, start_x + w0 + wh / 2, 674, 32, (1.0, 0.88, 0.20))
        # 後段白字
        if parts[1]:
            w1 = ctx.text_extents(parts[1]).x_advance
            text(ctx, parts[1], start_x + w0 + wh + w1 / 2, 674, 32, C['white'])

engine.subtitle = custom_sub

# ==================== 場景定義 ====================

# 0 開場：案發現場檔案
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    t9, tc, tn = ep.kw(0, "九點"), ep.kw(0, "吹冷氣"), ep.kw(0, "毫無關係")
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #001 絕密調查檔案", 640, 160, size=28)
        text(ctx, "辦公室碳冒險", 640, 245, 60, (0.12, 0.12, 0.15))
        text(ctx, "上班族的日常排碳帳本", 640, 310, 32, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        # 打字機內文
        items = ["案發現場：辦公室工位 (九點打卡)", "日常習慣：全天冷氣、外帶拿鐵、午餐外送", "嫌疑目標：究竟是誰偷走了地球的碳預算？"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    # 蓋下大紅印章「案發現場」 (蓋在檔案右上方)
    q = prog(u, tn - 0.3, 0.35)
    if q > 0:
        ctx.save(); pop(ctx, 920, 220, q)
        red_stamp(ctx, "案發現場", 920, 220, ang=-0.18, s=1.1)
        ctx.restore()

# 1 案件大綱：三條線索板
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CLUES INVESTIGATION BOARD 線索板", 640, 75, size=26)
    t1, t2, t3 = ep.kw(1, "隱形電氣怪獸"), ep.kw(1, "一杯拿鐵"), ep.kw(1, "數位碳足跡")

    # 三張拍立得證物
    cards = [
        (t1, 260, 340, -0.04, "01 電氣怪獸", office_ac),
        (t2, 640, 330, 0.03, "02 外送飲食", latte_cup),
        (t3, 1020, 345, -0.03, "03 數位足跡", server_rack)
    ]
    pins = []
    for t0, xx, yy, ang, lab, draw_fn in cards:
        p = prog(u, t0 - 0.3, 0.45)
        if p > 0:
            ctx.save(); pop(ctx, xx, yy, p)
            polaroid(ctx, xx, yy, 260, 320, ang=ang, label=lab)
            ctx.save(); ctx.translate(xx, yy - 20); ctx.rotate(ang)
            draw_fn(ctx, 0, 0, 0.75)
            ctx.restore()
            red_pin(ctx, xx, yy - 145)
            ctx.restore()
        pins.append((xx, yy - 145))

    # 連接紅線
    if u > t2 - 0.1:
        red_string(ctx, pins[0][0], pins[0][1], pins[1][0], pins[1][1], sag=35, p=prog(u, t2 - 0.1, 0.4))
    if u > t3 - 0.1:
        red_string(ctx, pins[1][0], pins[1][1], pins[2][0], pins[2][1], sag=35, p=prog(u, t3 - 0.1, 0.4))

# 2 上班族自白書
def s2(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SUSPECT'S CONFESSION 上班族自白", 380, 85, size=24)
    tf, ts, tq = ep.kw(2, "沒開工廠"), ep.kw(2, "沒煙囪"), ep.kw(2, "能排多少碳")

    # 左側：工位證物照片 (辦公桌＋電腦＋咖啡)
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 380, 380, ang=-0.03, label="證物A：辦公室標準工位")
        ctx.save(); ctx.translate(330, 330); ctx.rotate(-0.03)
        office_pc(ctx, -60, 0, 0.9, on=True)
        latte_cup(ctx, 80, 35, 0.8)
        ctx.restore()
        red_pin(ctx, 330, 180)
        # 手繪紅圈
        if u > ts:
            red_circle(ctx, 330, 320, 130, 95, -0.05)
        ctx.restore()

    # 右側：自白便條
    q = prog(u, tf - 0.2, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 850, 350, q)
        torn_paper(ctx, 850, 350, 480, 340, ang=0.03, bg=(0.97, 0.96, 0.92))
        text(ctx, "上班族問訊筆錄", 850, 240, 32, (0.15, 0.15, 0.2))
        text(ctx, "「我只是個普通上班族，", 850, 305, 26, (0.3, 0.3, 0.35))
        text(ctx, "沒工廠、沒煙囪，", 850, 345, 26, (0.3, 0.3, 0.35))
        text(ctx, "每天吹冷氣打鍵盤，能排多少碳？」", 850, 385, 24, (0.3, 0.3, 0.35))
        ctx.restore()

    # 大黑粗體打在畫面上「普通人？」(完全還原參考影片 f_001.png)
    k = prog(u, tq - 0.2, 0.35)
    if k > 0:
        ctx.save(); pop(ctx, 850, 470, k)
        ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(68)
        ctx.move_to(850 - 150, 490)
        ctx.set_source_rgb(0.9, 0.15, 0.15); ctx.show_text("普通人？")
        ctx.restore()

# 3 震撼調查結果：單日十公斤！
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "INVESTIGATION VERDICT 調查結論", 640, 85, size=26)
    td, t10 = ep.kw(3, "度過一天"), ep.kw(3, "十公斤")

    # 中央巨大證物夾板
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 860, 400, ang=0.01, bg=(0.97, 0.96, 0.90))
        text(ctx, "一位標準白領上班族・單日碳排帳本", 640, 210, 32, (0.3, 0.3, 0.35))

        # 巨大衝擊性數字 10 kg
        q = prog(u, t10 - 0.3, 0.45)
        if q > 0:
            # 螢光筆塗抹底色
            highlighter(ctx, 360, 360, 560, 80, (1.0, 0.88, 0.20, 0.6))
            ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            ctx.set_font_size(110)
            ctx.move_to(400, 370)
            ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.show_text("10")
            ctx.set_font_size(54); ctx.move_to(560, 360)
            ctx.set_source_rgb(0.85, 0.2, 0.15); ctx.show_text("kg CO2e / 天")

        text(ctx, "相當於燃燒 5 公斤燃煤、或小客車行駛 50 公里！", 640, 440, 26, (0.4, 0.4, 0.45))
        ctx.restore()

    # 蓋下大紅印章「高耗能警戒」
    if u > t10 + 0.2:
        red_stamp(ctx, "高耗能警戒", 900, 270, ang=-0.18, s=1.15)

# 4 第一站：隱形怪獸・空調
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "01 隱形怪獸・中央空調", 260, 80, size=24)
    tc, t45, t2 = ep.kw(4, "吃電巨獸"), ep.kw(4, "4.5"), ep.kw(4, "超過兩公斤")

    # 左側：拍立得照片 (19度冷氣出風口)
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 400, 380, ang=-0.02, label="辦公室常年維持 19°C–21°C")
        ctx.save(); ctx.translate(330, 310); ctx.rotate(-0.02)
        office_ac(ctx, 0, 0, 1.0, cold=True)
        ctx.restore()
        red_pin(ctx, 330, 180)
        red_stamp(ctx, "吃電之王", 440, 250, ang=-0.15, s=0.9)
        ctx.restore()

    # 右側：電費與碳排數據撕紙
    q = prog(u, t45 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 350, q)
        torn_paper(ctx, 860, 350, 520, 360, ang=0.02, bg=(0.96, 0.95, 0.91))
        text(ctx, "中央空調・人均耗能分攤", 860, 220, 30, (0.15, 0.15, 0.2))

        # 4.5 度大字＋螢光筆
        highlighter(ctx, 640, 305, 440, 50)
        text(ctx, "單人每日耗電：4.5 度", 860, 295, 34, (0.1, 0.1, 0.1))

        # 計算公式
        text(ctx, "4.5 度 × 0.466 kg/度", 860, 365, 28, (0.4, 0.4, 0.45))
        text(ctx, "＝ 2.1 kg CO2e / 每天", 860, 420, 36, (0.85, 0.15, 0.15))
        ctx.restore()

# 5 第一站續：其他電氣與伺服器
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "01 隱形怪獸・徹夜耗電", 260, 80, size=24)
    tp, tl, ts, t5 = ep.kw(5, "主機螢幕"), ep.kw(5, "走廊常亮"), ep.kw(5, "伺服器"), ep.kw(5, "五公斤")

    # 三張橫列證物便條
    items = [
        (tp, 260, "電腦主機不關", "+0.8 kg", office_pc),
        (tl, 640, "照明走廊長明燈", "+0.6 kg", None),
        (ts, 1020, "機房伺服器運轉", "+1.2 kg", server_rack)
    ]
    for t0, xx, lab, val, draw_fn in items:
        p = prog(u, t0 - 0.3, 0.45)
        if p > 0:
            ctx.save(); pop(ctx, xx, 310, p)
            polaroid(ctx, xx, 310, 280, 300, ang=0.015 * (1 if xx > 500 else -1), label=lab)
            if draw_fn:
                ctx.save(); ctx.translate(xx, 280)
                draw_fn(ctx, 0, 0, 0.65)
                ctx.restore()
            else:
                ctx.arc(xx, 280, 45, 0, 2 * math.pi); ctx.set_source_rgb(1.0, 0.85, 0.2); ctx.fill()
                text(ctx, "24hr ON", xx, 285, 22, (0.2, 0.2, 0.2))
            red_pin(ctx, xx, 175)
            # 數值標籤
            black_tape(ctx, val, xx, 420, size=22, bg=(0.85, 0.15, 0.15))
            ctx.restore()

    # 底部總計長條
    q = prog(u, t5 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 640, 560, q)
        torn_paper(ctx, 640, 560, 880, 90, bg=(0.98, 0.98, 0.95))
        highlighter(ctx, 240, 560, 800, 40)
        text(ctx, "辦公室純電力人均排碳：4.5 kg CO2e / 天！", 640, 560, 32, (0.1, 0.1, 0.12))
        ctx.restore()

# 6 第二站：外送帳本・鮮奶拿鐵
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "02 外送帳本・晨間拿鐵", 260, 80, size=24)
    tl, tcow, t055 = ep.kw(6, "一杯拿鐵"), ep.kw(6, "乳牛養殖"), ep.kw(6, "0.55")

    # 左側：拿鐵杯照片
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 380, 380, ang=-0.03, label="外帶特大杯鮮奶拿鐵")
        ctx.save(); ctx.translate(330, 330); ctx.rotate(-0.03)
        latte_cup(ctx, 0, 0, 1.1)
        ctx.restore()
        red_pin(ctx, 330, 180)
        if u > tcow:
            red_circle(ctx, 330, 340, 70, 70)
        ctx.restore()

    # 右側：碳足跡解構單
    q = prog(u, t055 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 350, q)
        torn_paper(ctx, 860, 350, 520, 360, ang=0.02, bg=(0.97, 0.96, 0.91))
        text(ctx, "一杯拿鐵的碳成本", 860, 220, 30, (0.15, 0.15, 0.2))

        # 0.55 kg 大字
        highlighter(ctx, 630, 300, 460, 50)
        text(ctx, "單杯排碳：0.55 kg CO2e", 860, 290, 32, (0.1, 0.1, 0.1))

        text(ctx, "主要來源：80% 來自鮮奶養殖 (甲烷)", 860, 360, 24, (0.4, 0.4, 0.45))
        text(ctx, "（黑咖啡只有 0.05 kg，差距達 10 倍！）", 860, 410, 22, (0.85, 0.15, 0.15))
        ctx.restore()

# 7 第二站續：外送便當
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "02 外送帳本・排骨便當", 260, 80, size=24)
    tb, tc, t28 = ep.kw(7, "外送排骨便當"), ep.kw(7, "淋膜紙盒"), ep.kw(7, "2.8 公斤")

    # 左側：便當盒照片
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 330, 350, p)
        polaroid(ctx, 330, 350, 400, 380, ang=0.03, label="排骨便當＋淋膜紙盒＋免洗筷")
        ctx.save(); ctx.translate(330, 320); ctx.rotate(0.03)
        bento_box(ctx, 0, 0, 1.1)
        ctx.restore()
        red_pin(ctx, 330, 180)
        red_stamp(ctx, "重度包裝", 450, 260, ang=-0.14, s=0.9)
        ctx.restore()

    # 右側：外送明細帳單
    q = prog(u, t28 - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 860, 350, q)
        torn_paper(ctx, 860, 350, 520, 360, ang=-0.02, bg=(0.96, 0.95, 0.90))
        text(ctx, "外送午餐細部帳本", 860, 220, 30, (0.15, 0.15, 0.2))

        lines = [("炸排骨肉品食材", "1.8 kg"),
                 ("一次性淋膜盒與餐具", "0.4 kg"),
                 ("外送機車里程排放", "0.6 kg")]
        for k, (lab, val) in enumerate(lines):
            text(ctx, lab, 720, 275 + k * 42, 22, (0.35, 0.35, 0.4), align='l')
            text(ctx, val, 1020, 275 + k * 42, 24, (0.2, 0.2, 0.2), align='r')

        ctx.move_to(650, 400); ctx.line_to(1070, 400); ctx.set_source_rgb(0.7, 0.7, 0.7); ctx.set_line_width(2); ctx.stroke()
        highlighter(ctx, 640, 435, 440, 45)
        text(ctx, "一頓外送合計：2.8 kg CO2e", 860, 430, 28, (0.85, 0.15, 0.15))
        ctx.restore()

# 8 第三站：數位碳足跡・雲端
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "03 數位足跡・雲端機房", 260, 80, size=24)
    td, tz, tc, tr = ep.kw(8, "數位減碳"), ep.kw(8, "零碳排"), ep.kw(8, "雲端資料中心"), ep.kw(8, "日夜運轉")

    # 巨大報紙剪貼
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 920, 400, ang=-0.015, bg=(0.97, 0.96, 0.92))
        black_tape(ctx, "SPECIAL INVESTIGATION 深度調查", 640, 195, size=22)
        text(ctx, "無紙化真的是「零碳排」嗎？", 640, 260, 38, (0.1, 0.1, 0.15))

        highlighter(ctx, 240, 335, 800, 45)
        text(ctx, "「雲端不是飄在天上，它住在耗電的機房裡。」", 640, 330, 30, (0.2, 0.2, 0.25))

        text(ctx, "全球資料中心耗電量已超過多數中型國家總和，", 640, 405, 24, (0.4, 0.4, 0.45))
        text(ctx, "背後依靠龐大的電力網與冷卻系統 24 小時無休運轉！", 640, 445, 24, (0.4, 0.4, 0.45))
        red_pin(ctx, 200, 170); red_pin(ctx, 1080, 170)
        ctx.restore()

# 9 第三站續：垃圾郵件與視訊
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "03 數位足跡・實測數據", 260, 80, size=24)
    tm, t50, tv, t150 = ep.kw(9, "垃圾郵件"), ep.kw(9, "50 克"), ep.kw(9, "視訊會議"), ep.kw(9, "150 克")

    # 左側：陳年垃圾郵件
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 360, 350, p)
        polaroid(ctx, 360, 350, 380, 380, ang=-0.02, label="未清垃圾郵件 (帶附件)")
        ctx.save(); ctx.translate(360, 310); ctx.rotate(-0.02)
        email_inbox(ctx, 0, 0, 1.2, count="9999+")
        ctx.restore()
        red_pin(ctx, 360, 180)
        # 標籤
        black_tape(ctx, "50 g / 封 / 年", 360, 430, size=24, bg=(0.85, 0.15, 0.15))
        ctx.restore()

    # 右側：視訊會議高畫質
    q = prog(u, tv - 0.3, 0.45)
    if q > 0:
        ctx.save(); pop(ctx, 880, 350, q)
        torn_paper(ctx, 880, 350, 480, 360, ang=0.02, bg=(0.96, 0.95, 0.90))
        text(ctx, "高畫質視訊 (1 小時)", 880, 230, 28, (0.15, 0.15, 0.2))

        highlighter(ctx, 680, 300, 400, 45)
        text(ctx, "排放：150 g CO2e", 880, 290, 32, (0.85, 0.15, 0.15))

        text(ctx, "建議行動：", 720, 360, 24, (0.2, 0.2, 0.2), align='l')
        text(ctx, "• 降低至 720p 節省 80% 傳輸", 720, 400, 20, (0.4, 0.4, 0.45), align='l')
        text(ctx, "• 不必要時關閉視訊鏡頭", 720, 435, 20, (0.4, 0.4, 0.45), align='l')
        ctx.restore()

# 10 證物總盤點：單日十公斤！
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "EVIDENCE TOTAL TALLY 證物總盤點", 640, 75, size=26)
    tc, t45, t33, t22, t10, t200 = ep.kw(10, "證物盤點"), ep.kw(10, "4.5"), ep.kw(10, "3.3"), ep.kw(10, "2.2"), ep.kw(10, "破十公斤"), ep.kw(10, "兩百公斤")

    # 大張總結清單
    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.97, 0.96, 0.91))
        text(ctx, "白領上班族・單日碳排總結算", 640, 195, 32, (0.12, 0.12, 0.18))

        rows = [("空調與常亮電氣設備", "4.5 kg", t45),
                ("外帶拿鐵與外送午餐", "3.3 kg", t33),
                ("數位伺服器與用紙耗能", "2.2 kg", t22)]
        for k, (name, val, t_) in enumerate(rows):
            yy = 260 + k * 45
            text(ctx, f"• {name}", 320, yy, 26, (0.25, 0.25, 0.3), align='l')
            text(ctx, val, 960, yy, 28, (0.85, 0.15, 0.15), align='r')

        ctx.move_to(300, 395); ctx.line_to(980, 395); ctx.set_source_rgb(0.65, 0.65, 0.70); ctx.set_line_width(3); ctx.stroke()

        # 合計 10 kg
        highlighter(ctx, 320, 440, 640, 50)
        text(ctx, "單日總排碳量：10.0 kg CO2e / 人！", 640, 435, 34, (0.1, 0.1, 0.12))
        text(ctx, "單月 20 個工作天累積：整整 200 kg！", 640, 495, 26, (0.85, 0.15, 0.15))
        ctx.restore()

    if u > t10 + 0.2:
        red_stamp(ctx, "證物確鑿", 930, 270, ang=-0.15, s=1.1)

# 11 結案報告：三大防怪獸習慣
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CASE CLOSED 結案報告", 640, 75, size=26)
    tc, t1, tbox, tmail, ton = ep.kw(11, "結案報告"), ep.kw(11, "調高一度"), ep.kw(11, "自備環保餐盒"), ep.kw(11, "清空垃圾郵件"), ep.kw(11, "省下一噸碳")

    p = prog(u, 0.2, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 900, 410, ang=-0.01, bg=(0.97, 0.96, 0.92))
        text(ctx, "辦公室防怪獸三大對策", 640, 190, 34, (0.1, 0.1, 0.15))

        habits = [
            ("① 空調設定 26°C ＋ 下班隨手關機", "立減 1.5 kg / 天", t1),
            ("② 自備環保餐盒 ＋ 改喝燕麥奶拿鐵", "立減 1.8 kg / 天", tbox),
            ("③ 定期清空垃圾信 ＋ 視訊調降 720p", "立減 0.3 kg / 天", tmail)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        # 最終大 banner
        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "每位上班族一年可為地球省下：1 噸碳！", 640, 450, 34, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    # 結案大印章 (蓋在右上角空白處，不遮擋文字)
    if u > ton - 0.2:
        red_stamp(ctx, "結案 CLOSED", 950, 200, ang=-0.16, s=1.15)

# 執行
run("of1", "辦公室碳冒險 EP1",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP1_上班族的日常排碳帳本.mp4",
    wipes={2, 4, 6, 8, 10, 11})
