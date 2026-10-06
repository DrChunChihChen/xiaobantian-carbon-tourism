import re

with open("build_full_website.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Navigation link
old_nav = '<a href="#calculator" class="text-emerald-700 hover:text-emerald-800 transition flex items-center space-x-1">\n          <span>🧮</span>\n          <span>碳足跡試算器</span>\n        </a>\n        <a href="#handbook-reader" class="hover:text-emerald-700 transition">手冊全文</a>'
new_nav = '''<a href="#calculator" class="text-emerald-700 hover:text-emerald-800 transition flex items-center space-x-1">
          <span>🧮</span>
          <span>碳足跡試算器</span>
        </a>
        <a href="#videos" class="hover:text-emerald-700 transition flex items-center space-x-1">
          <span>🎬</span>
          <span>影音導覽動畫</span>
        </a>
        <a href="#handbook-reader" class="hover:text-emerald-700 transition">手冊全文</a>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    print("Updated navigation bar")
else:
    print("Warning: old_nav not matched precisely, trying regex...")
    content = re.sub(
        r'(<a href="#calculator".*?</a>)\s*(<a href="#handbook-reader")',
        r'\1\n        <a href="#videos" class="hover:text-emerald-700 transition flex items-center space-x-1"><span>🎬</span><span>影音導覽動畫</span></a>\n        \2',
        content,
        flags=re.DOTALL
    )

# 2. Add Video Section before Handbook Reader
video_section_html = '''
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
            國立臺中科技大學 URR團隊 子計畫H 打造 · Python 向量逐格動畫 ✕ 雙導遊專業導覽
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
'''

content = content.replace('  <!-- 手冊全文線上閱讀專區 (六大篇章分頁切換) -->\n', video_section_html, 1)

# 3. Add Video JavaScript logic before </body>
video_js = '''
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
'''

content = content.replace('  </script>\n</body>', video_js + '\n  </script>\n</body>', 1)

with open("build_full_website.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_full_website.py with Video section and JavaScript logic.")
