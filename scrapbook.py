"""刑偵調查剪貼風格繪圖模組 (Investigative Scrapbook Style)
提供復古牛皮紙/軟木板底紋、撕紙便籤、拍立得證物卡、黑色壓印膠帶、紅色圖釘、線索紅棉線、印泥大紅印章、螢光筆標記等元件。
"""
import math, random, cairo
from engine import W, H, C, prog, ease_out, pop

# ==================== 底紋與紙質 ====================

def cork_bg(ctx, w=W, h=H, tone='kraft'):
    """復古牛皮紙 / 軟木板質感底紋，帶有微米色漸層與四周暗角 (Vignette)"""
    # 底色微漸層
    pat = cairo.RadialGradient(w / 2, h / 2, 80, w / 2, h / 2, w * 0.72)
    if tone == 'kraft':
        pat.add_color_stop_rgb(0.0, 0.89, 0.85, 0.78)  # 中心較亮米黃
        pat.add_color_stop_rgb(0.7, 0.82, 0.77, 0.69)  # 中段暖褐
        pat.add_color_stop_rgb(1.0, 0.68, 0.62, 0.54)  # 邊緣壓暗
    else:
        pat.add_color_stop_rgb(0.0, 0.94, 0.92, 0.88)
        pat.add_color_stop_rgb(1.0, 0.78, 0.74, 0.68)
    ctx.rectangle(0, 0, w, h)
    ctx.set_source(pat)
    ctx.fill()

    # 模擬顆粒質感的隨機微點 (固定隨機種子以保證影片每格穩定)
    rnd = random.Random(1337)
    ctx.save()
    for _ in range(120):
        rx, ry = rnd.uniform(0, w), rnd.uniform(0, h)
        rad = rnd.uniform(1.0, 2.5)
        ctx.arc(rx, ry, rad, 0, 2 * math.pi)
        ctx.set_source_rgba(0.45, 0.38, 0.30, rnd.uniform(0.04, 0.09))
        ctx.fill()
    ctx.restore()

# ==================== 剪貼與偵探證物元件 ====================

def black_tape(ctx, text, x, y, ang=0, size=24, col=(1, 1, 1), bg=(0.10, 0.10, 0.12)):
    """黑色壓印膠帶標籤 (Dymo Label Tape)"""
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(ang)
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(size)
    ext = ctx.text_extents(text)
    pw, ph = ext.width + 36, size + 20
    # 膠帶陰影
    ctx.rectangle(-pw / 2 + 3, -ph / 2 + 4, pw, ph)
    ctx.set_source_rgba(0, 0, 0, 0.22); ctx.fill()
    # 膠帶本體
    ctx.rectangle(-pw / 2, -ph / 2, pw, ph)
    ctx.set_source_rgb(*bg); ctx.fill()
    # 邊緣微反光
    ctx.move_to(-pw / 2, -ph / 2 + 1); ctx.line_to(pw / 2, -ph / 2 + 1)
    ctx.set_source_rgba(1, 1, 1, 0.25); ctx.set_line_width(1.5); ctx.stroke()
    # 文字
    ctx.move_to(-ext.width / 2 - ext.x_bearing, -ext.height / 2 - ext.y_bearing)
    ctx.set_source_rgb(*col); ctx.show_text(text)
    ctx.restore()

def torn_paper(ctx, x, y, w, h, ang=0, bg=(0.96, 0.95, 0.91), seed=42):
    """撕紙便籤 (上下邊緣帶有不規則鋸齒撕痕)"""
    rnd = random.Random(seed)
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(ang)
    hw, hh = w / 2, h / 2

    # 撕紙路徑生成
    def path():
        ctx.new_path()
        # 上邊緣 (撕裂鋸齒)
        n_steps = int(w / 14)
        ctx.move_to(-hw, -hh)
        for i in range(1, n_steps):
            xx = -hw + i * (w / n_steps)
            yy = -hh + rnd.uniform(-4, 4)
            ctx.line_to(xx, yy)
        ctx.line_to(hw, -hh)
        # 右邊
        ctx.line_to(hw, hh)
        # 下邊緣 (撕裂鋸齒)
        for i in range(n_steps - 1, 0, -1):
            xx = -hw + i * (w / n_steps)
            yy = hh + rnd.uniform(-4, 4)
            ctx.line_to(xx, yy)
        ctx.line_to(-hw, hh)
        ctx.close_path()

    # 柔和落影
    ctx.save(); ctx.translate(4, 6)
    path(); ctx.set_source_rgba(0, 0, 0, 0.18); ctx.fill(); ctx.restore()

    # 紙張本體
    path(); ctx.set_source_rgb(*bg); ctx.fill()

    # 淡淡折痕或格線 (筆記本質感)
    ctx.set_source_rgba(0.5, 0.6, 0.7, 0.12); ctx.set_line_width(1.5)
    for yy in range(int(-hh + 40), int(hh - 20), 32):
        ctx.move_to(-hw + 16, yy); ctx.line_to(hw - 16, yy); ctx.stroke()

    ctx.restore()

