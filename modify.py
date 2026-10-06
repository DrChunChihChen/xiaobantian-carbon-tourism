import re

with open("build_full_website.py", "r", encoding="utf-8") as f:
    content = f.read()

# Generate the new handbook-reader section
new_handbook = """  <!-- 手冊全文線上閱讀專區 (六大篇章分頁切換) -->
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
          </div>
          <div class="grid grid-cols-1 gap-5">
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900 flex items-center space-x-1.5">
                <span>🏔️ 1.1 台地地形與世外桃源之由來</span>
              </h4>
              <p class="text-xs text-slate-600 leading-normal">
                小半天位於南投縣鹿谷鄉竹林村、竹豐村與和雅村一帶，為一處隆起的高位台地。東側倚靠鳳凰山脈，北與西兩側被北勢溪與溪頭群山環抱。海拔約600～1,100公尺，日夜溫差約8～10℃。常年雲霧繚繞，溼度高、日照柔和，是孟宗竹林與高山烏龍茶生長的黃金風土。
              </p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900 flex items-center space-x-1.5">
                <span>🎋 1.2 綠金傳奇：孟宗竹海與長源圳百年古圳</span>
              </h4>
              <p class="text-xs text-slate-600 leading-normal">
                全台面積最大、密度最高的孟宗竹林聚落，竹林覆蓋超過2,000公頃。孟宗竹40～60天即可成竹，年生質累積速率與吸碳能力約為一般溫帶林木的1.5至2.0倍。長源圳生態步道依水圳而建，兩側夾道翠竹形成數百公尺天然綠色隧道，夏季林下氣溫常比市區低4～6℃，是0能源消耗、0碳排的天然降溫森林步道。
              </p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900 flex items-center space-x-1.5">
                <span>💦 1.3 德興瀑布：萬級負離子的大自然冷氣房</span>
              </h4>
              <p class="text-xs text-slate-600 leading-normal">
                位於竹豐村深處，屬於北勢溪支流，為兩層跌水型瀑布。負離子濃度高達10,000～25,000 ions/cm³（一般市區僅約100～300 ions/cm³）。倡導遊客自備環保水壺裝取山泉冷泡茶，杜絕一次性塑膠瓶裝水垃圾。
              </p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900 flex items-center space-x-1.5">
                <span>🍵 1.4 凍頂茶香傳奇與石馬公園</span>
              </h4>
              <p class="text-xs text-slate-600 leading-normal">
                鹿谷鄉是台灣凍頂烏龍茶發源地。傳統採用龍眼木炭慢火細焙。小半天青農近年積極推展草生栽培與減化學肥料管理。石馬公園種植數百株河津櫻，呈現每年秋季開花、春節再次盛開的雙開奇景。以竹代塑生活美學：傳統竹編延伸至現代竹牙刷、竹吸管、高溫竹炭除臭除濕產品。
              </p>
            </div>
          </div>
        </div>

        <!-- 篇章二 -->
        <div id="tab-content-2" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-amber-50 border-l-4 border-amber-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-amber-950 text-base">【篇章二】低碳旅遊心法：無痕山林與責任消費</h3>
          </div>
          <div class="grid grid-cols-1 gap-5">
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900">2.1 責任漫遊核心原則: 低碳旅遊四大行動宣言</h4>
              <p class="text-xs text-slate-600">1.輕裝慢行：搭乘公共運具或高乘載共乘<br>2.在地旬味：多吃在地竹筍與蔬食，縮短食物里程<br>3.自備減塑：自備保溫瓶、環保餐具、盥洗備品毛巾<br>4.綠色採購：選購在地竹藝品與產銷履歷農特產</p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900">2.2 交通低碳化：大眾運輸與共乘接駁</h4>
              <p class="text-xs text-slate-600">交通往往佔一趟旅程總碳排放的50%～70%。自台中高鐵站搭乘台灣好行溪頭線，接駁車行碳排僅為自駕自用車之1/3至1/4。社區組織中巴或電動接駁車整合接駁。</p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900">2.3 在地旬味產地餐桌</h4>
              <p class="text-xs text-slate-600">小半天盛產冬筍（11～2月）、麻竹筍（6～9月）、綠竹筍。運輸距離小於5公里。牛肉碳排放係數高達約60 kg CO₂e/kg，豬肉約37.1 kg CO₂e/kg，而新鮮蔬菜與在地筍類通常低於1.5 kg CO₂e/kg。每增加一餐低碳竹筍蔬食合菜，人均即可減少2.5～3.8 kg CO₂e。</p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900">2.4 以竹代塑：天然生質的固碳革命</h4>
              <p class="text-xs text-slate-600">傳統塑膠牙刷每件製造排碳約0.05～0.12 kg CO₂e且掩埋後百年不腐；竹製牙刷採用天然孟宗竹切削，植物生長期間已吸收大氣中之CO₂，廢棄後可自然生物降解堆肥。</p>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
              <h4 class="font-bold text-slate-900">2.5 環保標章旅宿選住</h4>
              <p class="text-xs text-slate-600">不索取一次性備品、自備毛巾、夜間享受山間涼風少開冷氣，住宿每人每夜碳排僅2.4 kg vs 一般飯店5.2-9.8 kg。</p>
            </div>
          </div>
        </div>

        <!-- 篇章三 -->
        <div id="tab-content-3" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-sky-50 border-l-4 border-sky-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-sky-950 text-base">【篇章三】遊程碳盤查方法學：觀光署指引標準實作</h3>
          </div>
          
          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
            <h4 class="font-bold text-slate-900">3.1 為什麼旅行業要算碳？</h4>
            <p class="text-xs text-slate-600">政策法規驅動：交通部觀光署推動旅行業產品碳標籤。企業供應鏈ESG要求：上市櫃企業採購員工旅遊時日趨重視遊程碳足跡盤查證明。</p>
          </div>
          <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200 space-y-2">
            <h4 class="font-bold text-slate-900">3.2 盤查邊界與生命週期範疇</h4>
            <p class="text-xs text-slate-600">依ISO 14067與觀光署計算指引。邊界起迄：自旅客集合出發至旅程結束解散。範疇一（直接排放）：自家遊覽車燃油。範疇二（能源間接排放）：門市營運外購電力。範疇三（其他間接排放）：外包遊覽車、委託餐廳、合作飯店等供應鏈排放。</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-950 text-white space-y-2">
            <h4 class="font-bold text-emerald-400">3.3 碳足跡計算核心公式</h4>
            <p class="text-sm font-mono text-amber-300">碳排放量(kg CO₂e) = Σ(活動數據 × 排放係數 × GWP)</p>
            <p class="text-xs text-slate-400">活動數據：公升數、度數、人-公里、公斤數。GWP: CO₂=1, CH₄=28, N₂O=265 (AR5)</p>
          </div>

          <h4 class="font-bold text-slate-900 mt-4">3.4 觀光署指引五大服務構面與係數表</h4>
          <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden shadow-sm">
              <thead class="bg-slate-100 text-slate-800 font-bold">
                <tr>
                  <th class="p-3">服務構面</th>
                  <th class="p-3">項目</th>
                  <th class="p-3">參考排放係數</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-slate-600 bg-white">
                <tr><td class="p-3 font-bold" rowspan="3">① 門市與營業據點</td><td class="p-3">影印紙</td><td class="p-3">3.600 kg/包</td></tr>
                <tr><td class="p-3">外購電力 (114年)</td><td class="p-3">0.466 kg/度</td></tr>
                <tr><td class="p-3">生活垃圾</td><td class="p-3">0.360 kg/kg</td></tr>
                
                <tr><td class="p-3 font-bold bg-slate-50" rowspan="4">② 交通運輸服務</td><td class="p-3 bg-slate-50">柴油</td><td class="p-3 bg-slate-50">3.320 kg/L</td></tr>
                <tr><td class="p-3 bg-slate-50">汽油</td><td class="p-3 bg-slate-50">3.080 kg/L</td></tr>
                <tr><td class="p-3 bg-slate-50">PET瓶裝水</td><td class="p-3 bg-slate-50">0.121 kg/瓶</td></tr>
                <tr><td class="p-3 bg-slate-50">客運</td><td class="p-3 bg-slate-50">0.045~0.060 kg/人-公里</td></tr>

                <tr><td class="p-3 font-bold" rowspan="5">③ 餐飲美食服務</td><td class="p-3">牛肉</td><td class="p-3">60.000 kg/kg</td></tr>
                <tr><td class="p-3">豬肉</td><td class="p-3">37.100 kg/kg</td></tr>
                <tr><td class="p-3">雞肉</td><td class="p-3">9.870 kg/kg</td></tr>
                <tr><td class="p-3">在地蔬菜竹筍</td><td class="p-3">0.800~1.500 kg/kg</td></tr>
                <tr><td class="p-3">天然氣</td><td class="p-3">2.630 kg/m³</td></tr>

                <tr><td class="p-3 font-bold bg-slate-50" rowspan="3">④ 旅宿住宿服務</td><td class="p-3 bg-slate-50">一般三星飯店</td><td class="p-3 bg-slate-50">10.0~15.0 kg/間-夜</td></tr>
                <tr><td class="p-3 bg-slate-50">環保民宿</td><td class="p-3 bg-slate-50">4.0~6.5 kg/間-夜</td></tr>
                <tr><td class="p-3 bg-slate-50">拋棄式盥洗包</td><td class="p-3 bg-slate-50">0.250~0.400 kg/套</td></tr>

                <tr><td class="p-3 font-bold" rowspan="2">⑤ 遊憩體驗服務</td><td class="p-3">壓克力塑膠工藝材料</td><td class="p-3">2.800~4.500 kg/kg</td></tr>
                <tr><td class="p-3">天然竹材</td><td class="p-3">0.150~0.350 kg/kg</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- 篇章四 -->
        <div id="tab-content-4" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-red-50 border-l-4 border-red-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-red-950 text-base">【篇章四】小半天兩天一夜示範遊程實測盤查</h3>
          </div>
          
          <h4 class="font-bold text-slate-900 mt-4">4.1 示範遊程時間表</h4>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200">
              <h5 class="font-bold text-emerald-800 mb-2">Day 1：翠竹晨嵐・瀑布尋幽</h5>
              <ul class="text-xs text-slate-600 space-y-1">
                <li>09:30-11:30 長源圳生態古圳步道健行＆孟宗竹林綠色隧道漫步</li>
                <li>12:00-13:30 小半天在地竹筒飯風味午餐</li>
                <li>14:00-16:00 德興瀑布探幽</li>
                <li>16:30-18:00 凍頂烏龍茶席品茗體驗</li>
                <li>18:30 下榻小半天在地綠色環保民宿</li>
              </ul>
            </div>
            <div class="p-5 rounded-2xl bg-stone-50 border border-slate-200">
              <h5 class="font-bold text-emerald-800 mb-2">Day 2：竹藝傳承・茶香歸途</h5>
              <ul class="text-xs text-slate-600 space-y-1">
                <li>08:30-09:30 石馬公園晨間漫步</li>
                <li>10:00-12:00 小半天竹藝工坊手作體驗</li>
                <li>12:30-14:00 社區低碳茶餐佐野菜時令風味午餐</li>
                <li>14:30-15:30 在地小農市集</li>
                <li>16:00 搭乘台灣好行溪頭線低碳大眾接駁賦歸</li>
              </ul>
            </div>
          </div>

          <h4 class="font-bold text-slate-900 mt-4">4.2 碳盤查數據實測與對比分析</h4>
          <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-slate-200 rounded-xl overflow-hidden shadow-sm">
              <thead class="bg-slate-100 text-slate-800 font-bold">
                <tr>
                  <th class="p-3">構面</th>
                  <th class="p-3">傳統遊程 (Baseline)</th>
                  <th class="p-3">小半天低碳遊程 (Low-Carbon)</th>
                  <th class="p-3">差異</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-slate-600 bg-white">
                <tr>
                  <td class="p-3 font-bold">① 交通運輸</td>
                  <td class="p-3">自駕8.5L汽油+4瓶水 = 28.5kg</td>
                  <td class="p-3">大巴2.8L柴油 = 9.6kg</td>
                  <td class="p-3 text-emerald-600 font-bold">-66.3%</td>
                </tr>
                <tr>
                  <td class="p-3 font-bold bg-slate-50">② 餐飲美食</td>
                  <td class="p-3 bg-slate-50">牛排豬肉 = 14.2kg</td>
                  <td class="p-3 bg-slate-50">在地時令筍餐 = 3.8kg</td>
                  <td class="p-3 bg-slate-50 text-emerald-600 font-bold">-73.2%</td>
                </tr>
                <tr>
                  <td class="p-3 font-bold">③ 住宿服務</td>
                  <td class="p-3">一般山莊整晚空調 = 5.2kg</td>
                  <td class="p-3">環保民宿自然涼風 = 2.4kg</td>
                  <td class="p-3 text-emerald-600 font-bold">-53.8%</td>
                </tr>
                <tr>
                  <td class="p-3 font-bold bg-slate-50">④ 遊憩體驗</td>
                  <td class="p-3 bg-slate-50">塑膠紀念品 = 0.5kg</td>
                  <td class="p-3 bg-slate-50">竹藝DIY = 0.8kg</td>
                  <td class="p-3 bg-slate-50 text-amber-600 font-bold">+0.3kg (促進在地循環固碳)</td>
                </tr>
                <tr>
                  <td class="p-3 font-bold">⑤ 門市據點</td>
                  <td class="p-3">紙本宣傳 = 0.2kg</td>
                  <td class="p-3">數位電子手冊 = 0.2kg</td>
                  <td class="p-3 text-emerald-600 font-bold">源頭減廢100%</td>
                </tr>
                <tr class="bg-emerald-100 text-emerald-900 font-bold">
                  <td class="p-3">總計 (每人)</td>
                  <td class="p-3">48.6 kg</td>
                  <td class="p-3">16.8 kg</td>
                  <td class="p-3">-31.8 kg (-65.4%)</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="text-xs text-slate-500 mt-2">每人減碳 31.8 kg，相當於 2.6 棵成年孟宗竹年吸收量。20人團體可省下 636 kg CO₂e！</p>
        </div>

        <!-- 篇章五 -->
        <div id="tab-content-5" class="tab-content hidden space-y-5 text-sm text-slate-700 leading-relaxed">
          <div class="bg-purple-50 border-l-4 border-purple-600 p-4 rounded-r-2xl">
            <h3 class="font-black text-purple-950 text-base">【篇章五】減量效益評估、碳標籤認證與淨零路徑</h3>
          </div>
          <div class="space-y-3">
            <div class="p-4 rounded-2xl bg-stone-50 border border-slate-200 space-y-1.5">
              <h4 class="font-bold text-slate-900">5.1 旅行社取得觀光署遊程碳標籤通關指南</h4>
              <ul class="text-xs text-slate-600 space-y-2 mt-2">
                <li><strong>Step 1:</strong> 確立產品邊界</li>
                <li><strong>Step 2:</strong> 蒐集佐證單據 (加油發票、客運車票票根、民宿住宿憑證、食材產銷履歷單據)</li>
                <li><strong>Step 3:</strong> 計算與建立碳足跡報告書 (套用觀光署碳足跡計算表格，碳排熱點分析與減量成效)</li>
                <li><strong>Step 4:</strong> 第三公正方查核與登錄</li>
              </ul>
            </div>
            <div class="p-4 rounded-2xl bg-stone-50 border border-slate-200 space-y-1.5">
              <h4 class="font-bold text-slate-900">5.2 自願性碳抵換與不漂綠原則</h4>
              <p class="text-xs text-slate-600">先減量再抵換！不能以低價購買碳權直接宣稱零碳。旅客剩餘16.8 kg 可配合在地植樹護竹計畫或購買Gold Standard/VCS/環境部認證碳信用額度。</p>
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
  </section>"""

# Find the section and replace it
start_idx = content.find('  <!-- 手冊全文線上閱讀專區 (五大篇章分頁切換) -->')
end_idx = content.find('  <!-- 頁尾宣告 -->')
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_handbook + "\n\n" + content[end_idx:]

# Also update the switchTab function
old_switch = """    // 手冊章節切換邏輯
    function switchTab(idx) {
      for (let i = 1; i <= 5; i++) {"""
new_switch = """    // 手冊章節切換邏輯
    function switchTab(idx) {
      for (let i = 1; i <= 6; i++) {"""
content = content.replace(old_switch, new_switch)

with open("build_full_website.py", "w", encoding="utf-8") as f:
    f.write(content)
