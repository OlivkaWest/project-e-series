"""Партитура EP01. Темп 46 BPM, мотивы из D / F / E-bemol.

Нагнетание строится четырьмя средствами, а не крещендо:
  1. пульс в субнизе на 46 BPM, который незаметно ускоряется;
  2. малая секунда D–E♭ в струнах — интервал тревоги;
  3. тремоло в верхах, входящее во второй половине;
  4. полное снятие всех слоёв перед финалом.
"""
import numpy as np, wave, sys

SR = 48_000
BPM = 46.0
BEAT = 60.0 / BPM

D1, D2, Eb2, A2 = 36.71, 73.42, 77.78, 110.00
D3, F3, Eb3 = 146.83, 174.61, 155.56
rng = np.random.default_rng(46)


def t_of(n):
    return np.arange(n) / SR


def adsr(n, a, d, s, r):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    sus = max(0, n - a - d - r)
    e = np.concatenate([np.linspace(0, 1, a, endpoint=False),
                        np.linspace(1, s, d, endpoint=False),
                        np.full(sus, s),
                        np.linspace(s, 0, r)])
    return np.pad(e, (0, max(0, n - len(e))))[:n]


def bowed(freq, dur, detune=0.0, amp=1.0, bright=6, atk=None, rel=None):
    """Смычковый голос. Второй источник, разведённый на detune Гц, даёт биение.

    atk/rel в секундах. Без них атака пропорциональна длине — для длинного
    дрона это означает, что он входит треть эпизода и первые секунды пусты.
    """
    n = int(dur * SR); t = t_of(n)
    a = dur * 0.35 if atk is None else min(atk, dur * 0.45)
    r = dur * 0.40 if rel is None else min(rel, dur * 0.45)
    vib = np.sin(2 * np.pi * 4.6 * t) * 0.004
    def one(f):
        s = np.zeros(n)
        for k in range(1, bright + 1):
            s += (1.0 / k) * np.sin(2 * np.pi * f * k * t * (1 + vib))
        return s
    sig = one(freq) + (one(freq + detune) if detune else 0.0)
    return amp * sig * adsr(n, a, dur * 0.10, 0.9, r)


def sub_pulse(at, amp=1.0, freq=D1):
    """Удар в субнизе плюс «стук» в середине.

    Телефонный динамик не воспроизводит 37 Гц. Если пульс живёт только в
    субнизе, на телефоне главного средства нагнетания просто нет. Стук на
    5-й и 8-й гармонике переносит ритм в слышимый диапазон, не делая удар
    громким: в наушниках слышен низ, на телефоне — стук.
    """
    dur = 0.9; n = int(dur * SR); t = t_of(n)
    body = np.sin(2 * np.pi * freq * t) + 0.4 * np.sin(2 * np.pi * freq * 2 * t)
    body *= np.exp(-t * 6.5)
    # стук: короткий шумовой всплеск в полосе 300–900 Гц. Синус в этом
    # регистре читался бы как писк, шум — как удар по дереву.
    nz = rng.normal(0, 1, n)
    F = np.fft.rfft(nz); fr = np.fft.rfftfreq(n, 1 / SR)
    F *= np.exp(-((np.log(np.clip(fr, 1, None) / 520.0)) ** 2) / (2 * 0.45 ** 2))
    knock = np.fft.irfft(F, n)
    knock /= np.abs(knock).max() + 1e-9
    knock *= np.exp(-t * 34.0) * 0.16
    knock += 0.10 * np.sin(2 * np.pi * freq * 12 * t) * np.exp(-t * 40.0)
    return amp * (body + knock), at


def prepared(freq, dur, amp=1.0):
    """Препарированное пианино: негармоничные обертоны, металлический призвук."""
    n = int(dur * SR); t = t_of(n)
    s = np.zeros(n)
    for k, g in enumerate([1.0, .45, .30, .18, .11, .07], start=1):
        s += g * np.sin(2 * np.pi * freq * k * (1 + 0.0013 * k * k) * t)
    s += 0.25 * rng.normal(0, 1, n) * np.exp(-t * 110)
    return amp * s * adsr(n, 0.003, 0.5, 0.25, dur * 0.5)


def tremolo(freq, dur, rate=11.0, amp=1.0):
    """Тремоло в верхнем регистре — классический носитель тревоги."""
    n = int(dur * SR); t = t_of(n)
    s = (np.sin(2 * np.pi * freq * t) + 0.6 * np.sin(2 * np.pi * freq * 1.5 * t)
         + 0.3 * np.sin(2 * np.pi * freq * 2.02 * t))
    trem = 0.55 + 0.45 * np.sin(2 * np.pi * rate * t)
    return amp * s * trem * adsr(n, dur * 0.3, dur * 0.2, 0.85, dur * 0.35)


def riser(dur, f0=90, f1=520, amp=1.0):
    """Восходящая линия под финал. Не «сейчас испугают», а натяжение."""
    n = int(dur * SR); t = t_of(n)
    f = f0 * (f1 / f0) ** (t / dur)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + 0.5 * np.sin(ph * 2.01)
    noise = rng.normal(0, 1, n) * np.linspace(0, 1, n) ** 3 * 0.35
    return amp * (s * np.linspace(0.05, 1, n) ** 2 + noise)


