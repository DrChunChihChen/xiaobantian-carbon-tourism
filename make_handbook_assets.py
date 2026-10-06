"""繪製手冊內部插圖：
1. itinerary_chart.png：小半天兩天一夜低碳示範遊程路線圖 (阿天導覽)
2. carbon_comparison.png：五大服務構面碳足跡對比圖 (小綠診斷)
"""
import cairo, math, random, os
from engine import W, H, C, rrect, fillstroke, text, pop
from atian import atian
from xl import xiaolu

def draw_itinerary_chart(output_path="itinerary_chart.png"):
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)

    # 1. 溫和米白紙感背景
    ctx.set_source_rgb(0.98, 0.97, 0.94); ctx.paint()

    # 頂部標題區
    rrect(ctx, 40, 25, 1200, 75, 20)
    fillstroke(ctx, (0.24, 0.54, 0.38), stroke=C['navy'], lw=4)
    text(ctx, "【示範遊程】小半天兩天一夜慢活低碳行旅路線圖", 640, 62, 28, C['white'], bold=True)

    # 左右兩欄：Day 1 與 Day 2
    # 左側：Day 1 翠竹晨嵐・瀑布尋幽
    rrect(ctx, 40, 120, 580, 560, 24)
    fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 40, 120, 580, 55, 24)
    fillstroke(ctx, (0.30, 0.65, 0.45), stroke=C['navy'], lw=3.5)
    text(ctx, "Day 1 · 翠竹晨嵐 · 瀑布尋幽（高負離子健行）", 330, 150, 20, C['white'], bold=True)

    d1_steps = [
        ("09:30", "長源圳步道 ＆ 孟宗竹林隧道", "全台最大孟宗竹海，林下散步零碳浴", (0.24, 0.56, 0.35)),
        ("12:00", "小半天在地竹筒飯風味餐", "在地小農鮮筍、減肉蔬食縮短食物里程", (0.85, 0.55, 0.25)),
        ("14:00", "德興瀑布水氣負離子洗禮", "雙層瀑布萬級負離子，自備水壺品山泉", (0.25, 0.55, 0.78)),
        ("16:30", "凍頂高山茶席 · 夕陽雲海", "鹿谷有機茶席品茗，體驗茶人炭焙文化", (0.82, 0.65, 0.25)),
        ("18:30", "下榻小半天綠色環保民宿", "自備盥洗備品、夜宿山嵐涼爽免冷氣", (0.45, 0.35, 0.65)),
    ]
    for idx, (t_str, title, desc, col) in enumerate(d1_steps):
        y = 210 + idx * 92
        # 時間節點
        ctx.arc(80, y, 16, 0, 2*math.pi); fillstroke(ctx, col, stroke=C['navy'], lw=2.5)
        text(ctx, str(idx+1), 80, y + 1, 14, C['white'], bold=True)
        if idx < len(d1_steps) - 1:
            ctx.move_to(80, y + 16); ctx.line_to(80, y + 76); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
        # 內容卡
        rrect(ctx, 115, y - 26, 485, 58, 12); fillstroke(ctx, (0.96, 0.98, 0.96), stroke=C['navy'], lw=2)
        text(ctx, t_str, 155, y - 6, 14, col, bold=True)
        text(ctx, title, 205, y - 6, 16, C['navy'], bold=True, align='l')
        text(ctx, desc, 155, y + 16, 12, (0.4, 0.45, 0.48), bold=False, align='l')

    # 右側：Day 2 竹藝傳承 · 茶香歸途
    rrect(ctx, 660, 120, 580, 560, 24)
    fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 660, 120, 580, 55, 24)
    fillstroke(ctx, (0.22, 0.54, 0.50), stroke=C['navy'], lw=3.5)
    text(ctx, "Day 2 · 竹藝傳承 · 茶香歸途（以竹代塑生活）", 950, 150, 20, C['white'], bold=True)

    d2_steps = [
        ("08:30", "石馬公園晨間漫步 ＆ 櫻花林", "漫步小半天台地晨光，觀察林相小氣候", (0.85, 0.45, 0.55)),
        ("10:00", "小半天竹藝工坊 DIY 體驗", "以竹代塑！手作竹筷、竹編杯墊帶回家", (0.24, 0.56, 0.35)),
        ("12:30", "社區低碳茶餐佐野菜時令風味", "在地友善耕作產地餐桌，無一次性餐盒", (0.85, 0.55, 0.25)),
        ("14:30", "在地小農市集 · 採買綠色伴手禮", "竹筍乾、烏龍茶、竹炭花生，裸包裝減塑", (0.25, 0.55, 0.78)),
        ("16:00", "搭乘台灣好行低碳返程", "公共運具減碳 66%，完成無痕綠色旅行", (0.22, 0.54, 0.50)),
    ]
    for idx, (t_str, title, desc, col) in enumerate(d2_steps):
        y = 210 + idx * 92
        ctx.arc(700, y, 16, 0, 2*math.pi); fillstroke(ctx, col, stroke=C['navy'], lw=2.5)
        text(ctx, str(idx+1), 700, y + 1, 14, C['white'], bold=True)
        if idx < len(d2_steps) - 1:
            ctx.move_to(700, y + 16); ctx.line_to(700, y + 76); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(3); ctx.stroke()
        rrect(ctx, 735, y - 26, 485, 58, 12); fillstroke(ctx, (0.95, 0.98, 0.98), stroke=C['navy'], lw=2)
        text(ctx, t_str, 775, y - 6, 14, col, bold=True)
        text(ctx, title, 825, y - 6, 16, C['navy'], bold=True, align='l')
        text(ctx, desc, 775, y + 16, 12, (0.4, 0.45, 0.48), bold=False, align='l')

    # 在地嚮導阿天在角落點讚提示
    atian(ctx, 1170, 560, 0.38, 1.0, mouth=0.0, wave=True)

    # 外框
    ctx.rectangle(0, 0, W, H); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(10); ctx.stroke()
    surf.write_to_png(output_path)
    print(f"路線圖生成完畢 -> {output_path}")

