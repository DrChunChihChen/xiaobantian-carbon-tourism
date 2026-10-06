"""繪製《小半天永續低碳漫遊與遊程碳盤查手冊》封面主視覺大圖
結合：阿天 (在地嚮導) + 小綠 (碳盤查導遊) + 孟宗竹林 + 凍頂茶山 + 碳足跡徽章 + 復古手繪剪貼質感
"""
import cairo, math, random, os
import dc
from engine import W, H, C, rrect, fillstroke, text, pop, ease_out
from atian import atian
from xl import xiaolu

def draw_cover(output_path="cover.png"):
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)

    # 1. 底色背景：小半天山巒晨嵐漸層
    pat_bg = cairo.LinearGradient(0, 0, 0, H)
    pat_bg.add_color_stop_rgb(0.0, 0.92, 0.96, 0.94)  # 晨光透亮微藍綠
    pat_bg.add_color_stop_rgb(0.4, 0.88, 0.94, 0.88)  # 孟宗竹海清新淡綠
    pat_bg.add_color_stop_rgb(0.75, 0.96, 0.93, 0.84) # 暖金茶香大地
    pat_bg.add_color_stop_rgb(1.0, 0.82, 0.76, 0.65)  # 復古紙感木質調
    ctx.set_source(pat_bg)
    ctx.paint()

    # 2. 柔和白雲與雲海飄嵐
    def cloud(cx, cy, rx, ry, alpha=0.65):
        ctx.save()
        ctx.set_source_rgba(1.0, 1.0, 1.0, alpha)
        for dx, dy, r in [(0, 0, ry), (-rx*0.4, ry*0.1, ry*0.75), (rx*0.4, ry*0.1, ry*0.75),
                          (-rx*0.2, -ry*0.25, ry*0.7), (rx*0.2, -ry*0.25, ry*0.7)]:
            ctx.arc(cx + dx, cy + dy, r, 0, 2*math.pi)
            ctx.fill()
        ctx.restore()

    cloud(180, 260, 200, 48, 0.7)
    cloud(640, 230, 240, 52, 0.75)
    cloud(1100, 270, 220, 46, 0.65)

    # 3. 遠景山巒輪廓 (鹿谷凍頂山嶺)
    ctx.save()
    ctx.move_to(0, 360)
    ctx.curve_to(320, 290, 680, 380, 1000, 310)
    ctx.curve_to(1150, 280, 1240, 320, 1280, 300)
    ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    pat_mountain = cairo.LinearGradient(0, 280, 0, 720)
    pat_mountain.add_color_stop_rgba(0.0, 0.45, 0.68, 0.52, 0.45)
    pat_mountain.add_color_stop_rgba(1.0, 0.25, 0.50, 0.35, 0.75)
    ctx.set_source(pat_mountain)
    ctx.fill()
    ctx.restore()

    # 4. 孟宗竹林剪影（左右兩側環抱構圖）
    def bamboo_stalk(x, y0, y1, width, col=(0.28, 0.56, 0.36)):
        ctx.save()
        ctx.set_line_cap(cairo.LINE_CAP_BUTT)
        h_seg = 65
        curr_y = y0
        while curr_y < y1:
            next_y = min(curr_y + h_seg, y1)
            ctx.move_to(x, curr_y)
            ctx.line_to(x, next_y - 4)
            ctx.set_source_rgb(*col)
            ctx.set_line_width(width)
            ctx.stroke()
            # 竹節環
            ctx.move_to(x - width*0.65, next_y - 2)
            ctx.line_to(x + width*0.65, next_y - 2)
            ctx.set_source_rgb(0.18, 0.38, 0.24)
            ctx.set_line_width(4)
            ctx.stroke()
            curr_y = next_y
        ctx.restore()

    # 左側竹林群
    bamboo_stalk(45, 120, 720, 16, (0.24, 0.48, 0.30))
    bamboo_stalk(85, 80, 720, 18, (0.28, 0.54, 0.34))
    bamboo_stalk(135, 150, 720, 14, (0.34, 0.60, 0.40))
    
    # 右側竹林群
    bamboo_stalk(1140, 140, 720, 15, (0.34, 0.60, 0.40))
    bamboo_stalk(1190, 80, 720, 18, (0.28, 0.54, 0.34))
    bamboo_stalk(1235, 120, 720, 16, (0.24, 0.48, 0.30))

    # 竹葉飄舞裝飾
    def leaf_draw(lx, ly, sc, rot):
        ctx.save()
        ctx.translate(lx, ly); ctx.scale(sc, sc); ctx.rotate(rot)
        ctx.move_to(0, -14); ctx.curve_to(12, -8, 12, 8, 0, 14); ctx.curve_to(-12, 8, -12, -8, 0, -14); ctx.close_path()
        fillstroke(ctx, (0.38, 0.72, 0.42), stroke=C['navy'], lw=2.2)
        ctx.restore()

    leaves = [
        (90, 130, 0.9, -0.4), (60, 210, 1.1, 0.5), (140, 190, 0.8, -0.7),
        (1160, 160, 1.0, 0.6), (1210, 230, 0.9, -0.5), (1120, 210, 0.8, 0.4),
        (260, 290, 0.7, 0.3), (1020, 280, 0.75, -0.6)
    ]
    for lx, ly, sc, rot in leaves:
        leaf_draw(lx, ly, sc, rot)

    # 5. 地面綠色斜坡（營造開闊草地）
    ctx.save()
    ctx.move_to(0, 520)
    ctx.curve_to(340, 480, 750, 540, 1280, 500)
    ctx.line_to(1280, 720); ctx.line_to(0, 720); ctx.close_path()
    pat_ground = cairo.LinearGradient(0, 500, 0, 720)
    pat_ground.add_color_stop_rgb(0.0, 0.32, 0.64, 0.42)
    pat_ground.add_color_stop_rgb(1.0, 0.20, 0.46, 0.30)
    ctx.set_source(pat_ground)
    ctx.fill_preserve()
    ctx.set_source_rgb(*C['navy'])
    ctx.set_line_width(6)
    ctx.stroke()
    ctx.restore()

    # 6. 中央上半部：精緻手冊書名標題卡 (Cover Title Header Box)
    cx, cy = 640, 135
    w_box, h_box = 860, 195
    # 標題外框投影
    rrect(ctx, cx - w_box/2 + 8, cy - h_box/2 + 8, w_box, h_box, 28)
    ctx.set_source_rgba(0.12, 0.20, 0.15, 0.22); ctx.fill()

    # 標題卡底色（米白柔和底＋金綠外框）
    rrect(ctx, cx - w_box/2, cy - h_box/2, w_box, h_box, 28)
    ctx.set_source_rgb(0.99, 0.98, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(*C['navy']); ctx.set_line_width(5); ctx.stroke()

    # 內框細金線裝飾
    rrect(ctx, cx - w_box/2 + 8, cy - h_box/2 + 8, w_box - 16, h_box - 16, 22)
    ctx.set_source_rgb(0.85, 0.72, 0.42); ctx.set_line_width(2.5); ctx.stroke()

    # 頂部小標籤（標籤晶片）
    chip_w, chip_h = 360, 32
    rrect(ctx, cx - chip_w/2, cy - h_box/2 - 16, chip_w, chip_h, 16)
    fillstroke(ctx, (0.24, 0.58, 0.42), stroke=C['navy'], lw=3)
    text(ctx, "觀光署指引架構 ＋ 小半天低碳創生", cx, cy - h_box/2 + 1, 15, C['white'], bold=True)

    # 主標題第一行
    text(ctx, "小半天永續低碳漫遊", cx, cy - 32, 40, (0.16, 0.42, 0.26), bold=True)
    # 主標題第二行
    text(ctx, "與遊程碳盤查實務手冊", cx, cy + 18, 44, C['navy'], bold=True)

    # 副標題
    sub_tag = "綠色竹海生態 · 凍頂茶香旬味 · 五大構面碳足跡精準量化指引"
    text(ctx, sub_tag, cx, cy + 62, 18, (0.35, 0.45, 0.40), bold=True)

    # 7. 雙主角同台登場！
    # 左側主角：小半天在地嚮導・阿天 (A-Tian)，持小半天導遊旗揮手
    atian(ctx, 280, 435, 0.95, 1.2, mouth=0.0, wave=True, happy=True)
    # 阿天名牌徽章
    rrect(ctx, 150, 630, 260, 48, 24); fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 154, 634, 80, 40, 20); fillstroke(ctx, (0.26, 0.56, 0.38), stroke=C['navy'], lw=2.5)
    text(ctx, "在地嚮導", 194, 654, 16, C['white'], bold=True)
    text(ctx, "阿天 (A-Tian)", 315, 655, 20, C['navy'], bold=True)

    # 右側主角：碳盤查導遊・小綠 (Xiao-Lu)，持 CO2 計數旗指引
    xiaolu(ctx, 1000, 435, 0.95, 1.5, mouth=0.0, wave=True, point=True, happy=True)
    # 小綠名牌徽章
    rrect(ctx, 870, 630, 260, 48, 24); fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 874, 634, 80, 40, 20); fillstroke(ctx, C['teal2'], stroke=C['navy'], lw=2.5)
    text(ctx, "碳盤專家", 914, 654, 16, C['white'], bold=True)
    text(ctx, "小綠 (Xiao-Lu)", 1035, 655, 20, C['navy'], bold=True)

    # 8. 中央下方的核心亮點資訊卡 (Central Highlights Card)
    mid_cx, mid_cy = 640, 455
    card_w = 310
    rrect(ctx, mid_cx - card_w/2, mid_cy - 120, card_w, 240, 24)
    ctx.set_source_rgba(1.0, 1.0, 1.0, 0.95); ctx.fill_preserve()
    ctx.set_source_rgb(*C['navy']); ctx.set_line_width(4); ctx.stroke()

    # 亮點標籤列表（繪製向量微圖示）
    items = [
        ("孟宗竹海・以竹代塑", (0.24, 0.56, 0.35), "leaf"),
        ("凍頂茶席・在地旬味", (0.85, 0.55, 0.25), "tea"),
        ("遊程五大服務碳盤查", (0.25, 0.55, 0.78), "chart"),
        ("示範旅程減碳 65.4%", (0.88, 0.32, 0.32), "down"),
        ("觀光署指引標準對齊", (0.45, 0.35, 0.65), "star"),
    ]
    for idx, (label, color, icon_type) in enumerate(items):
        iy = mid_cy - 85 + idx * 42
        rrect(ctx, mid_cx - 145, iy - 16, 290, 34, 17)
        ctx.set_source_rgba(color[0], color[1], color[2], 0.12); ctx.fill_preserve()
        ctx.set_source_rgb(*color); ctx.set_line_width(2.2); ctx.stroke()

        # 繪製小向量 icon
        ix = mid_cx - 120
        ctx.save()
        if icon_type == "leaf":
            leaf_draw(ix, iy, 0.55, -0.4)
        elif icon_type == "tea":
            ctx.arc(ix, iy, 6, 0, 2*math.pi); fillstroke(ctx, color, stroke=C['navy'], lw=1.8)
        elif icon_type == "chart":
            for bar_i, bh in enumerate([6, 12, 16]):
                ctx.rectangle(ix - 7 + bar_i*6, iy + 8 - bh, 4, bh)
                fillstroke(ctx, color, stroke=C['navy'], lw=1.5)
        elif icon_type == "down":
            ctx.move_to(ix - 7, iy - 5); ctx.line_to(ix + 6, iy + 6)
            ctx.set_source_rgb(*color); ctx.set_line_width(3); ctx.stroke()
            ctx.move_to(ix + 6, iy - 1); ctx.line_to(ix + 6, iy + 6); ctx.line_to(ix - 1, iy + 6)
            ctx.set_source_rgb(*color); ctx.set_line_width(2.5); ctx.stroke()
        elif icon_type == "star":
            ctx.arc(ix, iy, 6, 0, 2*math.pi); fillstroke(ctx, color, stroke=C['navy'], lw=1.8)
        ctx.restore()

        text(ctx, label, mid_cx + 10, iy + 1, 16, color, bold=True)

    # 9. 復古品質認證印章 (Quality Stamp Sticker)
    stamp_x, stamp_y = 640, 635
    ctx.save()
    ctx.translate(stamp_x, stamp_y); ctx.rotate(-0.06)
    rrect(ctx, -100, -22, 200, 44, 12)
    ctx.set_source_rgb(0.92, 0.32, 0.32); ctx.fill_preserve()
    ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3.5); ctx.stroke()
    text(ctx, "★ 2026 淨零永續版 ★", 0, 1, 16, C['white'], bold=True)
    ctx.restore()

    # 10. 四角微暗角與精緻邊框 (Border & Framing)
    ctx.save()
    ctx.rectangle(0, 0, W, H)
    ctx.set_source_rgb(*C['navy'])
    ctx.set_line_width(12)
    ctx.stroke()
    ctx.restore()

    surf.write_to_png(output_path)
    print(f"手冊封面繪製完成 -> {output_path}")

if __name__ == "__main__":
    draw_cover()
