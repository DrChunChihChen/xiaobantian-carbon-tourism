"""辦公室碳冒險：CASE #003 通勤大搜查：遠距上班真的比較環保嗎？ (刑偵剪貼調查風格)"""
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

    highlights = [
        "170 克", "55 克", "30 克", "兩公噸", "四成", "2,500 公斤", "800 公斤", "400 公斤",
        "大眾運輸", "遠距工作", "冰水主機", "老舊冷氣", "通勤月票", "碳預算", "不減反增"
    ]
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

def car_sedan(ctx, x, y, s=1.0):
    """自用小客車 (單人駕駛，朝右行駛，左後底排氣)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.new_path()
    # 地面落影
    ctx.save(); ctx.translate(0, 38); ctx.scale(1, 0.2)
    ctx.arc(0, 0, 75, 0, math.pi * 2); ctx.set_source_rgba(0, 0, 0, 0.25); ctx.fill(); ctx.restore()

    # 排氣管 (車尾底部左側)
    ctx.rectangle(-76, 18, 10, 5); ctx.set_source_rgb(0.4, 0.42, 0.45); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(1.5); ctx.stroke()
    # 排氣煙霧 (往後方散逸)
    puffs = [(-86, 19, 6, 0.45), (-100, 16, 9, 0.35), (-118, 10, 13, 0.22)]
    for px, py, pr, pa in puffs:
        ctx.new_path()
        ctx.arc(px, py, pr, 0, math.pi * 2); ctx.set_source_rgba(0.55, 0.58, 0.62, pa); ctx.fill()

    # 車身本體 (紅色) - 車頭在右(x>0), 車尾在左(x<0)
    ctx.new_path()
    ctx.move_to(-72, 22); ctx.line_to(-72, 2); ctx.line_to(-52, 2); ctx.line_to(-32, -28)
    ctx.line_to(16, -28); ctx.line_to(38, 2); ctx.line_to(70, 4); ctx.line_to(72, 22); ctx.line_to(58, 22)
    ctx.arc_negative(42, 22, 16, 0, math.pi); ctx.line_to(-26, 22)
    ctx.arc_negative(-42, 22, 16, 0, math.pi); ctx.close_path()
    ctx.set_source_rgb(0.88, 0.22, 0.20); ctx.fill_preserve()
    ctx.set_source_rgb(0.25, 0.10, 0.10); ctx.set_line_width(3.5); ctx.stroke()

    # 車窗 (前後兩扇)
    ctx.new_path(); ctx.move_to(-46, 0); ctx.line_to(-28, -24); ctx.line_to(-6, -24); ctx.line_to(-6, 0); ctx.close_path()
    ctx.set_source_rgb(0.35, 0.72, 0.90); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()

    ctx.new_path(); ctx.move_to(-2, 0); ctx.line_to(-2, -24); ctx.line_to(14, -24); ctx.line_to(32, 0); ctx.close_path()
    ctx.set_source_rgb(0.35, 0.72, 0.90); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()

    # 車門分界與門把
    ctx.new_path(); ctx.move_to(-4, 0); ctx.line_to(-4, 21); ctx.set_source_rgb(0.25, 0.1, 0.1); ctx.set_line_width(2); ctx.stroke()
    ctx.rectangle(-18, 5, 8, 3); ctx.set_source_rgb(0.2, 0.1, 0.1); ctx.fill()
    ctx.rectangle(6, 5, 8, 3); ctx.set_source_rgb(0.2, 0.1, 0.1); ctx.fill()

    # 車尾燈 (左側紅色)
    ctx.rectangle(-72, 4, 4, 7); ctx.set_source_rgb(0.95, 0.15, 0.1); ctx.fill()
    # 車頭大燈 (右側亮黃)
    ctx.new_path(); ctx.arc(70, 8, 4, -math.pi/2, math.pi/2); ctx.set_source_rgb(1.0, 0.92, 0.3); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.2, 0.1); ctx.set_line_width(1.5); ctx.stroke()

    # 前後車輪
    for wx in (-42, 42):
        ctx.new_path(); ctx.arc(wx, 22, 14, 0, math.pi * 2)
        ctx.set_source_rgb(0.2, 0.22, 0.25); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()
        ctx.new_path(); ctx.arc(wx, 22, 7, 0, math.pi * 2)
        ctx.set_source_rgb(0.8, 0.82, 0.85); ctx.fill_preserve()
        ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(1.5); ctx.stroke()
    ctx.new_path()
    ctx.restore()

def scooter_bike(ctx, x, y, s=1.0):
    """速克達機車 (朝右行駛，踏板斜板坐墊排氣)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.new_path()
    # 地面落影
    ctx.save(); ctx.translate(0, 38); ctx.scale(1, 0.22)
    ctx.arc(0, 0, 60, 0, math.pi * 2); ctx.set_source_rgba(0, 0, 0, 0.25); ctx.fill(); ctx.restore()

    # 排氣管 (車尾底部左側)
    ctx.rectangle(-46, 18, 26, 6)
    ctx.set_source_rgb(0.3, 0.32, 0.35); ctx.fill_preserve()
    ctx.set_source_rgb(0.15, 0.15, 0.15); ctx.set_line_width(1.5); ctx.stroke()
    for i, ex in enumerate([-54, -64]):
        ctx.new_path()
        ctx.arc(ex, 19 - i * 3, 4 + i * 2, 0, math.pi * 2)
        ctx.set_source_rgba(0.55, 0.58, 0.62, 0.35 - i * 0.1); ctx.fill()

    # 前後車輪
    for wx in (-36, 36):
        ctx.new_path(); ctx.arc(wx, 22, 14, 0, math.pi * 2)
        ctx.set_source_rgb(0.2, 0.22, 0.25); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()
        ctx.new_path(); ctx.arc(wx, 22, 7, 0, math.pi * 2)
        ctx.set_source_rgb(0.8, 0.82, 0.85); ctx.fill_preserve()
        ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(1.5); ctx.stroke()

    # 機車車身主體 (亮黃/暖橘)
    ctx.new_path()
    ctx.move_to(-46, 16); ctx.curve_to(-48, 2, -40, -4, -26, -4); ctx.line_to(-6, -4)
    ctx.line_to(-6, 14); ctx.line_to(16, 14); ctx.line_to(22, 0); ctx.line_to(32, -22)
    ctx.line_to(26, -22); ctx.line_to(14, 10); ctx.line_to(-8, 10); ctx.line_to(-8, 16)
    ctx.close_path()
    ctx.set_source_rgb(0.96, 0.65, 0.12); ctx.fill_preserve()
    ctx.set_source_rgb(0.22, 0.15, 0.08); ctx.set_line_width(3); ctx.stroke()

    # 前叉
    ctx.new_path(); ctx.move_to(36, 22); ctx.line_to(28, -18)
    ctx.set_source_rgb(0.22, 0.22, 0.25); ctx.set_line_width(3); ctx.stroke()

    # 斜板高光面
    ctx.new_path(); ctx.move_to(20, 10); ctx.line_to(34, -20); ctx.line_to(31, -26); ctx.line_to(16, 12); ctx.close_path()
    ctx.set_source_rgb(0.98, 0.75, 0.20); ctx.fill_preserve()
    ctx.set_source_rgb(0.22, 0.15, 0.08); ctx.set_line_width(2.5); ctx.stroke()

    # 黑色坐墊
    ctx.new_path(); ctx.move_to(-44, -4); ctx.curve_to(-42, -14, -30, -14, -5, -12); ctx.line_to(-4, -4); ctx.close_path()
    ctx.set_source_rgb(0.18, 0.18, 0.20); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()

    # 龍頭手把與後照鏡
    ctx.new_path(); ctx.move_to(27, -24); ctx.line_to(20, -32); ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(3); ctx.stroke()
    ctx.new_path(); ctx.move_to(16, -33); ctx.line_to(24, -31); ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.set_line_width(4); ctx.stroke()
    ctx.new_path(); ctx.move_to(22, -32); ctx.line_to(18, -40); ctx.set_source_rgb(0.4, 0.4, 0.4); ctx.set_line_width(2); ctx.stroke()
    ctx.new_path(); ctx.arc(18, -41, 3.5, 0, math.pi * 2); ctx.set_source_rgb(0.85, 0.9, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(1.5); ctx.stroke()

    # 前大燈 (圓形亮黃)
    ctx.new_path(); ctx.arc(33, -16, 4.5, -math.pi/2, math.pi/2); ctx.set_source_rgb(1.0, 0.92, 0.3); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.2, 0.1); ctx.set_line_width(1.5); ctx.stroke()

    # 車尾燈 (紅色小方塊)
    ctx.rectangle(-46, 2, 3, 6); ctx.set_source_rgb(0.95, 0.15, 0.1); ctx.fill()

    ctx.new_path()
    ctx.restore()

