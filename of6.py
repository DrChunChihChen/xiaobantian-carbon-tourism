"""辦公室碳冒險：CASE #006 結案總動員！打造五星級綠色辦公室通關秘笈 (刑偵剪貼調查風格)"""
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
        "五星級", "26 到 28 度", "6%", "25%", "80%", "少一半", "五十公噸",
        "綠色辦公", "自動斷電", "電子簽章", "綠色採購", "下午茶福利金", "正式結案"
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

def smart_plug(ctx, x, y, s=1.0):
    """智慧節能定時排插"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 排插白色長條
    rrect(ctx, -75, -25, 150, 50, 8)
    ctx.set_source_rgb(0.95, 0.95, 0.96); ctx.fill_preserve()
    ctx.set_source_rgb(0.3, 0.35, 0.4); ctx.set_line_width(3); ctx.stroke()
    # 三個三孔插座
    for i in range(3):
        ix = -45 + i * 45
        ctx.rectangle(ix - 5, -12, 3, 10); ctx.rectangle(ix + 2, -12, 3, 10)
        ctx.arc(ix, 5, 3, 0, math.pi * 2)
        ctx.set_source_rgb(0.2, 0.25, 0.3); ctx.fill()
    # 綠色電源指示燈
    ctx.arc(60, 0, 5, 0, math.pi * 2); ctx.set_source_rgb(0.2, 0.85, 0.4); ctx.fill()
    ctx.restore()

def tea_mug(ctx, x, y, s=1.0):
    """茶水間環保馬克杯"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 杯身
    rrect(ctx, -28, -35, 56, 70, 8)
    ctx.set_source_rgb(0.2, 0.6, 0.45); ctx.fill_preserve()
    ctx.set_source_rgb(0.1, 0.3, 0.2); ctx.set_line_width(3); ctx.stroke()
    # 杯把
    ctx.move_to(28, -15); ctx.curve_to(50, -15, 50, 20, 28, 20)
    ctx.set_source_rgb(0.1, 0.3, 0.2); ctx.set_line_width(6); ctx.stroke()
    # 杯身環保葉片圖案
    ctx.arc(0, 0, 10, 0, math.pi); ctx.set_source_rgb(1, 1, 1); ctx.fill()
    ctx.restore()

def green_trophy(ctx, x, y, s=1.0):
    """減碳競賽金盃"""
    ctx.save(); ctx.translate(x, y); ctx.scale(s, s)
    # 底座
    ctx.rectangle(-25, 30, 50, 16); ctx.set_source_rgb(0.25, 0.25, 0.28); ctx.fill()
    ctx.rectangle(-15, 18, 30, 12); ctx.set_source_rgb(0.85, 0.7, 0.2); ctx.fill()
    # 獎杯杯體
    ctx.move_to(-30, -35); ctx.line_to(30, -35); ctx.line_to(20, 15); ctx.line_to(-20, 15); ctx.close_path()
    ctx.set_source_rgb(0.95, 0.8, 0.2); ctx.fill_preserve()
    ctx.set_source_rgb(0.65, 0.5, 0.1); ctx.set_line_width(3); ctx.stroke()
    # 雙耳把手
    for sign in (-1, 1):
        ctx.move_to(sign * 28, -25); ctx.curve_to(sign * 48, -20, sign * 48, 0, sign * 18, 5)
        ctx.set_source_rgb(0.85, 0.7, 0.2); ctx.set_line_width(4); ctx.stroke()
    # 綠色星標
    ctx.arc(0, -10, 8, 0, math.pi * 2); ctx.set_source_rgb(0.2, 0.8, 0.4); ctx.fill()
    ctx.restore()

# ==================== 場景定義 ====================