def impact(dur=2.2, amp=1.0):
    """Низкий удар с длинным хвостом."""
    n = int(dur * SR); t = t_of(n)
    s = (np.sin(2 * np.pi * 41 * t) + 0.6 * np.sin(2 * np.pi * 27 * t)
         + 0.3 * np.sin(2 * np.pi * 62 * t))
    s += rng.normal(0, 1, n) * np.exp(-t * 30) * 0.5
    return amp * s * np.exp(-t * 2.4)


def reverb(x, decay=2.0, mix=0.34, seed=3):
    """Объём: свёртка с затухающим шумовым откликом."""
    g = np.random.default_rng(seed)
    L = int(decay * SR)
    ir = g.normal(0, 1, L) * np.exp(-np.arange(L) / SR * (5.0 / decay))
    ir[: int(0.012 * SR)] = 0
    ir /= np.abs(ir).sum() / 40
    wet = np.convolve(x, ir)[: len(x)]
    return (1 - mix) * x + mix * wet


TOTAL = 18.20
N = int(TOTAL * SR)


def place(tr, sig, at):
    i = int(at * SR)
    if i >= len(tr): return
    j = min(len(tr), i + len(sig))
    tr[i:j] += sig[: j - i]


low  = np.zeros(N)   # субниз и удары
mid  = np.zeros(N)   # струны, пианино
high = np.zeros(N)   # тремоло, райзер

# ── 1. дрон: малая секунда D2–E♭2, растёт от порога к DANGER ────────────────
place(mid, bowed(D2, 15.2, detune=0.0, amp=0.55, atk=0.6, rel=1.4), 0.0)
place(mid, bowed(Eb2, 9.0, detune=0.0, amp=0.30, atk=1.2, rel=1.5), 5.2)
# та же секунда октавой выше и тише: в субнизе биение D–E♭ на телефоне не слышно
place(mid, bowed(D3, 15.2, amp=0.14, bright=4, atk=0.8, rel=1.4), 0.0)
place(mid, bowed(Eb3, 9.0, amp=0.10, bright=4, atk=1.2, rel=1.5), 5.2)
env_mid = np.interp(t_of(N), [0, 1.0, 5.2, 9.0, 12.8, 14.55, 14.75, 18.2],
                             [0.42, 0.50, 0.62, 0.82, 1.00, 1.00, 0.05, 0.05])
mid *= env_mid

# ── 2. пульс: 46 BPM, к финалу чуть чаще и громче ───────────────────────────
tm, step, k = 1.2, BEAT, 0
while tm < 14.5:
    amp = 0.35 + 0.55 * min(1.0, (tm - 1.2) / 12.0)
    s, at = sub_pulse(tm, amp=amp)
    place(low, s, at)
    step = BEAT * (1.0 - 0.16 * min(1.0, (tm - 1.2) / 12.0))   # незаметное ускорение
    tm += step; k += 1

# ── 3. MAIN  D → F → E♭  под коридором ──────────────────────────────────────
for f, at in zip([D3, F3, Eb3], [5.60, 5.60 + BEAT, 5.60 + 2 * BEAT]):
    place(mid, prepared(f, 2.8, amp=0.42), at)
place(mid, prepared(D3 / 2, 3.4, amp=0.26), 8.25)

# ── 4. ANOMALY  E♭ → F → D  под брелоком, октавой выше ──────────────────────
for f, at in zip([Eb3, F3, D3], [9.85, 9.85 + BEAT * .7, 9.85 + BEAT * 1.4]):
    place(mid, prepared(f * 2, 2.0, amp=0.24), at)

# ── 5. тремоло: входит с брелока, пик в DANGER ──────────────────────────────
place(high, tremolo(A2 * 4, 5.2, rate=9.5,  amp=0.10), 9.6)
place(high, tremolo(D3 * 4, 2.6, rate=13.0, amp=0.16), 12.5)

# ── 6. DANGER: удерживаемая D, второй голос расстроен на 4 Гц ───────────────
place(mid, bowed(D2, 2.4, detune=4.0, amp=0.75), 12.75)
place(low, impact(2.0, amp=0.55), 12.80)

# ── 7. провал 14,7–15,8: все слои сняты, остаётся тонкая нить в верхах ──────
place(high, tremolo(D3 * 6, 1.4, rate=7.0, amp=0.035), 14.9)

# ── 8. райзер и REVEAL ──────────────────────────────────────────────────────
place(high, riser(2.0, 90, 620, amp=0.16), 15.7)
for f, at in zip([D3 * 4, F3 * 4], [16.45, 16.45 + BEAT]):
    place(mid, prepared(f, 1.7, amp=0.20), at)

# ── 9. CLIFFHANGER: удар, срезанный монтажом ────────────────────────────────
place(low, impact(2.4, amp=1.0), 17.45)
place(mid, bowed(D1 * 2, 1.0, detune=1.5, amp=0.9), 17.45)

for tr in (low, mid, high):
    tr[int(18.14 * SR):] = 0                 # срез, не затухание

lowv  = low * 0.85
midv  = reverb(mid,  decay=2.4, mix=0.36, seed=3) * 0.75
highv = reverb(high, decay=3.0, mix=0.45, seed=9) * 0.70

mono = lowv + midv + highv
mono /= np.abs(mono).max()
mono = np.tanh(mono * 1.25) * 0.80            # мягкое ограничение

L = lowv + midv + np.roll(highv, -140)
R = lowv + np.roll(midv, 90) + highv
st = np.stack([L, R], axis=1)
st = st / np.abs(st).max() * 0.85
st = np.tanh(st * 1.2) * 0.82

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  ударов пульса: {k}")
