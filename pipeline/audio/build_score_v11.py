"""Партитура EP01 v11 под монтаж 47,04 с — только два трека.

Владелец оставил MAIN и FINAL, по 20,8 с каждый. На 47 секунд монтажа
это 41,6 с материала, поэтому каждый трек звучит дважды, но разными
кусками, и куски разнесены на полминуты.

Раскладка идёт от смысла, а не от арифметики:

  MAIN #1   ставится так, что его громкая часть 6,0-8,5 попадает на 8,2-10,7 —
            склейка на коридор;
  FINAL #1  ставится так, что его пик 8,0-9,0 попадает на 29,0-30,0 —
            табличка, поворот серии;
  провал    33,80-34,60, вход в десятисекундный шот с телефоном;
  MAIN #2   входит с 34,60 своим тихим началом: пять секунд почти ничего,
            потом его же громкая часть попадает на 40,1-43,1 — момент,
            когда фигура выходит из проёма;
  FINAL #2  берётся куском 16,55-19,70, где у трека свой провал и удар
            подряд, и ложится на последний шот.
"""
import subprocess, numpy as np, wave, sys

SR = 48_000
TOTAL, CUT = 47.10, 46.98
N = int(TOTAL * SR)
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


main, final = load("MAIN"), load("FINAL")
tr = np.zeros((N, 2))

# затакт 0,00-2,40: тихий кусок FINAL. Без него первые две секунды —
# цифровая тишина, а это провал хука, а не приём.
place(tr, ramp(final[int(6.00 * SR): int(8.40 * SR)], fin=0.30, fout=0.9), 0.0, 0.62)
place(tr, ramp(main, fin=0.05, fout=2.0), 2.20, 1.00)          # MAIN #1
place(tr, ramp(final[: int(12.8 * SR)], fin=1.5, fout=0.5), 21.00, 0.85)  # FINAL #1
tr[int(33.80 * SR):] = 0.0                                      # провал на входе

place(tr, ramp(main[: int(12.4 * SR)], fin=0.6), 34.60, 1.00)  # MAIN #2 — держит телефон
place(tr, ramp(final[int(16.55 * SR): int(19.70 * SR)], fin=0.10), 43.84, 1.00)  # FINAL #2

tr[int(CUT * SR):] = 0.0
peak = np.abs(tr).max()
if peak > 0: tr = tr / peak * 0.89

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((tr * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  срез {CUT}")
