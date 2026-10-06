"""用法: python3 tools/make_payloads.py mt1   → 讀 mt1/script.json，在 tts_mt1/ 產生每段的 TTS JSON"""
import json, os, sys
ep = sys.argv[1]
INS = ("請全程使用年輕男性的聲音。用道地的台灣國語口音說話，像一位活潑、熱情、充滿活力的台灣年輕男生老師，"
       "帶著笑意，語速輕快。只唸出文字內容。")
S = json.load(open(f"{ep}/script.json"))
os.makedirs(f"tts_{ep}", exist_ok=True)
for i, s in enumerate(S, 1):
    json.dump({"model": "google/gemini-3.8-flash-tts", "input": s, "voice": "Puck", "instructions": INS},
              open(f"tts_{ep}/{ep}_{i}.json", "w"), ensure_ascii=False)
print(len(S), "payloads ->", f"tts_{ep}/")
