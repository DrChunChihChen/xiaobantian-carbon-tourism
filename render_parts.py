"""分段輸出：python3 render_parts.py cf1 START_SEC END_SEC  /  python3 chunk.py cf1 mux OUT.mp4"""
import sys, runpy, subprocess, os
ARGV = list(sys.argv); mod, a = ARGV[1], ARGV[2]
import engine
captured = {}
def fake_run(self, out, argv): captured['ep'] = self; captured['out'] = out
engine.Episode.run = fake_run
sys.argv = [mod + ".py"]
runpy.run_path(mod + ".py", run_name="__main__")
ep = captured['ep']; d = ep.d; FPS, W, H = engine.FPS, engine.W, engine.H
if a == "mux":
    out = captured['out']
    engine.make_music(ep.audio, ep.TOTAL, f"{d}/mix.wav", seed=len(out))
    parts = [f"part_{int(s * FPS):06d}.mp4" for s in (0, 45, 90)]
    open(f"{d}/parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", f"{d}/parts.txt", "-i", f"{d}/mix.wav",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", out], check=True)
    print("done", out, ep.TOTAL)
else:
    s0, s1 = float(a), min(float(ARGV[3]), ep.TOTAL)
    f0, f1 = int(s0 * FPS), int(s1 * FPS)
    nf = int(ep.TOTAL * FPS); f1 = min(f1, nf)
    ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "veryfast", f"{d}/part_{f0:06d}.mp4"], stdin=subprocess.PIPE)
    import cairo
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H); ctx = cairo.Context(surf)
    for i in range(f0, f1):
        ctx.save(); ep.render(i / FPS, ctx); ctx.restore(); surf.flush(); ff.stdin.write(bytes(surf.get_data()))
    ff.stdin.close(); ff.wait(); print("chunk", f0, f1, "of", nf)