# 0 開場
def s0(ep, ctx, u, T, m):
    cork_bg(ctx)
    p = prog(u, 0.1, 0.45)
    if p > 0:
        ctx.save(); pop(ctx, 640, 320, p)
        torn_paper(ctx, 640, 320, 880, 430, ang=-0.015, bg=(0.96, 0.95, 0.91))
        black_tape(ctx, "CASE #006 最終結案總動員", 640, 160, size=28)
        text(ctx, "辦公室碳冒險：結案總通關秘笈", 640, 245, 48, (0.12, 0.12, 0.15))
        text(ctx, "從冷氣、拿鐵、紙張到 AI，重整企業日常排碳帳本！", 640, 310, 28, (0.45, 0.45, 0.50))
        red_pin(ctx, 230, 130); red_pin(ctx, 1050, 130)

        items = ["回顧六案：空調機房、外食杯盒、影印耗紙、單人自駕、硬體汰換", "終極挑戰：如何把高耗能辦公室，成功打造成五星級綠色企業？", "雙贏方程式：不增加員工麻煩、不浪費公司預算，一年省下數十萬！"]
        for i, it in enumerate(items):
            text(ctx, it, 640, 365 + i * 38, 22, (0.2, 0.2, 0.25))
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "終極結案 FINAL", 960, 175, ang=-0.14, s=1.05)

# 1 三大通關支柱
def s1(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THREE PILLARS 五星級綠色辦公室三大支柱", 640, 75, size=26)
    t1 = 0.5
    t2 = ep.kw(1, "五星級") - 1.0
    t3 = ep.kw(1, "綠色企業") - 0.5

    cards = [
        (t1, 260, 340, -0.04, "01 硬體節能智慧化", smart_plug),
        (t2, 640, 330, 0.03, "02 制度與流程革命", tea_mug),
        (t3, 1020, 345, -0.03, "03 全員參與減碳賽", green_trophy)
    ]
    pins = []
    for t_in, cx, cy, ang, title, drawer in cards:
        p = prog(u, t_in, 0.4)
        if p > 0:
            ctx.save(); pop(ctx, cx, cy, p)
            polaroid(ctx, cx, cy, 320, 360, ang, title)
            drawer(ctx, cx, cy - 30, 0.85)
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
    black_tape(ctx, "INTERROGATION 執行抗拒審訊", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 840, 380, ang=0.012, bg=(0.98, 0.96, 0.92))
        text(ctx, "傳統抗拒：減碳是不是又貴又麻煩？", 640, 210, 34, (0.85, 0.18, 0.15))
        text(ctx, "『員工抱怨不便、老闆擔心花錢，到底要怎麼在公司推動？』", 640, 275, 26, (0.3, 0.3, 0.35))

        green_trophy(ctx, 640, 350, 0.75)

        highlighter(ctx, 280, 445, 720, 45)
        text(ctx, "調查局警告：錯誤的方法才花錢！對的減碳反而為公司省大錢！", 640, 440, 26, (0.2, 0.2, 0.25))
        red_pin(ctx, 250, 180); red_pin(ctx, 1030, 180)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "消除阻力", 960, 215, ang=-0.16, s=1.1)

# 3 真相揭曉：落實綠色辦公省數十萬
def s3(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "THE REVEAL 環境部綠色辦公效益", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "五星級綠色辦公雙贏效應", 640, 195, 34, (0.15, 0.5, 0.25))

        # 兩大效益卡
        rrect(ctx, 230, 240, 380, 190, 12); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        text(ctx, "💰 有形財務實質回饋", 420, 270, 22, (0.15, 0.5, 0.25))
        text(ctx, "水電節約 25% + 採購紙張減 80%", 420, 310, 19, (0.3, 0.35, 0.35))
        chip(ctx, "每年省下數十萬水電採購預算", 420, 360, 1, C['green'], 20, C['white'])

        rrect(ctx, 670, 240, 380, 190, 12); ctx.set_source_rgb(0.92, 0.94, 0.98); ctx.fill()
        text(ctx, "🌱 無形企業永續競爭力", 860, 270, 22, (0.1, 0.4, 0.75))
        text(ctx, "通過政府認證 + 取得國際綠色訂單", 860, 310, 19, (0.35, 0.35, 0.4))
        chip(ctx, "ESG 評比卓越、吸引跨國頂級客戶", 860, 360, 1, (0.2, 0.5, 0.85), 19, C['white'])

        highlighter(ctx, 240, 465, 800, 48)
        text(ctx, "落實綠色辦公絕非成本負擔，而是提升利潤與形象的最佳投資！", 640, 460, 26, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "年省數十萬 WIN", 960, 215, ang=-0.14, s=1.05)

