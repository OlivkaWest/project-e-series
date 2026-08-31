"""Партитура EP01 v9 под монтаж 38,24 с.

Строится под один факт: тринадцатый шот идёт десять секунд без склейки.
Десять секунд одного плана вертикаль не держит сама — держать должен звук.
Поэтому под ним не тишина и не ровная подложка, а провал на входе и
восьмисекундное ползущее нарастание к моменту, когда фигура выходит.
"""
import subprocess, numpy as np, wave, sys

SR = 48_000
TOTAL = 38.30
N = int(TOTAL * SR)
SRC = "incoming/AUDIO_DUMP/SUNO_%s.mp3"


def load(name):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", SRC % name, "-map", "0:a",
         "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)


def ramp(x, fin=0.0, fout=0.0):
    e = np.ones(len(x))
    if fin:
        k = int(fin * SR); e[:k] *= np.linspace(0, 1, k)
    if fout:
        k = int(fout * SR); e[-k:] *= np.linspace(1, 0, k)
    return x * e[:, None]


def place(dst, src, at, gain=1.0):
    i = int(at * SR)
    if i >= len(dst) or i < 0: return
    j = min(len(dst), i + len(src))
    dst[i:j] += src[: j - i] * gain


main, danger, final, heart = (load("MAIN"), load("DANGER"),
                             load("FINAL"), load("HEARTBEAT"))
tr = np.zeros((N, 2))

# ── тело 0,00-21,00: MAIN один в один ───────────────────────────────────────
# громкая часть трека 6,0-8,5 приходится на склейку коридора (6,40),
# второй подъём 13,5-15 — на SH008, момент узнавания (14,60-16,80).
place(tr, ramp(main[: int(21.0 * SR)], fin=0.05, fout=0.6), 0.0, 1.0)

# ── DANGER: пик на SH011, свет по глазам (21,40-23,40) ──────────────────────
place(tr, ramp(danger[: int(6.5 * SR)], fin=0.35, fout=1.2), 18.80, 0.78)

# ── провал на входе в тринадцатый шот ───────────────────────────────────────
# на 25,60 снимается всё, кроме пульса, и больше не возвращается: дальше
# десять секунд одного плана держит только он.
tr[int(25.60 * SR):] = 0.0

# ── пульс: подложка с 21,0, она же несёт длинный тринадцатый шот ────────────
# ровный участок трека с собственной огибающей: провал на склейке,
# затем восемь секунд ползущего нарастания к выходу фигуры.
H_FROM, H_AT = 26.0, 21.00
h_len = 38.18 - H_AT
heart_seg = heart[int(H_FROM * SR): int((H_FROM + h_len) * SR)].copy()
t_h = np.arange(len(heart_seg)) / SR + H_AT
env = np.interp(t_h,
                [21.00, 25.40, 25.62, 26.90, 28.80, 31.20, 34.00, 35.60, 38.18],
                [0.20,  0.30,  0.03,  0.06,  0.26,  0.52,  0.80,  0.86,  0.86])
place(tr, heart_seg * env[:, None], H_AT, 1.0)

# ── финал ───────────────────────────────────────────────────────────────────
F_FROM, F_AT, CUT = 16.55, 35.64, 38.18
place(tr, ramp(final[int(F_FROM * SR): int((F_FROM + CUT - F_AT) * SR)], fin=0.10),
      F_AT, 1.0)

tr[int(CUT * SR):] = 0.0
peak = np.abs(tr).max()
if peak > 0: tr = tr / peak * 0.89

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((tr * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  срез {CUT}")
