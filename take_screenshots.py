import subprocess
import os
import time

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "file:///Users/chenchunchih/碳永續/碳導遊/index.html"
OUT_DIR = "/Users/chenchunchih/碳永續/碳導遊/screenshots"
os.makedirs(OUT_DIR, exist_ok=True)

# We can capture screenshots with different window sizes or scroll positions
# In headless chrome, window-size controls viewport.
# Let's write small HTML wrapper files or use chrome flags.
# Even simpler: we can render specific sections by injecting small CSS or scroll, OR full page screenshot:
cmd_full = [
    CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
    "--window-size=1280,3200",
    f"--screenshot={OUT_DIR}/screenshot_fullpage.png",
    URL
]
subprocess.run(cmd_full, check=True)
print("Captured fullpage screenshot")

