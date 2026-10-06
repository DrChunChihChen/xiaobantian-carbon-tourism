import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = Document()

# Standard margins (1 inch)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    
    # Header & Footer (Grayscale / B&W)
    header = section.header
    hp = header.paragraphs[0]
    hp.text = "國立臺中科技大學 大學社會責任實踐（USR）計畫 ｜ 子計畫H「智慧淨零農旅創生」成果報告"
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(8.5)
    hp.style.font.color.rgb = RGBColor(100, 100, 100)

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.text = "小半天休閒農業區遊程碳盤查、操作手冊、課程教案與計算網頁成果報告書"
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.style.font.name = "Arial"
    fp.style.font.size = Pt(8.5)
    fp.style.font.color.rgb = RGBColor(100, 100, 100)

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
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)

def add_subtitle(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(60, 60, 60)

def add_meta_box():
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F9F9F9") # Neutral light gray
    set_cell_margins(cell, 140, 140, 180, 180)
    
    borders_xml = f'''
    <w:tcBorders {nsdecls("w")}>
        <w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>
        <w:left w:val="single" w:sz="24" w:space="0" w:color="000000"/>
        <w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>
        <w:right w:val="single" w:sz="12" w:space="0" w:color="000000"/>
    </w:tcBorders>
    '''
    cell._tc.get_or_add_tcPr().append(parse_xml(borders_xml))
    
    lines = [
        ("計畫架構：", "教育部大學社會責任實踐（USR）計畫 ｜ 國立臺中科技大學 智慧產業學院"),
        ("子計畫名稱：", "子計畫H 智慧淨零農旅創生（落實現有產品碳盤查，編撰淨零永續操作手冊）"),
        ("子計畫主持人：", "陳俊智 博士（國立臺中科技大學 國際貿易經營系 助理教授）"),
        ("實踐合作場域：", "南投縣鹿谷鄉小半天休閒農業區（竹林村、竹豐村、和雅村）"),
        ("核心工作事項：", "1. 協助現有遊程碳盤查 ｜ 2. 完成淨零永續操作手冊 ｜ 3. 更新課程教案 ｜ 4. 建置旅遊碳足跡計算網頁"),
        ("計算規範依循：", "交通部觀光署《旅行業遊程碳足跡計算指引》、ISO 14067、環境部 114 年度電力排放係數 (0.466 kg CO₂e/度)")
    ]
    for idx, (label, val) in enumerate(lines):
        p = cell.add_paragraph() if idx > 0 else cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(label + " ")
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(0, 0, 0)
        r2 = p.add_run(val)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = RGBColor(40, 40, 40)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 30, 30)
    return p

def add_h3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(50, 50, 50)
    return p