# 4 第一站：硬體節能智慧化
def s4(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 01 硬體節能與智慧感應", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=0.01, bg=(0.97, 0.95, 0.91))
        text(ctx, "硬體智慧節能：待機耗電歸零", 640, 195, 34, (0.15, 0.2, 0.25))

        steps = [
            ("❄️ 全面更換一級能效變頻空調", "較老舊定頻機種節能 30% 以上，運轉安靜效率高"),
            ("💡 人體微波感應 LED 平板燈", "茶水間、會議室與洗手間無人自動關燈，用電砍半"),
            ("🔌 下班定時自動斷電排插", "徹底切斷影印機、電腦螢幕的待機耗電，防止暗耗")
        ]
        for i, (s_t, s_d) in enumerate(steps):
            yy = 250 + i * 54
            rrect(ctx, 220, yy - 18, 840, 44, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, s_t, 460, yy + 6, 21, (0.15, 0.45, 0.25))
            text(ctx, s_d, 820, yy + 6, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 240, 455, 800, 48)
        text(ctx, "善用智慧硬體科技，不必靠人工苦苦監督也能自動省電！", 640, 450, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "待機耗電歸零", 960, 215, ang=-0.14, s=1.05)

# 5 第一站深入：冷氣定溫 26 到 28 度
def s5(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "CLIMATE RULE 空調黃金定溫法則", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.95, 0.91))
        text(ctx, "空調定溫 26~28 度黃金法則", 640, 195, 34, (0.15, 0.2, 0.25))

        # 計算與對比卡片
        rrect(ctx, 230, 240, 400, 170, 10); ctx.set_source_rgb(0.92, 0.95, 0.92); ctx.fill()
        text(ctx, "🌡️ 26°C ~ 28°C ＋ 循環風扇", 430, 270, 22, (0.15, 0.5, 0.25))
        text(ctx, "加強氣流循環，體感溫度立降 2 度", 430, 305, 19, (0.3, 0.35, 0.35))
        chip(ctx, "體感涼爽舒服、員工不感冒", 430, 350, 1, C['green'], 20, C['white'])

        rrect(ctx, 670, 240, 380, 170, 10); ctx.set_source_rgb(0.98, 0.92, 0.92); ctx.fill()
        text(ctx, "⚡ 驚人節能效益計算", 860, 270, 22, (0.85, 0.2, 0.2))
        text(ctx, "冷氣溫度每調高 1 度", 860, 305, 20, (0.4, 0.3, 0.3))
        text(ctx, "全棟即省 6% 空調用電！", 860, 345, 28, C['red'])

        highlighter(ctx, 240, 445, 800, 48)
        text(ctx, "夏天不再穿厚外套吹冷氣，省電、省錢又兼顧同仁健康！", 640, 440, 26, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "每升1度省6%", 960, 215, ang=-0.14, s=1.05)

