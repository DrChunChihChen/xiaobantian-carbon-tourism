"""1930 年代復古橡皮管卡通風格模組 (Rubber Hose Cartoon Style)
專為直式 9:16 (720x1280) 打造，包含經典派狀眼、橡皮管四肢、白手套、條紋壁紙、復古擺鐘、黑板與手繪漫畫特效。
"""
import math, cairo
from engine import C, prog, ease_out, pop

W_V, H_V = 720, 1280

# ==================== 復古背景與環境 ====================

def vintage_room(ctx, u, w=W_V, h=H_V):
    """1930s 復古室內：米褐直條紋壁紙、深木地板、擺鐘、夜景窗戶"""
    # 條紋壁紙 (y: 0 ~ 920)
    bg1 = (0.91, 0.87, 0.78)
    bg2 = (0.85, 0.80, 0.70)
    ctx.rectangle(0, 0, w, 920); ctx.set_source_rgb(*bg1); ctx.fill()
    stripe_w = 40
    ctx.set_source_rgb(*bg2)
    for x in range(0, w, stripe_w * 2):
        ctx.rectangle(x, 0, stripe_w, 920); ctx.fill()

    # 壁紙上的微小圓點印花
    ctx.set_source_rgba(0.5, 0.45, 0.38, 0.25)
    for y in range(40, 920, 60):
        for x in range(20, w, 40):
            ctx.arc(x, y, 2.5, 0, 2 * math.pi); ctx.fill()

    # 踢腳線與木地板 (y: 920 ~ 1280)
    ctx.rectangle(0, 915, w, 20); ctx.set_source_rgb(0.35, 0.22, 0.14); ctx.fill()
    ctx.rectangle(0, 935, w, h - 935); ctx.set_source_rgb(0.48, 0.32, 0.20); ctx.fill()
    # 木板木紋分線
    ctx.set_source_rgb(0.32, 0.20, 0.12); ctx.set_line_width(3)
    for yy in range(990, h, 65):
        ctx.move_to(0, yy); ctx.line_to(w, yy); ctx.stroke()

    # 復古指針擺鐘 (左上方 x=120, y=180)
    retro_clock(ctx, 110, 180, u)

    # 復古窗戶與新月 (右上方 x=600, y=190)
    retro_window(ctx, 600, 190, u)

def retro_clock(ctx, x, y, u):
    """牆上擺鐘與搖擺鐘擺"""
    ctx.save(); ctx.translate(x, y)
    # 鐘擺 (左右搖晃)
    pend_ang = math.sin(u * 4.5) * 0.22
    ctx.save(); ctx.rotate(pend_ang)
    ctx.move_to(0, 45); ctx.line_to(0, 120)
    ctx.set_source_rgb(0.2, 0.2, 0.22); ctx.set_line_width(4); ctx.stroke()
    ctx.arc(0, 125, 14, 0, 2 * math.pi)
    ctx.set_source_rgb(0.85, 0.70, 0.25); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.22); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()

    # 圓鐘外框 (深木邊框)
    ctx.arc(0, 0, 52, 0, 2 * math.pi)
    ctx.set_source_rgb(0.45, 0.28, 0.16); ctx.fill_preserve()
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.set_line_width(5); ctx.stroke()
    # 鐘面白底
    ctx.arc(0, 0, 42, 0, 2 * math.pi)
    ctx.set_source_rgb(0.97, 0.96, 0.93); ctx.fill_preserve()
    ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(2); ctx.stroke()
    # 刻度
    for k in range(12):
        ang = k * math.pi / 6
        ctx.move_to(math.cos(ang) * 34, math.sin(ang) * 34)
        ctx.line_to(math.cos(ang) * 39, math.sin(ang) * 39)
        ctx.set_source_rgb(0.2, 0.2, 0.2); ctx.set_line_width(2.5); ctx.stroke()
    # 指針
    ctx.move_to(0, 0); ctx.line_to(12, -22); ctx.set_line_width(3.5); ctx.stroke() # 時針
    ctx.move_to(0, 0); ctx.line_to(-6, -30); ctx.set_line_width(2.5); ctx.stroke() # 分針
    ctx.arc(0, 0, 4, 0, 2 * math.pi); ctx.fill()
    ctx.restore()