def polaroid(ctx, x, y, w, h, ang=0, label=""):
    """拍立得相片框 (白色邊框、上方相片區、下方手寫註記區)"""
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(ang)
    hw, hh = w / 2, h / 2
    # 落影
    ctx.rectangle(-hw + 5, -hh + 7, w, h)
    ctx.set_source_rgba(0, 0, 0, 0.22); ctx.fill()
    # 白色相紙外框
    ctx.rectangle(-hw, -hh, w, h)
    ctx.set_source_rgb(0.97, 0.96, 0.94); ctx.fill()
    ctx.set_source_rgb(0.86, 0.85, 0.82); ctx.set_line_width(1.5); ctx.stroke()
    # 內部相片深色底區
    m_top = 16; m_side = 16; bottom_h = 56
    pw = w - m_side * 2
    ph = h - m_top - bottom_h
    ctx.rectangle(-hw + m_side, -hh + m_top, pw, ph)
    ctx.set_source_rgb(0.20, 0.21, 0.24); ctx.fill()
    # 下方註記文字
    if label:
        ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(20)
        ext = ctx.text_extents(label)
        ctx.move_to(-ext.width / 2 - ext.x_bearing, hh - bottom_h / 2 - ext.height / 2 - ext.y_bearing)
        ctx.set_source_rgb(0.25, 0.25, 0.28); ctx.show_text(label); ctx.new_path()
    ctx.restore()

def red_pin(ctx, x, y):
    """3D 鮮紅塑膠圖釘 (帶立體高光與落影)"""
    ctx.save()
    ctx.translate(x, y)
    # 圖釘落影 (向右下)
    ctx.save(); ctx.translate(5, 7); ctx.scale(1, 0.45)
    ctx.arc(0, 0, 11, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, 0.35); ctx.fill(); ctx.restore()
    # 釘針金屬部 (微露)
    ctx.move_to(-2, 0); ctx.line_to(4, 6); ctx.set_source_rgb(0.5, 0.5, 0.5); ctx.set_line_width(3); ctx.stroke()
    # 釘頭本體 (紅色球體漸層)
    pat = cairo.RadialGradient(-3, -4, 2, 0, 0, 12)
    pat.add_color_stop_rgb(0.0, 1.0, 0.45, 0.45) # 亮點
    pat.add_color_stop_rgb(0.4, 0.85, 0.15, 0.15) # 主紅
    pat.add_color_stop_rgb(1.0, 0.50, 0.05, 0.05) # 深影
    ctx.arc(0, 0, 11, 0, 2 * math.pi); ctx.set_source(pat); ctx.fill()
    # 高光點
    ctx.arc(-3, -3, 3.5, 0, 2 * math.pi); ctx.set_source_rgba(1, 1, 1, 0.8); ctx.fill()
    ctx.restore()

def red_string(ctx, x1, y1, x2, y2, sag=24, p=1.0):
    """線索紅棉線 (兩端連接圖釘，中間因重力自然下垂)"""
    if p <= 0: return
    ctx.save()
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 + sag
    # 陰影
    ctx.save(); ctx.translate(2, 4)
    ctx.move_to(x1, y1)
    cx, cy = x1 + (mx - x1) * p, y1 + (my - y1) * p
    ex, ey = x1 + (x2 - x1) * p, y1 + (y2 - y1) * p
    ctx.curve_to(x1 + (mx - x1) * 0.5 * p, y1 + (my - y1) * 0.5 * p, cx, cy, ex, ey)
    ctx.set_source_rgba(0, 0, 0, 0.20); ctx.set_line_width(3.5); ctx.stroke(); ctx.restore()
    # 紅線本體
    ctx.move_to(x1, y1)
    ctx.curve_to(x1 + (mx - x1) * 0.5 * p, y1 + (my - y1) * 0.5 * p, cx, cy, ex, ey)
    ctx.set_source_rgb(0.85, 0.18, 0.15); ctx.set_line_width(3.0); ctx.stroke()
    ctx.restore()

def red_stamp(ctx, text, x, y, ang=-0.14, s=1.0, col=(0.82, 0.18, 0.15)):
    """大紅色復古印章 (雙框、斑駁印泥印戳質感)"""
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(ang)
    ctx.scale(s, s)
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(36)
    ext = ctx.text_extents(text)
    pw = ext.width + 36
    ph = ext.height + 28

    # 雙框外框 (微粗不均勻線條)
    ctx.rectangle(-pw / 2, -ph / 2, pw, ph)
    ctx.set_source_rgba(*col, 0.88); ctx.set_line_width(5); ctx.stroke()
    ctx.rectangle(-pw / 2 + 5, -ph / 2 + 5, pw - 10, ph - 10)
    ctx.set_source_rgba(*col, 0.88); ctx.set_line_width(2.5); ctx.stroke()

    # 印章文字
    ctx.move_to(-ext.width / 2 - ext.x_bearing, -ext.height / 2 - ext.y_bearing)
    ctx.set_source_rgba(*col, 0.92); ctx.show_text(text)
    ctx.restore()

