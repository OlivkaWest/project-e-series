"""Партитура EP01 v10 под монтаж 47,04 с.

Хребет — SUNO_HEARTBEAT, он идёт сквозь всю вторую половину и не прерывается.
На нём держится тринадцатый шот: десять секунд одного плана без склейки
вертикаль сама не держит, держит звук.

Устройство:
  MAIN     ставится так, что его громкая часть попадает на склейку коридора,
           а финальный подъём — на волос и узнавание;
  DANGER   нарастает под табличкой и бьёт пиком на свет по глазам;
  провал   на входе в телефон, затем десять секунд ползущего роста;
  FINAL    берётся куском, где у трека свой провал и удар подряд.
"""
import subprocess, numpy as np, wave, sys

SR = 48_000
TOTAL = 47.10
N = int(TOTAL * SR)
CUT = 46.98
SRC = "incoming/AUDIO_DUMP/SUNO_%s.mp3"


def load(name):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", SRC % name, "-map", "0:a",
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

# ── MAIN со сдвигом 3,40 ────────────────────────────────────────────────────
# громкая часть трека 6,0-8,5 попадает на 9,40-11,90 — это SH004, коридор.
# подъём 13,5-15 попадает на шаги и брелок, финальный подъём 18,5-20,8 —
# на волос и узнавание.
place(tr, ramp(main, fin=0.05, fout=1.2), 2.20, 1.0)

# ── DANGER: нарастает под табличкой, пик на свет по глазам ──────────────────
place(tr, ramp(danger[: int(7.0 * SR)], fin=0.5, fout=1.0), 28.70, 0.80)

# ── всё, кроме пульса, снимается на входе в телефон ─────────────────────────
tr[int(33.80 * SR):] = 0.0

# ── пульс: сквозная подложка, она же несёт длинный тринадцатый шот ──────────
H_FROM, H_AT = 20.0, 0.00
seg = heart[int(H_FROM * SR): int((H_FROM + CUT - H_AT) * SR)].copy()
t = np.arange(len(seg)) / SR + H_AT
# пульс идёт с первого кадра: три секунды цифровой тишины на входе — это
# провал хука, а не приём. На 24-25 он подхватывает место, где кончается MAIN.
env = np.interp(t,
    [0.00, 3.00, 9.00, 18.00, 22.00, 24.00, 28.00, 32.00, 33.65,
     33.95, 35.20, 37.00, 39.50, 41.80, 43.60, CUT],
    [0.17, 0.19, 0.20, 0.22,  0.28,  0.36,  0.32,  0.34,  0.36,
     0.03,  0.06,  0.22,  0.46,  0.70,  0.82,  0.82])
place(tr, seg * env[:, None], H_AT, 1.0)

# ── финал: у трека на 16,55-18,40 свой провал и удар подряд ─────────────────
F_FROM, F_AT = 16.55, 43.84
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