def add_body(text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(40, 40, 40)
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
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(40, 40, 40)
    return p

def add_callout_bw(text, title="重點摘要"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F5F5F5") # Pure neutral light gray
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    borders_xml = f'''
    <w:tcBorders {nsdecls("w")}>
        <w:top w:val="none"/>
        <w:left w:val="single" w:sz="24" w:space="0" w:color="000000"/>
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
    r1.font.color.rgb = RGBColor(0, 0, 0)
    r2 = cp.add_run(text)
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(40, 40, 40)
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
        c_run.font.color.rgb = RGBColor(80, 80, 80)

print("Compiling Black & White report...")

# --- Front Matter ---
add_title("教育部大學社會責任實踐（USR）計畫 執行成果報告")
add_subtitle("子計畫H「智慧淨零農旅創生」：小半天場域遊程碳盤查、操作手冊、課程教案與計算網頁成果")
add_meta_box()

# --- Section 1 ---
add_h1("壹、計畫緣起與背景目標")

add_h2("一、高教深耕與大學社會責任（USR）計畫推動背景")
add_body("面對國家 2050 淨零轉型目標與全球永續觀光發展趨勢，國立臺中科技大學依循教育部大學社會責任實踐（USR）計畫架構，推動休閒農業與在地農村產業升級。觀光休閒產業為台灣重要的綠色經濟基石，然而傳統旅遊模式常伴隨高比例自駕交通、一次性塑膠備品耗損及食材長途運輸等問題。交通部觀光署遂公布《旅行業遊程碳足跡計算指引》，積極推展旅遊產品碳標籤；同時，企業客戶在落實 ESG 綠色採購時，亦高度要求供應商提供透明且具公信力之遊程碳足跡盤查證明。本校 USR 計畫即立足於此時代脈絡，扮演跨領域技術整合與在地培力之智庫角色。")

add_h2("二、子計畫H「智慧淨零農旅創生」之核心定位與產業痛點")
add_body("作為子計畫H（智慧淨零農旅創生）之計畫負責人，本團隊在初期深入場域調研時，明確鎖定實踐場域所面臨的三大核心痛點：")
add_bullet("實踐場域所在之農村聚落面臨高齡化挑戰，在地缺乏具備溫室氣體盤查、碳足跡計算與數位行銷能力之綠領青年人才。", "1. 綠領與智慧科技人才缺乏：")
add_bullet("多數休閒農業體驗與旅行產品缺乏標準化之溫室氣體排放量化數據，無法提出具科學依據之減碳成效佐證，難以銜接外部企業 ESG 採購市場。", "2. 缺乏科學化碳盤查機制：")
add_bullet("以往永續宣導多流於道德勸說與口號，欠缺具體可操作之實務指南及直觀易懂的數位試算工具，降低了業者與旅客的主動實踐意願。", "3. 欠缺標準作業手冊與數位工具：")
add_body("針對上述痛點，子計畫H 設定了明確的解題任務，將大學端的研究量能、生成式 AI 數位工具與碳管理專業，導入實踐場域，全面推動休閒農業綠色轉型。")

add_h2("三、實踐場域特質：南投鹿谷小半天休閒農業區")
add_body("本計畫實踐場域選定南投縣鹿谷鄉「小半天」地區（包含竹林村、竹豐村與和雅村）。小半天坐落於海拔 600 至 1,100 公尺之隆起高位河階台地，三面環山，長年雲霧繚繞，擁有全台灣面積最大、密度最高的孟宗竹林聚落（面積超過 2,000 公頃）。孟宗竹生長極迅速，40～60 天即可成竹，其年生質累積速率與吸碳能力約為一般溫帶闊葉林木之 1.5 至 2.0 倍，整座竹海每年碳吸存潛力高達 2.4 萬至 3 萬噸 CO₂。此外，小半天擁有清代古圳「長源圳生態步道」、萬級負離子飛瀑「德興瀑布」、傳統炭焙凍頂烏龍茶席，以及石馬公園河津櫻雙開奇景，具備發展高品質零碳示範旅遊之雄厚天然資本。")

add_h2("四、子計畫H 四大核心推動重點")
add_body("為具體解決場域痛點並達成計畫管考指標，本計畫全力聚焦落實以下四項核心工作，全數如期高品質完成：")
add_bullet("依循觀光署官方指引，深入場域完成五大服務構面之實測盤查與清冊建立。", "核心工作一：協助小半天場域進行現有遊程碳盤查 ── ")
add_bullet("編撰出版級標準指引，包含地理生態、無痕旅遊、盤查方法學、實測數據與認證路徑。", "核心工作二：完成實踐場域淨零永續操作手冊 ── ")
add_bullet("將場域盤查實務轉化為教材，融入校內專業課程與 iPAS 國家淨零證照考訓。", "核心工作三：更新課程教案 ── ")
add_bullet("開發純前端全自包含、免伺服器之互動式試算模擬平台，解決偏鄉展示痛點。", "核心工作四：協助小半天休閒農業區建置「旅遊碳足跡計算網頁」 ── ")

# --- Section 2 ---
add_h1("貳、核心成果一：協助小半天場域進行現有遊程碳盤查")

add_h2("一、盤查規範與方法學標準")
add_body("本計畫嚴格依循交通部觀光署《旅行業遊程碳足跡計算指引》與國際 ISO 14067 產品碳足跡標準進行盤查規劃。邊界定義為「搖籃到大門（Cradle-to-Gate）」之遊程服務生命週期，涵蓋旅客自集合報到出發開始，歷經全程表定交通、參訪體驗、餐飲美食、住宿過夜，直至旅程結束解散為止。盤查範疇明確劃分：")
add_bullet("自有運具燃油燃燒排放（如自有公務接駁車）。", "範疇一（直接排放）：")
add_bullet("門市及營業據點營運所消耗之外購電力（採用環境部最新公告 114 年度電力排放係數 0.466 kg CO₂e/度）。", "範疇二（能源間接排放）：")
add_bullet("遊覽車燃油、大眾運輸客運、委託餐廳食材、合作民宿住宿水電、景點門票與手作 DIY 耗材等供應鏈排放。此構面為旅行業最主要之排放來源。", "範疇三（其他間接排放）：")

add_h2("二、五大服務構面實測與活動數據蒐集")
add_body("依觀光署規範，本計畫將遊程拆解為五大服務構面，並建立標準化活動數據收集清單：①門市據點（用紙包數、電力度數、垃圾量）；②交通運輸（大巴柴油公升數、自駕汽油公升數、瓶裝水瓶數）；③餐飲美食（食材種類與重量、瓦斯消耗量、廚餘量）；④旅宿住宿（客房住宿夜數、空調用電度數、一次性盥洗包消耗套數）；⑤遊憩體驗（手作材料重量、識別證與活動耗材）。")

add_h2("三、兩天一夜示範遊程實測盤查數據比對分析")
add_body("本計畫以 20 人團體參與台中至小半天往返（總路程約 240 公里）兩天一夜經典慢活遊程為實測標的，將「傳統基準遊程（Baseline）」與「小半天低碳遊程（Low-Carbon）」每位旅客各項活動數據與排放量逐項比對：")

# Table in B&W
tbl_carbon = doc.add_table(rows=7, cols=6)
tbl_carbon.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_carbon.autofit = False
col_w = [Inches(1.1), Inches(1.8), Inches(0.8), Inches(1.8), Inches(0.8), Inches(0.8)]
for r in tbl_carbon.rows:
    for i, w in enumerate(col_w):
        r.cells[i].width = w

hdrs = ["服務構面", "傳統基準遊程 (Baseline) 每人數據", "基準碳排", "小半天低碳遊程 (Low-Carbon) 每人數據", "低碳碳排", "減碳成效"]
for i, h in enumerate(hdrs):
    c = tbl_carbon.cell(0, i)
    set_cell_background(c, "262626") # Dark charcoal/black
    set_cell_margins(c, 100, 100, 80, 80)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(h)
    run.font.bold = True
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

data_carbon = [
    ("① 交通運輸", "自駕車 240km 每人分攤 8.5L 汽油 + 4 瓶瓶裝水", "28.5 kg", "台灣好行大巴共乘 (每人 2.8L 柴油) + 自備保溫杯", "9.6 kg", "-66.3%"),
    ("② 餐飲美食", "4 餐傳統合菜含牛肉、烤豬肉、進口食材、拋棄式餐具", "14.2 kg", "4 餐在地時令鮮筍蔬食餐、烏龍茶餐、無免洗餐具", "3.8 kg", "-73.2%"),
    ("③ 住宿服務", "一般山莊飯店整晚開冷氣 + 全套拋棄式牙刷沐浴瓶", "5.2 kg", "小半天環保民宿自然涼風免冷氣 + 自備毛巾牙刷", "2.4 kg", "-53.8%"),
    ("④ 遊憩體驗", "購買外來市售進口塑膠吊飾紀念品", "0.5 kg", "孟宗竹藝工坊 DIY (天然孟宗竹切削，以竹代塑)", "0.8 kg", "+0.3 kg (固碳)"),
    ("⑤ 門市據點", "彩色紙本宣傳摺頁 (銅版紙) + 礦泉水廢瓶垃圾", "0.2 kg", "數位電子手冊 QR Code 導讀 + 0 瓶裝垃圾", "0.2 kg", "源頭減廢 100%"),
    ("全團每人合計", "每位旅客總碳足跡 (Total Baseline)", "48.6 kg", "小半天每位旅客總碳排 (Total Low-Carbon)", "16.8 kg", "-65.4%")
]

for row_idx, r_data in enumerate(data_carbon, start=1):
    is_tot = (row_idx == 6)
    bg = "EBEBEB" if is_tot else ("F9F9F9" if row_idx % 2 == 0 else "FFFFFF")
    for col_idx, val in enumerate(r_data):
        c = tbl_carbon.cell(row_idx, col_idx)
        set_cell_background(c, bg)
        set_cell_margins(c, 80, 80, 70, 70)
        p = c.paragraphs[0]
        if col_idx in (2, 4, 5):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(val)
        run.font.size = Pt(8.5)
        if is_tot:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)

doc.add_paragraph().paragraph_format.space_after = Pt(4)

add_callout_bw(
    "盤查實測數據證實：傳統遊程每位旅客產生約 48.6 kg CO₂e 碳排；透過本計畫輔導之低碳遊程規劃，每位旅客碳排放大幅降至 16.8 kg CO₂e，人均實質減碳高達 31.8 kg CO₂e（減碳幅度達 65.4%）！\n"
    "相當於每位旅客為地球節省下 2.6 棵成年孟宗竹整整一年的碳吸存量。單趟 20 人團體即可減少 636 kg CO₂e 排放；以年度 48 團常態推廣估算，年減碳效益突破 30.5 噸 CO₂e！",
    title="小半天遊程碳盤查量化成效總結"
)

# --- Section 3 ---
add_h1("參、核心成果二：完成實踐場域淨零永續操作手冊")

add_h2("一、《小半天永續低碳漫遊與遊程碳盤查實務手冊》編撰架構")
add_body("為使場域業者具備自主執行與持續推廣能力，本計畫完成了具備出版品質之《小半天永續低碳漫遊與遊程碳盤查實務手冊》（全書涵蓋五大核心篇章與實用附錄）：")
add_bullet("詳述隆起台地地形、2,000 公頃孟宗竹海之年生質累積速率與吸碳機制（每公頃年固碳 12～15 噸）、長源圳百年古圳（林下涼爽比市區低 4～6℃ 之天然零碳冷氣房）、德興瀑布萬級負離子環境洗禮（10,000～25,000 ions/cm³）、凍頂烏龍友善草生茶園，以及石馬公園河津櫻秋春雙開之生態特色。", "【篇章一】走進仙境小半天：地理人文與生態底蘊 ── ")
add_bullet("提出責任漫遊四大行動宣言（輕裝慢行、在地旬味、自備減塑、綠色採購）；深入分析大巴共乘（5.0 kg/人）與自駕（26.2 kg/人）之排碳差距；揭示牛肉高碳排（60 kg/kg）與在地竹筍蔬菜低碳排（0.8～1.5 kg/kg）之科學數據；倡導以竹代塑循環經濟與環保民宿夜間涼風免空調。", "【篇章二】低碳旅遊心法：無痕山林與責任消費 ── ")
add_bullet("完整闡釋 ISO 14067 與觀光署指引架構；明定碳排核心計算公式：碳排放量 = Σ (活動數據 × 排放係數 × GWP)；獨家設計「小綠教你算」三大手把手實算範例（交通柴油油耗計算、餐飲合菜食材盤查、住宿夜間電力盤查）；並整理出觀光署五大服務構面之最新排放係數速查表（含 114 年最新電力係數 0.466 kg/度）。", "【篇章三】遊程碳盤查方法學：觀光署指引標準實作 ── ")
add_bullet("完整收錄兩天一夜慢活行程時刻表（Day 1 瀑布竹海、Day 2 竹藝茶香）；詳列 20 人團體五大構面實測對比數據清冊，佐證人均減碳 31.8 kg (-65.4%) 之顯著績效。", "【篇章四】小半天兩天一夜示範遊程實測盤查 ── ")
add_bullet("詳述旅行社申請觀光署遊程產品碳標籤之四步驟作業指引（確立邊界 ➔ 蒐集憑證 ➔ 編撰報告 ➔ 第三方查核）；建立「先減量再抵換」之不漂綠原則；制定小半天 2025–2050 近中長期淨零路徑藍圖，目標邁向國際認證碳中和旅遊目的地。", "【篇章五】減量效益評估、碳標籤認證與淨零路徑 ── ")
add_bullet("提供出發前 5 大必備項目的旅客自主低碳 Check-List；附錄本計畫與在地業者共同擬定之「小半天在地永續綠色公約」宣誓詞。", "【附錄】出發前自主低碳檢核表與在地綠色公約 ── ")

add_h2("二、雙導遊 IP 人設建構與在地知識轉譯")
add_body("手冊特別創設「雙導遊聯手帶路」之擬人化角色 IP：在地青年嚮導「阿天」以親切熱情口吻解說竹海古圳風光，專精以竹代塑工藝；碳盤專家導遊「小綠」則以專業且生動之比喻拆解艱澀算式。透過雙主角的對話引導，將原本冰冷的溫室氣體數據轉化為生動有趣的綠色生活實踐指南。")

# --- Section 4 ---
add_h1("肆、核心成果三：更新課程教案與培育綠領人才")

add_h2("一、場域數據教材化：打造跨領域永續課程教案")
add_body("作為子計畫H負責人，本團隊將小半天實踐場域所獲取之第一手碳盤查實測數據、活動數據蒐集憑證及方法學計算模型，全數回饋並轉化為校內專業課程之全新教案。此一教案徹底顛覆傳統教科書之虛擬案例教學，讓學生直接面對真實產業環境中的碳排放問題，完成「學用合一」之深耕教育。")

add_h2("二、對接課程體系與跨領域人才培育")
add_body("更新後之教案深度融入國立臺中科技大學多門專業與通識課程體系：")
add_bullet("引導學生實際演練旅行業遊程碳足跡盤查計算表格，操作活動數據填報、碳排放係數配對及碳排熱點（Hotspot）分析，掌握範疇一、二、三劃分技能。", "1. 「智慧淨零碳管理」專業課程：")
add_bullet("結合環境部氣候變遷因應法、碳費徵收機制及國際歐盟 CBAM 趨勢，以小半天竹林碳匯與觀光署碳標籤制度為實務案例，探討地方綠色經濟轉型策略。", "2. 「環境與永續發展」通識課程：")
add_bullet("以小半天 2,000 公頃孟宗竹林為標的，探討以竹代塑、竹炭高溫固碳資材與自然碳匯之商業模式創新。", "3. 「循環經濟與地方創生」主題課程：")

add_h2("三、融入「iPAS 淨零碳規劃管理師」國家證照培訓")
add_body("本計畫教案進一步對接經濟部「iPAS 淨零碳規劃管理師」初級能力鑑定規範。教案涵蓋國際溫室氣體盤查準則（ISO 14064-1、ISO 14067）、排放係數庫查詢應用及實質減量規劃方法，有效提升修課學生通過國家級綠領專業證照之合格率，實質培育具備就業即戰力之產業永續專才。")

add_h2("四、導入生成式 AI 數位工具與師生場域實踐")
add_body("本計畫引導學生善用生成式 AI 工具（ChatGPT、Claude、Gemini、Perplexity）進行文獻調研與碳排資料初篩，並結合 Python 程式開發向量視覺化圖表與前端互動介面。修課學生在計畫團隊帶領下實際進駐小半天休閒農業區，與在地竹藝師、民宿主人及茶農深度對話，協助業者檢視日常營運中的能源消耗，實現「以專業回饋在地、以場域淬鍊專業」之大學社會責任精神。")

# --- Section 5 ---
add_h1("伍、核心成果四：協助小半天休閒農業區建置「旅遊碳足跡計算網頁」")

add_h2("一、系統開發理念：全自包含（Self-Contained）免伺服器架構")
add_body("針對偏鄉山區休閒農業區在推廣數位工具時常面臨的網路頻寬不穩、外鏈圖檔失效、CORS 跨域限制或伺服器維護成本高昂等問題，本計畫技術團隊採用創新的「Master Builder Script (build_full_website.py)」架構。整套系統包含所有向量角色立繪、高解析度資訊圖表、自訂樣式表與互動計算邏輯，全數經過 Base64 編碼內嵌於單一 index.html 檔案中（檔案約 1.6MB）。使用者無需架設後端資料庫或伺服器，直接使用任何標準瀏覽器即可 100% 離線相容開啟，確保現場解說推廣零破圖、零死角。")

add_h2("二、前端技術與響應式介面設計")
add_body("介面採用 Tailwind CSS 框架結合現代玻璃擬態（Glassmorphism）與大地自然色系（森綠、竹青、暖琥珀），提供流暢之微互動動畫與卡片式版面配置。全站具備高度響應式設計（RWD），在桌上型電腦、平板及智慧型手機直向檢視下皆能自動最適化呈現。")

add_h2("三、六大核心功能模組規劃")
add_bullet("呈現深邃山林氛圍、觀光署計算指引認證標章、三大關鍵 KPI 績效卡（-65.4% 減碳、2,000+ 公頃竹林、5 大構面盤查）及立體 3D 精裝手冊封面展示。", "模組 1：Hero 主視覺區 ── ")
add_bullet("收錄在地嚮導阿天與碳盤專家小綠之獨立透明立繪卡片、身分履歷、配備標籤與專業專長指標。", "模組 2：雙導遊官方立繪展示專區 ── ")
add_bullet("將兩天一夜低碳慢活行程視覺化為時間軸圖表，並呈現長源圳竹海、竹筒飯、德興瀑布、竹藝工坊四大特色站點卡。", "模組 3：示範行程路線全覽 ── ")
add_bullet("旅客可自由點選不同【交通運具】、【餐飲型態】、【住宿選擇】及【DIY體驗】方案；右側高對比儀表板即時演算人均碳足跡總量、減碳百分比、各構面佔比條圖，並自動折算為等同於幾棵成年孟宗竹整年吸收量。", "模組 4：遊程碳足跡即時互動試算模擬器 ── ")
add_bullet("以分頁標籤（Tab）形式完整收錄手冊篇章一至篇章五，包含詳細論述、公式說明、三項手把手計算教學與完整係數表格，並支援 window.print() 一鍵列印與 PDF 存檔。", "模組 5：手冊全文線上閱讀專區 ── ")
add_bullet("提供互動式 Checkbox 勾選檢核表，方便旅客行前點檢個人環保用具；下方陳列莊重之永續綠色公約誓詞。", "模組 6：附錄互動檢核與綠色公約 ── ")

add_h2("四、系統介面截圖與詳細功能解說")
add_body("以下透過系統實際運作畫面之高解析度截圖，逐一檢視各功能模組之設計實績：")

# 7 Figures in B&W report
add_figure("screenshots/fig1_hero.png", "圖 1：首頁主視覺區、核心數據指標與 3D 浮雕精裝手冊封面展示")
add_body("【圖 1 說明】主視覺區以深色大地漸變為基底，左側清楚標示觀光署計算指引依循與 114 年度電力排放係數 0.466 kg/度；下方呈現三大量化成果卡；右側展示 3D 立體精裝手冊封面，傳達嚴謹專業之出版品質。")

add_figure("screenshots/fig2_characters.png", "圖 2：雙導遊官方立繪專區（真・阿天 ✕ 真・綠導遊）")
add_body("【圖 2 說明】採用雙欄卡片設計，分別呈現在地青年阿天（手持小半天旗、竹葉遮陽帽）與碳盤專家小綠（手持 CO₂ 計數旗、星型髮夾）之專屬立繪，並詳列各自背景設定、經典台詞與五星專業能力雷達。")

add_figure("screenshots/fig3_itinerary.png", "圖 3：小半天兩天一夜慢活低碳示範遊程路線圖與特色站點")
add_body("【圖 3 說明】整合團隊繪製之示範遊程全景時程圖表，輔以長源圳竹海、產地時令竹筒飯、德興瀑布水氣及竹藝工坊四大特色亮點卡，引導旅客理解各遊程節點之生態保育與低碳意涵。")

add_figure("screenshots/fig4_calculator.png", "圖 4：遊程碳足跡即時互動試算模擬器與動態 ESG 減碳儀表板")
add_body("【圖 4 說明】模擬器上方收錄五大構面減碳對比圖；下方左側提供旅客自由勾選不同運具、飲食、住宿及 DIY 體驗；右側高對比儀表板即時動態演算人均碳排、長條圖比例及成年孟宗竹折算顆數。")

add_figure("screenshots/fig5_handbook_calc.png", "圖 5：手冊全文線上閱讀專區（篇章三：碳盤查公式、計算教學與係數表）")
add_body("【圖 5 說明】手冊閱讀器第 3 頁籤完整展示觀光署指引盤查方法學，包含「小綠教你算」三大手把手算式拆解（交通、餐飲、住宿）及五大服務構面之最新排放係數速查對照表。")

add_figure("screenshots/fig6_handbook_data.png", "圖 6：手冊全文線上閱讀專區（篇章四：示範遊程實測數據逐項對比清冊）")
add_body("【圖 6 說明】手冊閱讀器第 4 頁籤完整陳列 20 人團體兩天一夜實測比對清冊，逐項對照傳統自駕遊程與低碳遊程之具體活動數據與每人碳排放量，清楚佐證人均減碳 31.8 kg (-65.4%) 之成效。")

add_figure("screenshots/fig7_handbook_appendix.png", "圖 7：手冊全文線上閱讀專區（附錄：自主低碳檢核表與綠色公約）")
add_body("【圖 7 說明】手冊閱讀器第 6 頁籤提供互動式 Checkbox 勾選框，方便旅客行前逐項確認個人自備品；下方附上本計畫與在地業者共同簽署之小半天永續綠色公約全文。")

# --- Section 6 ---
add_h1("陸、計畫自訂績效指標達成情形與未來展望")

add_h2("一、子計畫H 績效指標達成情形檢核")
add_body("對照本校 USR 計畫書所訂定之年度管考績效目標，子計畫H 各項指標均已 100% 圓滿達成：")

tbl_perf = doc.add_table(rows=5, cols=5)
tbl_perf.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_perf.autofit = False
perf_w = [Inches(1.2), Inches(2.2), Inches(1.0), Inches(1.3), Inches(0.8)]
for r in tbl_perf.rows:
    for i, w in enumerate(perf_w):
        r.cells[i].width = w

p_hdrs = ["子計畫代號", "原訂績效指標項目", "原訂目標值", "實際執行成果", "達成率"]
for i, h in enumerate(p_hdrs):
    c = tbl_perf.cell(0, i)
    set_cell_background(c, "262626")
    set_cell_margins(c, 100, 100, 80, 80)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(h)
    run.font.bold = True
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

perf_data = [
    ("H 智慧淨零農旅創生", "協助小半天場域進行現有遊程碳盤查", "1 式", "完成 20 人兩天一夜五大構面實測盤查清冊", "100%"),
    ("H 智慧淨零農旅創生", "完成實踐場域淨零永續操作手冊", "1 式", "完成《小半天永續低碳漫遊與碳盤查手冊》全書", "100%"),
    ("H 智慧淨零農旅創生", "更新課程教案", "1 式", "完成跨領域碳盤查教案並融入 iPAS 證照培訓", "100%"),
    ("H 智慧淨零農旅創生", "協助小半天休閒農業區建置「旅遊碳足跡計算網頁」", "1 式", "建置完成全自包含互動試算平台 (index.html)", "100%")
]

for row_idx, r_data in enumerate(perf_data, start=1):
    bg = "F9F9F9" if row_idx % 2 == 0 else "FFFFFF"
    for col_idx, val in enumerate(r_data):
        c = tbl_perf.cell(row_idx, col_idx)
        set_cell_background(c, bg)
        set_cell_margins(c, 80, 80, 70, 70)
        p = c.paragraphs[0]
        if col_idx in (2, 4):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(val)
        run.font.size = Pt(8.5)
        if col_idx == 4:
            run.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(4)

add_h2("二、產學合作、地方創生與社會責任實踐效益")
add_bullet("將觀光署繁複艱澀的指引法規，轉化為親民有趣的「雙導遊圖解」與「線上即時試算模擬器」，大幅降低一般旅客與中小業者的學習門檻。", "1. 專業知識轉譯與普及化：")
add_bullet("深入小半天高位台地，深度挖掘 2,000 公頃孟宗竹海之天然碳匯價值與竹藝工藝，輔導在地民宿、餐廳及小農建立低碳綠色產品線。", "2. 深化場域價值與在地創生：")
add_bullet("產出符合觀光署指引之標準化盤查清冊範本，可直接提供給國內中小型旅行業者使用，助力其承接企業員工 ESG 綠色旅遊採購標案。", "3. 賦能產業鏈結與標準化：")

add_h2("三、未來深化推動路徑與願景")
add_body("立足於現階段亮眼成果，子計畫H 將持續推動以下三大深化工作：")
add_bullet("輔導在地業者正式向交通部觀光署提出遊程碳足跡標籤認證申請，爭取成為南投縣首批獲證之農旅示範行程。", "1. 取得官方碳標籤認證：")
add_bullet("結合林業及自然保育署資源，深化小半天 2,000 公頃孟宗竹海在地森林碳匯方法學研究，探索竹林碳權認證與在地抵換機制。", "2. 深化在地竹林碳匯研究：")
add_bullet("整合實質減量與在地碳匯抵換，推動小半天休閒農業區成為全台灣第一個通過國際認證之「100% 碳中和永續旅遊示範目的地（Carbon Neutral Destination）」，樹立大學社會責任實踐之典範標竿！", "3. 邁向全台首座碳中和休閒農業區：")

# Save document
bw_docx_path = "/Users/chenchunchih/碳永續/碳導遊/小半天永續低碳漫遊與遊程碳盤查實務手冊暨互動網站成果報告書.docx"
doc.save(bw_docx_path)
print(f"B&W DOCX report successfully generated at: {bw_docx_path}")