def highlighter(ctx, x, y, w, h, col=(1.0, 0.88, 0.15, 0.50)):
    """螢光黃劃線標記 (半透明、邊緣帶有馬克筆自然塗抹感)"""
    ctx.save()
    ctx.rectangle(x, y - h * 0.8, w, h)
    ctx.set_source_rgba(*col)
    ctx.fill()
    ctx.restore()

def red_circle(ctx, x, y, rx=60, ry=45, ang=0):
    """紅筆手繪圈選標記 (像刑偵照片上的嫌犯標註)"""
    ctx.save()
    ctx.translate(x, y); ctx.rotate(ang)
    ctx.scale(rx, ry)
    ctx.arc(0, 0, 1.0, 0, 2 * math.pi)
    ctx.set_source_rgba(0.85, 0.15, 0.15, 0.85); ctx.set_line_width(0.12); ctx.stroke()
    ctx.restore()

# ==================== 辦公室道具繪製 ====================

def office_ac(ctx, x, y, s=1.0, cold=True):
    """辦公室中央冷氣出風口"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 冷氣機身
    ctx.rectangle(-120, -45, 240, 90)
    ctx.set_source_rgb(0.96, 0.96, 0.96); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(4); ctx.stroke()
    # 導風百葉
    for i in range(3):
        ctx.move_to(-100, -10 + i * 14); ctx.line_to(100, -10 + i * 14)
        ctx.set_source_rgb(0.65, 0.65, 0.70); ctx.set_line_width(3); ctx.stroke()
    # 溫度顯示「19°C」
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24); ctx.move_to(50, -16)
    ctx.set_source_rgb(0.1, 0.45, 0.85); ctx.show_text("19°C")
    # 冷風噴射線
    if cold:
        for k in range(4):
            xx = -80 + k * 50
            ctx.move_to(xx, 50); ctx.curve_to(xx - 15, 75, xx + 15, 95, xx, 120)
            ctx.set_source_rgba(0.2, 0.6, 0.9, 0.6); ctx.set_line_width(4); ctx.stroke()
    ctx.restore()

def office_pc(ctx, x, y, s=1.0, on=True):
    """電腦螢幕與主機 (徹夜亮著)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 螢幕外框
    ctx.rectangle(-90, -70, 180, 115)
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill()
    # 螢幕顯示區
    ctx.rectangle(-82, -62, 164, 98)
    if on:
        pat = cairo.LinearGradient(0, -62, 0, 36)
        pat.add_color_stop_rgb(0, 0.25, 0.45, 0.75)
        pat.add_color_stop_rgb(1, 0.15, 0.25, 0.45)
        ctx.set_source(pat); ctx.fill()
        # 螢幕上的視窗
        ctx.rectangle(-65, -45, 70, 45); ctx.set_source_rgba(1, 1, 1, 0.4); ctx.fill()
        ctx.rectangle(15, -40, 55, 60); ctx.set_source_rgba(1, 1, 1, 0.3); ctx.fill()
    else:
        ctx.set_source_rgb(0.08, 0.08, 0.1); ctx.fill()
    # 支架底座
    ctx.rectangle(-12, 45, 24, 25); ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.fill()
    ctx.rectangle(-40, 70, 80, 12); ctx.set_source_rgb(0.2, 0.2, 0.25); ctx.fill()
    ctx.restore()

