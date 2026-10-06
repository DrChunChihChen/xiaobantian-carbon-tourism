"""升級生成頂級質感、全內嵌 Base64 絕不破圖的《小半天永續低碳漫遊與遊程碳盤查實務手冊》互動首頁
"""
import base64, os

def get_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

img_cover = get_b64("cover.png")
img_atian = get_b64("real_atian.png")
img_xiaolu = get_b64("real_xiaolu.png")
img_itinerary = get_b64("itinerary_chart.png")
img_carbon = get_b64("carbon_comparison.png")

html_content = f'''<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>小半天永續低碳漫遊與遊程碳盤查實務手冊</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700;900&display=swap');
    body {{
      font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    .glass-card {{
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(226, 232, 240, 0.8);
    }}
    .glass-dark {{
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}
    .glow-green {{
      box-shadow: 0 0 35px -5px rgba(16, 185, 129, 0.35);
    }}
    .glow-amber {{
      box-shadow: 0 0 35px -5px rgba(245, 158, 11, 0.30);
    }}
    .book-shadow {{
      box-shadow: -15px 20px 35px -5px rgba(0, 0, 0, 0.35), 0 5px 15px rgba(0, 0, 0, 0.2);
    }}
  </style>
</head>
<body class="bg-gradient-to-b from-stone-50 via-emerald-50/20 to-stone-100 text-slate-800 antialiased selection:bg-emerald-500 selection:text-white">

  <!-- 頂部精緻導航列 -->
  <header class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-emerald-100 shadow-sm transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between">
      <!-- 品牌 Logo 與雙導遊同台標誌 -->
      <a href="#" class="flex items-center space-x-3 group">
        <div class="flex -space-x-2.5 overflow-hidden items-center p-0.5 bg-emerald-50 rounded-full border border-emerald-200">
          <img src="{img_atian}" class="inline-block h-10 w-10 rounded-full ring-2 ring-emerald-500 bg-white object-contain shadow-sm transform group-hover:scale-110 transition duration-200" alt="真・阿天">
          <img src="{img_xiaolu}" class="inline-block h-10 w-10 rounded-full ring-2 ring-teal-500 bg-white object-contain shadow-sm transform group-hover:scale-110 transition duration-200" alt="真・綠導遊">
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <span class="font-extrabold text-emerald-950 text-base sm:text-lg tracking-tight">小半天永續漫遊</span>
            <span class="hidden sm:inline-flex text-[11px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full border border-emerald-300">阿天 ✕ 綠導遊</span>
          </div>
          <p class="text-[10px] text-slate-500 hidden sm:block tracking-wider font-medium">觀光署指引架構 · 遊程碳盤查實務</p>
        </div>
      </a>

      <!-- 導覽連結 -->
      <nav class="hidden md:flex items-center space-x-7 text-sm font-semibold text-slate-600">
        <a href="#about" class="hover:text-emerald-700 transition">手冊特色</a>
        <a href="#characters" class="hover:text-emerald-700 transition">雙導遊檔案</a>
        <a href="#itinerary" class="hover:text-emerald-700 transition">示範遊程</a>
        <a href="#calculator" class="text-emerald-700 hover:text-emerald-800 transition flex items-center space-x-1">
          <span>🧮</span>
          <span>碳足跡試算器</span>
        </a>
        <a href="#videos" class="hover:text-emerald-700 transition flex items-center space-x-1">
          <span>🎬</span>
          <span>影音導覽動畫</span>
        </a>
        <a href="#handbook-reader" class="hover:text-emerald-700 transition">手冊全文</a>
      </nav>

      <!-- 右側行動按鈕 -->
      <div class="flex items-center space-x-2">
        <a href="#calculator" class="bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs sm:text-sm font-bold px-4 sm:px-5 py-2.5 rounded-xl shadow-md hover:shadow-lg transition transform hover:-translate-y-0.5">
          即時試算遊程碳排
        </a>
      </div>
    </div>
  </header>

  <!-- 主視覺 Hero Section (雜誌出版風格) -->
  <section id="about" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 sm:pt-10 pb-12">
    <div class="relative rounded-3xl overflow-hidden bg-gradient-to-br from-emerald-950 via-slate-900 to-teal-950 text-white shadow-2xl border border-emerald-800/40 p-6 sm:p-10 lg:p-14">
      
      <!-- 氛圍裝飾光斑與背景林海紋理 -->
      <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-teal-500/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-[radial-gradient(circle_at_center,rgba(16,185,129,0.08)_0,transparent_70%)] pointer-events-none"></div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center relative z-10">
        
        <!-- 左欄：核心標題與訴求 -->
        <div class="lg:col-span-7 space-y-6">
          <!-- 雙重官方指引認證標籤 -->
          <div class="flex flex-wrap items-center gap-2">
            <span class="inline-flex items-center space-x-1.5 bg-emerald-500/20 border border-emerald-400/40 text-emerald-200 px-3 py-1 rounded-full text-xs font-semibold">
              <span>🌿 交通部觀光署計算指引依循</span>
            </span>
            <span class="inline-flex items-center space-x-2 bg-white/10 border border-white/20 text-white px-3 py-1 rounded-full text-xs font-medium">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>114年度最新電力排放係數 0.466 kg/度</span>
            </span>
          </div>

          <!-- 主標題 -->
          <div class="space-y-2">
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight text-white">
              小半天永續低碳漫遊<br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-300 via-teal-200 to-amber-200">
                與遊程碳盤查實務手冊
              </span>
            </h1>
            <p class="text-emerald-300/90 text-sm sm:text-base font-semibold tracking-wide">
              全台首創 · 孟宗竹海生態 ✕ 凍頂烏龍茶席 ✕ 五大服務構面碳足跡精準量化
            </p>
          </div>

          <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-light">
            由小半天在地嚮導 <strong class="text-white font-semibold">阿天</strong> 與遊程碳盤查專家 <strong class="text-white font-semibold">綠導遊小綠</strong> 攜手帶路！打破以往永續旅遊流於口號的限制，將小半天長源圳竹海、德興瀑布、石馬公園與竹藝工坊，轉化為看得見、算得清的標準化低碳遊程清冊。
          </p>

          <!-- 三大成效指標卡片 -->
          <div class="grid grid-cols-3 gap-3 pt-1">
            <div class="bg-white/10 backdrop-blur-md rounded-2xl p-3.5 border border-white/10">
              <div class="text-[11px] text-emerald-300 font-medium">示範行程減碳</div>
              <div class="text-2xl sm:text-3xl font-black text-white mt-1">-65.4%</div>
              <div class="text-[10px] text-slate-400 mt-0.5">實測降至 16.8 kg</div>
            </div>
            <div class="bg-white/10 backdrop-blur-md rounded-2xl p-3.5 border border-white/10">
              <div class="text-[11px] text-amber-300 font-medium">以竹代塑碳匯</div>
              <div class="text-2xl sm:text-3xl font-black text-white mt-1">2,000+</div>
              <div class="text-[10px] text-slate-400 mt-0.5">公頃全台最大孟宗竹林</div>
            </div>
            <div class="bg-white/10 backdrop-blur-md rounded-2xl p-3.5 border border-white/10">
              <div class="text-[11px] text-sky-300 font-medium">服務構面盤查</div>
              <div class="text-2xl sm:text-3xl font-black text-white mt-1">5 大構面</div>
              <div class="text-[10px] text-slate-400 mt-0.5">交通/餐飲/住宿/門市/體驗</div>
            </div>
          </div>

          <!-- 動作按鈕 -->
          <div class="pt-2 flex flex-wrap gap-3">
            <a href="#handbook-reader" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold px-6 py-3 rounded-xl shadow-lg transition text-sm flex items-center space-x-2">
              <span>📖</span>
              <span>線上閱覽手冊全文</span>
            </a>
            <a href="#calculator" class="bg-white/15 hover:bg-white/25 border border-white/25 text-white font-bold px-6 py-3 rounded-xl transition text-sm flex items-center space-x-2">
              <span>🧮</span>
              <span>試算旅程省多少碳</span>
            </a>
          </div>
        </div>

        <!-- 右欄：真・手冊封面立體書模 (100% 內嵌 Base64，絕不破圖) -->
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="relative group w-full max-w-sm sm:max-w-md">
            <!-- 懸浮徽章 -->
            <div class="absolute -top-3 -right-3 z-20 bg-amber-400 text-slate-950 text-xs font-black px-3.5 py-1.5 rounded-full shadow-lg border border-amber-300 transform rotate-3 flex items-center space-x-1">
              <span>★</span>
              <span>2026 淨零認證實踐版</span>
            </div>

            <!-- 立體手冊封面外框 -->
            <div class="rounded-2xl overflow-hidden border-4 border-emerald-400/50 book-shadow bg-slate-900 transform transition duration-500 group-hover:scale-[1.02] group-hover:-translate-y-1">
              <img src="{img_cover}" alt="小半天永續低碳漫遊與遊程碳盤查實務手冊封面" class="w-full h-auto object-cover block">
              
              <!-- 封面底部長條說明 -->
              <div class="bg-gradient-to-t from-slate-950 via-slate-900/90 to-transparent p-4 text-center">
                <p class="text-xs text-emerald-200 font-semibold flex items-center justify-center space-x-1.5">
                  <span>🎨 程式向量逐格引擎繪製 · 出版級主視覺</span>
                </p>
              </div>
            </div>
          </div>
          <span class="text-xs text-slate-400 mt-3 font-medium">▲ 阿天（小半天旗）與綠導遊（CO₂旗）雙主角封面</span>
        </div>

      </div>
    </div>
  </section>

  <!-- 雙主角官方立繪檔案專區 (真・阿天 ✕ 真・綠導遊) -->
  <section id="characters" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <span class="text-xs uppercase tracking-widest text-emerald-700 font-extrabold bg-emerald-100/80 px-3.5 py-1 rounded-full border border-emerald-300">Official Character Showcase</span>
      <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-3">雙導遊聯手帶路・專業又接地氣</h2>
      <p class="text-slate-600 text-sm mt-1.5 leading-relaxed">
        告別死板的法規宣導！由在地長大的青年導遊阿天，搭檔熟悉國際盤查標準的綠導遊小綠，帶您暢遊小半天並落實碳足跡盤查。
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      
      <!-- 卡片 1：真・阿天 -->
      <div class="glass-card rounded-3xl p-6 sm:p-8 border-2 border-emerald-200 glow-green hover:border-emerald-500 transition duration-300 flex flex-col justify-between relative overflow-hidden">
        <div class="space-y-5">
          <!-- 頂部身分條 -->
          <div class="flex items-center justify-between">
            <span class="inline-flex items-center space-x-1.5 bg-emerald-100 text-emerald-900 font-black text-xs px-3 py-1 rounded-full border border-emerald-300">
              <span>🎋</span>
              <span>小半天竹海之子</span>
            </span>
            <span class="text-xs font-bold text-slate-400">在地嚮導 No.01</span>
          </div>

          <!-- 立繪與基本介紹 -->
          <div class="flex flex-col sm:flex-row items-center sm:items-start space-y-4 sm:space-y-0 sm:space-x-6">
            <!-- 阿天高解析立繪圖 (Base64) -->
            <div class="w-40 h-40 sm:w-44 sm:h-44 rounded-2xl bg-gradient-to-b from-amber-50 to-emerald-50 border-2 border-emerald-400/40 p-2 shrink-0 shadow-md flex items-center justify-center">
              <img src="{img_atian}" alt="真・阿天 (A-Tian)" class="w-full h-full object-contain filter drop-shadow">
            </div>

            <!-- 角色履歷 -->
            <div class="space-y-2 text-center sm:text-left">
              <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2">
                <h3 class="text-2xl font-black text-slate-900">阿天 (A-Tian)</h3>
                <span class="bg-emerald-600 text-white text-[11px] font-bold px-2 py-0.5 rounded">小半天旗</span>
              </div>
              <p class="text-xs text-slate-600 leading-relaxed">
                南投鹿谷鄉在地熱血青年。頭戴綴有嫩綠竹葉徽章的卡其遮陽帽、身穿山林綠登山背心，手中永遠精神抖擻地揮舞「小半天」導遊旗！從小在孟宗竹海與烏龍茶園長大。
              </p>
              
              <!-- 裝備配備標籤 -->
              <div class="flex flex-wrap gap-1.5 pt-1 justify-center sm:justify-start">
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">竹葉遮陽帽</span>
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">登山短靴</span>
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">高固碳竹杯</span>
              </div>
            </div>
          </div>

          <!-- 嚮導台詞 -->
          <div class="bg-emerald-50/90 border border-emerald-200 text-emerald-900 p-3.5 rounded-2xl text-xs font-medium leading-relaxed">
            <span class="font-bold text-emerald-800">🗣️ 阿天說：</span>「來小半天深呼吸！長源圳竹海與德興瀑布就是老天爺賜給我們最棒的 0 碳排負離子清淨機！」
          </div>
        </div>

        <!-- 底部特色專長 -->
        <div class="mt-5 pt-4 border-t border-slate-200/80 grid grid-cols-3 text-center text-xs">
          <div>
            <div class="text-[10px] text-slate-400">竹海步道熟稔度</div>
            <div class="font-bold text-emerald-800 text-sm mt-0.5">100%</div>
          </div>
          <div>
            <div class="text-[10px] text-slate-400">以竹代塑倡議</div>
            <div class="font-bold text-emerald-800 text-sm mt-0.5">★★★★★</div>
          </div>
          <div>
            <div class="text-[10px] text-slate-400">茶席品茗帶路</div>
            <div class="font-bold text-emerald-800 text-sm mt-0.5">在地達人</div>
          </div>
        </div>
      </div>

      <!-- 卡片 2：真・綠導遊 (小綠) -->
      <div class="glass-card rounded-3xl p-6 sm:p-8 border-2 border-teal-200 glow-amber hover:border-teal-500 transition duration-300 flex flex-col justify-between relative overflow-hidden">
        <div class="space-y-5">
          <!-- 頂部身分條 -->
          <div class="flex items-center justify-between">
            <span class="inline-flex items-center space-x-1.5 bg-teal-100 text-teal-900 font-black text-xs px-3 py-1 rounded-full border border-teal-300">
              <span>📊</span>
              <span>觀光署碳盤查認證</span>
            </span>
            <span class="text-xs font-bold text-slate-400">碳盤專家 No.02</span>
          </div>

          <!-- 立繪與基本介紹 -->
          <div class="flex flex-col sm:flex-row items-center sm:items-start space-y-4 sm:space-y-0 sm:space-x-6">
            <!-- 小綠高解析立繪圖 (Base64) -->
            <div class="w-40 h-40 sm:w-44 sm:h-44 rounded-2xl bg-gradient-to-b from-sky-50 to-teal-50 border-2 border-teal-400/40 p-2 shrink-0 shadow-md flex items-center justify-center">
              <img src="{img_xiaolu}" alt="真・綠導遊 (Xiao-Lu)" class="w-full h-full object-contain filter drop-shadow">
            </div>

            <!-- 角色履歷 -->
            <div class="space-y-2 text-center sm:text-left">
              <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2">
                <h3 class="text-2xl font-black text-slate-900">綠導遊・小綠</h3>
                <span class="bg-teal-600 text-white text-[11px] font-bold px-2 py-0.5 rounded">CO₂ 旗</span>
              </div>
              <p class="text-xs text-slate-600 leading-relaxed">
                人稱「綠導遊」，專精交通部觀光署《旅行業遊程碳足跡計算指引》與 ISO 14067。戴綠色休閒帽、手持代表溫室氣體的黃色 CO₂ 計數旗，擅長將枯燥的碳排算式化為生動的減碳行動！
              </p>
              
              <!-- 裝備配備標籤 -->
              <div class="flex flex-wrap gap-1.5 pt-1 justify-center sm:justify-start">
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">CO₂ 計數旗</span>
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">星型馬尾夾</span>
                <span class="bg-slate-100 text-slate-700 text-[10px] font-semibold px-2 py-0.5 rounded">碳盤查計算表</span>
              </div>
            </div>
          </div>

          <!-- 導遊台詞 -->
          <div class="bg-teal-50/90 border border-teal-200 text-teal-900 p-3.5 rounded-2xl text-xs font-medium leading-relaxed">
            <span class="font-bold text-teal-800">🗣️ 綠導遊說：</span>「不算不知道，一算省一半！跟著綠導遊，吃得當季、搭得節能，每一位旅客都是拯救地球的減碳英雄！」
          </div>
        </div>

        <!-- 底部特色專長 -->
        <div class="mt-5 pt-4 border-t border-slate-200/80 grid grid-cols-3 text-center text-xs">
          <div>
            <div class="text-[10px] text-slate-400">數據盤查精確度</div>
            <div class="font-bold text-teal-800 text-sm mt-0.5">100%</div>
          </div>
          <div>
            <div class="text-[10px] text-slate-400">指引法規掌握度</div>
            <div class="font-bold text-teal-800 text-sm mt-0.5">★★★★★</div>
          </div>
          <div>
            <div class="text-[10px] text-slate-400">遊程減碳規劃力</div>
            <div class="font-bold text-teal-800 text-sm mt-0.5">-65.4% 實證</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 示範遊程全覽 (結合高清路線圖圖表) -->
  <section id="itinerary" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="bg-white rounded-3xl p-6 sm:p-10 border border-emerald-100 shadow-xl">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
        <div>
          <span class="text-xs bg-emerald-100 text-emerald-800 font-extrabold px-3 py-1 rounded-full border border-emerald-300">Featured Route</span>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-2">小半天兩天一夜慢活示範遊程</h2>
          <p class="text-slate-600 text-xs sm:text-sm mt-1">全台最具代表性的低碳竹茶行旅 · 實測人均僅 16.8 kg CO₂e</p>
        </div>
        <div class="inline-flex items-center space-x-2 text-xs bg-emerald-50 text-emerald-900 border border-emerald-300 px-4 py-2.5 rounded-2xl shadow-sm">
          <span class="text-lg">🏆</span>
          <span>每位旅客較傳統遊程<strong>實質減碳 31.8 公斤</strong></span>
        </div>
      </div>

      <!-- 程式繪製之高清路線圖圖表 (Base64 絕不破圖) -->
      <div class="mb-10 rounded-2xl overflow-hidden border-2 border-emerald-200/80 shadow-lg bg-stone-50">
        <img src="{img_itinerary}" alt="小半天兩天一夜慢活低碳行旅路線圖" class="w-full h-auto object-cover block">
      </div>

      <!-- 亮點站點卡片 -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200">
          <div class="font-bold text-emerald-900 text-sm mb-1">🌿 長源圳竹海隧道</div>
          <p class="text-slate-600 leading-relaxed">全台最大孟宗竹林，健行步行 0 碳排，林下涼爽天然冷氣房。</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50/60 border border-amber-200">
          <div class="font-bold text-amber-900 text-sm mb-1">🥢 產地時令竹筒飯</div>
          <p class="text-slate-600 leading-relaxed">在地小農現採冬筍與麻竹筍，縮短食材里程，無免洗一次性餐盒。</p>
        </div>
        <div class="p-4 rounded-2xl bg-sky-50/60 border border-sky-200">
          <div class="font-bold text-sky-900 text-sm mb-1">💦 德興瀑布水氣仙境</div>
          <p class="text-slate-600 leading-relaxed">上萬個負離子水氣，自備保溫水壺盛裝山泉冷泡茶，0 瓶裝水廢棄。</p>
        </div>
        <div class="p-4 rounded-2xl bg-purple-50/60 border border-purple-200">
          <div class="font-bold text-purple-900 text-sm mb-1">🎋 小半天竹藝工坊</div>
          <p class="text-slate-600 leading-relaxed">以竹代塑手作 DIY，製作天然竹筷、竹編杯墊，將碳匯帶回家。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 核心量化工具：遊程碳足跡即時互動試算模擬器 -->
  <section id="calculator" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="bg-gradient-to-br from-slate-900 via-emerald-950 to-teal-950 rounded-3xl p-6 sm:p-10 lg:p-12 text-white shadow-2xl border border-emerald-700/40">
      
      <div class="max-w-3xl mb-8">
        <span class="text-xs uppercase tracking-widest text-emerald-400 font-black bg-emerald-500/20 px-3.5 py-1 rounded-full border border-emerald-400/30">Interactive ESG Dashboard</span>
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black mt-3 text-white">遊程碳足跡即時互動試算器</h2>
        <p class="text-slate-300 text-xs sm:text-sm mt-2 leading-relaxed">
          依據交通部觀光署計算指引與 114 年度最新電力排放係數（0.466 kg/度），點選您的旅行方案，即時計算每人碳排放量與減碳百分比！
        </p>
      </div>

      <!-- 程式繪製之高清五大構面碳盤查圖表 (Base64 絕不破圖) -->
      <div class="mb-10 rounded-2xl overflow-hidden border-2 border-emerald-500/30 shadow-xl bg-slate-950/60">
        <img src="{img_carbon}" alt="每位旅客遊程碳足跡五大構面減碳對比分析" class="w-full h-auto object-cover block">
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- 左側：情境選擇控制面板 (Options) -->
        <div class="lg:col-span-7 space-y-4">
          
          <!-- 1. 交通運具 -->
          <div class="bg-white/10 backdrop-blur-md rounded-2xl p-4 border border-white/10">
            <label class="text-xs font-bold text-emerald-300 flex items-center space-x-2 mb-2.5">
              <span>🚌 ① 交通運輸模式（往返約 240 公里）</span>
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
              <button onclick="setOption('trans', 'public')" id="btn-trans-public" class="opt-btn trans-btn p-3 rounded-xl border text-left transition bg-emerald-500 text-slate-950 font-bold border-emerald-400 shadow">
                <div class="font-bold">台灣好行 / 大巴</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 9.6 kg</div>
              </button>
              <button onclick="setOption('trans', 'van')" id="btn-trans-van" class="opt-btn trans-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">包車接駁 (9人座)</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 18.2 kg</div>
              </button>
              <button onclick="setOption('trans', 'car')" id="btn-trans-car" class="opt-btn trans-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">自駕小客車 (2人)</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 28.5 kg</div>
              </button>
            </div>
          </div>

          <!-- 2. 餐飲型態 -->
          <div class="bg-white/10 backdrop-blur-md rounded-2xl p-4 border border-white/10">
            <label class="text-xs font-bold text-amber-300 flex items-center space-x-2 mb-2.5">
              <span>🥢 ② 餐飲飲食型態（2天4餐）</span>
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
              <button onclick="setOption('food', 'low')" id="btn-food-low" class="opt-btn food-btn p-3 rounded-xl border text-left transition bg-emerald-500 text-slate-950 font-bold border-emerald-400 shadow">
                <div class="font-bold">小半天在地筍蔬餐</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 3.8 kg</div>
              </button>
              <button onclick="setOption('food', 'mid')" id="btn-food-mid" class="opt-btn food-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">一般特色風味合菜</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 7.6 kg</div>
              </button>
              <button onclick="setOption('food', 'high')" id="btn-food-high" class="opt-btn food-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">高牛肉/海鮮大餐</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 14.2 kg</div>
              </button>
            </div>
          </div>

          <!-- 3. 住宿型態 -->
          <div class="bg-white/10 backdrop-blur-md rounded-2xl p-4 border border-white/10">
            <label class="text-xs font-bold text-sky-300 flex items-center space-x-2 mb-2.5">
              <span>🏡 ③ 住宿旅館選擇（1晚）</span>
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
              <button onclick="setOption('hotel', 'eco')" id="btn-hotel-eco" class="opt-btn hotel-btn p-3 rounded-xl border text-left transition bg-emerald-500 text-slate-950 font-bold border-emerald-400 shadow">
                <div class="font-bold">小半天環保民宿</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 2.4 kg</div>
              </button>
              <button onclick="setOption('hotel', 'standard')" id="btn-hotel-standard" class="opt-btn hotel-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">一般山莊旅館</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 5.2 kg</div>
              </button>
              <button onclick="setOption('hotel', 'resort')" id="btn-hotel-resort" class="opt-btn hotel-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">大型豪華度假酒店</div>
                <div class="text-[11px] opacity-80 mt-0.5">人均約 9.8 kg</div>
              </button>
            </div>
          </div>

          <!-- 4. 體驗與自備減塑 -->
          <div class="bg-white/10 backdrop-blur-md rounded-2xl p-4 border border-white/10">
            <label class="text-xs font-bold text-purple-300 flex items-center space-x-2 mb-2.5">
              <span>🎋 ④ 體驗活動與自備減塑習慣</span>
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <button onclick="setOption('diy', 'bamboo')" id="btn-diy-bamboo" class="opt-btn diy-btn p-3 rounded-xl border text-left transition bg-emerald-500 text-slate-950 font-bold border-emerald-400 shadow">
                <div class="font-bold">孟宗竹工藝 DIY (以竹代塑)</div>
                <div class="text-[11px] opacity-80 mt-0.5">自備環保水壺毛巾 (1.0 kg)</div>
              </button>
              <button onclick="setOption('diy', 'plastic')" id="btn-diy-plastic" class="opt-btn diy-btn p-3 rounded-xl border text-left transition bg-white/5 hover:bg-white/15 text-slate-200 border-white/10">
                <div class="font-bold">購買市售塑膠紀念品</div>
                <div class="text-[11px] opacity-80 mt-0.5">使用拋棄式瓶裝水備品 (3.2 kg)</div>
              </button>
            </div>
          </div>

        </div>

        <!-- 右側：即時試算儀表板 (Live Result Dashboard) -->
        <div class="lg:col-span-5 bg-white text-slate-900 rounded-3xl p-6 sm:p-8 shadow-2xl border-4 border-emerald-400">
          <div class="text-center pb-6 border-b border-slate-100">
            <div class="text-xs font-bold uppercase tracking-widest text-slate-400">每人每趟遊程碳足跡</div>
            <div class="flex items-baseline justify-center space-x-2 mt-2">
              <span id="total-carbon" class="text-5xl sm:text-6xl font-black text-emerald-600 transition-all duration-300">16.8</span>
              <span class="text-xl font-bold text-slate-600">kg CO₂e</span>
            </div>
            <div class="inline-flex items-center space-x-1.5 mt-3 bg-emerald-50 text-emerald-800 text-xs font-bold px-3.5 py-1.5 rounded-full border border-emerald-200 shadow-sm">
              <span id="reduction-rate">-65.4%</span>
              <span class="text-[11px] font-normal text-slate-500">（相較傳統自駕遊程基準 48.6 kg）</span>
            </div>
          </div>

          <!-- 各構面碳排佔比細項 -->
          <div class="py-6 space-y-3.5 text-xs">
            <div class="flex justify-between items-center text-slate-600">
              <span class="flex items-center space-x-2">
                <span class="w-3 h-3 rounded-full bg-emerald-500 inline-block shadow-sm"></span>
                <span>交通運輸碳排</span>
              </span>
              <span id="detail-trans" class="font-bold text-slate-900 text-sm">9.6 kg</span>
            </div>
            <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
              <div id="bar-trans" class="bg-emerald-500 h-2 rounded-full transition-all duration-300" style="width: 57%"></div>
            </div>

            <div class="flex justify-between items-center text-slate-600 pt-1">
              <span class="flex items-center space-x-2">
                <span class="w-3 h-3 rounded-full bg-amber-500 inline-block shadow-sm"></span>
                <span>餐飲食材碳排</span>
              </span>
              <span id="detail-food" class="font-bold text-slate-900 text-sm">3.8 kg</span>
            </div>
            <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
              <div id="bar-food" class="bg-amber-500 h-2 rounded-full transition-all duration-300" style="width: 23%"></div>
            </div>

            <div class="flex justify-between items-center text-slate-600 pt-1">
              <span class="flex items-center space-x-2">
                <span class="w-3 h-3 rounded-full bg-sky-500 inline-block shadow-sm"></span>
                <span>旅宿住宿碳排</span>
              </span>
              <span id="detail-hotel" class="font-bold text-slate-900 text-sm">2.4 kg</span>
            </div>
            <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
              <div id="bar-hotel" class="bg-sky-500 h-2 rounded-full transition-all duration-300" style="width: 14%"></div>
            </div>

            <div class="flex justify-between items-center text-slate-600 pt-1">
              <span class="flex items-center space-x-2">
                <span class="w-3 h-3 rounded-full bg-purple-500 inline-block shadow-sm"></span>
                <span>體驗活動與備品廢棄</span>
              </span>
              <span id="detail-diy" class="font-bold text-slate-900 text-sm">1.0 kg</span>
            </div>
            <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
              <div id="bar-diy" class="bg-purple-500 h-2 rounded-full transition-all duration-300" style="width: 6%"></div>
            </div>
          </div>

          <!-- 環境效益回饋 -->
          <div class="bg-emerald-50/90 border border-emerald-200 rounded-2xl p-4 text-xs space-y-1.5 mt-1 shadow-sm">
            <div class="font-bold text-emerald-950 flex items-center space-x-1.5">
              <span>🌱 減碳環境效益換算：</span>
            </div>
            <p class="text-slate-700 leading-relaxed font-medium" id="eco-equivalent">
              每位旅客為地球省下約 <strong>31.8 kg CO₂e</strong>，相當於 <strong>2.6 棵成年孟宗竹</strong> 整整一整年的碳吸存量！
            </p>
          </div>

          <div class="mt-6 text-center">
            <button onclick="alert('已成功將當前試算方案【人均 ' + document.getElementById('total-carbon').innerText + ' kg CO2e】儲存為您的綠色履歷卡片！')" class="w-full bg-slate-950 hover:bg-slate-800 text-white font-bold py-3.5 rounded-xl text-xs transition shadow hover:shadow-lg flex items-center justify-center space-x-2">
              <span>📥</span>
              <span>保存我的遊程碳足跡清冊卡</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  </section>


  <!-- 原創影音導覽與教學動畫專區 (小半天系列 EP1-EP6 ✕ 碳導遊小綠系列 EP1-EP7) -->
  <section id="videos" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="bg-gradient-to-br from-slate-900 via-emerald-950 to-slate-900 rounded-3xl p-6 sm:p-10 border border-emerald-800/40 text-white shadow-2xl">
      
      <!-- 標題與系列切換按鈕 -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-8 pb-6 border-b border-emerald-800/30">
        <div>
          <span class="text-xs uppercase tracking-widest text-emerald-300 font-extrabold bg-emerald-500/20 px-3.5 py-1 rounded-full border border-emerald-400/30 inline-flex items-center space-x-1.5">
            <span>🎬</span>
            <span>Official Animated Video Series · 雙系列原創影音</span>
          </span>
          <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black mt-3 text-white">
            小半天生態行旅 ✕ 碳導遊小綠 影音導覽專區
          </h2>
          <p class="text-slate-300 text-xs sm:text-sm mt-1.5">
            國立臺中科技大學 USR團隊 子計畫H 打造 · Python 向量逐格動畫 ✕ 雙導遊專業導覽
          </p>
        </div>
        
        <!-- 系列切換按鈕 -->
        <div class="flex items-center space-x-2 bg-slate-800/90 p-1.5 rounded-2xl border border-white/10 text-xs font-bold shrink-0">
          <button onclick="switchVideoSeries('xbt')" id="btn-series-xbt" class="px-4 py-2.5 rounded-xl transition bg-emerald-500 text-slate-950 font-black shadow-md flex items-center space-x-1.5">
            <span>🎋</span>
            <span>小半天系列 (EP1–EP6)</span>
          </button>
          <button onclick="switchVideoSeries('xl')" id="btn-series-xl" class="px-4 py-2.5 rounded-xl transition text-slate-300 hover:text-white font-semibold flex items-center space-x-1.5">
            <span>📊</span>
            <span>碳導遊小綠系列 (EP1–EP7)</span>
          </button>
        </div>
      </div>

      <!-- 主播放器劇院 (Theater Video Player) -->
      <div class="bg-black/90 rounded-2xl overflow-hidden border-2 border-emerald-500/40 shadow-2xl mb-8">
        <div class="relative aspect-video max-h-[540px] w-full flex items-center justify-center bg-black">
          <video id="main-video-player" controls preload="metadata" class="w-full h-full object-contain" src="videos/xbt_ep1_origin.mp4" poster="videos/thumbnails/xbt_ep1_origin.jpg">
            您的瀏覽器不支援 HTML5 影片播放。
          </video>
        </div>
        
        <!-- 播放器下方資訊條 -->
        <div class="p-4 sm:p-6 bg-slate-950/95 flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-t border-white/10">
          <div class="space-y-1">
            <div class="flex items-center space-x-2">
              <span id="player-badge" class="bg-emerald-500 text-slate-950 text-xs font-black px-2.5 py-0.5 rounded-md">EP1</span>
              <h3 id="player-title" class="text-base sm:text-xl font-black text-white">小半天 EP1：世外桃源由來</h3>
            </div>
            <p id="player-desc" class="text-xs sm:text-sm text-slate-300">走進南投鹿谷鄉小半天，探索高位台地地形、晨昏雲霧繚繞之仙境由來與微氣候特色。</p>
          </div>
          <div class="shrink-0 flex items-center space-x-3">
            <span id="player-author" class="text-xs bg-emerald-950/90 text-emerald-300 border border-emerald-500/40 px-3.5 py-1.5 rounded-xl font-bold flex items-center space-x-1.5">
              <span>👤</span><span>在地嚮導・阿天 帶路</span>
            </span>
          </div>
        </div>
      </div>

      <!-- 集數選擇卡片清單 (Episode Grid) -->
      <div>
        <div class="flex items-center justify-between mb-3.5">
          <h4 id="series-grid-title" class="text-xs sm:text-sm font-bold uppercase tracking-wider text-emerald-400 flex items-center space-x-2">
            <span>📺</span>
            <span>點擊下方集數立即切換播放：小半天生態行旅系列 (全 6 集)</span>
          </h4>
          <span class="text-[11px] text-slate-400">點擊卡片自動切換並播放</span>
        </div>
        <div id="video-card-grid" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3.5">
          <!-- 卡片將由 JavaScript 動態渲染 -->
        </div>
      </div>

    </div>
  </section>

  <!-- 手冊全文線上閱讀專區 (六大篇章分頁切換) -->
  <section id="handbook-reader" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
    <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-xl">
      
      <div class="flex flex-col md:flex-row md:items-center justify-between pb-6 border-b border-slate-200 gap-4">
        <div>
          <span class="text-xs bg-emerald-100 text-emerald-900 font-black px-3 py-1 rounded-full border border-emerald-300">Handbook Full Text</span>
          <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-2">手冊全文線上閱讀專區</h2>
          <p class="text-slate-600 text-xs sm:text-sm mt-1">點選下方分頁標籤，即時查閱各篇章完整內容、計算公式與作業清冊</p>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="window.print()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold px-4 py-2.5 rounded-xl transition flex items-center space-x-1.5 border border-slate-300 shadow-sm">
            <span>🖨️</span>
            <span>列印 / 存為 PDF 手冊</span>
          </button>
        </div>
      </div>

      <!-- 分頁標籤按鈕列 -->
      <div class="flex overflow-x-auto space-x-2 py-4 border-b border-slate-100 text-xs font-bold scrollbar-none">
        <button onclick="switchTab(1)" id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm">
          篇章一：走進仙境小半天
        </button>
        <button onclick="switchTab(2)" id="tab-btn-2" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0">
          篇章二：低碳旅遊心法
        </button>
        <button onclick="switchTab(3)" id="tab-btn-3" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0">
          篇章三：遊程碳盤查方法學
        </button>
        <button onclick="switchTab(4)" id="tab-btn-4" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0">
          篇章四：兩天一夜實測清冊
        </button>
        <button onclick="switchTab(5)" id="tab-btn-5" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0">
          篇章五：減量認證與淨零路徑
        </button>
        <button onclick="switchTab(6)" id="tab-btn-6" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0">
          附錄：旅客出發前自主低碳 Check-List
        </button>
      </div>

      <!-- 內容展示區 -->
      <div class="py-6">
        
        <!-- 篇章一 -->
        <div id="tab-content-1" class="tab-content space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-emerald-50 border-l-4 border-emerald-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-emerald-950 text-base">【篇章一】走進仙境小半天：地理人文與生態底蘊</h3>
            <p class="text-xs text-emerald-800 mt-1">導遊阿天：「小半天是一塊被大自然溫柔親吻的天然綠色台地！從清晨的雲海到午後的竹風，每一刻都是最好的深呼吸時光。」</p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 flex items-center space-x-1.5 text-base">
              <span>🏔️ 1.1 台地地形與世外桃源之由來</span>
            </h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              小半天位於南投縣鹿谷鄉竹林村、竹豐村與和雅村一帶，為一處由地殼運動隆起形成的高位河階台地。東側倚靠鳳凰山脈（主峰海拔 1,698 公尺），北與西兩側被北勢溪與溪頭群山環抱，形成天然的三面屏障地形。
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div class="bg-white p-3 rounded-xl border border-emerald-200 text-center">
                <div class="text-2xl font-black text-emerald-700">600～1,100</div>
                <div class="text-[11px] text-slate-500">海拔高度（公尺）</div>
              </div>
              <div class="bg-white p-3 rounded-xl border border-emerald-200 text-center">
                <div class="text-2xl font-black text-emerald-700">8～10°C</div>
                <div class="text-[11px] text-slate-500">日夜溫差</div>
              </div>
              <div class="bg-white p-3 rounded-xl border border-emerald-200 text-center">
                <div class="text-2xl font-black text-emerald-700">85%+</div>
                <div class="text-[11px] text-slate-500">年均相對濕度</div>
              </div>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
              由於海拔適中且日夜溫差明顯，清晨山嵐與午後水氣容易在冷暖交替之間凝結為漫天雲霧。從遠處望去，整座台地宛如漂浮在半天高空之中，因而得名「小半天」。常年雲霧繚繞的微氣候特徵，讓此地成為孟宗竹林與高山烏龍茶生長的黃金風土——溼度高而日照柔和，恰好抑制病蟲害、促進茶葉胺基酸累積，造就了凍頂烏龍茶濃醇甘韻的獨特風味。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 flex items-center space-x-1.5 text-base">
              <span>🎋 1.2 綠金傳奇：孟宗竹海與長源圳百年古圳</span>
            </h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              小半天擁有全台灣面積最大、密度最高的孟宗竹林聚落，竹林覆蓋面積超過 <strong>2,000 公頃</strong>。孟宗竹（學名 <em>Phyllostachys pubescens</em>）為生長極為迅速之多年生禾本科植物，從竹筍破土到成竹僅需 40～60 天，最高可長至 20 公尺以上。
            </p>
            <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-4 space-y-2">
              <div class="font-bold text-emerald-900 text-sm">🌿 天然高固碳生物質——為什麼竹子是碳匯寶庫？</div>
              <p class="text-xs text-slate-600 leading-relaxed">
                孟宗竹的年生質（Biomass）累積速率與吸碳能力約為一般溫帶闊葉林木的 <strong>1.5～2.0 倍</strong>。根據林業及自然保育署研究資料，每公頃孟宗竹林每年可固定約 <strong>12～15 噸 CO₂</strong>。以小半天 2,000 公頃竹林估算，整座竹海每年碳吸存量高達約 <strong>24,000～30,000 噸 CO₂</strong>，相當於一座小型火力發電廠的年排放量！這正是小半天推動低碳旅遊最強大的天然後盾。
              </p>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>長源圳生態步道</strong>是清代先民為引水灌溉梯田茶園而鑿建的百年古圳，流水終年不絕。步道依水圳而建，兩側夾道翠竹形成數百公尺天然綠色隧道。夏季林下的氣溫常比山下市區低 4～6°C，宛如天然冷氣房——遊客行走其間完全不需空調電力，是 <strong>0 能源消耗、0 碳排放</strong>的理想生態旅遊場域。步道平坦好走，全程約 1.5 公里，適合老幼同行，沿途可觀察竹根盤結、蕨類附生與溪流生態。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 flex items-center space-x-1.5 text-base">
              <span>💦 1.3 德興瀑布：萬級負離子的大自然冷氣房</span>
            </h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              位於小半天竹豐村深處的德興瀑布，屬於北勢溪支流，為兩層跌水型瀑布，總落差約 50 公尺。水流自數十公尺懸崖飛瀉而下，水珠劇烈碰撞產生細緻水霧（又稱 Lenard effect），經環保署與學術單位實測，瀑布區負離子濃度高達：
            </p>
            <div class="grid grid-cols-2 gap-3">
              <div class="bg-sky-50 p-3 rounded-xl border border-sky-200 text-center">
                <div class="text-2xl font-black text-sky-700">10,000～25,000</div>
                <div class="text-[11px] text-slate-500">ions/cm³ · 德興瀑布實測</div>
              </div>
              <div class="bg-red-50 p-3 rounded-xl border border-red-200 text-center">
                <div class="text-2xl font-black text-red-400">100～300</div>
                <div class="text-[11px] text-slate-500">ions/cm³ · 一般都市平均</div>
              </div>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
              負離子有助於人體呼吸道淨化、穩定自律神經，被稱為「空氣維他命」。本手冊倡導遊客<strong>「自備環保水壺裝取山泉冷泡茶」</strong>，在享受瀑布水氣洗禮的同時，從源頭杜絕一次性塑膠瓶裝水垃圾——瀑布下游水質清澈甘冽，直接取泉冷泡凍頂烏龍茶，風味絕佳！
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 flex items-center space-x-1.5 text-base">
              <span>🍵 1.4 凍頂茶香傳奇與茶文化</span>
            </h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              鹿谷鄉是台灣凍頂烏龍茶的發源地，相傳清朝咸豐年間由林鳳池自福建武夷山帶回茶苗栽種於凍頂山。傳統採用<strong>龍眼木炭慢火細焙</strong>，歷經初焙、覆焙、團揉等十數道工序，賦予茶湯濃醇果香與熟成焙火喉韻。
            </p>
            <p class="text-sm text-slate-600 leading-relaxed">
              近年小半天青農積極推展<strong>草生栽培</strong>（以地被植物取代除草劑）與<strong>減化學肥料管理</strong>，大幅降低農藥與氮肥施用所造成的溫室氣體（N₂O）排放。有機友善茶園不僅保護了土壤微生物多樣性，也讓茶湯更加純淨天然。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 flex items-center space-x-1.5 text-base">
              <span>🌸 1.5 石馬公園與竹藝工藝傳承</span>
            </h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              石馬公園種植數百株河津櫻，因小半天獨特的高山微氣候（秋季涼爽但不至嚴寒），呈現每年<strong>「9 月秋季開花、春節再次盛開」的雙開奇景</strong>，是全台極為罕見的一年兩花期現象，吸引大量賞櫻人潮。
            </p>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>以竹代塑生活美學</strong>——小半天竹藝師傳承百年竹編技法，從傳統竹籃、竹篩延伸至現代竹牙刷、竹吸管、竹纖維餐盤、高溫竹炭除臭除濕產品，展現從搖籃到搖籃（Cradle to Cradle, C2C）的循環資材價值。竹製品在生命終了後可自然生物降解、回歸土壤，完全不留下塑膠微粒污染。
            </p>
          </div>
        </div>

        <!-- 篇章二 -->
        <div id="tab-content-2" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-amber-50 border-l-4 border-amber-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-amber-950 text-base">【篇章二】低碳旅遊心法：無痕山林與責任消費實踐</h3>
            <p class="text-xs text-amber-800 mt-1">碳導遊小綠：「低碳不是苦行，而是更有品味、更有溫度的精緻慢遊！選對交通、吃對食材，一趟旅程就能省下超過 30 公斤碳排。」</p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🌿 2.1 責任漫遊（Responsible Travel）核心原則</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              低碳旅遊並非「刻苦窮遊」，而是在旅途各環節中，<strong>有意識地選擇友善環境的交通、餐飲與住宿</strong>，將碳排放降至最低，並將經濟效益回饋給在地守護環境的社區與小農。聯合國世界旅遊組織（UNWTO）統計，觀光產業佔全球碳排放約 8%，其中交通佔最大宗。改變旅行方式，就是改變地球未來。
            </p>
            <div class="bg-amber-50 border border-amber-200 rounded-xl p-4">
              <div class="font-bold text-amber-900 text-sm mb-2">📋 低碳旅遊四大行動宣言</div>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                <div class="bg-white p-3 rounded-lg border border-amber-100">
                  <div class="font-bold text-amber-800">1. 輕裝慢行</div>
                  <p class="text-slate-600 mt-1">搭乘公共運具或高乘載共乘，漫步健行步道。一台大巴載 40 人 vs 20 台自駕車，碳效率差 10 倍以上！</p>
                </div>
                <div class="bg-white p-3 rounded-lg border border-amber-100">
                  <div class="font-bold text-amber-800">2. 在地旬味</div>
                  <p class="text-slate-600 mt-1">多吃在地竹筍與蔬食，縮短食物里程。小半天鮮筍從田間到餐桌不到 5 公里，幾乎零運輸碳排。</p>
                </div>
                <div class="bg-white p-3 rounded-lg border border-amber-100">
                  <div class="font-bold text-amber-800">3. 自備減塑</div>
                  <p class="text-slate-600 mt-1">自備保溫瓶、環保餐具、盥洗備品毛巾，告別拋棄式製品。一趟兩天行程至少減少 8 件一次性塑膠廢棄物。</p>
                </div>
                <div class="bg-white p-3 rounded-lg border border-amber-100">
                  <div class="font-bold text-amber-800">4. 綠色採購</div>
                  <p class="text-slate-600 mt-1">選購在地竹藝品（以竹代塑）與產銷履歷農特產，讓旅遊消費直接回饋在地守護環境的社區。</p>
                </div>
              </div>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🚌 2.2 交通低碳化：大眾運輸與共乘接駁</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              交通往往佔一趟旅程總碳排放的 <strong>50%～70%</strong>，是最大的排碳熱點。以台中到小半天來回約 240 公里為例：
            </p>
            <div class="overflow-x-auto">
              <table class="w-full text-xs border border-slate-200 rounded-xl overflow-hidden">
                <thead class="bg-slate-100 text-slate-800 font-bold">
                  <tr>
                    <th class="p-2.5 text-left">交通方式</th>
                    <th class="p-2.5 text-center">油耗計算</th>
                    <th class="p-2.5 text-center">每人碳排</th>
                    <th class="p-2.5 text-center">相對比較</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 bg-white">
                  <tr class="bg-red-50">
                    <td class="p-2.5 font-bold">自駕休旅車（2人乘坐）</td>
                    <td class="p-2.5 text-center">240km / 14km/L = 17L 汽油，17 x 3.08 / 2人</td>
                    <td class="p-2.5 text-center font-bold text-red-700">26.2 kg</td>
                    <td class="p-2.5 text-center">基準 100%</td>
                  </tr>
                  <tr>
                    <td class="p-2.5 font-bold">9人座包車（滿載）</td>
                    <td class="p-2.5 text-center">240km / 8km/L = 30L 柴油，30 x 3.32 / 9人</td>
                    <td class="p-2.5 text-center font-bold text-amber-700">11.1 kg</td>
                    <td class="p-2.5 text-center text-emerald-700">-57.6%</td>
                  </tr>
                  <tr class="bg-emerald-50">
                    <td class="p-2.5 font-bold">台灣好行大巴（40人乘坐）</td>
                    <td class="p-2.5 text-center">240km / 4km/L = 60L 柴油，60 x 3.32 / 40人</td>
                    <td class="p-2.5 text-center font-bold text-emerald-700">5.0 kg</td>
                    <td class="p-2.5 text-center text-emerald-700 font-bold">-80.9%</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
              選擇大眾運輸出行，每人單趟交通碳排可從 26.2 kg 降至 5.0 kg！再加上社區組織中巴或電動接駁車整合接駁，避免遊客一人一車開上山，減緩山區道路壅塞與怠速廢氣排放。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🥗 2.3 在地旬味產地餐桌：吃當季、吃在地</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              小半天盛產冬筍（11～2 月）、麻竹筍（6～9 月）、綠竹筍，鮮筍自產地直送餐桌，運輸距離小於 5 公里，食物里程幾乎為零。推廣少肉多蔬食，用數據說話：
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
              <div class="bg-red-50 p-3 rounded-xl border border-red-200">
                <div class="text-lg font-black text-red-700">60.0</div>
                <div class="text-slate-500">kg CO₂e/kg</div>
                <div class="font-bold text-red-600 mt-1">牛肉</div>
              </div>
              <div class="bg-orange-50 p-3 rounded-xl border border-orange-200">
                <div class="text-lg font-black text-orange-700">37.1</div>
                <div class="text-slate-500">kg CO₂e/kg</div>
                <div class="font-bold text-orange-600 mt-1">豬肉</div>
              </div>
              <div class="bg-yellow-50 p-3 rounded-xl border border-yellow-200">
                <div class="text-lg font-black text-yellow-700">9.9</div>
                <div class="text-slate-500">kg CO₂e/kg</div>
                <div class="font-bold text-yellow-600 mt-1">雞肉</div>
              </div>
              <div class="bg-emerald-50 p-3 rounded-xl border border-emerald-200">
                <div class="text-lg font-black text-emerald-700">0.8～1.5</div>
                <div class="text-slate-500">kg CO₂e/kg</div>
                <div class="font-bold text-emerald-600 mt-1">在地鮮筍蔬菜</div>
              </div>
            </div>
            <div class="bg-amber-50 border border-amber-200 rounded-xl p-3 text-xs text-amber-900">
              <strong>📐 小綠教你算：</strong>假設一桌合菜 10 人份，傳統餐含牛肉 0.8 kg + 豬肉 1.2 kg。碳排 = 0.8 x 60 + 1.2 x 37.1 = <strong>92.5 kg</strong>（每人 9.25 kg）。改為在地筍蔬餐 3.0 kg 蔬菜竹筍，碳排 = 3.0 x 1.2 = <strong>3.6 kg</strong>（每人僅 0.36 kg），單餐減碳達 <strong>96%</strong>！
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🎋 2.4 以竹代塑：天然生質的固碳革命</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              傳統塑膠牙刷、塑膠梳子每件製造排碳約 0.05～0.12 kg CO₂e，且掩埋後百年不腐，最終分解為危害海洋生態的塑膠微粒。竹製牙刷採用天然孟宗竹切削，植物生長期間已透過光合作用吸收大氣中之 CO₂，製程能耗極低，廢棄後可自然生物降解堆肥。
            </p>
            <p class="text-sm text-slate-600 leading-relaxed">
              小半天竹炭製品更具除臭、調濕、遠紅外線功能，一袋竹炭除濕包可反覆使用 2～3 年，全面取代化學除濕劑。每位旅客選購竹製伴手禮，就是在支持在地循環經濟、減少塑膠汙染！
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🏡 2.5 環保標章旅宿選住</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              住宿碳排的最大來源是<strong>空調用電</strong>與<strong>一次性備品消耗</strong>。小半天因海拔較高，夜間氣溫常降至 20°C 以下，山間涼風讓旅客能舒適入睡而完全不需開冷氣。主動不索取一次性備品（牙刷、牙膏、浴帽、拖鞋），自備毛巾減少洗滌能耗，每人每夜住宿碳排僅 <strong>2.4 kg</strong>，相比一般山莊飯店的 5.2～9.8 kg，減碳幅度高達 <strong>53%～76%</strong>。
            </p>
          </div>
        </div>

        <!-- 篇章三 -->
        <div id="tab-content-3" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-sky-50 border-l-4 border-sky-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-sky-950 text-base">【篇章三】遊程碳盤查方法學：觀光署指引標準實作</h3>
            <p class="text-xs text-sky-800 mt-1">碳導遊小綠：「盤查不是玄學，掌握『活動數據 x 排放係數』就能精準算碳！讓我手把手帶你算一遍。」</p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">📋 3.1 為什麼旅行業要算碳？</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>政策法規驅動</strong>：交通部觀光署推動旅行業產品碳標籤認證，鼓勵同業建立低碳遊程產品線。環境部溫室氣體減量及管理法亦將觀光產業納入淨零轉型路徑規劃。
            </p>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>企業供應鏈 ESG 要求</strong>：國內外上市櫃企業採購員工旅遊或獎勵旅遊時，日趨重視「遊程碳足跡盤查證明」與「減碳績效報告」。擁有碳標籤的遊程產品，將成為企業 ESG 報告書中的亮點項目，是旅行社未來的核心競爭力。
            </p>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>消費者意識崛起</strong>：新世代旅客關心自己「一趟旅行到底排了多少碳」，願意為低碳旅程支付合理的綠色溢價。透明的碳排數據，是贏得信任的最佳行銷武器。
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🔍 3.2 盤查邊界與生命週期範疇</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              依照 ISO 14067 產品碳足跡標準與觀光署計算指引，遊程盤查邊界為<strong>「搖籃到大門（Cradle-to-Gate）」</strong>——自旅客於集合地點報到出發開始，歷經所有表定交通、參訪、餐飲、住宿，直至旅程結束解散為止。
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div class="bg-blue-50 p-4 rounded-xl border border-blue-200 space-y-1">
                <div class="font-bold text-blue-900 text-sm">範疇一（Scope 1）</div>
                <div class="text-xs text-blue-700 font-semibold">直接排放</div>
                <p class="text-xs text-slate-600">旅行社自身擁有或控制之運具排放。例如：自購公務車油耗、自家遊覽車柴油發動機。</p>
              </div>
              <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-200 space-y-1">
                <div class="font-bold text-indigo-900 text-sm">範疇二（Scope 2）</div>
                <div class="text-xs text-indigo-700 font-semibold">能源間接排放</div>
                <p class="text-xs text-slate-600">門市、服務據點營運所消耗的外購電力。例如：辦公室照明、電腦、影印機用電。</p>
              </div>
              <div class="bg-purple-50 p-4 rounded-xl border border-purple-200 space-y-1">
                <div class="font-bold text-purple-900 text-sm">範疇三（Scope 3）</div>
                <div class="text-xs text-purple-700 font-semibold">其他間接排放</div>
                <p class="text-xs text-slate-600">外包遊覽車燃油、大眾運輸客運、委託餐廳食材、合作飯店住宿、景點門票與手作耗材等供應鏈排放。<strong>此為旅行業最大排放源。</strong></p>
              </div>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-slate-950 text-white space-y-3">
            <h4 class="font-bold text-emerald-400 text-base">🧮 3.3 碳足跡計算核心公式</h4>
            <div class="bg-slate-900 p-4 rounded-xl border border-slate-700 text-center">
              <p class="text-lg font-mono font-bold text-amber-300">
                碳排放量 (kg CO₂e) = Σ (活動數據 x 排放係數 x GWP)
              </p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
              <div class="bg-slate-800 p-3 rounded-lg">
                <div class="font-bold text-emerald-300">活動數據 (Activity Data)</div>
                <p class="text-slate-400 mt-1">公升數（油耗）、度數（電力）、人-公里（運輸）、公斤數（食材、垃圾）等可量測的消耗量。</p>
              </div>
              <div class="bg-slate-800 p-3 rounded-lg">
                <div class="font-bold text-amber-300">排放係數 (Emission Factor)</div>
                <p class="text-slate-400 mt-1">依據環境部碳足跡資訊網及觀光署資料庫所公告之物質對應排碳係數。</p>
              </div>
              <div class="bg-slate-800 p-3 rounded-lg">
                <div class="font-bold text-sky-300">全球暖化潛勢 (GWP)</div>
                <p class="text-slate-400 mt-1">CO₂ = 1, CH₄ = 28, N₂O = 265（依 IPCC 第五次評估報告 AR5）。多數情況直接使用「kg CO₂e」合併計算。</p>
              </div>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-sky-50 border border-sky-200 space-y-3">
            <h4 class="font-bold text-sky-900 text-base">📐 3.3.1 小綠教你算 — 交通構面計算範例</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>題目：</strong>一台 43 人座遊覽車（柴油引擎），從台中載 40 位旅客前往小半天，單程 120 公里。請計算每位旅客的交通碳排放量。
            </p>
            <div class="bg-white p-4 rounded-xl border border-sky-200 space-y-2 text-sm font-mono">
              <div class="text-slate-600"><span class="text-sky-700 font-bold">Step 1</span> 計算油耗：120 km / 4 km/L = <strong>30 公升柴油</strong></div>
              <div class="text-slate-600"><span class="text-sky-700 font-bold">Step 2</span> 套用排放係數：30 L x 3.320 kg CO₂e/L = <strong>99.6 kg CO₂e</strong>（全車）</div>
              <div class="text-slate-600"><span class="text-sky-700 font-bold">Step 3</span> 人均分攤：99.6 / 40 人 = <strong class="text-emerald-700">2.49 kg CO₂e/人</strong>（單程）</div>
              <div class="text-slate-600"><span class="text-sky-700 font-bold">Step 4</span> 往返碳排：2.49 x 2 = <strong class="text-emerald-700">4.98 kg CO₂e/人</strong>（來回）</div>
            </div>
            <p class="text-xs text-sky-800">加上車上每人發放 1 瓶 600ml 瓶裝水（0.121 kg/瓶），總交通碳排 = 4.98 + 0.121 = <strong>5.10 kg CO₂e/人</strong></p>
          </div>

          <div class="p-5 rounded-2xl bg-amber-50 border border-amber-200 space-y-3">
            <h4 class="font-bold text-amber-900 text-base">📐 3.3.2 小綠教你算 — 餐飲構面計算範例</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>題目：</strong>午餐合菜 4 桌（10 人/桌），菜單含：豬肉 1.5 kg/桌、雞肉 1.0 kg/桌、在地竹筍蔬菜 3.0 kg/桌、天然氣烹飪 0.8 m³/桌。計算每人碳排。
            </p>
            <div class="bg-white p-4 rounded-xl border border-amber-200 space-y-2 text-sm font-mono">
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 1</span> 豬肉：1.5 kg x 37.1 = <strong>55.65 kg</strong></div>
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 2</span> 雞肉：1.0 kg x 9.87 = <strong>9.87 kg</strong></div>
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 3</span> 竹筍蔬菜：3.0 kg x 1.2 = <strong>3.60 kg</strong></div>
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 4</span> 天然氣：0.8 m³ x 2.63 = <strong>2.10 kg</strong></div>
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 5</span> 每桌合計：55.65 + 9.87 + 3.60 + 2.10 = <strong>71.22 kg</strong></div>
              <div class="text-slate-600"><span class="text-amber-700 font-bold">Step 6</span> 每人分攤：71.22 / 10 人 = <strong class="text-amber-700">7.12 kg CO₂e/人</strong>（一餐）</div>
            </div>
            <p class="text-xs text-amber-800">如改為全竹筍蔬食餐（無肉），每桌碳排 = 3.0 x 1.2 + 2.10 = <strong>5.70 kg</strong>，每人僅 <strong>0.57 kg</strong>，減碳達 <strong>92%</strong>！</p>
          </div>

          <div class="p-5 rounded-2xl bg-emerald-50 border border-emerald-200 space-y-3">
            <h4 class="font-bold text-emerald-900 text-base">📐 3.3.3 小綠教你算 — 住宿構面計算範例</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>題目：</strong>小半天環保民宿，20 間客房（2 人/房），民宿當晚共用電 80 度。每房提供 1 套拋棄式盥洗包（但 15 間房的旅客已自備）。計算每人住宿碳排。
            </p>
            <div class="bg-white p-4 rounded-xl border border-emerald-200 space-y-2 text-sm font-mono">
              <div class="text-slate-600"><span class="text-emerald-700 font-bold">Step 1</span> 電力碳排：80 度 x 0.466 kg/度 = <strong>37.28 kg</strong>（全館）</div>
              <div class="text-slate-600"><span class="text-emerald-700 font-bold">Step 2</span> 盥洗包碳排：5 套（僅 5 房使用） x 0.35 kg/套 = <strong>1.75 kg</strong></div>
              <div class="text-slate-600"><span class="text-emerald-700 font-bold">Step 3</span> 住宿合計：37.28 + 1.75 = <strong>39.03 kg</strong></div>
              <div class="text-slate-600"><span class="text-emerald-700 font-bold">Step 4</span> 人均分攤：39.03 / 40 人 = <strong class="text-emerald-700">0.976 kg CO₂e/人</strong></div>
            </div>
            <p class="text-xs text-emerald-800">若全團旅客都自備盥洗用具（0 套拋棄式備品），每人碳排更降至 37.28/40 = <strong>0.932 kg</strong>！可見自備盥洗備品的減塑行動真的有效。</p>
          </div>

          <div class="space-y-3">
            <h4 class="font-bold text-slate-900 text-base">📊 3.4 觀光署指引五大服務構面與最新排放係數速查表</h4>
            <p class="text-sm text-slate-600">以下係數參考環境部碳足跡資訊網及觀光署遊程碳足跡計算指引，實際盤查時請依最新公告版本為準。</p>
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden shadow-sm">
                <thead class="bg-slate-100 text-slate-800 font-bold">
                  <tr>
                    <th class="p-3">服務構面</th>
                    <th class="p-3">盤查項目</th>
                    <th class="p-3">建議蒐集之活動數據</th>
                    <th class="p-3">排放係數（參考值）</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 text-slate-600 bg-white">
                  <tr><td class="p-3 font-bold" rowspan="3">① 門市與營業據點</td><td class="p-3">影印紙 (A4 70g 500張)</td><td class="p-3">用紙包數</td><td class="p-3 font-mono">3.600 kg/包</td></tr>
                  <tr><td class="p-3">外購電力 (114年度)</td><td class="p-3">分攤用電度數</td><td class="p-3 font-mono font-bold text-emerald-700">0.466 kg/度</td></tr>
                  <tr><td class="p-3">生活垃圾焚化</td><td class="p-3">垃圾重量</td><td class="p-3 font-mono">0.360 kg/kg</td></tr>
                  
                  <tr class="bg-slate-50"><td class="p-3 font-bold" rowspan="4">② 交通運輸服務</td><td class="p-3">車用柴油</td><td class="p-3">遊覽車油耗公升數</td><td class="p-3 font-mono">3.320 kg/L</td></tr>
                  <tr class="bg-slate-50"><td class="p-3">車用汽油</td><td class="p-3">自駕車油耗公升數</td><td class="p-3 font-mono">3.080 kg/L</td></tr>
                  <tr class="bg-slate-50"><td class="p-3">PET 瓶裝水 (600ml)</td><td class="p-3">車上發放瓶數</td><td class="p-3 font-mono">0.121 kg/瓶</td></tr>
                  <tr class="bg-slate-50"><td class="p-3">市區/公路客運</td><td class="p-3">搭乘人-公里數</td><td class="p-3 font-mono">0.045~0.060 kg/人-km</td></tr>

                  <tr><td class="p-3 font-bold" rowspan="5">③ 餐飲美食服務</td><td class="p-3">牛肉</td><td class="p-3">食材重量 (kg)</td><td class="p-3 font-mono text-red-600 font-bold">60.000 kg/kg</td></tr>
                  <tr><td class="p-3">豬肉</td><td class="p-3">食材重量 (kg)</td><td class="p-3 font-mono">37.100 kg/kg</td></tr>
                  <tr><td class="p-3">雞肉</td><td class="p-3">食材重量 (kg)</td><td class="p-3 font-mono">9.870 kg/kg</td></tr>
                  <tr><td class="p-3">在地蔬菜竹筍</td><td class="p-3">食材重量 (kg)</td><td class="p-3 font-mono text-emerald-600 font-bold">0.800~1.500 kg/kg</td></tr>
                  <tr><td class="p-3">天然氣 (烹飪)</td><td class="p-3">瓦斯消耗量 (m³)</td><td class="p-3 font-mono">2.630 kg/m³</td></tr>

                  <tr class="bg-slate-50"><td class="p-3 font-bold" rowspan="3">④ 旅宿住宿服務</td><td class="p-3">一般三星飯店客房</td><td class="p-3">住宿間-夜數</td><td class="p-3 font-mono">10.0~15.0 kg/間-夜</td></tr>
                  <tr class="bg-slate-50"><td class="p-3">環保標章/低碳民宿</td><td class="p-3">住宿間-夜數</td><td class="p-3 font-mono text-emerald-600 font-bold">4.0~6.5 kg/間-夜</td></tr>
                  <tr class="bg-slate-50"><td class="p-3">拋棄式盥洗備品包</td><td class="p-3">耗損套數</td><td class="p-3 font-mono">0.250~0.400 kg/套</td></tr>

                  <tr><td class="p-3 font-bold" rowspan="2">⑤ 遊憩體驗服務</td><td class="p-3">壓克力/塑膠手工藝材料</td><td class="p-3">DIY 材料重量 (kg)</td><td class="p-3 font-mono">2.800~4.500 kg/kg</td></tr>
                  <tr><td class="p-3">在地天然竹材</td><td class="p-3">竹材重量 (kg)</td><td class="p-3 font-mono text-emerald-600 font-bold">0.150~0.350 kg/kg</td></tr>
                </tbody>
              </table>
            </div>
            <p class="text-xs text-slate-500 mt-2">* 排放係數來源：環境部碳足跡資訊網、114年度電力排放係數、交通部觀光署遊程碳足跡計算指引。實際盤查請以最新公告版本為準。</p>
          </div>

          <div class="p-5 rounded-2xl bg-purple-50 border border-purple-200 space-y-3">
            <h4 class="font-bold text-purple-900 text-base">💡 3.5 實務操作小提醒——資料蒐集與紀錄</h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="bg-white p-3 rounded-lg border border-purple-100">
                <div class="font-bold text-purple-800">📝 加油收據保存</div>
                <p class="text-slate-600 mt-1">請遊覽車司機於每次加油時保留統一發票或簽單，記錄加油公升數。這是交通構面最重要的活動數據來源。</p>
              </div>
              <div class="bg-white p-3 rounded-lg border border-purple-100">
                <div class="font-bold text-purple-800">🍽️ 餐廳食材清單</div>
                <p class="text-slate-600 mt-1">事先與合作餐廳協商，請廚師提供每桌菜單的主要肉品與蔬菜重量估算。在地小農可提供產銷履歷作為佐證。</p>
              </div>
              <div class="bg-white p-3 rounded-lg border border-purple-100">
                <div class="font-bold text-purple-800">🏨 住宿電力度數</div>
                <p class="text-slate-600 mt-1">請民宿業者提供當晚總用電度數（可查電錶），再以入住人數分攤計算。比直接套用「間-夜」估算更精確。</p>
              </div>
              <div class="bg-white p-3 rounded-lg border border-purple-100">
                <div class="font-bold text-purple-800">📱 數位化記錄</div>
                <p class="text-slate-600 mt-1">建議使用數位表單（Google Forms 或 Excel）即時記錄各環節活動數據，避免紙本遺失，也實踐無紙化精神。</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 篇章四 -->
        <div id="tab-content-4" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-red-50 border-l-4 border-red-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-red-950 text-base">【篇章四】小半天兩天一夜示範遊程實測盤查</h3>
            <p class="text-xs text-red-800 mt-1">阿天 + 小綠聯合實測：以 20 人團體兩天一夜為例，完整演示從數據蒐集到碳排計算的全流程！</p>
          </div>
          
          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🗓️ 4.1 示範遊程時間表（兩天一夜慢活行程）</h4>
            <p class="text-sm text-slate-600">團體規模：20 人 ｜ 往返車程約 240 公里 ｜ 住宿 1 晚 ｜ 正餐 4 餐</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-5 rounded-2xl bg-emerald-50 border border-emerald-200 space-y-2">
              <h5 class="font-bold text-emerald-900 text-sm">🌿 Day 1：翠竹晨嵐・瀑布尋幽</h5>
              <div class="space-y-2 text-xs text-slate-600">
                <div class="flex items-start space-x-2">
                  <span class="bg-emerald-200 text-emerald-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">09:30</span>
                  <div><strong>長源圳生態古圳步道健行＆孟宗竹林綠色隧道漫步</strong><br>全程步行，0 碳排。享受森林浴與萬級負離子洗禮。步道全長約 1.5 km，平坦好走。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-amber-200 text-amber-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">12:00</span>
                  <div><strong>小半天在地竹筒飯風味午餐</strong><br>產地現採旬味鮮筍餐，食材運輸 &lt; 5 km。無免洗餐具，竹筒飯容器天然可降解。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-sky-200 text-sky-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">14:00</span>
                  <div><strong>德興瀑布探幽</strong><br>雙層瀑布萬級負離子洗禮。自備保溫瓶取飲優質山泉水冷泡茶，0 瓶裝水垃圾產出。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-amber-200 text-amber-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">16:30</span>
                  <div><strong>凍頂烏龍茶席品茗體驗</strong><br>高山茶園夕陽與雲海。體驗有機炭焙茶道，了解草生栽培減碳做法。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-indigo-200 text-indigo-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">18:30</span>
                  <div><strong>下榻小半天在地綠色環保民宿</strong><br>自備盥洗毛巾牙刷、夜宿山嵐涼爽免空調。民宿採用 LED 節能燈具與太陽能熱水。</div>
                </div>
              </div>
            </div>
            <div class="p-5 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
              <h5 class="font-bold text-amber-900 text-sm">🎋 Day 2：竹藝傳承・茶香歸途</h5>
              <div class="space-y-2 text-xs text-slate-600">
                <div class="flex items-start space-x-2">
                  <span class="bg-pink-200 text-pink-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">08:30</span>
                  <div><strong>石馬公園晨間漫步</strong><br>欣賞雙開河津櫻與台地晨曦景觀。步行 0 碳排，清晨空氣品質極佳。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-emerald-200 text-emerald-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">10:00</span>
                  <div><strong>小半天竹藝工坊手作體驗</strong><br>以竹代塑！製作專屬竹筷、竹編杯墊帶回家。天然竹材碳足跡僅塑膠材料的 1/10。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-amber-200 text-amber-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">12:30</span>
                  <div><strong>社區低碳茶餐佐野菜時令風味午餐</strong><br>在地小農地產地消。以高山蔬菜、竹筍料理為主，搭配凍頂烏龍茶飲。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-purple-200 text-purple-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">14:30</span>
                  <div><strong>在地小農市集</strong><br>選購無包裝竹筍乾、烏龍茶、竹炭除濕包。直接與農民交易，不經過中間商包裝物流。</div>
                </div>
                <div class="flex items-start space-x-2">
                  <span class="bg-sky-200 text-sky-900 font-bold px-2 py-0.5 rounded text-[10px] shrink-0 mt-0.5">16:00</span>
                  <div><strong>搭乘台灣好行溪頭線低碳大眾接駁賦歸</strong><br>大巴共乘回台中高鐵站，人均碳排僅為自駕車的 1/4～1/5。</div>
                </div>
              </div>
            </div>
          </div>

          <div class="space-y-3">
            <h4 class="font-bold text-slate-900 text-base">📊 4.2 碳盤查數據實測與對比分析</h4>
            <p class="text-sm text-slate-600">以下將「傳統自駕高碳遊程」與「小半天低碳示範遊程」每位旅客之活動數據與排放量逐項比對。每一欄的碳排數字，都是依照篇章三的公式「活動數據 x 排放係數」計算而來。</p>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden shadow-sm">
              <thead class="bg-slate-800 text-white font-bold">
                <tr>
                  <th class="p-3">服務構面</th>
                  <th class="p-3">傳統基準遊程 (Baseline) · 每人數據</th>
                  <th class="p-3 text-center">基準碳排</th>
                  <th class="p-3">小半天低碳遊程 · 每人數據</th>
                  <th class="p-3 text-center">低碳碳排</th>
                  <th class="p-3 text-center">減碳幅度</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-slate-600 bg-white">
                <tr>
                  <td class="p-3 font-bold text-slate-800">① 交通運輸</td>
                  <td class="p-3">自駕休旅車 240km<br><span class="text-[10px] text-slate-400">每人耗油 8.5L 汽油 (8.5x3.08=26.2) + 4 瓶瓶裝水 (4x0.121=0.5) + 怠速排放</span></td>
                  <td class="p-3 text-center font-bold text-red-700">28.5 kg</td>
                  <td class="p-3">台灣好行大巴共乘<br><span class="text-[10px] text-slate-400">每人分攤 2.8L 柴油 (2.8x3.32=9.3) + 自備保溫杯 0 瓶裝水</span></td>
                  <td class="p-3 text-center font-bold text-emerald-700">9.6 kg</td>
                  <td class="p-3 text-center font-bold text-emerald-600">-66.3%</td>
                </tr>
                <tr class="bg-slate-50">
                  <td class="p-3 font-bold text-slate-800">② 餐飲美食</td>
                  <td class="p-3">4 餐合菜含牛排、烤豬肉<br><span class="text-[10px] text-slate-400">進口食材 + 一次性餐具 + 高碳肉品</span></td>
                  <td class="p-3 text-center font-bold text-red-700">14.2 kg</td>
                  <td class="p-3">4 餐在地時令竹筍餐、茶餐<br><span class="text-[10px] text-slate-400">減肉蔬食、無免洗餐具、食材運輸 &lt; 5km</span></td>
                  <td class="p-3 text-center font-bold text-emerald-700">3.8 kg</td>
                  <td class="p-3 text-center font-bold text-emerald-600">-73.2%</td>
                </tr>
                <tr>
                  <td class="p-3 font-bold text-slate-800">③ 住宿服務</td>
                  <td class="p-3">一般山莊飯店<br><span class="text-[10px] text-slate-400">吹冷氣整晚 + 全套拋棄式牙刷沐浴瓶</span></td>
                  <td class="p-3 text-center font-bold text-red-700">5.2 kg</td>
                  <td class="p-3">小半天環保民宿<br><span class="text-[10px] text-slate-400">自然涼風通風免空調 + 自備毛巾牙刷</span></td>
                  <td class="p-3 text-center font-bold text-emerald-700">2.4 kg</td>
                  <td class="p-3 text-center font-bold text-emerald-600">-53.8%</td>
                </tr>
                <tr class="bg-slate-50">
                  <td class="p-3 font-bold text-slate-800">④ 遊憩體驗</td>
                  <td class="p-3">走馬看花購買紀念品<br><span class="text-[10px] text-slate-400">進口塑膠射出小吊飾</span></td>
                  <td class="p-3 text-center font-bold text-red-700">0.5 kg</td>
                  <td class="p-3">升級 2小時竹藝工坊深度手作<br><span class="text-[10px] text-emerald-700 font-semibold">以竹代塑長期固碳 + 收益留地方</span></td>
                  <td class="p-3 text-center font-bold text-amber-700">0.8 kg</td>
                  <td class="p-3 text-center font-bold text-amber-600">+0.3 kg<br><span class="text-[10px]">體驗深化 / 機具電力</span></td>
                </tr>
                <tr>
                  <td class="p-3 font-bold text-slate-800">⑤ 門市據點</td>
                  <td class="p-3">紙本宣傳摺頁（彩色銅版紙）<br><span class="text-[10px] text-slate-400">+ 礦泉水廢瓶垃圾</span></td>
                  <td class="p-3 text-center font-bold text-red-700">0.2 kg</td>
                  <td class="p-3">數位電子手冊 QR Code 導讀<br><span class="text-[10px] text-slate-400">0 紙張 + 0 瓶裝垃圾</span></td>
                  <td class="p-3 text-center font-bold text-emerald-700">0.2 kg</td>
                  <td class="p-3 text-center font-bold text-emerald-600">源頭減廢 100%</td>
                </tr>
                <tr class="bg-emerald-100 text-emerald-900 font-bold text-sm">
                  <td class="p-3">全團每人合計</td>
                  <td class="p-3" colspan="2">傳統遊程每人碳足跡：<strong>48.6 kg CO₂e</strong></td>
                  <td class="p-3" colspan="2">低碳遊程每人碳足跡：<strong>16.8 kg CO₂e</strong></td>
                  <td class="p-3 text-center text-lg">-65.4%</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 小綠專家解惑卡片 (解除視覺錯置) -->
          <div class="bg-emerald-50/90 border-2 border-emerald-300 rounded-2xl p-4 sm:p-5 flex items-start space-x-3 text-xs leading-relaxed text-slate-700">
            <span class="text-2xl shrink-0 mt-0.5">💡</span>
            <div class="space-y-1">
              <div class="font-bold text-emerald-900 text-sm flex items-center space-x-2">
                <span>小綠專家解析：【為何第④項遊憩體驗數值微增 0.3 kg？】</span>
                <span class="bg-emerald-200 text-emerald-800 text-[10px] px-2 py-0.5 rounded font-black">真實盤查不漂綠</span>
              </div>
              <p>
                在傳統遊程中，旅客只是路過購買一個幾十克的廉價塑膠小吊飾；而小半天低碳遊程將活動<strong>升級為扎實的「2小時在地竹藝深度手作工坊」</strong>！
                雖然因工坊打磨機具電力使活動碳排略增 <strong>+0.3 kg</strong>，但天然孟宗竹器具備<strong>長期生質固碳與替代塑膠</strong>效益，且觀光收益 100% 留在地方社區。在體驗大幅升級的同時，全團人均碳排依然實質大降 <strong>-65.4%（省下 31.8 kg CO₂e）</strong>！
              </p>
            </div>
          </div>

          <div class="bg-emerald-50 border-2 border-emerald-300 rounded-2xl p-5 space-y-2">
            <div class="font-bold text-emerald-900 text-base">🏆 盤查實測總結</div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
              <div class="bg-white p-3 rounded-xl border border-emerald-200">
                <div class="text-2xl font-black text-emerald-700">31.8 kg</div>
                <div class="text-xs text-slate-600">每位旅客實質減碳量</div>
              </div>
              <div class="bg-white p-3 rounded-xl border border-emerald-200">
                <div class="text-2xl font-black text-emerald-700">2.6 棵</div>
                <div class="text-xs text-slate-600">等同成年孟宗竹年碳吸存量</div>
              </div>
              <div class="bg-white p-3 rounded-xl border border-emerald-200">
                <div class="text-2xl font-black text-emerald-700">636 kg</div>
                <div class="text-xs text-slate-600">一團 20 人總省碳量</div>
              </div>
            </div>
            <p class="text-xs text-emerald-800 text-center mt-2">換算：若每月出團 4 次（全年 48 團），年度累計減碳量高達 <strong>30,528 kg（約 30.5 噸）CO₂e</strong>，等同 2,544 棵孟宗竹年吸收量！</p>
          </div>
        </div>

        <!-- 篇章五 -->
        <div id="tab-content-5" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-purple-50 border-l-4 border-purple-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-purple-950 text-base">【篇章五】減量效益評估、碳標籤認證與淨零路徑</h3>
            <p class="text-xs text-purple-800 mt-1">小綠：「先實質減碳 65%，再抵換剩餘 16.8 kg——這才是不漂綠的真零碳！」</p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🏅 5.1 旅行社取得觀光署「遊程碳標籤」通關指南</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              取得碳標籤不僅是環保形象加分，更是未來承接企業 ESG 旅遊、政府獎勵旅遊標案的硬門檻。以下四步驟詳解申請流程：
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              <div class="bg-purple-50 p-4 rounded-xl border border-purple-200 text-center space-y-2">
                <div class="text-3xl font-black text-purple-700">Step 1</div>
                <div class="font-bold text-purple-900 text-sm">確立產品邊界</div>
                <p class="text-xs text-slate-600">完成遊程服務構面範圍認定，明確「交通、餐飲、住宿、遊憩、門市」五大構面之涵蓋範圍。定義產品功能單位（如：每人每趟次兩天一夜遊程）。</p>
              </div>
              <div class="bg-indigo-50 p-4 rounded-xl border border-indigo-200 text-center space-y-2">
                <div class="text-3xl font-black text-indigo-700">Step 2</div>
                <div class="font-bold text-indigo-900 text-sm">蒐集佐證單據</div>
                <p class="text-xs text-slate-600">保存加油發票（公升數）、客運車票票根、民宿住宿憑證（用電度數）、在地餐飲食材產銷履歷單據、DIY 材料採購紀錄。所有原始憑證至少保存 3 年。</p>
              </div>
              <div class="bg-sky-50 p-4 rounded-xl border border-sky-200 text-center space-y-2">
                <div class="text-3xl font-black text-sky-700">Step 3</div>
                <div class="font-bold text-sky-900 text-sm">計算與編撰報告</div>
                <p class="text-xs text-slate-600">套用觀光署碳足跡計算表格，逐一填入各構面活動數據與排放係數，產出碳排熱點分析圖（Hotspot Analysis）與具體減量成效評估。撰寫正式碳足跡報告書。</p>
              </div>
              <div class="bg-emerald-50 p-4 rounded-xl border border-emerald-200 text-center space-y-2">
                <div class="text-3xl font-black text-emerald-700">Step 4</div>
                <div class="font-bold text-emerald-900 text-sm">第三方查核登錄</div>
                <p class="text-xs text-slate-600">通過具備資格之查證機構（如 SGS、BSI、TUV 等）實地查驗，取得環境部與觀光署核發之「遊程碳足跡標籤」。標籤有效期通常為 3～5 年，期間需定期更新數據。</p>
              </div>
            </div>
          </div>

          <div class="p-5 rounded-2xl bg-red-50 border border-red-200 space-y-3">
            <h4 class="font-bold text-red-900 text-base">🚫 5.2 自願性碳抵換（Carbon Offsetting）與不漂綠原則</h4>
            <p class="text-sm text-slate-600 leading-relaxed">
              <strong>先減量，再抵換！</strong>這是最重要的原則。不能企圖以低價購買碳權直接宣稱「零碳旅遊」——這就是典型的<strong>漂綠（Greenwashing）</strong>行為。
            </p>
            <div class="bg-white p-4 rounded-xl border border-red-200 space-y-2">
              <div class="font-bold text-red-800 text-sm">正確的淨零路徑：</div>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="bg-emerald-50 p-3 rounded-lg border border-emerald-200 text-center">
                  <div class="font-bold text-emerald-800">第一步：實質減量</div>
                  <p class="text-slate-600 mt-1">透過大眾運輸、產地蔬食與減塑措施，已實現 <strong>-65.4%</strong> 碳排減量（從 48.6 降至 16.8 kg）。</p>
                </div>
                <div class="bg-amber-50 p-3 rounded-lg border border-amber-200 text-center">
                  <div class="font-bold text-amber-800">第二步：識別剩餘排放</div>
                  <p class="text-slate-600 mt-1">每位旅客無可避免的 <strong>16.8 kg CO₂e</strong>（包含必要交通燃油、基礎用電等），需透過抵換中和。</p>
                </div>
                <div class="bg-sky-50 p-3 rounded-lg border border-sky-200 text-center">
                  <div class="font-bold text-sky-800">第三步：碳權抵換</div>
                  <p class="text-slate-600 mt-1">旅行社可購買符合 Gold Standard / VCS / 環境部認證之碳信用額度，或配合在地植樹護竹計畫進行抵換。</p>
                </div>
              </div>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
              以小半天 2,000 公頃竹林年固碳 24,000 噸計算，全年 48 團（960 人次）產生的 16,128 kg（約 16 噸）剩餘排放，僅佔竹海年碳吸存量的 <strong>0.067%</strong>——小半天的竹海碳匯綽綽有餘，完全有能力支撐「100% 碳中和假期」的承諾！
            </p>
          </div>

          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-3">
            <h4 class="font-bold text-slate-900 text-base">🛤️ 5.3 小半天永續旅遊淨零路徑藍圖</h4>
            <p class="text-sm text-slate-600 leading-relaxed">從短期的基礎減量到中長期的淨零目標，規劃如下：</p>
            <div class="space-y-2">
              <div class="flex items-start space-x-3">
                <div class="bg-emerald-500 text-white font-bold text-xs px-3 py-1 rounded-full shrink-0 mt-0.5">近期</div>
                <div class="text-xs text-slate-600"><strong>2025-2026：</strong>完成碳足跡盤查方法學建立、示範遊程碳標籤申請、旅客低碳行為引導機制（Check-List、數位手冊、QR Code 導覽）。</div>
              </div>
              <div class="flex items-start space-x-3">
                <div class="bg-amber-500 text-white font-bold text-xs px-3 py-1 rounded-full shrink-0 mt-0.5">中期</div>
                <div class="text-xs text-slate-600"><strong>2027-2030：</strong>社區全面導入電動接駁車、民宿安裝太陽能光電設施、推動在地小農有機認證覆蓋率達 80%、與林業署合作建立竹林碳匯方法學。</div>
              </div>
              <div class="flex items-start space-x-3">
                <div class="bg-purple-500 text-white font-bold text-xs px-3 py-1 rounded-full shrink-0 mt-0.5">長期</div>
                <div class="text-xs text-slate-600"><strong>2031-2050：</strong>實現小半天休閒農業區 100% 淨零碳排旅遊示範區，成為台灣第一個通過國際認證的「碳中和永續旅遊目的地（Carbon Neutral Destination）」。</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 附錄 (篇章六) -->
        <div id="tab-content-6" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-blue-50 border-l-4 border-blue-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-blue-950 text-base">【附錄】旅客出發前自主低碳 Check-List</h3>
          </div>
          
          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200">
            <h4 class="font-bold text-slate-900 mb-3">附錄一：旅客出發前自主低碳 Check-List</h4>
            <div class="space-y-3">
              <label class="flex items-center space-x-3 cursor-pointer">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-emerald-600 rounded">
                <span class="text-sm text-slate-700">1. 已備妥個人水壺或保溫杯</span>
              </label>
              <label class="flex items-center space-x-3 cursor-pointer">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-emerald-600 rounded">
                <span class="text-sm text-slate-700">2. 已備妥隨身環保餐具與食物袋</span>
              </label>
              <label class="flex items-center space-x-3 cursor-pointer">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-emerald-600 rounded">
                <span class="text-sm text-slate-700">3. 已自備個人盥洗用具（牙刷、牙膏、梳子、毛巾）</span>
              </label>
              <label class="flex items-center space-x-3 cursor-pointer">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-emerald-600 rounded">
                <span class="text-sm text-slate-700">4. 著輕便防滑健行鞋與透氣排汗衣物</span>
              </label>
              <label class="flex items-center space-x-3 cursor-pointer">
                <input type="checkbox" class="form-checkbox h-5 w-5 text-emerald-600 rounded">
                <span class="text-sm text-slate-700">5. 手機已儲存電子手冊離線檔案</span>
              </label>
            </div>
          </div>
          
          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200">
            <h4 class="font-bold text-slate-900 mb-2">附錄二：小半天在地永續綠色公約</h4>
            <p class="text-sm text-slate-600 italic bg-white p-4 rounded-xl border border-slate-200">
              「我們承諾守護小半天的翠竹、古圳與甘泉。以謙遜之心慢步山林，不留一片垃圾，不折一枝修竹；優先品嚐在地旬味，支持以竹代塑生活工藝。讓每一次出發，都是對地球溫柔的祝福！」
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 頁尾宣告 -->
  <footer class="bg-white border-t border-slate-200 py-10 text-center text-xs text-slate-500 space-y-3">
    <div class="flex justify-center items-center space-x-3 font-bold text-slate-800 text-sm">
      <span>小半天休閒農業區</span>
      <span>·</span>
      <span>旅行業遊程碳足跡計算指引</span>
      <span>·</span>
      <span>永續低碳漫遊手冊</span>
    </div>
    <p>依循交通部觀光署 113 年《旅行業遊程碳足跡計算指引》與環境部 114 年度電力排放係數 (0.466 kg CO2e/度) 規範製作</p>
    <p class="text-slate-400">© 2026 國立台中科技大學 USR團隊企劃作品</p>
  </footer>

  <!-- 試算器邏輯 JavaScript -->
  <script>
    const state = {{
      trans: 'public',
      food: 'low',
      hotel: 'eco',
      diy: 'bamboo'
    }};

    const values = {{
      trans: {{ public: 9.6, van: 18.2, car: 28.5 }},
      food: {{ low: 3.8, mid: 7.6, high: 14.2 }},
      hotel: {{ eco: 2.4, standard: 5.2, resort: 9.8 }},
      diy: {{ bamboo: 1.0, plastic: 3.2 }}
    }};

    const baseline = 48.6; // 傳統自駕+合菜+一般飯店基準

    function setOption(category, key) {{
      state[category] = key;

      // 更新按鈕樣式
      document.querySelectorAll(`.${{category}}-btn`).forEach(btn => {{
        btn.classList.remove('bg-emerald-500', 'text-slate-950', 'font-bold', 'border-emerald-400', 'shadow');
        btn.classList.add('bg-white/5', 'hover:bg-white/15', 'text-slate-200', 'border-white/10');
      }});

      const activeBtn = document.getElementById(`btn-${{category}}-${{key}}`);
      if (activeBtn) {{
        activeBtn.classList.add('bg-emerald-500', 'text-slate-950', 'font-bold', 'border-emerald-400', 'shadow');
        activeBtn.classList.remove('bg-white/5', 'hover:bg-white/15', 'text-slate-200', 'border-white/10');
      }}

      calculate();
    }}

    function calculate() {{
      const v_trans = values.trans[state.trans];
      const v_food = values.food[state.food];
      const v_hotel = values.hotel[state.hotel];
      const v_diy = values.diy[state.diy];

      const total = v_trans + v_food + v_hotel + v_diy;
      const reduction = ((baseline - total) / baseline * 100).toFixed(1);
      const savedKg = (baseline - total).toFixed(1);
      const bambooSaved = (Math.max(0, baseline - total) / 12).toFixed(1);

      document.getElementById('total-carbon').innerText = total.toFixed(1);
      
      const rateEl = document.getElementById('reduction-rate');
      if (total < baseline) {{
        rateEl.innerText = `-${{reduction}}%`;
        rateEl.parentElement.className = "inline-flex items-center space-x-1.5 mt-3 bg-emerald-50 text-emerald-800 text-xs font-bold px-3.5 py-1.5 rounded-full border border-emerald-200 shadow-sm";
      }} else {{
        rateEl.innerText = `+${{Math.abs(reduction)}}% (超標)`;
        rateEl.parentElement.className = "inline-flex items-center space-x-1.5 mt-3 bg-red-50 text-red-800 text-xs font-bold px-3.5 py-1.5 rounded-full border border-red-200 shadow-sm";
      }}

      document.getElementById('detail-trans').innerText = `${{v_trans.toFixed(1)}} kg`;
      document.getElementById('detail-food').innerText = `${{v_food.toFixed(1)}} kg`;
      document.getElementById('detail-hotel').innerText = `${{v_hotel.toFixed(1)}} kg`;
      document.getElementById('detail-diy').innerText = `${{v_diy.toFixed(1)}} kg`;

      document.getElementById('bar-trans').style.width = `${{(v_trans / total * 100).toFixed(0)}}%`;
      document.getElementById('bar-food').style.width = `${{(v_food / total * 100).toFixed(0)}}%`;
      document.getElementById('bar-hotel').style.width = `${{(v_hotel / total * 100).toFixed(0)}}%`;
      document.getElementById('bar-diy').style.width = `${{(v_diy / total * 100).toFixed(0)}}%`;

      document.getElementById('eco-equivalent').innerHTML = total < baseline
        ? `每位旅客為地球省下約 <strong>${{savedKg}} kg CO₂e</strong>，相當於 <strong>${{bambooSaved}} 棵成年孟宗竹</strong> 整整一整年的碳吸存量！`
        : `此行程碳排略高於基準值，建議透過調整公共交通接駁或增加在地低碳竹筍蔬食來降低排放！`;
    }}

    // 手冊章節切換邏輯
    function switchTab(idx) {{
      for (let i = 1; i <= 6; i++) {{
        const content = document.getElementById(`tab-content-${{i}}`);
        const btn = document.getElementById(`tab-btn-${{i}}`);
        if (i === idx) {{
          content.classList.remove('hidden');
          btn.className = "tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm";
        }} else {{
          content.classList.add('hidden');
          btn.className = "tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0";
        }}
      }}
    }}

    // ==========================================
    // 影音導覽播放器邏輯
    // ==========================================
    const videoSeriesData = {{
      xbt: {{
        name: '小半天生態行旅系列 (全 6 集)',
        author: '在地嚮導・阿天 帶路',
        badgeColor: 'bg-emerald-500 text-slate-950',
        episodes: [
          {{ ep: 'EP1', title: '小半天 EP1：世外桃源由來', desc: '走進南投鹿谷鄉小半天，探索高位台地地形、晨昏雲霧繚繞之仙境由來與微氣候特色。', src: 'videos/xbt_ep1_origin.mp4', poster: 'videos/thumbnails/xbt_ep1_origin.jpg' }},
          {{ ep: 'EP2', title: '小半天 EP2：孟宗竹海長源圳', desc: '漫步全台面積最大 2,000 公頃孟宗竹海綠色隧道，探尋清代長源圳百年流水歷史。', src: 'videos/xbt_ep2_bamboo.mp4', poster: 'videos/thumbnails/xbt_ep2_bamboo.jpg' }},
          {{ ep: 'EP3', title: '小半天 EP3：德興瀑布與雙瀑', desc: '探訪深山雙層飛瀑，感受水珠劇烈碰撞產生萬級負離子的大自然冷氣房洗禮。', src: 'videos/xbt_ep3_waterfall.mp4', poster: 'videos/thumbnails/xbt_ep3_waterfall.jpg' }},
          {{ ep: 'EP4', title: '小半天 EP4：凍頂烏龍茶香傳奇', desc: '鹿谷凍頂茶鄉傳統龍眼木炭焙工藝，搭配友善環境草生栽培，減少溫室氣體排放。', src: 'videos/xbt_ep4_tea.mp4', poster: 'videos/thumbnails/xbt_ep4_tea.jpg' }},
          {{ ep: 'EP5', title: '小半天 EP5：石馬公園與竹藝傳奇', desc: '欣賞河津櫻每年秋季與春節雙開奇景，體驗以竹代塑生活工藝與天然高固碳資材。', src: 'videos/xbt_ep5_sakura_bamboo.mp4', poster: 'videos/thumbnails/xbt_ep5_sakura_bamboo.jpg' }},
          {{ ep: 'EP6', title: '小半天 EP6：兩天一夜低碳全攻略', desc: '兩天一夜示範行程全紀錄！實測每人減碳 31.8 公斤，相當於 2.6 棵孟宗竹年吸收量。', src: 'videos/xbt_ep6_itinerary.mp4', poster: 'videos/thumbnails/xbt_ep6_itinerary.jpg' }}
        ]
      }},
      xl: {{
        name: '碳導遊小綠系列 (全 7 集)',
        author: '碳盤專家・小綠 講解',
        badgeColor: 'bg-teal-400 text-slate-950',
        episodes: [
          {{ ep: 'EP1', title: '碳導遊小綠 EP1：旅行社也要算碳', desc: '旅行社帶團也要算碳嗎？觀光署指引推動與國內外企業 ESG 綠色旅遊新風潮。', src: 'videos/xl_ep1_travel_carbon.mp4', poster: 'videos/thumbnails/xl_ep1_travel_carbon.jpg' }},
          {{ ep: 'EP2', title: '碳導遊小綠 EP2：範疇一自家排的碳', desc: '拆解直接溫室氣體排放——自家遊覽車燃油發動機消耗與公務車油耗盤查。', src: 'videos/xl_ep2_scope1.mp4', poster: 'videos/thumbnails/xl_ep2_scope1.jpg' }},
          {{ ep: 'EP3', title: '碳導遊小綠 EP3：範疇二買來的電', desc: '能源間接排放——採用 114 年度最新電力係數 0.466 kg/度盤查門市與據點用電。', src: 'videos/xl_ep3_scope2.mp4', poster: 'videos/thumbnails/xl_ep3_scope2.jpg' }},
          {{ ep: 'EP4', title: '碳導遊小綠 EP4：範疇三上下游的碳', desc: '旅行業最龐大的排放來源——外包大巴、委託餐廳食材、合作飯店與體驗耗材。', src: 'videos/xl_ep4_scope3.mp4', poster: 'videos/thumbnails/xl_ep4_scope3.jpg' }},
          {{ ep: 'EP5', title: '碳導遊小綠 EP5：碳足跡的邊界', desc: '搖籃到大門的生命週期界定——旅客自集合報到開始至旅程結束解散之邊界規範。', src: 'videos/xl_ep5_boundary.mp4', poster: 'videos/thumbnails/xl_ep5_boundary.jpg' }},
          {{ ep: 'EP6', title: '碳導遊小綠 EP6：動手算一趟旅程', desc: '活動數據 × 排放係數實測演練——手把手計算交通、餐飲、住宿每一公斤碳排放。', src: 'videos/xl_ep6_calculation.mp4', poster: 'videos/thumbnails/xl_ep6_calculation.jpg' }},
          {{ ep: 'EP7', title: '碳導遊小綠 EP7：總整理', desc: '遊程碳盤查與減碳心法大複習——吃得當季、搭得節能，每一位旅客都是拯救地球的英雄。', src: 'videos/xl_ep7_summary.mp4', poster: 'videos/thumbnails/xl_ep7_summary.jpg' }}
        ]
      }}
    }};

    let currentSeries = 'xbt';
    let currentEpIdx = 0;

    function renderVideoCards() {{
      const series = videoSeriesData[currentSeries];
      const grid = document.getElementById('video-card-grid');
      grid.innerHTML = '';

      document.getElementById('series-grid-title').innerHTML = `<span>📺</span><span>點擊下方集數立即切換播放：${{series.name}}</span>`;

      series.episodes.forEach((ep, idx) => {{
        const isCurrent = idx === currentEpIdx;
        const card = document.createElement('div');
        card.className = `cursor-pointer rounded-xl overflow-hidden border-2 transition duration-200 transform hover:-translate-y-1 bg-slate-900 ${{
          isCurrent ? 'border-emerald-400 ring-2 ring-emerald-500/50 shadow-lg scale-[1.02]' : 'border-white/10 hover:border-emerald-400/60'
        }}`;
        card.onclick = () => selectVideo(idx);

        card.innerHTML = `
          <div class="relative aspect-video bg-black overflow-hidden group">
            <img src="${{ep.poster}}" alt="${{ep.title}}" class="w-full h-full object-cover transition duration-300 group-hover:scale-105">
            <div class="absolute inset-0 bg-black/40 flex items-center justify-center opacity-70 group-hover:opacity-100 transition">
              <span class="w-8 h-8 rounded-full bg-emerald-500/90 text-slate-950 flex items-center justify-center font-bold text-xs shadow-md">▶</span>
            </div>
            <span class="absolute top-1.5 left-1.5 text-[10px] font-black px-1.5 py-0.5 rounded ${{series.badgeColor}} shadow">
              ${{ep.ep}}
            </span>
          </div>
          <div class="p-2 sm:p-2.5">
            <div class="font-bold text-xs text-white truncate">${{ep.title}}</div>
            <div class="text-[10px] text-slate-400 line-clamp-1 mt-0.5">${{ep.desc}}</div>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function selectVideo(idx) {{
      currentEpIdx = idx;
      const ep = videoSeriesData[currentSeries].episodes[idx];
      const player = document.getElementById('main-video-player');

      player.src = ep.src;
      player.poster = ep.poster;
      player.load();
      player.play().catch(e => console.log('Autoplay blocked, waiting user click'));

      document.getElementById('player-badge').innerText = ep.ep;
      document.getElementById('player-badge').className = `${{videoSeriesData[currentSeries].badgeColor}} text-xs font-black px-2.5 py-0.5 rounded-md`;
      document.getElementById('player-title').innerText = ep.title;
      document.getElementById('player-desc').innerText = ep.desc;
      document.getElementById('player-author').innerHTML = `<span>👤</span><span>${{videoSeriesData[currentSeries].author}}</span>`;

      renderVideoCards();
    }}

    function switchVideoSeries(key) {{
      currentSeries = key;
      currentEpIdx = 0;

      const btnXbt = document.getElementById('btn-series-xbt');
      const btnXl = document.getElementById('btn-series-xl');

      if (key === 'xbt') {{
        btnXbt.className = 'px-4 py-2.5 rounded-xl transition bg-emerald-500 text-slate-950 font-black shadow-md flex items-center space-x-1.5';
        btnXl.className = 'px-4 py-2.5 rounded-xl transition text-slate-300 hover:text-white font-semibold flex items-center space-x-1.5';
      }} else {{
        btnXl.className = 'px-4 py-2.5 rounded-xl transition bg-teal-400 text-slate-950 font-black shadow-md flex items-center space-x-1.5';
        btnXbt.className = 'px-4 py-2.5 rounded-xl transition text-slate-300 hover:text-white font-semibold flex items-center space-x-1.5';
      }}

      selectVideo(0);
    }}

    // 頁面載入時初始化渲染影片卡片
    document.addEventListener('DOMContentLoaded', () => {{
      renderVideoCards();
    }});

  </script>
</body>
</html>
'''

# 寫入工作區
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 寫入 Artifacts 目錄
artifact_dir = "/Users/chenchunchih/.gemini/antigravity/brain/ffffa1ca-bacc-4bc5-9685-daf8c3584b33"
with open(os.path.join(artifact_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"頂級完整版 index.html 生成成功！大小約 {len(html_content)} bytes")
