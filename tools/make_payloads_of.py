"""辦公室調查系列：調查記者/紀實解密男聲(Charon)"""
import json, os, sys
ep = sys.argv[1]
INSTR = ("請全程使用沉穩、冷靜、富有調查報導與紀實質感的男聲。用道地的台灣國語口音說話，"
         "咬字清晰，語速適中，句式分明，像一位專業的調查記者在揭開案發現場的真相。數字請用中文自然唸出。只唸出文字內容。")
S = json.load(open(f"{ep}/script.json"))
os.makedirs(f"tts_{ep}", exist_ok=True)
for i, s in enumerate(S, 1):
    json.dump({"model": "google/gemini-3.8-flash-tts", "input": s, "voice": "Charon",
               "instructions": INSTR},
              open(f"tts_{ep}/{ep}_{i}.json", "w"), ensure_ascii=False)
print(len(S), "payloads ->", f"tts_{ep}/")