def retro_window(ctx, x, y, u):
    """深木十字窗與窗外夜空新月"""
    ctx.save(); ctx.translate(x, y)
    # 窗框落影
    ctx.rectangle(-65, -80, 130, 160)
    ctx.set_source_rgb(0.12, 0.12, 0.16); ctx.fill_preserve()
    ctx.set_source_rgb(0.35, 0.22, 0.14); ctx.set_line_width(8); ctx.stroke()
    # 窗外夜空與月亮
    ctx.save()
    ctx.rectangle(-61, -76, 122, 152); ctx.clip()
    # 新月
    ctx.arc(20, -25, 32, 0, 2 * math.pi)
    ctx.set_source_rgb(0.98, 0.95, 0.85); ctx.fill()
    ctx.arc(8, -32, 28, 0, 2 * math.pi)
    ctx.set_source_rgb(0.12, 0.12, 0.16); ctx.fill()
    # 閃爍小星星
    star_blink = 0.5 + 0.5 * math.sin(u * 5)
    ctx.arc(-30, 30, 3, 0, 2 * math.pi); ctx.set_source_rgba(1, 1, 1, star_blink); ctx.fill()
    ctx.arc(35, 45, 2.5, 0, 2 * math.pi); ctx.set_source_rgba(1, 1, 1, 1 - star_blink); ctx.fill()
    ctx.restore()
    # 木質十字窗格
    ctx.move_to(-65, 0); ctx.line_to(65, 0); ctx.set_source_rgb(0.35, 0.22, 0.14); ctx.set_line_width(6); ctx.stroke()
    ctx.move_to(0, -80); ctx.line_to(0, 80); ctx.stroke()
    ctx.restore()

# ==================== 1930s 卡通面部與肢體元件 ====================

def pie_eye(ctx, x, y, r=13, wedge_ang=-0.8, look=(0, 0)):
    """經典 1930s 派狀眼 (Pie-cut eye / Pac-man eye)"""
    ctx.save()
    ctx.translate(x + look[0], y + look[1])
    # 黑眼珠
    ctx.arc(0, 0, r, 0, 2 * math.pi)
    ctx.set_source_rgb(0.10, 0.10, 0.12); ctx.fill()
    # 派狀缺角 (白色小扇形楔子切口)
    ctx.move_to(0, 0)
    ctx.arc(0, 0, r * 1.15, wedge_ang - 0.40, wedge_ang + 0.40)
    ctx.close_path()
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill()
    ctx.restore()

def swirl_eye(ctx, x, y, r=13, t=0):
    """暈眩蚊香眼 (螺旋線)"""
    ctx.save(); ctx.translate(x, y)
    ctx.set_source_rgb(0.10, 0.10, 0.12); ctx.set_line_width(3.5); ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.new_path()
    for i in range(40):
        th = i * 0.25 + t * 6
        rad = (i / 40.0) * r
        xx = math.cos(th) * rad
        yy = math.sin(th) * rad
        (ctx.move_to if i == 0 else ctx.line_to)(xx, yy)
    ctx.stroke()
    ctx.restore()

def cartoon_glove(ctx, x, y, ang=0, s=1.0):
    """經典米奇/貝蒂波普白手套 (白色手套＋背部三道黑線)"""
    ctx.save(); ctx.translate(x, y); ctx.rotate(ang); ctx.scale(s, s)
    # 手腕蓬鬆袖口 (白色橢圓)
    ctx.save(); ctx.scale(1, 0.55); ctx.arc(0, 16, 15, 0, 2 * math.pi); ctx.restore()
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    # 手掌圓掌
    ctx.arc(0, 0, 16, 0, 2 * math.pi)
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    # 大拇指
    ctx.arc(-14, -6, 7, 0, 2 * math.pi); ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(2.5); ctx.stroke()
    # 手背三道黑線
    for sd in (-5, 0, 5):
        ctx.move_to(sd, -7); ctx.line_to(sd * 0.9, 5)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(2.2); ctx.stroke()
    ctx.restore()