def mrt_train(ctx, x, y, s=1.0):
    """捷運/電聯車廂"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    ctx.new_path()
    # 地面落影
    ctx.save(); ctx.translate(0, 48); ctx.scale(1, 0.2)
    ctx.arc(0, 0, 85, 0, math.pi * 2); ctx.set_source_rgba(0, 0, 0, 0.25); ctx.fill(); ctx.restore()

    # 車體長方
    rrect(ctx, -80, -40, 160, 70, 8)
    ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.25, 0.3); ctx.set_line_width(4); ctx.stroke()
    # 捷運彩條 (藍/綠)
    ctx.rectangle(-80, 5, 160, 12); ctx.set_source_rgb(0.1, 0.6, 0.8); ctx.fill()
    # 車窗
    for wx in (-55, -20, 15, 50):
        ctx.rectangle(wx, -25, 22, 22); ctx.set_source_rgb(0.2, 0.3, 0.45); ctx.fill()
    # 車輪底盤
    for wx in (-50, 50):
        ctx.arc(wx, 36, 10, 0, math.pi * 2); ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.fill()
    ctx.new_path()
    ctx.restore()

def home_ac_unit(ctx, x, y, s=1.0):
    """居家分離式冷氣室內機"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    rrect(ctx, -75, -30, 150, 60, 6)
    ctx.set_source_rgb(0.97, 0.97, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.25, 0.25, 0.28); ctx.set_line_width(3); ctx.stroke()
    # 出風口
    ctx.rectangle(-65, 12, 130, 10); ctx.set_source_rgb(0.82, 0.85, 0.88); ctx.fill()
    # 吹出的冷風波浪
    for k in range(3):
        ctx.move_to(-40 + k * 35, 25)
        ctx.curve_to(-35 + k * 35, 45, -50 + k * 35, 60, -45 + k * 35, 80)
        ctx.set_source_rgba(0.3, 0.7, 0.95, 0.5); ctx.set_line_width(3); ctx.stroke()
    # 溫度顯示
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(14); ctx.move_to(35, -5); ctx.set_source_rgb(0.2, 0.8, 0.3); ctx.show_text("20°C")
    ctx.restore()