def draw_carbon_comparison(output_path="carbon_comparison.png"):
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)

    # 1. 背景色
    ctx.set_source_rgb(0.96, 0.97, 0.98); ctx.paint()

    # 頂部標題區
    rrect(ctx, 40, 25, 1200, 75, 20)
    fillstroke(ctx, (0.18, 0.45, 0.65), stroke=C['navy'], lw=4)
    text(ctx, "【數據實測】每位旅客遊程碳足跡五大構面減碳對比分析", 640, 62, 28, C['white'], bold=True)

    # 左側：總量對比柱狀卡
    rrect(ctx, 40, 120, 360, 560, 24)
    fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 40, 120, 360, 52, 24)
    fillstroke(ctx, C['navy'], stroke=C['navy'], lw=3.5)
    text(ctx, "遊程人均碳排放總量對比", 220, 148, 18, C['white'], bold=True)

    # 傳統遊程柱狀 (48.6 kg)
    rrect(ctx, 90, 210, 100, 360, 16)
    fillstroke(ctx, (0.88, 0.35, 0.35), stroke=C['navy'], lw=3)
    text(ctx, "48.6", 140, 245, 24, C['white'], bold=True)
    text(ctx, "kg", 140, 275, 16, C['white'], bold=True)
    text(ctx, "傳統自駕遊", 140, 595, 16, (0.88, 0.35, 0.35), bold=True)

    # 低碳遊程柱狀 (16.8 kg)
    bar_h = 360 * (16.8 / 48.6)
    rrect(ctx, 230, 210 + (360 - bar_h), 100, bar_h, 16)
    fillstroke(ctx, (0.24, 0.64, 0.40), stroke=C['navy'], lw=3)
    text(ctx, "16.8", 280, 210 + (360 - bar_h) + 35, 24, C['white'], bold=True)
    text(ctx, "kg", 280, 210 + (360 - bar_h) + 65, 16, C['white'], bold=True)
    text(ctx, "小半天低碳遊", 280, 595, 16, (0.24, 0.64, 0.40), bold=True)

    # 減碳減量幅度徽章
    rrect(ctx, 90, 625, 240, 42, 21)
    fillstroke(ctx, (0.98, 0.85, 0.30), stroke=C['navy'], lw=3)
    text(ctx, "實質減碳達 -65.4%", 210, 648, 18, C['navy'], bold=True)

    # 右側：五大服務構面明細表格與進度條
    rrect(ctx, 425, 120, 815, 560, 24)
    fillstroke(ctx, C['white'], stroke=C['navy'], lw=3.5)
    rrect(ctx, 425, 120, 815, 52, 24)
    fillstroke(ctx, (0.22, 0.56, 0.52), stroke=C['navy'], lw=3.5)
    text(ctx, "交通部觀光署五大服務構面明細清冊 (依 114 最新係數試算)", 832, 148, 18, C['white'], bold=True)

    items = [
        ("① 交通運輸服務", "自駕小客車 240km 改搭 台灣好行大巴+低碳接駁", "28.5 kg", "9.6 kg", "-66.3%", (0.25, 0.55, 0.78), 28.5, 9.6),
        ("② 餐飲美食服務", "傳統多肉豪華合菜 改選 在地時令竹筍蔬食風味餐", "14.2 kg", "3.8 kg", "-73.2%", (0.85, 0.55, 0.25), 14.2, 3.8),
        ("③ 住宿旅館服務", "一般飯店+拋棄式備品 改住 環保標章民宿+自備毛巾牙刷", "5.2 kg", "2.4 kg", "-53.8%", (0.45, 0.35, 0.65), 5.2, 2.4),
        ("④ 遊憩體驗服務", "市售塑膠外來紀念品 改為 孟宗竹工藝 DIY (以竹代塑天然固碳)", "0.5 kg", "0.8 kg", "以竹代塑", (0.24, 0.56, 0.35), 0.5, 0.8),
        ("⑤ 門市與廢棄物", "紙本手冊+瓶裝水垃圾 改為 數位微手冊+自備保溫瓶 0 廢棄", "0.2 kg", "0.2 kg", "源頭減量", (0.40, 0.45, 0.50), 0.2, 0.2),
    ]

    for idx, (cat, desc, c_base, c_low, rate, col, v_base, v_low) in enumerate(items):
        y = 205 + idx * 95
        # 標題與描述
        rrect(ctx, 445, y - 22, 180, 32, 8); fillstroke(ctx, col, stroke=C['navy'], lw=2)
        text(ctx, cat, 535, y - 4, 14, C['white'], bold=True)
        text(ctx, desc, 640, y - 4, 13, (0.35, 0.40, 0.45), bold=False, align='l')

        # 數值對照
        text(ctx, f"基準: {c_base}", 450, y + 26, 14, (0.80, 0.30, 0.30), bold=True, align='l')
        text(ctx, f"低碳: {c_low}", 570, y + 26, 14, (0.20, 0.60, 0.35), bold=True, align='l')
        rrect(ctx, 690, y + 10, 85, 26, 6); fillstroke(ctx, (0.92, 0.96, 0.92), stroke=(0.20, 0.60, 0.35), lw=1.5)
        text(ctx, rate, 732, y + 25, 13, (0.15, 0.50, 0.25), bold=True)

        # 比較橫條可視化
        max_w = 420
        # 基準條
        bw1 = (v_base / 30.0) * max_w
        rrect(ctx, 790, y + 10, bw1, 11, 4); fillstroke(ctx, (0.88, 0.45, 0.45), stroke=C['navy'], lw=1.5)
        # 低碳條
        bw2 = (v_low / 30.0) * max_w
        rrect(ctx, 790, y + 25, bw2, 11, 4); fillstroke(ctx, (0.30, 0.70, 0.45), stroke=C['navy'], lw=1.5)

    # 碳盤專家小綠在右下角說明
    xiaolu(ctx, 1170, 560, 0.38, 1.0, mouth=0.0, point=True)

    # 外框
    ctx.rectangle(0, 0, W, H); ctx.set_source_rgb(*C['navy']); ctx.set_line_width(10); ctx.stroke()
    surf.write_to_png(output_path)
    print(f"對比圖生成完畢 -> {output_path}")

if __name__ == "__main__":
    draw_itinerary_chart()
    draw_carbon_comparison()