# ==================== 復古橡皮管角色：小綠 & 阿德 ====================

def retro_xiaolu(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True):
    """1930s 復古橡皮管小綠導遊"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    bob = -abs(math.sin(t * 5.0)) * 10
    ctx.translate(0, bob)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)

    # 橡皮管腿部
    for sd in (-1, 1):
        ctx.move_to(sd * 18, 120); ctx.curve_to(sd * 22, 150, sd * 20, 175, sd * 22, 195)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(12); ctx.stroke()
        # 黑色圓頭卡通皮鞋
        ctx.save(); ctx.translate(sd * 24, 195); ctx.scale(1.3, 0.7)
        ctx.arc(0, 0, 15, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.fill()

    # 綠色復古小連身裙 (A 字剪裁)
    ctx.move_to(-38, 45); ctx.line_to(38, 45)
    ctx.line_to(55, 125); ctx.line_to(-55, 125); ctx.close_path()
    ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4.5); ctx.stroke()
    # 白色小翻領
    ctx.move_to(-25, 45); ctx.line_to(0, 65); ctx.line_to(25, 45)
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
    # 裙面小黃葉徽章
    ctx.arc(0, 85, 7, 0, 2 * math.pi); ctx.set_source_rgb(0.95, 0.85, 0.25); ctx.fill()

    # 橡皮管雙臂
    ang_w = math.sin(t * 8) * 0.35
    if wave:
        # 揮舞右手旗幟
        ctx.move_to(32, 55); ctx.curve_to(70, 45, 90, 10 + ang_w * 40, 75, -25 + ang_w * 35)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(11); ctx.stroke()
        cartoon_glove(ctx, 75, -25 + ang_w * 35, ang=-0.4, s=0.9)
        # 復古 CO2 小旗子
        fx, fy = 75, -25 + ang_w * 35
        ctx.move_to(fx, fy); ctx.line_to(fx + 25, fy - 65); ctx.set_source_rgb(0.3, 0.2, 0.1); ctx.set_line_width(5); ctx.stroke()
        ctx.move_to(fx + 25, fy - 65); ctx.line_to(fx + 105, fy - 45); ctx.line_to(fx + 25, fy - 25); ctx.close_path()
        ctx.set_source_rgb(0.95, 0.85, 0.25); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3); ctx.stroke()
        ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(15); ctx.move_to(fx + 38, fy - 40); ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.show_text("CO2")
    else:
        ctx.move_to(32, 55); ctx.curve_to(65, 75, 70, 100, 55, 115)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(11); ctx.stroke()
        cartoon_glove(ctx, 55, 115, ang=0.4, s=0.85)

    # 左手叉腰或指向
    if point:
        ctx.move_to(-32, 55); ctx.curve_to(-70, 45, -95, 30, -115, 20)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(11); ctx.stroke()
        cartoon_glove(ctx, -115, 20, ang=1.5, s=0.9)
    else:
        ctx.move_to(-32, 55); ctx.curve_to(-60, 75, -65, 100, -50, 115)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(11); ctx.stroke()
        cartoon_glove(ctx, -50, 115, ang=-0.4, s=0.85)

    # 頭部 (大圓形白皮膚)
    ctx.arc(0, -15, 58, 0, 2 * math.pi)
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()

    # 1930s 復古波浪短髮 (黑色外翻鮑伯短髮)
    ctx.move_to(-58, -15); ctx.curve_to(-65, -60, -35, -78, 0, -78)
    ctx.curve_to(35, -78, 65, -60, 58, -15)
    ctx.curve_to(45, -45, 15, -50, 0, -42)
    ctx.curve_to(-15, -50, -45, -45, -58, -15); ctx.close_path()
    ctx.set_source_rgb(0.12, 0.12, 0.15); ctx.fill()
    # 兩側俏皮外翻髮捲
    for sd in (-1, 1):
        ctx.arc(sd * 56, -8, 14, 0, 2 * math.pi); ctx.fill()

    # 綠色復古小導遊帽 (歪戴在右邊)
    ctx.save(); ctx.translate(18, -75); ctx.rotate(0.25)
    ctx.rectangle(-28, -20, 56, 22)
    ctx.set_source_rgb(0.28, 0.62, 0.40); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3.5); ctx.stroke()
    ctx.move_to(-35, 2); ctx.line_to(35, 2)
    ctx.set_source_rgb(0.2, 0.45, 0.28); ctx.set_line_width(5); ctx.stroke()
    ctx.restore()

    # 經典派狀眼 (Pie-cut eyes)
    blink = (t % 3.6) < 0.14
    if not blink:
        pie_eye(ctx, -20, -15, r=13, wedge_ang=-0.75)
        pie_eye(ctx, 20, -15, r=13, wedge_ang=-0.75)
    else:
        for ex in (-20, 20):
            ctx.move_to(ex - 12, -15); ctx.line_to(ex + 12, -15)
            ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()

    # 小圓鼻子
    ctx.arc(0, 3, 4, 0, 2 * math.pi); ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.fill()

    # 嘴巴 (開合說話 / 甜美微笑)
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 24); ctx.scale(1, (6 + 18 * mouth) / 12)
        ctx.arc(0, 0, 12, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.fill_preserve()
        # 紅色舌頭
        ctx.save(); ctx.translate(0, 26); ctx.arc(0, 0, 7, 0, math.pi); ctx.set_source_rgb(0.85, 0.25, 0.25); ctx.fill(); ctx.restore()
    else:
        ctx.arc(0, 16, 12, 0.15 * math.pi, 0.85 * math.pi)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()

    # 冒汗珠
    if sweat:
        dy = (t * 40) % 25
        ctx.arc(58, -35 + dy, 7, 0, 2 * math.pi); ctx.set_source_rgb(0.4, 0.75, 0.95); ctx.fill()

    ctx.restore()

def retro_boss(ctx, x, y, s, t, mouth=0.0, puzzled=False, happy=False, wave=False):
    """1930s 復古橡皮管阿德老闆"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    bob = -abs(math.sin(t * 4.2)) * 8
    ctx.translate(0, bob)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)

    # 橡皮管短腿
    for sd in (-1, 1):
        ctx.move_to(sd * 24, 130); ctx.curve_to(sd * 28, 160, sd * 26, 185, sd * 28, 205)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(15); ctx.stroke()
        # 肥厚大黑鞋
        ctx.save(); ctx.translate(sd * 30, 205); ctx.scale(1.4, 0.8)
        ctx.arc(0, 0, 18, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.fill()

    # 圓滾滾大肚子西裝 (深灰/褐復古背心)
    ctx.save(); ctx.scale(1.15, 1)
    ctx.arc(0, 80, 56, 0, 2 * math.pi); ctx.restore()
    ctx.set_source_rgb(0.32, 0.30, 0.35); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()
    # 白色襯衫 V 領口＋紅色領結
    ctx.move_to(-20, 32); ctx.line_to(0, 65); ctx.line_to(20, 32); ctx.close_path()
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill()
    ctx.arc(0, 42, 6, 0, 2 * math.pi); ctx.set_source_rgb(0.85, 0.2, 0.15); ctx.fill()
    # 背心黃銅金鈕扣
    for by in (75, 95):
        ctx.arc(0, by, 4.5, 0, 2 * math.pi); ctx.set_source_rgb(0.95, 0.8, 0.2); ctx.fill()

    # 橡皮管雙臂
    if puzzled:
        # 左手抓頭
        ctx.move_to(-45, 60); ctx.curve_to(-80, 40, -75, -20, -50, -45)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(13); ctx.stroke()
        cartoon_glove(ctx, -50, -45, ang=-1.8, s=0.95)
        # 右手攤手
        ctx.move_to(45, 60); ctx.curve_to(80, 80, 95, 95, 80, 110)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(13); ctx.stroke()
        cartoon_glove(ctx, 80, 110, ang=0.5, s=0.95)
    elif wave or happy:
        # 雙手歡呼或比讚
        ctx.move_to(-45, 60); ctx.curve_to(-75, 40, -85, 0, -70, -25)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(13); ctx.stroke()
        cartoon_glove(ctx, -70, -25, ang=-0.8, s=0.95)
        ctx.move_to(45, 60); ctx.curve_to(75, 40, 85, 0, 70, -25)
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(13); ctx.stroke()
        cartoon_glove(ctx, 70, -25, ang=0.8, s=0.95)
    else:
        for sd in (-1, 1):
            ctx.move_to(sd * 45, 60); ctx.curve_to(sd * 75, 80, sd * 80, 105, sd * 65, 120)
            ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(13); ctx.stroke()
            cartoon_glove(ctx, sd * 65, 120, ang=sd * 0.4, s=0.9)

    # 圓滾滾大頭 (光頭白膚)
    ctx.arc(0, -18, 62, 0, 2 * math.pi)
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(5); ctx.stroke()

    # 光頭兩側的少許黑髮
    for sd in (-1, 1):
        ctx.arc(sd * 60, -12, 10, 0, 2 * math.pi); ctx.set_source_rgb(0.2, 0.2, 0.22); ctx.fill()

    # 圓形復古黑框眼鏡
    for ex in (-25, 25):
        ctx.arc(ex, -20, 20, 0, 2 * math.pi)
        ctx.set_source_rgba(0.9, 0.95, 1.0, 0.45); ctx.fill_preserve()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()

    # 眼鏡中樑
    ctx.move_to(-5, -20); ctx.line_to(5, -20); ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()

    # 眼睛 (派狀眼 或 困惑蚊香眼)
    if puzzled:
        swirl_eye(ctx, -25, -20, r=11, t=t)
        swirl_eye(ctx, 25, -20, r=11, t=t)
    else:
        blink = (t % 3.8) < 0.14
        if not blink:
            pie_eye(ctx, -25, -20, r=11, wedge_ang=-0.7)
            pie_eye(ctx, 25, -20, r=11, wedge_ang=-0.7)
        else:
            for ex in (-25, 25):
                ctx.move_to(ex - 10, -20); ctx.line_to(ex + 10, -20)
                ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()

    # 招牌濃密黑色八字鬍
    ctx.save(); ctx.translate(0, 10)
    ctx.move_to(-28, 5); ctx.curve_to(-15, -8, -5, -4, 0, 2)
    ctx.curve_to(5, -4, 15, -8, 28, 5)
    ctx.curve_to(12, 12, -12, 12, -28, 5); ctx.close_path()
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.fill()
    ctx.restore()

    # 嘴巴
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 30); ctx.scale(1, (5 + 16 * mouth) / 10)
        ctx.arc(0, 0, 10, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.fill()
    else:
        if happy:
            ctx.arc(0, 22, 10, 0.15 * math.pi, 0.85 * math.pi)
            ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4); ctx.stroke()
        else:
            ctx.move_to(-10, 30); ctx.line_to(10, 30); ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(3.5); ctx.stroke()

    # 困惑大汗珠
    if puzzled:
        dy = (t * 40) % 25
        ctx.arc(-62, -35 + dy, 8, 0, 2 * math.pi); ctx.set_source_rgb(0.4, 0.75, 0.95); ctx.fill()

    ctx.restore()

