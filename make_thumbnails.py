import os
import subprocess

thumb_dir = "/Users/chenchunchih/碳永續/碳導遊/videos/thumbnails"
os.makedirs(thumb_dir, exist_ok=True)
vid_dir = "/Users/chenchunchih/碳永續/碳導遊/videos"

for f in os.listdir(vid_dir):
    if f.endswith(".mp4"):
        v_path = os.path.join(vid_dir, f)
        base = os.path.splitext(f)[0]
        t_path = os.path.join(thumb_dir, f"{base}.jpg")
        if not os.path.exists(t_path):
            cmd = [
                "/opt/homebrew/bin/ffmpeg", "-y", "-ss", "00:00:03",
                "-i", v_path, "-vframes", "1", "-q:v", "2",
                "-vf", "scale=640:-1",
                t_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Generated thumbnail: {t_path}")
        else:
            print(f"Thumbnail exists: {t_path}")

print("All thumbnails ready.")
