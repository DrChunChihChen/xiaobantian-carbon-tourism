import re
import os
import subprocess
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE_HTML = "/Users/chenchunchih/碳永續/碳導遊/index.html"
OUT_DIR = "/Users/chenchunchih/碳永續/碳導遊/screenshots"
os.makedirs(OUT_DIR, exist_ok=True)

with open(BASE_HTML, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's create screenshots for:
# 1. Main View / Hero (0 to 880)
# 2. Characters section (880 to 1680)
# 3. Itinerary section (1680 to 2800)
# 4. Calculator section (2800 to 4200)

im_tall = Image.open('screenshots/full_tall.png')
W, H = im_tall.size

# Let's inspect where sections lie by finding pixel colors or slicing
# Let's generate targeted screenshots by setting window sizes and scrolling, OR by injecting HTML wrappers:

def render_html_snippet(name, custom_html, width=1280, height=900):
    tmp_path = f"{OUT_DIR}/_tmp_{name}.html"
    with open(tmp_path, 'w', encoding='utf-8') as tf:
        tf.write(custom_html)
    out_png = f"{OUT_DIR}/{name}.png"
    cmd = [
        CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={out_png}",
        f"file://{tmp_path}"
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_path):
        os.remove(tmp_path)
    print(f"Rendered {out_png}")

# 1. Hero section
render_html_snippet("fig1_hero", html.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#about){display:none;} footer{display:none;}</style>'), height=780)

# 2. Characters section
render_html_snippet("fig2_characters", html.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#characters){display:none;} header{display:none;} footer{display:none;}</style>'), height=820)

# 3. Itinerary section
render_html_snippet("fig3_itinerary", html.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#itinerary){display:none;} header{display:none;} footer{display:none;}</style>'), height=1050)

# 4. Calculator section
render_html_snippet("fig4_calculator", html.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#calculator){display:none;} header{display:none;} footer{display:none;}</style>'), height=1400)

# 5. Handbook Reader - Tab 3 (碳盤查方法學與計算教學)
html_tab3 = html.replace('id="tab-content-1" class="tab-content', 'id="tab-content-1" class="tab-content hidden')
html_tab3 = html_tab3.replace('id="tab-content-3" class="tab-content hidden', 'id="tab-content-3" class="tab-content')
html_tab3 = html_tab3.replace('id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"', 'id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"')
html_tab3 = html_tab3.replace('id="tab-btn-3" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"', 'id="tab-btn-3" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"')
render_html_snippet("fig5_handbook_calc", html_tab3.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#handbook-reader){display:none;} header{display:none;} footer{display:none;}</style>'), height=1350)

# 6. Handbook Reader - Tab 4 (示範遊程實測盤查比對表)
html_tab4 = html.replace('id="tab-content-1" class="tab-content', 'id="tab-content-1" class="tab-content hidden')
html_tab4 = html_tab4.replace('id="tab-content-4" class="tab-content hidden', 'id="tab-content-4" class="tab-content')
html_tab4 = html_tab4.replace('id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"', 'id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"')
html_tab4 = html_tab4.replace('id="tab-btn-4" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"', 'id="tab-btn-4" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"')
render_html_snippet("fig6_handbook_data", html_tab4.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#handbook-reader){display:none;} header{display:none;} footer{display:none;}</style>'), height=1200)

# 7. Handbook Reader - Tab 6 (附錄自主低碳檢核表與公約)
html_tab6 = html.replace('id="tab-content-1" class="tab-content', 'id="tab-content-1" class="tab-content hidden')
html_tab6 = html_tab6.replace('id="tab-content-6" class="tab-content hidden', 'id="tab-content-6" class="tab-content')
html_tab6 = html_tab6.replace('id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"', 'id="tab-btn-1" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"')
html_tab6 = html_tab6.replace('id="tab-btn-6" class="tab-btn px-4 py-2.5 rounded-xl transition bg-slate-100 hover:bg-slate-200 text-slate-700 shrink-0"', 'id="tab-btn-6" class="tab-btn px-4 py-2.5 rounded-xl transition bg-emerald-600 text-white shrink-0 shadow-sm"')
render_html_snippet("fig7_handbook_appendix", html_tab6.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#handbook-reader){display:none;} header{display:none;} footer{display:none;}</style>'), height=900)

