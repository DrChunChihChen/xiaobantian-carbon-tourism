#!/bin/bash
# 用法: bash tools/prep.sh mt1   → 把 tts_mt1/mt1_K.pcm 加速 1.1 倍，存成 mt1/cK.pcm（引擎讀這個）
EP=$1; mkdir -p $EP
for f in tts_$EP/${EP}_*.pcm; do b=${f##*/}; i=${b%.pcm}; i=${i#${EP}_}
  ffmpeg -y -v error -f s16le -ar 24000 -ac 1 -i "$f" -af atempo=1.1 -f s16le -ar 24000 -ac 1 $EP/c$i.pcm
done; ls $EP/*.pcm | wc -l
