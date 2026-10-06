#!/bin/bash
# 用法: bash tools/tts.sh mt1     （金鑰放在 ~/.openrouter_key，不要寫進程式）
EP=$1; cd "tts_$EP" || exit 1
K=$(tr -d ' \n\r' < ~/.openrouter_key)
for f in ${EP}_*.json; do n=${f%.json}
  curl -s --max-time 180 -o $n.pcm -w "$n %{http_code} %{size_download}\n" \
    https://openrouter.ai/api/v1/audio/speech \
    -H "Authorization: Bearer $K" -H 'Content-Type: application/json' --data-binary @$f
done
