import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    header = section.header
    hp = header.paragraphs[0]
    hp.text = "國立臺中科技大學 URR團隊 ｜ 小半天永續低碳漫遊與遊程碳盤查實務成果報告"
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(8.5)
    hp.style.font.color.rgb = RGBColor(120, 120, 120)

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.text = "小半天永續低碳漫遊手冊暨互動網站成果報告書 · 2026 淨零實踐版"
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.style.font.name = "Arial"
    fp.style.font.size = Pt(8.5)
    fp.style.font.color.rgb = RGBColor(140, 140, 140)

def set_cell_background(cell, fill_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_title(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = RGBColor(6, 78, 59) # Deep emerald

def add_subtitle(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(16)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 118, 110)

def add_meta_box():
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F0FDF4")
    set_cell_margins(cell, 150, 150, 200, 200)
    
    borders_xml = f'''
    <w:tcBorders {nsdecls("w")}>
        <w:top w:val="single" w:sz="12" w:space="0" w:color="10B981"/>
        <w:left w:val="single" w:sz="24" w:space="0" w:color="059669"/>
        <w:bottom w:val="single" w:sz="12" w:space="0" w:color="10B981"/>
        <w:right w:val="single" w:sz="12" w:space="0" w:color="10B981"/>
    </w:tcBorders>
    '''
    cell._tc.get_or_add_tcPr().append(parse_xml(borders_xml))
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(2)
    cp.paragraph_format.space_after = Pt(2)
    
    lines = [
        ("執行團隊：", "國立臺中科技大學 URR團隊（大學社會責任實踐與地方創生團隊）"),
        ("企劃主題：", "小半天永續低碳漫遊與遊程碳盤查實務手冊暨互動網站"),
        ("雙導遊主持：", "小半天在地嚮導・阿天 (A-Tian) ✕ 專業遊程碳盤查導遊・小綠 (Xiao-Lu)"),
        ("指導規範：", "交通部觀光署《旅行業遊程碳足跡計算指引》、ISO 14067、環境部最新公告係數"),
        ("基準電力係數：", "114 年度最新電力排放係數 0.466 kg CO₂e/度"),
        ("成果產出：", "完整永續手冊全文（含六大篇章與附錄）、全自包含互動網站平台（index.html）、本成果報告書")
    ]
    for label, val in lines:
        p = cell.add_paragraph() if cell.paragraphs[0].text else cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(label + " ")
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(6, 95, 70)
        r2 = p.add_run(val)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = RGBColor(6, 95, 70)
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 118, 110)
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_body_p(text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.2
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_callout(text, title="重點提示", fill_hex="ECFDF5", border_hex="10B981"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    borders_xml = f'''
    <w:tcBorders {nsdecls("w")}>
        <w:top w:val="none"/>
        <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>
        <w:bottom w:val="none"/>
        <w:right w:val="none"/>
    </w:tcBorders>
    '''
    cell._tc.get_or_add_tcPr().append(parse_xml(borders_xml))
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(2)
    cp.paragraph_format.space_after = Pt(2)
    r1 = cp.add_run(f"【{title}】 ")
    r1.font.bold = True
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = RGBColor(6, 95, 70)
    r2 = cp.add_run(text)
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_figure(img_path, caption):
    if os.path.exists(img_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run()
        run.add_picture(img_path, width=Inches(5.8))
        
        cp = doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.paragraph_format.space_before = Pt(1)
        cp.paragraph_format.space_after = Pt(8)
        c_run = cp.add_run(f"▲ {caption}")
        c_run.font.name = "Arial"
        c_run.font.size = Pt(9)
        c_run.font.bold = True
        c_run.font.color.rgb = RGBColor(71, 85, 105)

print("Starting document content compilation...")

# --- Title Section ---
add_title("《小半天永續低碳漫遊與遊程碳盤查實務手冊暨互動網站成果報告書》")
add_subtitle("綠色竹海生態・凍頂茶香旬味・五大構面碳足跡精準量化與全數位自包含互動平台開發")
add_meta_box()

# --- Chapter 1 ---
add_heading_1("第一章：專案背景與執行願景")

add_heading_2("1.1 政策驅動與綠色永續旅遊轉型")
add_body_p("在全球加速迎向 2050 淨零排放（Net Zero Emissions）、台灣正式公布《臺灣 2050 淨零轉型關鍵戰略》之際，觀光與旅行產業亦迎來深度的低碳典範轉移。傳統觀光模式長期以來面臨高自駕比例、高石化燃料依賴、高肉品食材里程及一次性塑膠備品過量等問題，導致每趟遊程產生可觀的溫室氣體排放。為此，交通部觀光署積極推動《旅行業遊程碳足跡計算指引》，鼓勵旅行業者針對其產品進行碳盤查並申請產品碳標籤；各大上市櫃企業在編撰 ESG 永續報告書及採購員工旅遊或獎勵旅遊時，亦高度要求供應商提供清晰量化之碳足跡報告。")

add_heading_2("1.2 鹿谷小半天場域特質與高碳匯生態底蘊")
add_body_p("南投縣鹿谷鄉「小半天」地區（涵蓋竹林村、竹豐村與和雅村）坐落於海拔 600 至 1,100 公尺之隆起高位台地，東倚鳳凰山脈，北與西為北勢溪與溪頭群山環繞。此一獨特微氣候常年雲霧繚繞、日夜溫差達 8～10℃，形成全台面積最大、密度最高的孟宗竹林聚落（覆蓋超過 2,000 公頃）。孟宗竹（Phyllostachys pubescens）為生長極迅速之多年生禾本科植物，40～60 天即可成竹，其年生質累積速率與吸碳能力為一般溫帶闊葉林木之 1.5 至 2.0 倍，整座竹海每年碳吸存潛力高達 2.4 萬至 3 萬噸 CO₂。此外，小半天擁有清代鑿建之「長源圳生態步道」、萬級負離子飛瀑「德興瀑布」、全台烏龍茶發源之凍頂茶席，以及罕見之「石馬公園」河津櫻雙開奇景，具備發展高品質零碳慢活行旅之絕佳風土條件。")

add_heading_2("1.3 核心宗旨：從口號走向精準量化的實務指引")
add_body_p("以往許多永續旅遊專案多停留在「自備環保筷」、「隨手關燈」等口號式倡議，缺乏具公信力之科學盤查數據支撐，導致民眾與旅遊從業人員難以具體感知減碳效益。國立臺中科技大學 URR團隊（大學社會責任與地方創生團隊）針對此一痛點，以觀光署官方指引為骨幹、小半天在地特色為載體，打造了一套「算得清、看得見、可驗證」的實務手冊與互動平台，讓旅行社同業有明確工具依循，讓旅人深刻體會每項綠色選擇帶來的減碳成效。")

add_heading_2("1.4 雙導遊企劃特色：在地青年「阿天」✕ 專業碳盤專家「小綠」")
add_body_p("為解決法規與碳排計算容易給人枯燥艱澀的距離感，本專案首創「雙導遊聯手主持」之 IP 敘事框架：")
add_bullet("在地熱血青年，頭戴綴有嫩綠竹葉徽章的卡其遮陽帽、身穿山林綠背心，手持小半天導遊旗。熟悉竹海步道、茶席文化與以竹代塑生活工藝，負責帶領旅人領略在地人文與生態之美。", "小半天在地嚮導・阿天 (A-Tian)：")
add_bullet("遊程碳盤查專家，頭戴休閒綠帽、佩戴星型髮夾，手持代表溫室氣體的黃色 CO₂ 計數旗。專精觀光署指引公式與 ISO 14067，負責以生動易懂的語言拆解計算邏輯與減碳效益。", "碳盤查專家導遊・小綠 (Xiao-Lu)：")
add_body_p("雙主角同台穿梭於手冊章節與網站各模組，形成「感性在地深度體驗」與「理性科學碳排量化」的完美交織。")

# --- Chapter 2 ---
add_heading_1("第二章：永續實務手冊製作內容與方法學架構")
add_body_p("《小半天永續低碳漫遊與遊程碳盤查實務手冊》以五大篇章及附錄組成，架構嚴謹、內容詳實，兼顧旅遊導覽性與標準作業程序（SOP）之工具性：")

add_heading_2("2.1 篇章一：走進仙境小半天（地理人文與生態底蘊）")
add_bullet("台地地形與微氣候成因：闡述海拔 600～1,100 公尺高位河階台地地形，水氣在日夜溫差下凝結形成雲霧仙境之由來。", "1.1 地形氣候：")
add_bullet("2,000公頃孟宗竹海與長源圳古圳：詳述孟宗竹高年生質固碳機制（年固碳 12～15 噸/公頃）與清代古圳百年引水歷史；長源圳林下氣溫比市區低 4～6℃，為 0 能源消耗之天然冷氣步道。", "1.2 綠金傳奇：")
add_bullet("德興瀑布水氣負離子：實測負離子濃度達 10,000～25,000 ions/cm³（市區僅約 100～300），倡導自備水壺裝取山泉冷泡茶，達成源頭減廢。", "1.3 瀑布仙境：")
add_bullet("凍頂烏龍茶與草生栽培：介紹龍眼木炭焙工藝與友善農法草生栽培，降低化學氮肥之 N₂O 排放。", "1.4 茶香傳奇：")
add_bullet("石馬公園雙開河津櫻與以竹代塑工藝：記錄 9 月秋季與農曆春節兩度綻放之奇景，並推廣以竹牙刷、竹杯墊取代一次性塑膠。", "1.5 櫻花竹藝：")

add_heading_2("2.2 篇章二：低碳旅遊心法（無痕山林與責任消費）")
add_body_p("提出「責任漫遊（Responsible Travel）」四大行動宣言：【輕裝慢行】、【在地旬味】、【自備減塑】與【綠色採購】。並深度對比不同交通模式之排碳差異：台中至小半天往返 240 公里，自駕休旅車每人排碳 26.2 kg，大巴共乘僅 5.0 kg（-80.9%）。在飲食方面，揭露牛肉排碳高達 60.0 kg/kg、豬肉 37.1 kg/kg，而在地鮮筍蔬菜僅 0.8～1.5 kg/kg，推廣產地旬味竹筍風味合菜，每人每餐可減少 2.5～3.8 kg 碳排。住宿方面，推廣小半天環保民宿夜間涼風免空調與自備備品，人均住宿排碳降至 2.4 kg。")

add_heading_2("2.3 篇章三：遊程碳盤查方法學（觀光署指引標準實作）")
add_body_p("依循 ISO 14067 與交通部觀光署計算指引，確立邊界為「集合報到出發至旅程結束解散」之服務生命週期。明確區分範疇一（自有車輛燃料）、範疇二（門市外購電力）與範疇三（外包運具、餐廳食材、合作飯店住宿、門票手作資材等其他間接排放）。")
add_callout(
    "碳排放量 (kg CO₂e) = Σ (活動數據 Activity Data × 排放係數 Emission Factor × GWP)\n"
    "• 活動數據：油耗公升數、用電度數、搭乘人-公里、食材重量、垃圾公斤數\n"
    "• 排放係數：環境部碳足跡資訊網及觀光署資料庫（電力採 114 年度最新係數 0.466 kg CO₂e/度）\n"
    "• 全球暖化潛勢 (GWP)：CO₂=1, CH₄=28, N₂O=265 (IPCC AR5)",
    title="遊程碳足跡核心計算公式"
)
add_body_p("手冊並獨家設計「小綠教你算」三大實務教學手把手演練：")
add_bullet("遊覽車 120 km 油耗 30L 柴油 × 3.320 kg/L = 99.6 kg，40 人分攤單程 2.49 kg，往返 4.98 kg；加上瓶裝水 0.121 kg，總計 5.10 kg/人。", "交通構面實算：")
add_bullet("傳統合菜含牛肉 0.8kg(48kg) + 豬肉 1.2kg(44.5kg) + 瓦斯 0.8m³(2.1kg)，10 人桌每人 9.46 kg；在地筍蔬餐 3kg 鮮筍蔬菜(3.6kg) + 瓦斯(2.1kg)，每人僅 0.57 kg，單餐減碳達 94%！", "餐飲構面實算：")
add_bullet("民宿當晚用電 80 度 × 0.466 kg/度 = 37.28 kg，40 人分攤每人僅 0.932 kg，佐證免空調與自備盥洗用具之巨大節能效益。", "住宿構面實算：")

add_heading_2("2.4 篇章四：兩天一夜示範遊程實測盤查清冊")
add_body_p("本專案以一團 20 人參與兩天一夜旅程（往返 240 公里）進行實測盤查比對，建立五大構面清冊：")

# Table for comparison
tbl = doc.add_table(rows=7, cols=6)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.autofit = False
col_widths = [Inches(1.0), Inches(1.8), Inches(0.8), Inches(1.8), Inches(0.8), Inches(0.8)]
for row in tbl.rows:
    for i, w in enumerate(col_widths):
        row.cells[i].width = w

headers = ["服務構面", "傳統基準遊程 (Baseline)", "基準碳排", "小半天低碳遊程 (Low-Carbon)", "低碳碳排", "減碳效益"]
for i, h in enumerate(headers):
    cell = tbl.cell(0, i)
    set_cell_background(cell, "1E293B")
    set_cell_margins(cell, 100, 100, 80, 80)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.bold = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(255, 255, 255)

data = [
    ("① 交通運輸", "自駕車 240km 每人油耗 8.5L 汽油 + 4瓶瓶裝水", "28.5 kg", "台灣好行大巴共乘 (每人 2.8L 柴油) + 自備水壺", "9.6 kg", "-66.3%"),
    ("② 餐飲美食", "4餐合菜含牛肉、烤豬肉、進口食材、一次性餐具", "14.2 kg", "4餐在地時令竹筍餐、茶餐、減肉蔬食、無免洗餐具", "3.8 kg", "-73.2%"),
    ("③ 住宿服務", "一般山莊飯店整晚開冷氣 + 全套拋棄式備品", "5.2 kg", "小半天環保民宿自然涼風免空調 + 自備毛巾牙刷", "2.4 kg", "-53.8%"),
    ("④ 遊憩體驗", "購買外來市售進口塑膠紀念品", "0.5 kg", "孟宗竹藝 DIY 體驗 (天然孟宗竹切削，以竹代塑)", "0.8 kg", "+0.3 kg (固碳)"),
    ("⑤ 門市據點", "彩色紙本宣傳摺頁 + 瓶裝水廢棄物", "0.2 kg", "數位電子手冊 QR Code 導讀 + 0 瓶裝垃圾", "0.2 kg", "減廢 100%"),
    ("全團每人合計", "每位旅客總碳足跡 (Total Baseline)", "48.6 kg", "小半天每位旅客總碳排 (Total Low-Carbon)", "16.8 kg", "-65.4%")
]

for row_idx, row_data in enumerate(data, start=1):
    is_total = (row_idx == 6)
    bg_color = "DCFCE7" if is_total else ("F8FAFC" if row_idx % 2 == 0 else "FFFFFF")
    for col_idx, val in enumerate(row_data):
        cell = tbl.cell(row_idx, col_idx)
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, 80, 80, 70, 70)
        p = cell.paragraphs[0]
        if col_idx in (2, 4, 5):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(val)
        r.font.size = Pt(8.5)
        if is_total:
            r.font.bold = True
            r.font.color.rgb = RGBColor(6, 95, 70) if col_idx != 2 else RGBColor(185, 28, 28)

doc.add_paragraph().paragraph_format.space_after = Pt(4)

add_body_p("實測結果顯示：傳統遊程人均排碳 48.6 kg CO₂e，小半天示範行程降至 16.8 kg CO₂e，每位旅客實質減少 31.8 kg CO₂e（-65.4%），相當於 2.6 棵成年孟宗竹整整一年的碳吸存量！單團 20 人即可省下 636 kg CO₂e。")

add_heading_2("2.5 篇章五：減量認證、碳標籤與淨零路徑")
add_bullet("四步驟流程：①確立產品邊界 ➔ ②蒐集佐證單據（加油發票、客運票根、住宿憑證、食材履歷） ➔ ③計算與編撰碳足跡報告書 ➔ ④第三方公正機構現勘查驗登錄。", "觀光署碳標籤申請：")
add_bullet("「先減量，再抵換！」絕不以廉價購買碳權直接宣稱零碳以防漂綠。旅客無可避免之 16.8 kg 剩餘排放，可結合在地竹林保育計畫或合格碳信用中和。", "不漂綠原則：")
add_bullet("近期（2025-2026）建立盤查制度；中期（2027-2030）導入電動接駁與太陽能；長期（2031-2050）達成全區國際認證碳中和旅遊示範目的地。", "小半天淨零路徑：")

add_heading_2("2.6 附錄：旅客自主低碳 Check-List 與永續綠色公約")
add_body_p("設計了出發前 5 大必備檢核項目（保溫水壺、隨身餐具、自備盥洗包、健行輕裝、手機離線手冊），並由產學與旅人共同簽署「小半天在地永續綠色公約」，落實無痕山林。")

# --- Chapter 3 ---
add_heading_1("第三章：互動網站系統架構與技術實作")

add_heading_2("3.1 零外部依賴、全自包含（Self-Contained）架構")
add_body_p("許多專案網頁在不同電腦或內聯 iframe/WebView 預覽時，常因相對路徑錯誤、CORS 跨域限制或外部圖檔外鏈失效而產生破圖與樣式崩潰。國立臺中科技大學 URR團隊針對此問題，採用「Master Builder Script (build_full_website.py)」架構，將所有高解析度向量立繪、行程圖表、數據圖表全數以 Base64 編碼內嵌於單一 index.html 檔案中（檔案大小約 1.6MB）。使用者無需架設後端伺服器、無需外連靜態資源伺服器，直接以任何瀏覽器雙擊即可 100% 完美呈現所有視覺效果與互動功能。")

add_heading_2("3.2 向量圖形渲染與角色立繪生成")
add_body_p("本專案視覺並非使用現成圖庫，而是以團隊開發之 Python Pycairo 向量圖形引擎逐格繪製：")
add_bullet("阿天立繪 (real_atian.png)：精準繪製遮陽帽、翠綠竹葉徽章、小半天導遊旗、登山背心與自然親切笑容。", "在地導遊阿天：")
add_bullet("綠導遊立繪 (real_xiaolu.png)：繪製綠色休閒帽、星型髮夾、亮黃色 CO₂ 計數旗，展現專業盤查專家風采。", "碳盤專家小綠：")
add_bullet("手冊封面 (cover.png)：雙主角並肩立於孟宗竹林與茶山前，配戴 2026 淨零認證徽章，達出版品級質感。", "精裝手冊封面：")
add_bullet("時程路線圖 (itinerary_chart.png) 與 五構面對比圖 (carbon_comparison.png)：以精確比例繪製時間軸卡片與條狀數據對比圖。", "專業資訊圖表：")

add_heading_2("3.3 現代響應式 UI/UX 與視覺設計系統")
add_body_p("前端採用現代化設計語言，兼顧學術嚴謹性與青年活潑感：")
add_bullet("以森綠（Emerald #059669）、竹青（Teal #0D9488）、暖琥珀（Amber #D97706）與大地石色（Stone #78716C）構建溫暖自然基調。", "大地生態色彩計畫：")
add_bullet("卡片採用白底半透明磨砂質感（backdrop-filter: blur(12px)），搭配微光漸變邊框（glow-green / glow-amber），提升層次感。", "玻璃擬態質感 (Glassmorphism)：")
add_bullet("完整支援桌面大螢幕、平板與智慧型手機直向閱覽，導航列隨滾動自動固定並具模糊背景效果。", "全響應式版面 (RWD)：")

add_heading_2("3.4 六大核心互動功能模組詳解")
add_bullet("具備大氣漸變光暈、指引認證徽章、三大成效統計卡（-65.4% 減碳、2,000+公頃竹海、5大構面盤查）及具備陰影與光澤之 3D 浮雕書模展示。", "模組 1：Hero 主視覺區")
add_bullet("雙導遊大尺寸透明背景立繪、身分稱號、配備標籤、經典嚮導台詞與星級能力雷達指標。", "模組 2：雙導遊檔案專區")
add_bullet("整合向量時程圖表，輔以長源圳竹海、竹筒飯、德興瀑布、竹藝工坊四大亮點特色卡。", "模組 3：示範行程路線全覽")
add_bullet("旅客可即時切換【交通工具】（大巴/包車/自駕）、【餐飲型態】（旬味竹筍/風味合菜/高碳肉餐）、【住宿選擇】（環保民宿/山莊/星級酒店）及【DIY體驗】（以竹代塑/塑膠品），右側儀表板即時動態更新總碳排、減碳率、四大構面百分比條及成年孟宗竹折算顆數！", "模組 4：遊程碳足跡即時互動試算器")
add_bullet("支援六大分頁即時切換（篇章一至篇章五＋附錄），包含完整文字、公式、表格、手把手實算教學，並內建 window.print() 一鍵列印/存為 PDF 功能。", "模組 5：手冊全文線上閱讀專區")
add_bullet("提供互動式 Checkbox 勾選框，方便旅客出發前自主點檢；下方陳列莊重之永續綠色公約全文。", "模組 6：附錄互動檢核與綠色公約")

# --- Chapter 4 ---
add_heading_1("第四章：系統介面截圖與詳細功能解說")
add_body_p("本章透過實際系統運作之高解析度畫面截圖，詳細展示各核心區塊之視覺編排與功能機制：")

# Screenshot 1
add_heading_2("4.1 首頁主視覺 Hero Banner 與 3D 封面展示")
add_body_p("主視覺採用深邃山林漸變背景，左側醒目標示觀光署計算指引依循與 114 年度最新電力係數（0.466 kg/度），陳列三大 KPI 指標卡；右側展示立體 3D 陰影手冊封面，直觀傳達出版品級質感。")
add_figure("screenshots/fig1_hero.png", "圖 1：首頁主視覺區、核心數據指標與 3D 浮雕精裝手冊封面")

# Screenshot 2
add_heading_2("4.2 雙導遊官方立繪展示專區（阿天 ✕ 綠導遊）")
add_body_p("採用雙欄卡片設計，分別呈現在地嚮導阿天與碳盤專家小綠之專屬立繪。卡片內清楚標示角色履歷、配備特徵（小半天旗 vs CO₂ 計數旗）、導遊台詞與專業專長指標。")
add_figure("screenshots/fig2_characters.png", "圖 2：在地青年阿天與碳盤查專家小綠之官方立繪與專業履歷卡片")

# Screenshot 3
add_heading_2("4.3 兩天一夜示範遊程全景路線圖與特色亮點")
add_body_p("將兩天一夜的低碳竹茶行旅時程表視覺化，搭配長源圳竹海、產地竹筒飯、德興瀑布水氣、竹藝工坊四大亮點卡，引導旅客理解各景點之生態與低碳意涵。")
add_figure("screenshots/fig3_itinerary.png", "圖 3：小半天兩天一夜慢活低碳示範遊程路線圖與站點亮點")

# Screenshot 4
add_heading_2("4.4 遊程碳足跡即時互動試算模擬器（ESG Dashboard）")
add_body_p("模擬器上方陳列五大構面碳盤查圖表，下方左側提供旅客自由點選不同交通、餐飲、住宿及體驗方案；右側白色高對比儀表板即時演算人均碳排，動態呈現 -65.4% 減碳效益與相當於 2.6 棵孟宗竹年吸收量之換算。")
add_figure("screenshots/fig4_calculator.png", "圖 4：即時互動碳足跡試算模擬器與動態 ESG 減碳儀表板")

# Screenshot 5
add_heading_2("4.5 手冊全文線上閱讀器——碳盤查計算教學與係數速查")
add_body_p("手冊全文閱讀器第 3 頁籤深度收錄遊程碳盤查方法學，包含三大「小綠教你算」算式拆解（交通、餐飲、住宿）以及觀光署 5 大服務構面之完整最新排放係數對照表。")
add_figure("screenshots/fig5_handbook_calc.png", "圖 5：手冊全文線上閱讀專區——遊程碳盤查核心公式、計算教學與係數速查表")

# Screenshot 6
add_heading_2("4.6 手冊全文線上閱讀器——示範遊程實測數據比對清冊")
add_body_p("手冊全文閱讀器第 4 頁籤完整收錄兩天一夜實測比對清冊，逐列對照傳統自駕遊程與低碳遊程之具體活動數據與每人碳排放量，清楚標示 48.6 kg 降至 16.8 kg 之實證成效。")
add_figure("screenshots/fig6_handbook_data.png", "圖 6：手冊全文線上閱讀專區——兩天一夜實測數據逐項對比清冊")

# Screenshot 7
add_heading_2("4.7 手冊全文線上閱讀器——旅客自主低碳檢核表與綠色公約")
add_body_p("手冊全文閱讀器第 6 頁籤提供互動式 Checkbox 勾選清單，旅客可逐項確認行前自備品；下方附上國立臺中科技大學 URR團隊與在地業者共同擬定之永續綠色公約誓詞。")
add_figure("screenshots/fig7_handbook_appendix.png", "圖 7：手冊全文線上閱讀專區——出發前自主低碳 Check-List 與永續綠色公約")

# --- Chapter 5 ---
add_heading_1("第五章：效益分析、教育推廣與未來展望")

add_heading_2("5.1 實質減碳效益與環境回饋")
add_body_p("透過本專案之科學量化實證，證實一趟小半天兩天一夜低碳行程可實質減少 65.4% 的碳足跡（每人減少 31.8 kg CO₂e）。以單團 20 人計算，一趟旅程即可減少 636 kg CO₂e 排放；若小半天休閒農業區常態性推廣此遊程，以每週 1 團（年出 48 團）估算，全年累計減碳量將突破 30,528 kg（約 30.5 噸 CO₂e），等同於為地球保留了 2,544 棵成年孟宗竹整年的碳匯量，對地方淨零轉型貢獻卓著。")

add_heading_2("5.2 大學社會責任（USR/URR）產學與地方創生實踐意涵")
add_body_p("國立臺中科技大學 URR團隊透過本計畫，具體落實了以下三大面向之大學社會責任：")
add_bullet("將觀光署深奧的碳足跡計算指引，轉化為直觀的「小綠教你算」公式與即時互動試算工具，降低一般大眾與青年學子的學習門檻。", "知識轉譯與普及化：")
add_bullet("深入鹿谷小半天孟宗竹林、古圳步道與茶園，挖掘在地「以竹代塑」與「產地餐桌」之生態價值，協助地方建立具有綠色競爭力的遊程產品。", "在地深耕與創生賦能：")
add_bullet("提供旅行同業可以直接套用的遊程碳足跡盤查清冊範本，助力國內中小型旅行業者銜接企業 ESG 獎勵旅遊市場。", "產業鏈結與標準建立：")

add_heading_2("5.3 旅行同業培力與社區推廣策略")
add_body_p("本手冊與互動網站不僅是一份成果報告，更具備高度的實務推廣價值。後續將規劃辦理「旅行業遊程碳盤查實務工作坊」，輔導鹿谷鄉在地民宿、餐飲業者與導遊領隊掌握活動數據蒐集要領；並透過數位網頁 QR Code 於小半天遊客中心、長源圳步道入口及合作民宿廣泛布設，讓每位到訪遊客都能用手機即時閱覽手冊、試算自己的旅程碳排。")

add_heading_2("5.4 未來深化發展與全台首座「碳中和旅遊目的地」願景")
add_body_p("立足於當前成果，URR 團隊下一步將攜手林業及自然保育署與第三方碳驗證機構，推動三大深化行動：")
add_bullet("正式向交通部觀光署提出「小半天永續低碳漫遊」產品碳足跡標籤申請，爭取成為南投縣首批獲證之低碳示範遊程。", "1. 取得官方碳標籤認證：")
add_bullet("與林業及自然保育署南投分署合作，針對小半天 2,000 公頃孟宗竹海進行在地森林碳匯方法學研究，探索竹林碳權認證機制。", "2. 竹林碳匯方法學深化：")
add_bullet("整合實質減量與在地竹林碳匯抵換，推動小半天休閒農業區成為全台灣第一個通過國際驗證的「100% 碳中和永續旅遊示範區（Carbon Neutral Tourism Destination）」，樹立台灣淨零生態旅遊之全新標竿！", "3. 邁向全區淨零示範：")

# Save document
docx_path = "/Users/chenchunchih/碳永續/碳導遊/小半天永續低碳漫遊與遊程碳盤查實務手冊暨互動網站成果報告書.docx"
doc.save(docx_path)
print(f"Successfully generated DOCX report at: {docx_path}")
