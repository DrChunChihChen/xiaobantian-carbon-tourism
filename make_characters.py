"""繪製阿天與綠導遊（小綠）專屬立繪頭像卡 (Transparent PNG / High-res Cards)
"""
import cairo, math
import dc
from engine import C, rrect, fillstroke, text
from atian import atian
from xl import xiaolu

def draw_real_atian(output_path="real_atian.png", size=500):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)
    # 背景光圈
    ctx.save()
    pat = cairo.RadialGradient(size/2, size/2 + 20, 40, size/2, size/2 + 20, size*0.48)
    pat.add_color_stop_rgba(0.0, 0.92, 0.98, 0.92, 0.95)
    pat.add_color_stop_rgba(0.7, 0.85, 0.95, 0.86, 0.7)
    pat.add_color_stop_rgba(1.0, 0.85, 0.95, 0.86, 0.0)
    ctx.arc(size/2, size/2 + 20, size*0.45, 0, 2*math.pi)
    ctx.set_source(pat)
    ctx.fill()
    ctx.restore()

    # 繪製阿天
    atian(ctx, size/2 + 25, size/2 + 50, 0.82, t=1.2, mouth=0.0, wave=True, happy=True)
    surf.write_to_png(output_path)
    print(f"真阿天頭像繪製完成 -> {output_path}")

def draw_real_xiaolu(output_path="real_xiaolu.png", size=500):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)
    # 背景光圈
    ctx.save()
    pat = cairo.RadialGradient(size/2, size/2 + 20, 40, size/2, size/2 + 20, size*0.48)
    pat.add_color_stop_rgba(0.0, 0.88, 0.98, 0.96, 0.95)
    pat.add_color_stop_rgba(0.7, 0.80, 0.92, 0.94, 0.7)
    pat.add_color_stop_rgba(1.0, 0.80, 0.92, 0.94, 0.0)
    ctx.arc(size/2, size/2 + 20, size*0.45, 0, 2*math.pi)
    ctx.set_source(pat)
    ctx.fill()
    ctx.restore()

    # 繪製小綠
    xiaolu(ctx, size/2 - 25, size/2 + 50, 0.82, t=1.5, mouth=0.0, wave=True, point=True, happy=True)
    surf.write_to_png(output_path)
    print(f"真綠導遊小綠頭像繪製完成 -> {output_path}")

if __name__ == "__main__":
    draw_real_atian()
    draw_real_xiaolu()