# 6 第二站：制度與環境升級
def s6(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 02 制度與無塑環境升級", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.012, bg=(0.96, 0.95, 0.91))
        text(ctx, "無紙化與不塑環境升級", 640, 190, 34, (0.15, 0.5, 0.25))

        upgrades = [
            ("📄 全面電子公文與數位簽章", "跨部門報帳線上化，合約簽核無紙化，用紙減 80%"),
            ("🚰 採用節水標章感應水龍頭", "自動出水省水 40%，防止忘記關水造成的無謂水資源浪費"),
            ("🍽️ 茶水間設置高溫洗碗機與公用環保杯", "提供消毒杯盤餐具，徹底終結外送免洗餐具與塑膠袋")
        ]
        for i, (u_t, u_d) in enumerate(upgrades):
            yy = 250 + i * 54
            rrect(ctx, 220, yy - 18, 840, 44, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, u_t, 460, yy + 6, 21, (0.15, 0.45, 0.25))
            text(ctx, u_d, 820, yy + 6, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 240, 465, 800, 45)
        text(ctx, "完善基礎環境設施，讓員工不知不覺中自然養成減塑好習慣！", 640, 460, 26, (0.15, 0.5, 0.25))
        red_pin(ctx, 210, 155); red_pin(ctx, 1070, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "免洗餐具清零", 960, 215, ang=-0.14, s=1.05)

# 7 第二站深入：綠色採購標準
def s7(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "PROCUREMENT 企業綠色採購標準", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 400, ang=0.015, bg=(0.98, 0.96, 0.93))
        text(ctx, "綠色採購：從源頭垃圾清零", 640, 195, 34, (0.2, 0.2, 0.25))

        procures = [
            ("🌲 100% 選用 FSC 永續認證影印紙", "保證木材來自負責任管理的森林，不破壞原始雨林"),
            ("🖊️ 採購可替換筆芯與補充式文具", "拒絕一次性塑膠筆桿，文具用品使用壽命延長五倍"),
            ("📦 綠色供應鏈評選機制", "將供應商減碳承諾與包裝循環率納入年度採購評分")
        ]
        for i, (p_t, p_d) in enumerate(procures):
            yy = 250 + i * 50
            rrect(ctx, 220, yy - 18, 840, 42, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, p_t, 460, yy + 5, 21, (0.15, 0.45, 0.25))
            text(ctx, p_d, 820, yy + 5, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 250, 445, 780, 45)
        text(ctx, "用企業的採購預算，投票給保護地球的永續品牌！", 640, 440, 26, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 160); red_pin(ctx, 1060, 160)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "綠色標章優先", 960, 215, ang=-0.14, s=1.05)

# 8 第三站：激勵全員參與的減碳文化
def s8(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "SITE 03 激勵全員參與的減碳文化", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=-0.01, bg=(0.96, 0.96, 0.92))
        text(ctx, "全員參與：打造趣味減碳賽", 640, 195, 34, (0.15, 0.5, 0.25))

        challenges = [
            ("🍱 無塑外送吃貨週", "全員外食自備保溫盒打卡", (0.2, 0.5, 0.8)),
            ("🚶 綠色通勤步數大賽", "捷運步行爬樓梯累積里程", C['green']),
            ("🏆 部門減碳積分排行", "每季優勝隊伍奪得永續金盃", (0.9, 0.55, 0.1))
        ]
        for k, (t_box, d_box, col) in enumerate(challenges):
            cx = 320 + k * 320
            rrect(ctx, cx - 140, 250, 280, 140, 8); ctx.set_source_rgb(0.92, 0.94, 0.96); ctx.fill()
            chip(ctx, t_box, cx, 285, 1, col, 20, C['white'])
            text(ctx, d_box, cx, 345, 18, (0.3, 0.35, 0.4))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "把枯燥的環保規定，變成全體同仁樂在其中的團隊遊戲！", 640, 435, 28, (0.15, 0.5, 0.25))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "正向激勵 FUN", 960, 215, ang=-0.14, s=1.05)

# 9 減碳折算下午茶福利
def s9(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "INCENTIVE 減碳成果折算下午茶福利金", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 345, p)
        torn_paper(ctx, 640, 345, 880, 400, ang=0.012, bg=(0.97, 0.95, 0.91))
        text(ctx, "省下電費：全數回饋下午茶！", 640, 195, 34, (0.2, 0.2, 0.25))

        incentives = [
            ("🍰 50% 省下水電費回饋下午茶基金", "每季電費較去年同期降低的金額，一半撥充員工下午茶點心"),
            ("☕ 自備環保杯外帶咖啡現折 5 元補助", "公司額外加碼補貼，鼓勵同仁自備杯具，塑膠杯使用歸零"),
            ("🏅 年度綠色英雄獎與帶薪環保假", "表揚減碳貢獻最高的個人與部門，頒發帶薪一日環保志工假")
        ]
        for i, (i_t, i_d) in enumerate(incentives):
            yy = 250 + i * 50
            rrect(ctx, 220, yy - 18, 840, 42, 6); ctx.set_source_rgb(0.93, 0.94, 0.96); ctx.fill()
            text(ctx, i_t, 460, yy + 5, 21, (0.15, 0.45, 0.25))
            text(ctx, i_d, 820, yy + 5, 18, (0.45, 0.45, 0.5))

        highlighter(ctx, 250, 440, 780, 45)
        text(ctx, "讓每位同仁都能享受減碳的甜蜜果實，全員都是綠色行動家！", 640, 435, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 220, 155); red_pin(ctx, 1060, 155)
        ctx.restore()

    if u > 3.2:
        red_stamp(ctx, "全員共享 WIN-WIN", 960, 215, ang=-0.14, s=1.05)