def chiller_plant(ctx, x, y, s=1.0):
    """中央空調冰水主機 / 機房"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 工業冷卻機櫃
    rrect(ctx, -75, -50, 150, 100, 4)
    ctx.set_source_rgb(0.3, 0.4, 0.45); ctx.fill_preserve()
    ctx.set_source_rgb(0.15, 0.2, 0.25); ctx.set_line_width(4); ctx.stroke()
    # 冷卻管道
    ctx.move_to(-75, -25); ctx.line_to(-95, -25); ctx.line_to(-95, 25); ctx.line_to(-75, 25)
    ctx.set_source_rgb(0.2, 0.6, 0.8); ctx.set_line_width(8); ctx.stroke()
    # 散熱風扇柵格
    for row in range(3):
        ctx.rectangle(-55, -35 + row * 26, 110, 18); ctx.set_source_rgb(0.18, 0.24, 0.28); ctx.fill()
    # 效率標籤
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12); ctx.move_to(-40, 40); ctx.set_source_rgb(0.2, 0.9, 0.4); ctx.show_text("HIGH COP 6.5")
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #003 上班族通勤大搜查", 640, 160, size=28)
        text(ctx, "每天清晨七點半的浩大遷徙", 560, 245, 46, (0.12, 0.12, 0.15))
        text(ctx, "擠捷運、催油門、塞公路，到底排了多少碳？", 640, 310, 30, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        items = ["案發現場：尖峰時段的高速公路與雙北捷運站", "核心謎團：遠距工作真的等於『零排碳』拯救地球嗎？", "驚人落差：不同通勤方式，年碳排竟相差高達十倍！"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "立案調查", 960, 185, ang=-0.14, s=1.05)

# 1 三條調查線索
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THREE CLUES 通勤調查線索板", 640, 75, size=26)
    t1, t2, t3 = ep.kw(1, "交通工具"), ep.kw(1, "塞車"), ep.kw(1, "居家遠距")

    cards = [
        (t1, 260, 340, -0.04, "01 工具碳排懸殊", car_sedan),
        (t2, 640, 330, 0.03, "02 塞車隱形消耗", None),
        (t3, 1020, 345, -0.03, "03 居家空調盲區", home_ac_unit)
    ]
    pins = []
    for t_in, cx, cy, ang, title, drawer in cards:
        p = prog(u, t_in, 0.4)
        if p > 0:
            ctx.save(); pop(ctx, cx, cy, p)
            polaroid(ctx, cx, cy, 320, 360, ang, title)
            if drawer:
                drawer(ctx, cx, cy - 30, 0.85)
            elif title == "02 塞車隱形消耗":
                # 塞車紅綠燈圖示
                rrect(ctx, cx - 25, cy - 80, 50, 100, 10)
                ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.fill()
                for i, col in enumerate([(0.9, 0.2, 0.2), (0.9, 0.7, 0.1), (0.2, 0.8, 0.3)]):
                    ctx.arc(cx, cy - 55 + i * 28, 10, 0, math.pi * 2)
                    ctx.set_source_rgb(*col); ctx.fill()
            red_pin(ctx, cx, cy - 165)
            pins.append((cx, cy - 165))
            ctx.restore()

    if len(pins) >= 2:
        red_string(ctx, pins[0][0], pins[0][1], pins[1][0], pins[1][1], sag=18)
    if len(pins) >= 3:
        red_string(ctx, pins[1][0], pins[1][1], pins[2][0], pins[2][1], sag=-15)

# 2 迷思審訊
def s2(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "INTERROGATION 迷思審訊", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 840, 380, ang=0.012, bg=(0.98, 0.96, 0.92))
        text(ctx, "直覺迷思：居家上班＝零碳排？", 500, 210, 32, (0.85, 0.18, 0.15))
        text(ctx, "『不用搭車出門，企業碳排直接歸零，地球得救了？』", 640, 275, 28, (0.3, 0.3, 0.35))

        # 居家筆電圖示
        rrect(ctx, 640 - 70, 320, 140, 90, 8); ctx.set_source_rgb(0.85, 0.88, 0.92); ctx.fill()
        ctx.rectangle(640 - 60, 330, 120, 70); ctx.set_source_rgb(0.2, 0.25, 0.3); ctx.fill()
        ctx.rectangle(640 - 90, 410, 180, 14); ctx.set_source_rgb(0.7, 0.73, 0.78); ctx.fill()

        highlighter(ctx, 280, 445, 720, 45)
        text(ctx, "調查局警告：魔鬼藏在看不見的能源轉換效率裡！", 640, 440, 26, (0.2, 0.2, 0.25))
        red_pin(ctx, 250, 180); red_pin(ctx, 1030, 180)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "疑點重重", 970, 210, ang=-0.16, s=1.0)

# 3 真相揭曉：冷氣大陷阱
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THE TWIST 調查大逆轉", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "夏日老舊冷氣大陷阱", 480, 195, 32, (0.85, 0.15, 0.15))

        # 對比卡
        rrect(ctx, 230, 240, 380, 190, 12); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        text(ctx, "🏢 辦公室中央空調", 420, 270, 24, (0.15, 0.5, 0.25))
        text(ctx, "高效率冰水主機 + 數百人共享", 420, 310, 20, (0.3, 0.35, 0.35))
        chip(ctx, "每人每小時 0.15 度", 420, 360, 1, C['green'], 22, C['white'])

        rrect(ctx, 670, 240, 380, 190, 12); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🏠 居家單獨吹冷氣", 860, 270, 24, (0.85, 0.2, 0.2))
        text(ctx, "老舊三級能效窗型/分離式", 860, 310, 20, (0.35, 0.3, 0.3))
        chip(ctx, "每人每小時 0.9~1.2 度", 860, 360, 1, C['red'], 22, C['white'])

        highlighter(ctx, 240, 465, 800, 48)
        text(ctx, "在家吹整天老舊冷氣，排碳量反而高出整整四成！", 640, 460, 30, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "排碳反增 40%", 970, 190, ang=-0.12, s=0.95)

# 4 第一站：通勤工具大對決
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 01 通勤工具碳排大對決", 640, 75, size=26)
    t1 = ep.kw(4, "捷運")
    t2 = ep.kw(4, "機車")
    t3 = ep.kw(4, "開車")

    modes = [
        (t1, 280, 340, "捷運 / 公車", "30 g", "每人每公里", C['green'], mrt_train, 0.85),
        (t2, 640, 340, "燃油機車", "55 g", "每人每公里", (0.92, 0.58, 0.12), scooter_bike, 1.15),
        (t3, 1000, 340, "單人自駕汽車", "170 g", "每人每公里", C['red'], car_sedan, 0.90)
    ]

    for t_in, cx, cy, name, val, sub_t, col, drawer, sc in modes:
        p = prog(u, t_in, 0.35)
        if p > 0:
            ctx.save(); pop(ctx, cx, cy, p)
            polaroid(ctx, cx, cy, 320, 360, 0, name)
            ctx.new_path()
            drawer(ctx, cx, cy - 45, sc)
            ctx.new_path()
            chip(ctx, f"{val} CO2e", cx, cy + 55, 1, col, 26, C['white'])
            text(ctx, sub_t, cx, cy + 96, 17, (0.75, 0.78, 0.82))
            red_pin(ctx, cx, cy - 165)
            ctx.restore()

    if u > t3 + 0.3:
        red_stamp(ctx, "相差近 6 倍！", 930, 150, ang=-0.12, s=1.0)

# 5 第一站深入：桃園台北來回 60 公里
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CRIME SCENE 案例：桃園-台北每日 60 公里", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=0.01, bg=(0.97, 0.95, 0.91))
        text(ctx, "長距離單人自駕：碳排毀滅者", 480, 195, 32, (0.85, 0.15, 0.15))

        # 計算卡片
        rrect(ctx, 230, 240, 400, 170, 10); ctx.set_source_rgb(0.92, 0.92, 0.95); ctx.fill()
        text(ctx, "📊 通勤里程與天數計算", 430, 270, 22, (0.2, 0.25, 0.3))
        text(ctx, "來回 60 公里 × 240 工作天", 430, 310, 20, (0.35, 0.4, 0.45))
        text(ctx, "＝ 每年行駛 14,400 公里", 430, 345, 22, (0.1, 0.45, 0.8))

        rrect(ctx, 670, 240, 380, 170, 10); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "🔥 汽車年總碳排放", 860, 270, 22, (0.85, 0.2, 0.2))
        text(ctx, "14,400 km × 170 g/km", 860, 305, 20, (0.4, 0.3, 0.3))
        text(ctx, "＝ 2,448 公斤", 860, 345, 34, C['red'])

        highlighter(ctx, 240, 445, 800, 48)
        text(ctx, "單人自駕通勤突破兩公噸，直接透支全球人均年度碳預算！", 640, 440, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "預算破表 OVERDUE", 980, 185, ang=-0.12, s=0.95)

# 6 第二站：冰水主機 vs 個別冷氣
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 02 冰水主機 vs 個別冷氣效率", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.012, bg=(0.96, 0.95, 0.91))
        text(ctx, "規模經濟：集中供冷 vs 分散耗能", 640, 190, 34, (0.15, 0.2, 0.25))

        # 左邊：辦公室冰水機
        rrect(ctx, 220, 230, 380, 210, 10); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        chiller_plant(ctx, 410, 290, 0.7)
        text(ctx, "🏢 100人 辦公室集中冷房", 410, 375, 22, (0.15, 0.5, 0.25))
        text(ctx, "平均每人耗電僅 0.15 度/時", 410, 405, 18, (0.35, 0.4, 0.4))

        # 右邊：100 台居家冷氣
        rrect(ctx, 680, 230, 380, 210, 10); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        home_ac_unit(ctx, 870, 290, 0.75)
        text(ctx, "🏠 100戶 各自開居家空調", 870, 375, 22, (0.85, 0.2, 0.2))
        text(ctx, "每人耗電 0.8 ~ 1.2 度/時", 870, 405, 18, (0.45, 0.35, 0.35))

        highlighter(ctx, 240, 470, 800, 45)
        text(ctx, "在家各自開冷氣，總能源消耗比在辦公室暴增 5 倍以上！", 640, 465, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 155); red_pin(ctx, 1070, 155)
        ctx.restore()

# 7 第二站深究：英國研究報告
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "EVIDENCE 國際權威氣候研究報告", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 390, ang=0.015, bg=(0.98, 0.96, 0.93))
        text(ctx, "英國智庫：遠距工作淨排放真相", 480, 195, 32, (0.2, 0.2, 0.25))

        evidence_items = [
            "① 冬季暖氣 / 夏季極端高溫冷氣：居家耗能急劇飆升",
            "② 若員工家中缺乏高能效空調，通勤減少的碳排全被冷氣吃光",
            "③ 結論：極端氣候季節『全遠距』反而使全體社會碳排不減反增！"
        ]
        for i, it in enumerate(evidence_items):
            yy = 265 + i * 46
            rrect(ctx, 230, yy - 18, 820, 38, 6); ctx.set_source_rgb(0.92, 0.93, 0.95); ctx.fill()
            text(ctx, it, 640, yy + 4, 21, (0.25, 0.25, 0.3))

        highlighter(ctx, 260, 435, 760, 45)
        text(ctx, "真正環保不是盲目遠距，而是綜合考量氣候與能效！", 640, 430, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "實測證實 VERIFIED", 960, 195, ang=-0.14, s=1.0)

# 8 第三站：最佳解答
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 03 真正的綠色通勤解答", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.96, 0.92))
        text(ctx, "黃金混和模式：彈性遠距＋大眾運輸", 640, 195, 34, (0.15, 0.5, 0.25))

        # 三大支柱卡
        pillars = [
            ("每週 1~2 天遠距", "省下 20~40% 通勤里程", (0.2, 0.5, 0.8)),
            ("進辦公室搭捷運", "每公里僅 30 克極低排碳", C['green']),
            ("酷夏寒冬集中辦公", "發揮冰水主機規模能效", (0.9, 0.55, 0.1))
        ]
        for k, (t_box, d_box, col) in enumerate(pillars):
            cx = 320 + k * 320
            rrect(ctx, cx - 140, 250, 280, 140, 8); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
            chip(ctx, t_box, cx, 285, 1, col, 20, C['white'])
            text(ctx, d_box, cx, 345, 18, (0.3, 0.35, 0.4))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "兼顧生活彈性與環境永續的最佳平衡點！", 640, 435, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

# 9 企業推手
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CORPORATE ACTION 企業綠色通勤行動", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=0.012, bg=(0.97, 0.95, 0.91))
        text(ctx, "企業助力：讓低碳通勤成為全員文化", 530, 195, 32, (0.2, 0.2, 0.25))

        actions = [
            ("🚇 補助大眾運輸通勤月票 (TPASS)", "直接降低員工自駕開車誘因"),
            ("🚌 設置企業共享接駁專車", "打通捷運站與園區最後一哩路"),
            ("🚗 建立員工共乘媒合平台與專屬車位", "提高自駕乘載率，車流減半")
        ]
        for i, (act, ben) in enumerate(actions):
            yy = 260 + i * 50
            rrect(ctx, 220, yy - 18, 840, 40, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, act, 440, yy + 5, 21, (0.15, 0.45, 0.25))
            text(ctx, ben, 820, yy + 5, 19, (0.45, 0.45, 0.5))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "每年為公司與員工砍掉數百公噸通勤碳排放！", 640, 435, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "雙贏政策 WIN-WIN", 960, 195, ang=-0.14, s=1.0)

# 10 證物盤點
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "ANNUAL BALANCE 交通工具年度碳帳本", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "證物盤點：年通勤碳排總結算", 640, 190, 34, (0.15, 0.2, 0.25))

        rows = [
            ("🚗 單人自駕汽車", "2,500 公斤 CO2e", "高危險嚴重超標", C['red']),
            ("🛵 燃油機車通勤", "800 公斤 CO2e", "中度碳足跡", (0.9, 0.55, 0.1)),
            ("🚇 捷運與大眾運輸", "400 公斤 CO2e", "最佳模範低碳解", C['green']),
        ]
        for k, (mode, amount, status, col) in enumerate(rows):
            yy = 250 + k * 56
            rrect(ctx, 230, yy - 18, 820, 45, 8); ctx.set_source_rgb(0.92, 0.93, 0.95); ctx.fill()
            text(ctx, mode, 360, yy + 7, 24, (0.2, 0.2, 0.25))
            chip(ctx, amount, 640, yy + 7, 1, col, 24, C['white'])
            text(ctx, status, 900, yy + 7, 20, col)

        highlighter(ctx, 250, 450, 780, 45)
        text(ctx, "從開車改搭捷運，一年一人一口氣省下 2.1 公噸碳！", 640, 445, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 150); red_pin(ctx, 1070, 150)
        ctx.restore()

# 11 結案報告
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    tt = T
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.98, 0.96, 0.92))
        text(ctx, "CASE #003 結案行動三原則", 540, 195, 34, (0.15, 0.2, 0.25))

        habits = [
            ("① 大眾運輸優先：捷運公車或電巴", "年省 2 噸碳", 1.0),
            ("② 居家上班定溫：冷氣 27°C 加電扇", "減能耗 30%", 2.5),
            ("③ 彈性每週共乘或一至兩天遠距", "最佳黃金平衡", tt - 0.5)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "聰明通勤與生活，每天上班路都是低碳實踐！", 640, 450, 32, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    if u > tt - 0.3:
        red_stamp(ctx, "結案 CLOSED", 960, 195, ang=-0.16, s=1.05)

# 執行
run("of3", "辦公室碳冒險 EP3",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP3_遠距上班真的環保嗎.mp4",
    wipes={2, 4, 6, 8, 10, 11})
