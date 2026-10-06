import subprocess

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "file:///Users/chenchunchih/碳永續/碳導遊/index.html"
OUT = "/Users/chenchunchih/碳永續/碳導遊/screenshots/fig8_videos.png"

# Render HTML snippet showing the video section
with open("index.html", "r", encoding="utf-8") as f:
    h = f.read()

snippet = h.replace('class="scroll-smooth">', 'class="scroll-smooth"><style>section:not(#videos){display:none;} header{display:none;} footer{display:none;}</style>')
with open("screenshots/_tmp_vid.html", "w", encoding="utf-8") as tf:
    tf.write(snippet)

cmd = [
    CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
    "--window-size=1280,1100",
    f"--screenshot={OUT}",
    "file:///Users/chenchunchih/碳永續/碳導遊/screenshots/_tmp_vid.html"
]
subprocess.run(cmd, check=True)
print("Screenshot captured at:", OUT)