# 10 結案成績單
def s10(ep, ctx, u, T, m):
    cork_bg(ctx)
    black_tape(ctx, "REPORT CARD 五星級綠色辦公室結案成績單", 640, 75, size=26)
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 900, 410, ang=-0.015, bg=(0.96, 0.95, 0.90))
        text(ctx, "年度卓越減碳成效總結", 640, 190, 34, (0.15, 0.2, 0.25))

        rows = [
            ("⚡ 辦公室用電度數", "節省 25%", "年減 15 公噸 CO2e", C['green']),
            ("📄 紙張公文消耗量", "減少 80%", "年減 8 公噸 CO2e", C['green']),
            ("🗑️ 垃圾與廢棄物量", "降低 50%", "年減 5 公噸 CO2e", C['green']),
            ("🚗 通勤與採購優化", "循環租賃", "年減 22 公噸 CO2e", C['green']),
        ]
        for k, (mode, amount, status, col) in enumerate(rows):
            yy = 245 + k * 50
            rrect(ctx, 230, yy - 18, 820, 42, 8); ctx.set_source_rgb(0.92, 0.93, 0.95); ctx.fill()
            text(ctx, mode, 380, yy + 6, 22, (0.2, 0.2, 0.25))
            chip(ctx, amount, 650, yy + 6, 1, col, 22, C['white'])
            text(ctx, status, 900, yy + 6, 20, (0.15, 0.5, 0.25))

        highlighter(ctx, 250, 455, 780, 45)
        text(ctx, "一家五星級綠色辦公室，一年替地球省下超過五十公噸碳！", 640, 450, 28, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 150); red_pin(ctx, 1070, 150)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "年省 50 噸碳", 960, 215, ang=-0.14, s=1.05)

# 11 結案報告與全劇終
def s11(ep, ctx, u, T, m):
    cork_bg(ctx)
    tt = T
    p = prog(u, 0.1, 0.4)
    if p > 0:
        ctx.save(); pop(ctx, 640, 350, p)
        torn_paper(ctx, 640, 350, 880, 410, ang=0.01, bg=(0.98, 0.96, 0.92))
        text(ctx, "《辦公室碳冒險》正式全劇終結案！", 640, 195, 36, (0.15, 0.2, 0.25))

        habits = [
            ("① 隨手關燈關機：徹底清零空載耗能", "節能好習慣", 1.0),
            ("② 自備杯盒餐具：享受健康不塑日常", "免洗餐具零", 2.5),
            ("③ 綠色採購大眾通勤：共創永續未來", "實質大減碳", tt - 0.5)
        ]
        for k, (title, eff, t_) in enumerate(habits):
            yy = 260 + k * 55
            black_tape(ctx, title, 500, yy, size=22, col=(1, 1, 1), bg=(0.2, 0.22, 0.26))
            chip(ctx, eff, 950, yy, 1, C['green'], 22, C['white'])

        highlighter(ctx, 280, 455, 720, 50)
        text(ctx, "每一個日常微小選擇，都在重新書寫地球的未來！", 640, 450, 30, (0.85, 0.15, 0.15))
        red_pin(ctx, 210, 165); red_pin(ctx, 1070, 165)
        ctx.restore()

    if u > 3.0:
        red_stamp(ctx, "全案偵破 SOLVED", 950, 190, ang=-0.14, s=1.1)

    if u > tt - 0.3:
        red_stamp(ctx, "正式結案 CLOSED", 950, 260, ang=-0.16, s=1.15)

# 執行
run("of6", "辦公室碳冒險 EP6",
    [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11],
    "辦公室碳冒險_EP6_五星級綠色辦公室通關秘笈.mp4",
    wipes={2, 4, 6, 8, 10, 11})
