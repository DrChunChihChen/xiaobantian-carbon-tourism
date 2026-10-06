import subprocess
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
URL = "file:///Users/chenchunchih/碳永續/碳導遊/index.html"

# capture with 1280x6000 so nothing is cut off
cmd = [
    CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
    "--window-size=1280,5500",
    "--screenshot=screenshots/full_tall.png",
    URL
]
subprocess.run(cmd, check=True)
im = Image.open('screenshots/full_tall.png')
print('Tall size:', im.size)
