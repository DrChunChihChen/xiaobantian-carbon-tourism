"""讀取已生成的圖片並轉換為 base64 字串，生成獨立無外部檔案依賴的頂級現代網頁 index.html
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

print(f"圖片轉碼完成：Cover {len(img_cover)} bytes, Atian {len(img_atian)} bytes, Xiaolu {len(img_xiaolu)} bytes")
