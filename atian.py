"""小半天導遊：阿天 (A-Tian)
在地青年導遊角色 — 陽光活潑、卡其戶外登山遮陽帽（綴有青竹葉徽章）、軍綠戶外導遊背心、手持「小半天」導遊旗
"""
import dc
from dc import *

# 阿天專屬色彩盤
HAT_COLOR = (0.86, 0.80, 0.68)      # 卡其遮陽帽
HAT_BAND = (0.22, 0.48, 0.32)       # 墨綠帽帶
HAIR_ATIAN = (0.24, 0.18, 0.14)     # 深棕短髮
VEST_ATIAN = (0.26, 0.56, 0.38)     # 戶外山林綠背心
VEST_DARK = (0.18, 0.42, 0.28)      # 背心滾邊深綠
TEE_INNER = (0.98, 0.96, 0.90)      # 內搭米白 T 恤
PANTS_ATIAN = (0.76, 0.66, 0.52)    # 戶外卡其褲
BOOTS_COLOR = (0.42, 0.26, 0.16)    # 登山短靴

def bamboo_leaf_badge(ctx, x, y, s=1.0):
    """帽帶上的小半天竹葉徽章"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.rotate(-0.3)
    # 兩片嫩綠竹葉
    for ang, dx, col in [(-0.4, -4, C['green']), (0.3, 4, C['yellow'])]:
        ctx.save(); ctx.rotate(ang)
        ctx.move_to(0, -12); ctx.curve_to(8, -6, 8, 6, 0, 12); ctx.curve_to(-8, 6, -8, -6, 0, -12); ctx.close_path()
        fillstroke(ctx, col, stroke=C['navy'], lw=2.2)
        ctx.restore()
    ctx.restore()

def flag_atian(ctx, hx, hy, t, ang=-1.45, L=175, d=1):
    """阿天的導遊旗：飄揚旗幟上印著『小半天』"""
    ex, ey = hx + math.cos(ang) * L, hy + math.sin(ang) * L
    # 竹製/木質旗桿
    ctx.move_to(hx, hy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(9); ctx.stroke()
    ctx.move_to(hx, hy); ctx.line_to(ex, ey); ctx.set_source_rgb(0.82, 0.68, 0.42); ctx.set_line_width(5); ctx.stroke()
    
    # 旗桿頂端小金球
    ctx.arc(ex, ey - 4, 8, 0, 2 * math.pi); fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=3)
    
    # 飄動旗面
    f = math.sin(t * 7) * 8
    ctx.move_to(ex, ey)
    ctx.curve_to(ex + d * 45, ey - 8 + f, ex + d * 80, ey + 6 - f, ex + d * 118, ey + 24 + f * 0.5)
    ctx.curve_to(ex + d * 80, ey + 42 + f, ex + d * 45, ey + 56 - f, ex + d * 4, ey + 62)
    ctx.close_path()
    fillstroke(ctx, C['yellow'], stroke=C['navy'], lw=4)
    
    # 旗幟文字「小半天」
    ctx.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(20)
    tx = ex + d * 48
    ty = ey + 32 + f * 0.3
    text(ctx, "小半天", tx, ty, 20, C['navy'], bold=True)

def atian(ctx, x, y, s, t, mouth=0.0, wave=False, point=False, sweat=False, happy=True, look=0.0):
    """
    小半天導遊・阿天 (A-Tian)
    陽光開朗的在地青年導遊，戴戶外漁夫帽、竹葉徽章、穿綠色健行背心，拿「小半天」導遊旗
    """
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    
    # 腳下圓形陰影
    ctx.save(); ctx.scale(1, 0.18); ctx.arc(0, 250 / 0.18, 95, 0, 2 * math.pi); ctx.set_source_rgba(0, 0, 0, 0.10); ctx.fill(); ctx.restore()
    
    # 說話或呼吸時的上下輕微起伏
    bob = -abs(math.sin(t * 4.2)) * 12
    ctx.translate(0, bob + 200); ctx.rotate(math.sin(t * 2.1) * 0.05); ctx.translate(0, -200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)

    # 1. 雙腿與登山鞋
    for sd in (-1, 1):
        ctx.move_to(sd * 26, 196); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(28); ctx.stroke()
        ctx.move_to(sd * 26, 196); ctx.line_to(sd * 28, 234); ctx.set_source_rgb(*PANTS_ATIAN); ctx.set_line_width(20); ctx.stroke()
        # 登山短靴
        rrect(ctx, sd * 28 - 22 + sd * 6, 228, 46, 20, 10); fillstroke(ctx, BOOTS_COLOR, stroke=C['navy'], lw=4)
        # 靴帶細節
        ctx.move_to(sd * 28 - 6, 233); ctx.line_to(sd * 28 + 12, 233); ctx.set_source_rgb(*C['orange']); ctx.set_line_width(3); ctx.stroke()

    # 2. 內搭 T 恤身體
    ctx.move_to(-58, 86); ctx.curve_to(-72, 150, -74, 186, -70, 206); ctx.line_to(70, 206); ctx.curve_to(74, 186, 72, 150, 58, 86)
    ctx.curve_to(30, 72, -30, 72, -58, 86); ctx.close_path(); fillstroke(ctx, TEE_INNER, stroke=C['navy'], lw=5)

    # 3. 戶外健行背心（兩側前片 + 口袋）
    for sd in (-1, 1):
        ctx.move_to(sd * 58, 86); ctx.curve_to(sd * 72, 150, sd * 74, 186, sd * 70, 206); ctx.line_to(sd * 12, 206)
        ctx.line_to(sd * 8, 120); ctx.line_to(sd * 30, 78); ctx.close_path(); fillstroke(ctx, VEST_ATIAN, stroke=C['navy'], lw=5)
        # 口袋
        rrect(ctx, sd * 44 - 15, 148, 30, 26, 6); fillstroke(ctx, VEST_DARK, stroke=C['navy'], lw=3)
    
    # 4. 手臂與動作
    def arm(sx, sy, ex, ey):
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(26); ctx.stroke()
        ctx.move_to(sx, sy); ctx.line_to(ex, ey); ctx.set_source_rgb(*TEE_INNER); ctx.set_line_width(17); ctx.stroke()
        ctx.arc(ex, ey, 12, 0, 2 * math.pi); fillstroke(ctx, SKIN, stroke=C['navy'], lw=4)

    if wave:
        # 揮舞小半天導遊旗
        ang = -2.3 + 0.4 * math.sin(t * 9)
        hx, hy = -60 + math.cos(ang) * 74, 106 + math.sin(ang) * 74
        flag_atian(ctx, hx, hy, t, ang=-2.1 + 0.3 * math.sin(t * 9), L=125, d=-1)
        arm(-60, 106, hx, hy)
    else:
        hx, hy = -86, 160
        flag_atian(ctx, hx, hy, t, ang=-1.95, L=210, d=-1)
        arm(-60, 106, hx, hy)

    if point:
        ex, ey = 128, 44 + math.sin(t * 3) * 6
        arm(60, 106, ex, ey)
        star(ctx, ex + 28, ey - 26, 14, C['yellow'], 1, rot=t * 2, outline=True)
    else:
        arm(60, 106, 82, 170)

    # 5. 後腦勺短髮（清爽男孩短髮）
    ctx.move_to(-86, -15); ctx.curve_to(-90, 20, -82, 38, -60, 44); ctx.line_to(60, 44)
    ctx.curve_to(82, 38, 90, 20, 86, -15); ctx.curve_to(70, -80, -70, -80, -86, -15); ctx.close_path()
    fillstroke(ctx, HAIR_ATIAN, stroke=C['navy'], lw=5)

    # 6. 雙耳
    for sd in (-1, 1):
        ctx.arc(sd * 85, 2, 16, 0, 2 * math.pi); fillstroke(ctx, SKIN, stroke=C['navy'], lw=4)

    # 7. 臉部輪廓
    ctx.arc(0, -6, 80, 0, 2 * math.pi); fillstroke(ctx, SKIN, stroke=C['navy'], lw=5)

    # 8. 兩側鬢角與額前短髮瀏海（陽光清爽碎髮）
    # 鬢角
    for sd in (-1, 1):
        ctx.move_to(sd * 82, -18); ctx.line_to(sd * 82, 12); ctx.line_to(sd * 72, -4); ctx.close_path()
        fillstroke(ctx, HAIR_ATIAN, stroke=C['navy'], lw=3.5)

    # 額前短碎髮
    ctx.move_to(-80, -10); ctx.curve_to(-75, -42, -40, -52, -25, -30)
    ctx.curve_to(-15, -48, 10, -50, 20, -32)
    ctx.curve_to(35, -52, 65, -44, 80, -10)
    ctx.curve_to(60, -22, 35, -25, 20, -18)
    ctx.curve_to(0, -22, -25, -25, -45, -18); ctx.close_path()
    fillstroke(ctx, HAIR_ATIAN, stroke=C['navy'], lw=4.5)

    # 8. 戶外遮陽帽（漁夫帽/登山帽）
    # (a) 帽冠
    ctx.move_to(-76, -38); ctx.curve_to(-72, -112, 72, -112, 76, -38); ctx.close_path()
    fillstroke(ctx, HAT_COLOR, stroke=C['navy'], lw=5)

    # (b) 墨綠色帽帶
    rrect(ctx, -74, -58, 148, 20, 6); fillstroke(ctx, HAT_BAND, stroke=C['navy'], lw=3.5)
    bamboo_leaf_badge(ctx, 0, -48, s=1.1)

    # (c) 外翻帽沿（前後立體感弧形帽簷）
    ctx.move_to(-98, -34); ctx.curve_to(-40, -22, 40, -22, 98, -34)
    ctx.curve_to(106, -44, 88, -48, 76, -42)
    ctx.curve_to(35, -34, -35, -34, -76, -42)
    ctx.curve_to(-88, -48, -106, -44, -98, -34); ctx.close_path()
    fillstroke(ctx, HAT_COLOR, stroke=C['navy'], lw=5)

    # 9. 眼睛與表情
    blink = (t % 3.4) < 0.13
    for ex_ in (-30, 30):
        ctx.save(); ctx.translate(ex_ + look * 6, 8); ctx.scale(1, 0.12 if blink else 1)
        ctx.arc(0, 0, 12, 0, 2 * math.pi); ctx.set_source_rgb(*C['navy']); ctx.fill()
        if not blink:
            # 陽光朝氣高光
            ctx.arc(4, -4, 4.5, 0, 2 * math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
            ctx.arc(-3, 4, 2.0, 0, 2 * math.pi); ctx.fill()
        ctx.restore()
        # 陽光粗眉毛
        sd = -1 if ex_ < 0 else 1
        ctx.move_to(ex_ - 14, -20); ctx.curve_to(ex_ - 5, -27, ex_ + 5, -27, ex_ + 14, -20)
        ctx.set_source_rgb(*HAIR_ATIAN); ctx.set_line_width(5.5); ctx.stroke()

    # 雙頰陽光元氣腮紅
    for ex_ in (-52, 52):
        ctx.arc(ex_, 32, 12, 0, 2 * math.pi); ctx.set_source_rgba(*C['pink'], 0.75); ctx.fill()

    # 嘴型動態
    if mouth > 0.08:
        ctx.save(); ctx.translate(0, 42); ctx.scale(1, (4 + 18 * mouth) / 13); ctx.arc(0, 0, 13, 0, 2 * math.pi); ctx.restore()
        ctx.set_source_rgb(*C['navy']); ctx.fill_preserve(); ctx.new_path()
    else:
        if happy:
            ctx.arc(0, 32, 16, 0.15 * math.pi, 0.85 * math.pi)
        else:
            ctx.arc(0, 52, 12, 1.2 * math.pi, 1.8 * math.pi)
        ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()

    if sweat:
        dy = (t * 40) % 30
        ctx.move_to(92, -40 + dy); ctx.curve_to(76, -12 + dy, 80, 0 + dy, 92, 0 + dy)
        ctx.curve_to(104, 0 + dy, 108, -12 + dy, 92, -40 + dy); fillstroke(ctx, (0.55, 0.80, 1), lw=3)

    ctx.restore()

# 替換全域模板預設主持人為阿天
dc.doctor = atian

if __name__ == "__main__":
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    background(ctx, 0, 1)
    atian(ctx, 300, 330, 1.0, 0.5, 0, wave=True)
    atian(ctx, 700, 330, 1.0, 1.7, 0.6, point=True)
    atian(ctx, 1100, 540, 0.45, 2.2, 0)
    surf.write_to_png("atian.png")
    print("阿天角色預覽圖生成完成 -> atian.png")
