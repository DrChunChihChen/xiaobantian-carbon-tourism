import sys, numpy as np
def f0(path, sr=24000):
    a = np.fromfile(path, dtype="<i2").astype(np.float32)
    fr = int(0.04 * sr); hop = int(0.02 * sr); out = []
    thr = np.percentile(np.abs(a), 90) * 0.3
    for i in range(0, len(a) - fr, hop):
        x = a[i:i + fr]
        if np.sqrt(np.mean(x ** 2)) < thr * 0.5: continue
        x = x - x.mean()
        c = np.correlate(x, x, 'full')[fr - 1:]
        lo, hi = sr // 400, sr // 70
        k = lo + np.argmax(c[lo:hi])
        if c[k] > 0.45 * c[0]: out.append(sr / k)
    return np.median(out) if out else 0
for p in sys.argv[1:]:
    print(p.split("/")[-1], round(f0(p)))