def server_rack(ctx, x, y, s=1.0):
    """機房伺服器機櫃"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 機櫃黑框
    ctx.rectangle(-70, -110, 140, 220)
    ctx.set_source_rgb(0.12, 0.13, 0.16); ctx.fill_preserve()
    ctx.set_source_rgb(0.35, 0.35, 0.40); ctx.set_line_width(4); ctx.stroke()
    # 伺服器層板 (6層)
    for i in range(6):
        yy = -95 + i * 34
        ctx.rectangle(-60, yy, 120, 26)
        ctx.set_source_rgb(0.22, 0.24, 0.28); ctx.fill()
        # 散熱孔線
        for k in range(4):
            ctx.move_to(-40 + k * 18, yy + 6); ctx.line_to(-40 + k * 18, yy + 20)
            ctx.set_source_rgb(0.1, 0.1, 0.1); ctx.set_line_width(2.5); ctx.stroke()
        # 閃爍訊號燈
        col1 = (0.2, 0.85, 0.4) if i % 2 == 0 else (0.3, 0.6, 1.0)
        col2 = (1.0, 0.7, 0.1) if i == 3 else (0.2, 0.85, 0.4)
        ctx.arc(36, yy + 13, 4, 0, 2 * math.pi); ctx.set_source_rgb(*col1); ctx.fill()
        ctx.arc(48, yy + 13, 4, 0, 2 * math.pi); ctx.set_source_rgb(*col2); ctx.fill()
    ctx.restore()

def latte_cup(ctx, x, y, s=1.0):
    """外帶鮮奶拿鐵紙杯 (帶杯套與塑膠凸蓋)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 白色梯形杯身
    ctx.move_to(-40, -50); ctx.line_to(40, -50)
    ctx.line_to(30, 60); ctx.line_to(-30, 60); ctx.close_path()
    ctx.set_source_rgb(0.96, 0.95, 0.92); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(3.5); ctx.stroke()
    # 牛皮紙隔熱杯套
    ctx.move_to(-36, -16); ctx.line_to(36, -16)
    ctx.line_to(32, 28); ctx.line_to(-32, 28); ctx.close_path()
    ctx.set_source_rgb(0.78, 0.58, 0.38); ctx.fill_preserve()
    ctx.set_source_rgb(0.45, 0.30, 0.15); ctx.set_line_width(2.5); ctx.stroke()
    # 咖啡豆標籤
    ctx.arc(0, 6, 8, 0, 2 * math.pi); ctx.set_source_rgb(0.95, 0.9, 0.8); ctx.fill()
    # 黑色塑膠飲用杯蓋
    ctx.rectangle(-44, -66, 88, 16)
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill()
    ctx.rectangle(-18, -72, 36, 8)
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill()
    ctx.restore()

def bento_box(ctx, x, y, s=1.0):
    """外送便當盒 (塑膠格層＋免洗筷包)"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 便當主盒
    ctx.rectangle(-80, -55, 160, 110)
    ctx.set_source_rgb(0.85, 0.35, 0.25); ctx.fill_preserve() # 醬汁橘紅外盒
    ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(4); ctx.stroke()
    # 飯區 (白米飯)
    ctx.rectangle(-70, -45, 75, 90)
    ctx.set_source_rgb(0.98, 0.98, 0.96); ctx.fill()
    ctx.arc(-32, 0, 5, 0, 2 * math.pi); ctx.set_source_rgb(0.8, 0.1, 0.1); ctx.fill() # 紅梅子
    # 大炸排骨肉排 (油亮金褐)
    ctx.rectangle(12, -45, 58, 55)
    ctx.set_source_rgb(0.65, 0.35, 0.15); ctx.fill()
    for k in range(3):
        ctx.move_to(20 + k * 16, -40); ctx.line_to(20 + k * 16, 5)
        ctx.set_source_rgb(0.4, 0.18, 0.08); ctx.set_line_width(3); ctx.stroke()
    # 小菜格 (黃金醃蘿蔔與青菜)
    ctx.rectangle(12, 16, 26, 30); ctx.set_source_rgb(0.95, 0.8, 0.15); ctx.fill()
    ctx.rectangle(44, 16, 26, 30); ctx.set_source_rgb(0.25, 0.65, 0.35); ctx.fill()
    # 斜放的免洗竹筷包
    ctx.save(); ctx.translate(-20, -70); ctx.rotate(-0.25)
    ctx.rectangle(-70, -7, 140, 14); ctx.set_source_rgb(0.95, 0.95, 0.92); ctx.fill_preserve()
    ctx.set_source_rgb(0.8, 0.2, 0.2); ctx.set_line_width(2); ctx.stroke()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(10); ctx.move_to(-25, 4); ctx.set_source_rgb(0.8, 0.2, 0.2); ctx.show_text("衛生筷")
    ctx.restore()
    ctx.restore()

def email_inbox(ctx, x, y, s=1.0, count="9999+"):
    """垃圾信箱與陳年未讀郵件"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 信封折角外型
    ctx.rectangle(-75, -50, 150, 100)
    ctx.set_source_rgb(0.96, 0.95, 0.92); ctx.fill_preserve()
    ctx.set_source_rgb(0.25, 0.25, 0.30); ctx.set_line_width(4); ctx.stroke()
    ctx.move_to(-75, -50); ctx.line_to(0, 8); ctx.line_to(75, -50)
    ctx.set_source_rgb(0.3, 0.3, 0.35); ctx.set_line_width(3.5); ctx.stroke()
    # 紅色未讀紅標泡泡
    ctx.arc(65, -45, 26, 0, 2 * math.pi)
    ctx.set_source_rgb(0.85, 0.15, 0.15); ctx.fill()
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(15); ctx.move_to(45, -39)
    ctx.set_source_rgb(1, 1, 1); ctx.show_text(count)
    ctx.restore()
