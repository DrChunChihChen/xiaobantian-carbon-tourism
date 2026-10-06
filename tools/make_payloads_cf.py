"""碳導遊系列：小綠(女聲 Leda)、阿德老闆(男聲 Orus)。用法: python3 tools/make_payloads_cf.py cf1"""
import json, os, sys
ep = sys.argv[1]
GREEN = ("請全程使用年輕女性的聲音。用道地的台灣國語口音說話，像一位活潑、熱情、充滿活力的台灣年輕女生導遊，"
         "帶著笑意，語速輕快。數字請用中文自然唸出。只唸出文字內容。")
BOSS = ("請全程使用中年男性的聲音。用道地的台灣國語口音說話，像一位親切、有點困惑、愛發問的台灣旅行社老闆，"
        "語氣自然。只唸出文字內容。")
BOSS_SEG = set(json.load(open(f"{ep}/boss.json"))) if os.path.exists(f"{ep}/boss.json") else {3, 12}
S = json.load(open(f"{ep}/script.json"))
os.makedirs(f"tts_{ep}", exist_ok=True)
for i, s in enumerate(S, 1):
    boss = i in BOSS_SEG
    json.dump({"model": "google/gemini-3.8-flash-tts", "input": s, "voice": "Charon" if boss else "Leda",
               "instructions": BOSS if boss else GREEN},
              open(f"tts_{ep}/{ep}_{i}.json", "w"), ensure_ascii=False)
print(len(S), "payloads ->", f"tts_{ep}/")