# ==================== 1930s 復古黑板與道具 ====================

def retro_blackboard(ctx, x, y, w, h, title=""):
    """復古深綠色大黑板 (木框＋粉筆字)"""
    ctx.save(); ctx.translate(x, y)
    hw, hh = w / 2, h / 2
    # 橡木外框
    ctx.rectangle(-hw, -hh, w, h)
    ctx.set_source_rgb(0.42, 0.28, 0.16); ctx.fill_preserve()
    ctx.set_source_rgb(0.15, 0.15, 0.18); ctx.set_line_width(5); ctx.stroke()
    # 內部深墨綠黑板面
    ctx.rectangle(-hw + 14, -hh + 14, w - 28, h - 28)
    ctx.set_source_rgb(0.16, 0.28, 0.22); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.15, 0.12); ctx.set_line_width(3); ctx.stroke()
    # 標題 (粉筆字)
    if title:
        ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(28)
        ext = ctx.text_extents(title)
        ctx.move_to(-ext.width / 2, -hh + 50)
        ctx.set_source_rgb(0.98, 0.95, 0.85); ctx.show_text(title)
        # 底線
        ctx.move_to(-ext.width / 2 - 10, -hh + 60); ctx.line_to(ext.width / 2 + 10, -hh + 60)
        ctx.set_source_rgba(0.98, 0.95, 0.85, 0.6); ctx.set_line_width(2.5); ctx.stroke()
    # 粉筆槽
    ctx.rectangle(-hw + 30, hh - 10, w - 60, 8); ctx.set_source_rgb(0.35, 0.22, 0.14); ctx.fill()
    ctx.restore()

