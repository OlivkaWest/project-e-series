"""Сборка партитуры EP01 из треков Suno под монтаж 18,17 с.

Правки идут по монтажному листу, а не на слух: точки склеек взяты из
season-01/episode-001/EDIT_LIST.md.

Соблюдаются правила bible/SOUND_LANGUAGE.md §2:
  4. тишина 1-2 с, полная, все слои сняты — 14,70...16,30;
  7. финал обрывается монтажным cut'ом, без затухания — 18,14.
"""
import subprocess, numpy as np, wave, sys

SR = 48_000
TOTAL = 25.50
N = int(TOTAL * SR)
SRC = "incoming/AUDIO_DUMP/SUNO_%s.mp3"


def load(name):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", SRC % name, "-map", "0:a",
         "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)


def ramp(x, fin=0.0, fout=0.0):
    n = len(x)
    e = np.ones(n)
    if fin:
        k = int(fin * SR); e[:k] *= np.linspace(0, 1, k)
    if fout:
        k = int(fout * SR); e[-k:] *= np.linspace(1, 0, k)
    return x * e[:, None]


def place(dst, src, at, gain=1.0):
    i = int(at * SR)
    j = min(len(dst), i + len(src))
    dst[i:j] += src[: j - i] * gain


main, danger, final = load("MAIN"), load("DANGER"), load("FINAL")
tr = np.zeros((N, 2))

# ── 1. тело 0,00-21,55: MAIN ложится один в один ────────────────────────────
# у трека собственное нарастание: тихо до 5,0; громко 6,0-8,5 — это ровно
# склейка на коридор (5,80); откат 9-13; второй подъём 13,5-15 приходится на
# SH008, момент узнавания (13,20-15,20). Растягивать и резать не пришлось.
# Хвост трека (17,5-20,8) идёт под SH011 и SH012.
BODY_END, MUTE_IN = 21.05, 0.25
seg = main[: int((BODY_END + MUTE_IN) * SR)]
place(tr, ramp(seg, fin=0.05, fout=MUTE_IN), 0.0, 1.0)

# ── 2. DANGER подкладывается с 15,30, пик приходится на 18,80 ───────────────
# у трека нарастание 0->3,5 с пиком -11 дБ. Пик ставим на SH011 (свет по
# глазам, 17,80-19,60), а начало подъёма — на SH010, то есть на сам поворот.
D_AT = 15.30
d_len = BODY_END + MUTE_IN - D_AT
place(tr, ramp(danger[: int(d_len * SR)], fin=0.35, fout=MUTE_IN), D_AT, 0.72)

# ── 3. тишина 21,55-22,60: все слои сняты (правило 4) ───────────────────────
# две секунды, предел по правилу 4. Ложится ровно на SH013 — приём М2
# BACKGROUND HORROR, где библия отдельно запрещает музыкальный удар.
# Раз в серию тишина, раз в серию событие в глубине: пусть совпадут.
SIL_A, SIL_B = 21.30, 23.00
tr[int(SIL_A * SR):int(SIL_B * SR)] = 0.0

# ── 4. финал: у FINAL провал до -36 дБ на 16,7-17,2 и удар на 17,3 ──────────
# берём этот кусок целиком: тихий REVEAL, из которого вырывается CLIFFHANGER.
F_FROM, F_AT = 16.55, 23.00
CUT = 25.39
f_len = CUT - F_AT
place(tr, ramp(final[int(F_FROM * SR): int((F_FROM + f_len) * SR)], fin=0.08),
      F_AT, 1.0)

# ── 5. срез монтажом, без затухания хвоста (правило 7) ──────────────────────
tr[int(CUT * SR):] = 0.0

peak = np.abs(tr).max()
tr = tr / peak * 0.89 if peak > 0 else tr

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((tr * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  тишина {SIL_B-SIL_A:.2f} с  срез {CUT}")
