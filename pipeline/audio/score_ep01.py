"""Музыкальная партитура EP01 по bible/SOUND_LANGUAGE.md §3 и MUSIC.md.

Темп 46 BPM. Мотивы строятся из D, F, E-bemol.
Инструменты синтезируются, а не берутся из библиотек: нужен точный контроль
над расстройкой и биением, на которых держится нагнетание.
"""
import numpy as np, wave, sys

SR = 48_000
BPM = 46.0
BEAT = 60.0 / BPM                      # 1.304 с

D3, F3, Eb3 = 146.83, 174.61, 155.56
D2 = D3 / 2


def env(n, a, d, s_lvl, r, sustain_n=None):
    """ADSR по числу отсчётов."""
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    s = max(0, n - a - d - r) if sustain_n is None else sustain_n
    out = np.concatenate([
        np.linspace(0, 1, a, endpoint=False),
        np.linspace(1, s_lvl, d, endpoint=False),
        np.full(s, s_lvl),
        np.linspace(s_lvl, 0, r),
    ])
    return np.pad(out, (0, max(0, n - len(out))))[:n]


def prepared_note(freq, dur, amp=1.0):
    """Препарированное пианино: между струнами металл, поэтому обертоны
    негармоничны, а атака содержит короткий шумовой призвук."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    sig = np.zeros(n)
    # негармонические частичные тоны: коэффициент неточности растёт с номером
    for k, gain in enumerate([1.0, 0.42, 0.26, 0.15, 0.09], start=1):
        stretch = 1 + 0.0012 * k ** 2          # инharmonicity струны с грузом
        sig += gain * np.sin(2 * np.pi * freq * k * stretch * t)
    # металлический призвук удара
    click = np.random.default_rng(int(freq)).normal(0, 1, n) * np.exp(-t * 90)
    sig += 0.20 * click
    return amp * sig * env(n, 0.004, 0.55, 0.22, dur * 0.55)


def bowed(freq, dur, detune_hz=0.0, amp=1.0):
    """Виолончельный голос. Два источника, разведённые на detune_hz,
    дают биение — на нём строится DANGER."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    def voice(f):
        s = np.zeros(n)
        for k, g in enumerate([1.0, 0.5, 0.33, 0.2, 0.12, 0.07], start=1):
            s += g / k * np.sin(2 * np.pi * f * k * t + np.sin(2 * np.pi * 4.7 * t) * 0.02)
        return s
    sig = voice(freq) + (voice(freq + detune_hz) if detune_hz else 0)
    return amp * sig * env(n, 0.35, 0.4, 0.85, min(1.2, dur * 0.3))


def drone(dur, f=46.0, amp=1.0):
    """Дрон 46 Гц — «дом внимателен». Почти неслышен, но его снятие
    ощущается как провал."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    sig = (np.sin(2 * np.pi * f * t)
           + 0.35 * np.sin(2 * np.pi * f * 2 * t + 0.4)
           + 0.12 * np.sin(2 * np.pi * f * 0.5 * t))
    breathe = 1 + 0.10 * np.sin(2 * np.pi * 0.09 * t)     # медленное дыхание
    return amp * sig * breathe


def room(dur, amp=1.0, seed=7):
    """Комнатный тон: розовый шум, срезанный сверху."""
    n = int(dur * SR)
    w = np.random.default_rng(seed).normal(0, 1, n)
    b = np.zeros(n); a = 0.0
    for i in range(n):                      # однополюсный ФНЧ ~ 700 Гц
        a += 0.09 * (w[i] - a); b[i] = a
    return amp * b / (np.abs(b).max() + 1e-9)


def place(track, sig, at):
    """Кладёт сигнал на дорожку, обрезая всё, что выходит за хронометраж."""
    i = int(at * SR)
    if i >= len(track):
        return
    j = min(len(track), i + len(sig))
    track[i:j] += sig[: j - i]


TOTAL = 18.20
N = int(TOTAL * SR)
mix = np.zeros(N)

# --- слой 1: дрон. Растёт от порога слышимости к DANGER, снимается под экраном
d = drone(TOTAL, amp=1.0)
ramp = np.interp(np.arange(N) / SR,
                 [0.0, 5.5, 12.8, 14.6, 14.7, 16.3, 18.2],
                 [0.16, 0.30, 0.85, 0.85, 0.05, 0.05, 0.55])
place(mix, d * ramp * 0.30, 0.0)

# --- слой 2: комнатный тон
place(mix, room(TOTAL) * 0.055, 0.0)

# --- m01 MAIN  D → F → E♭  под коридором и шагами
for i, (f, at) in enumerate(zip([D3, F3, Eb3], [5.60, 5.60 + BEAT, 5.60 + 2 * BEAT])):
    place(mix, prepared_note(f, 2.6, amp=0.085), at)
# отзвук мотива октавой ниже — «дом слышит»
place(mix, prepared_note(D3 / 2, 3.2, amp=0.05), 8.20)

# --- m02 ANOMALY  E♭ → F → D  под брелоком
for f, at in zip([Eb3, F3, D3], [9.85, 9.85 + BEAT * 0.75, 9.85 + BEAT * 1.5]):
    place(mix, prepared_note(f * 2, 1.9, amp=0.055), at)

# --- m03 DANGER: удерживаемая D, второй голос расстроен, биение 4 Гц
place(mix, bowed(D2, 2.6, detune_hz=4.0, amp=0.075), 12.75)
place(mix, bowed(D3, 2.2, detune_hz=4.0, amp=0.040), 12.95)

# --- пауза 14.70–16.33: под экраном сняты все слои, кроме следа дрона
# (цена показывается в том числе отсутствием звука)

# --- m05 REVEAL: MAIN на две октавы выше, вдвое медленнее — под резинкой
for f, at in zip([D3 * 4, F3 * 4], [16.40, 16.40 + BEAT]):
    place(mix, prepared_note(f, 1.8, amp=0.030), at)

# --- m06 CLIFFHANGER STING: один удар низкой струны, обрывается монтажом
sting = bowed(D2 / 2, 1.4, detune_hz=1.5, amp=0.30)
sting *= np.exp(-np.arange(len(sting)) / SR * 1.1)
place(mix, sting, 17.55)
mix[int(18.14 * SR):] = 0                 # срез, а не затухание

peak = np.abs(mix).max()
mix = mix / peak * 0.72
stereo = np.stack([mix, np.roll(mix, 32)], axis=1)      # лёгкая расстановка

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((stereo * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  пик {peak:.3f}")