def shout_bubble(ctx, text, x, y, w, h, tail_dir="down"):
    """1930s 尖角漫畫對話框 (驚爆感)"""
    ctx.save(); ctx.translate(x, y)
    hw, hh = w / 2, h / 2
    # 鋸齒邊緣
    n = 16
    ctx.new_path()
    for i in range(n):
        ang1 = (i / n) * 2 * math.pi
        ang2 = ((i + 0.5) / n) * 2 * math.pi
        r1 = max(hw, hh)
        r2 = r1 + 14
        x1, y1 = math.cos(ang1) * hw, math.sin(ang1) * hh
        x2, y2 = math.cos(ang2) * (hw + 14), math.sin(ang2) * (hh + 12)
        (ctx.move_to if i == 0 else ctx.line_to)(x1, y1)
        ctx.line_to(x2, y2)
    ctx.close_path()
    ctx.set_source_rgb(0.98, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.set_line_width(4.5); ctx.stroke()

    # 對話框內文字
    ctx.select_font_face("Noto Sans CJK TC", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(26)
    ext = ctx.text_extents(text)
    ctx.move_to(-ext.width / 2 - ext.x_bearing, -ext.height / 2 - ext.y_bearing)
    ctx.set_source_rgb(0.1, 0.1, 0.12); ctx.show_text(text)
    ctx.restore()

def action_rays(ctx, cx, cy, u, col1=(0.85, 0.22, 0.18), col2=(0.95, 0.88, 0.70)):
    """1930s 漫畫放射狀速度線 (Shock Rays)"""
    ctx.save(); ctx.translate(cx, cy)
    n = 24
    rot = (u * 0.4) % (2 * math.pi / n)
    ctx.rotate(rot)
    for i in range(n):
        ang1 = i * (2 * math.pi / n)
        ang2 = (i + 0.5) * (2 * math.pi / n)
        ctx.move_to(0, 0)
        ctx.line_to(math.cos(ang1) * 900, math.sin(ang1) * 900)
        ctx.line_to(math.cos(ang2) * 900, math.sin(ang2) * 900)
        ctx.close_path()
        ctx.set_source_rgba(*(col1 if i % 2 == 0 else col2), 0.35)
        ctx.fill()
    ctx.restore()
