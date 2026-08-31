"""Партитура EP01 «Сорок шестая». Темп 46 BPM.

Материал задан библией, а не вкусом: `bible/SOUND_LANGUAGE.md` §3 —
препарированное пианино, одна виолончель, челеста, металлические предметы.
Слой 9 там же требует, чтобы мотив шёл **через плёнку и металл**.

Отсюда вся конструкция v3:

  * ни одного чистого синуса как инструмента — металл синтезируется модально,
    негармоничными модами с разной скоростью затухания у каждой;
  * всё проходит через ленту: детонация (wow 0,6 Гц + flutter 7 Гц),
    насыщение и потеря верха. Именно нестабильность высоты делает звук больным;
  * реверс-наплывы стоят только под «неправильной деталью» — правило 5;
  * тишина 14,90–15,90 полная, все слои сняты — правило 4;
  * одновременно звучит не более четырёх слоёв — §1. Проверяется в конце.

Никаких скримеров: правило 1. Громкость к финалу не растёт — растёт плотность,
а перед финалом всё снимается.
"""
import numpy as np, wave, sys

SR = 48_000
BPM = 46.0
BEAT = 60.0 / BPM
TOTAL = 18.20
N = int(TOTAL * SR)

# строй: D / F / E-bemol
D1, D2, Eb2, F2 = 36.71, 73.42, 77.78, 87.31
D3, Eb3, F3 = 146.83, 155.56, 174.61
D4, Eb4, F4 = 293.66, 311.13, 349.23

rng = np.random.default_rng(46)


def t_of(n):
    return np.arange(n) / SR


def env_exp(n, atk, dec):
    """Ударная огибающая: короткая атака, экспоненциальный спад."""
    t = t_of(n)
    a = np.clip(t / max(atk, 1e-5), 0, 1)
    return a * np.exp(-t / dec)


def lowpass(x, fc):
    """Однополюсный ФНЧ. Нужен для потери верха на ленте и для глухости войлока."""
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def fftconv(x, ir):
    """Свёртка через БПФ: прямая на таких длинах считалась бы минутами."""
    L = len(x) + len(ir) - 1
    M = 1 << (L - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, M) * np.fft.rfft(ir, M), M)
    return y[: len(x)]


# ─── лента ──────────────────────────────────────────────────────────────────

def tape(x, wow=0.0016, flutter=0.0007, drive=1.6, hf=7200, seed=1):
    """Плёнка: детонация высоты, насыщение, потеря верха.

    Детонация — главное средство. Ровная высота читается как синтезатор;
    плавающая на доли процента читается как больной механизм.
    """
    g = np.random.default_rng(seed)
    n = len(x); t = t_of(n)
    ph_w, ph_f = g.uniform(0, 6.28, 2)
    drift = g.normal(0, 1, n)
    drift = np.cumsum(drift) / SR
    drift = drift / (np.abs(drift).max() + 1e-9)
    warp = (wow * np.sin(2 * np.pi * 0.6 * t + ph_w)
            + flutter * np.sin(2 * np.pi * 7.3 * t + ph_f)
            + wow * 0.8 * drift)
    idx = np.clip((t + warp) * SR, 0, n - 1)
    y = np.interp(idx, np.arange(n), x)
    y = np.tanh(y * drive) / np.tanh(drive)
    return lowpass(y, hf)


def reverse_swell(sig, tail=1.6, mix=0.9, seed=5):
    """Реверс-наплыв: звук вплывает в удар, а не вылетает из него.

    По правилу 5 ставится только под «неправильной деталью» в кадре.
    """
    r = sig[::-1]
    g = np.random.default_rng(seed)
    L = int(tail * SR)
    ir = g.normal(0, 1, L) * np.exp(-np.arange(L) / SR * (4.0 / tail))
    wet = fftconv(r, ir / (np.abs(ir).sum() / 30))[::-1]
    return mix * wet


def room(x, decay=2.6, mix=0.34, seed=3, pre=0.018):
    """Объём подъезда: свёртка с затухающим шумовым откликом."""
    g = np.random.default_rng(seed)
    L = int(decay * SR)
    ir = g.normal(0, 1, L) * np.exp(-np.arange(L) / SR * (5.0 / decay))
    ir[: int(pre * SR)] = 0
    ir /= np.abs(ir).sum() / 40
    return (1 - mix) * x + mix * fftconv(x, ir)


# ─── инструменты (палитра из библии §3) ─────────────────────────────────────

BELL = np.array([1.00, 2.02, 2.41, 3.01, 3.77, 4.08, 5.13, 6.24, 7.71])
PLATE = np.array([1.00, 1.59, 2.14, 2.30, 2.65, 2.92, 3.16, 4.11, 5.06])


def metal(f0, dur, amp=1.0, ratios=PLATE, decay=1.2, seed=0, bright=1.0):
    """Металлический предмет. Модальный синтез: негармоничные моды,
    у каждой своя скорость затухания. Верхние гаснут быстрее — так звучит удар
    по металлу, в отличие от суммы синусов, которая звучит как орган."""
    g = np.random.default_rng(seed + 17)
    n = int(dur * SR); t = t_of(n)
    s = np.zeros(n)
    for k, r in enumerate(ratios):
        f = f0 * r * (1 + g.normal(0, 0.004))
        if f > SR * 0.45:
            break
        gain = bright ** k / (1 + 0.9 * k)
        s += gain * np.sin(2 * np.pi * f * t + g.uniform(0, 6.28)) \
             * np.exp(-t / (decay / (1 + 0.55 * k)))
    strike = g.normal(0, 1, n) * np.exp(-t * 260) * 0.5
    s = s / (np.abs(s).max() + 1e-9) + strike
    return amp * s


def prep_piano(freq, dur, amp=1.0, seed=0):
    """Препарированное пианино: между струнами проложен войлок.

    Войлок глушит обертоны и превращает ноту в стук с высотой. Поэтому здесь
    сильный шумовой транзиент, негармоничность и короткое затухание, а не
    длинный чистый тон."""
    g = np.random.default_rng(seed + 41)
    n = int(dur * SR); t = t_of(n)
    s = np.zeros(n)
    for k, gain in enumerate([1.0, .38, .21, .12, .06, .03], start=1):
        f = freq * k * (1 + 0.0016 * k * k)
        s += gain * np.sin(2 * np.pi * f * t) * np.exp(-t / (0.9 / (1 + 0.7 * k)))
    thud = g.normal(0, 1, n) * np.exp(-t * 90) * 0.55
    thud = lowpass(thud, 900)
    body = (s / (np.abs(s).max() + 1e-9)) * 0.8 + thud
    return amp * lowpass(body, 2600) * env_exp(n, 0.004, dur * 0.42)


def celesta(freq, dur, amp=1.0, seed=0):
    """Челеста: колокольные моды, верхняя октава, длинный чистый хвост."""
    return amp * metal(freq, dur, amp=1.0, ratios=BELL[:6],
                       decay=dur * 0.75, seed=seed, bright=0.92) \
           * env_exp(int(dur * SR), 0.002, dur * 0.5)


def cello(freq, dur, amp=1.0, detune=0.0, seed=0, press=1.0):
    """Виолончель. Пилообразный спектр, шум смычка и резонанс корпуса —
    без шума смычка получается синтезатор, а не струна."""
    g = np.random.default_rng(seed + 7)
    n = int(dur * SR); t = t_of(n)
    vib = np.sin(2 * np.pi * 4.4 * t + g.uniform(0, 6.28)) * 0.0035

    def voice(f):
        s = np.zeros(n)
        for k in range(1, 15):
            s += (1.0 / k ** 1.15) * np.sin(2 * np.pi * f * k * t * (1 + vib)
                                            + g.uniform(0, 6.28))
        return s

    s = voice(freq) + (voice(freq + detune) if detune else 0.0)
    s /= np.abs(s).max() + 1e-9
    bow = lowpass(g.normal(0, 1, n), 4200) * 0.10 * press
    s = s + bow
    a = min(0.35, dur * 0.30)
    e = np.clip(t / a, 0, 1) * np.clip((dur - t) / max(dur * 0.30, 1e-3), 0, 1)
    return amp * lowpass(s, 3400) * e


def bowed_metal(dur, amp=1.0, f0=D3, seed=0):
    """Трение металла: шум, прогнанный через банк резонаторов.
    Слой 3 библии — трос, петли, кольцо о ручку."""
    g = np.random.default_rng(seed + 91)
    n = int(dur * SR); t = t_of(n)
    src = g.normal(0, 1, n)
    out = np.zeros(n)
    for r in [1.0, 2.41, 3.77, 5.13, 7.71]:
        f = f0 * r
        if f > SR * 0.45:
            break
        out += np.sin(2 * np.pi * f * t) * lowpass(np.abs(src), 9.0)
    out /= np.abs(out).max() + 1e-9
    e = np.clip(t / (dur * 0.4), 0, 1) * np.clip((dur - t) / (dur * 0.45), 0, 1)
    return amp * out * e


# ─── дорожки по инструментам ────────────────────────────────────────────────

TR = {k: np.zeros(N) for k in
      ("drone", "pulse", "piano", "celesta", "cello", "friction")}


def place(name, sig, at):
    tr = TR[name]
    i = int(at * SR)
    if i >= len(tr) or i < 0:
        return
    j = min(len(tr), i + len(sig))
    tr[i:j] += sig[: j - i]


# 1. дрон 46 Гц — «дом внимателен». Слой 2.
#    Ровный синусовый бас читается как гул холодильника. Поэтому дрон дышит:
#    медленная амплитудная модуляция от шума и рост от 0,10 к 0,40.
n_dr = int(15.0 * SR); t_dr = t_of(n_dr)
dr = (np.sin(2 * np.pi * 46.0 * t_dr)
      + 0.5 * np.sin(2 * np.pi * 92.0 * t_dr)
      + 0.26 * np.sin(2 * np.pi * 138.0 * t_dr)
      + 0.13 * np.sin(2 * np.pi * 184.0 * t_dr))
breath = lowpass(rng.normal(0, 1, n_dr), 0.45)
breath = 1.0 + 0.34 * breath / (np.abs(breath).max() + 1e-9)
grow = np.interp(t_dr, [0, 1.6, 5.5, 9.8, 12.8, 14.5], [0.10, 0.16, 0.24, 0.32, 0.42, 0.42])
dr *= np.clip(t_dr / 0.7, 0, 1) * breath * grow
place("drone", dr, 0.0)

# 2. пульс 46 BPM — удар по металлу, не синус. Незаметно ускоряется.
tm, k = 1.2, 0
while tm < 14.4:
    prog = min(1.0, (tm - 1.2) / 12.0)
    hit = metal(D1 * 2, 0.85, amp=0.14 + 0.42 * prog,
                ratios=PLATE, decay=0.42, seed=k, bright=0.88)
    place("pulse", hit, tm)
    tm += BEAT * (1.0 - 0.16 * prog)
    k += 1

# 3. реверс-наплывы — только под «неправильной деталью» (правило 5):
#    SH002 зеркало 1,63 и SH006 брелок 9,77.
for at, f in ((1.63, D3), (9.77, Eb4)):
    seed_ = int(at * 10)
    sw = reverse_swell(metal(f, 1.5, amp=0.5, ratios=BELL, decay=0.9, seed=seed_),
                       tail=1.4, seed=seed_)
    place("friction", sw * 0.5, at - 1.15)

# 4. MAIN «дом»  D → F → E♭ — препарированное пианино, под коридором
for f, at in zip([D3, F3, Eb3], [5.60, 5.60 + BEAT, 5.60 + 2 * BEAT]):
    place("piano", prep_piano(f, 2.6, amp=0.60, seed=int(f)), at)
place("piano", prep_piano(D2, 3.0, amp=0.34, seed=9), 8.30)

# 5. трение металла под шагами и брелоком — слой 3
place("friction", bowed_metal(2.6, amp=0.12, f0=Eb3, seed=2), 7.70)
place("friction", bowed_metal(2.0, amp=0.15, f0=F3, seed=4), 9.90)

# 6. ANOMALY «ты это увидел»  E♭ → F → D — челеста, верхняя октава, под брелоком
for f, at in zip([Eb4, F4, D4], [9.95, 9.95 + BEAT * .7, 9.95 + BEAT * 1.4]):
    place("celesta", celesta(f * 2, 1.8, amp=0.42, seed=int(f)), at)

# 7. DANGER «уже поздно» — удерживаемая D, второй голос расстроен на 4 Гц.
#    Под SH011 (свет по глазам), до провала.
place("cello", cello(D2, 2.6, amp=0.62, detune=4.0, seed=3, press=1.3), 12.30)
place("cello", cello(D3, 2.2, amp=0.26, detune=4.0, seed=8, press=0.9), 12.60)

# 8. ТИШИНА 14,90–15,90 — полная, все слои сняты (правило 4).
SIL_A, SIL_B = 14.90, 15.90
for name in TR:
    TR[name][int(SIL_A * SR):int(SIL_B * SR)] = 0.0
for name in ("drone", "pulse", "piano", "cello"):
    TR[name][int(SIL_A * SR):] = 0.0

# 9. REVEAL «пересмотри» — MAIN на две октавы выше, вдвое медленнее, челеста,
#    на пороге слышимости. Под SH014, резинка на ручке.
for f, at in zip([D4 * 2, F4 * 2, Eb4 * 2],
                 [16.45, 16.45 + BEAT * 0.5, 16.45 + BEAT * 1.0]):
    place("celesta", celesta(f, 1.5, amp=0.34, seed=int(f) % 999), at)

# 10. CLIFFHANGER — один удар по низкой струне виолончели, срезан монтажом
place("cello", cello(D1 * 2, 1.6, amp=1.35, detune=1.2, seed=11, press=1.6), 17.40)

# ─── лента, объём, свод ─────────────────────────────────────────────────────

proc = {
    "drone":    lambda x: tape(x, wow=0.0009, flutter=0.0004, drive=2.2, hf=5200, seed=2),
    "pulse":    lambda x: tape(x, wow=0.0011, flutter=0.0006, drive=1.9, hf=8000, seed=3),
    "piano":    lambda x: room(tape(x, wow=0.0020, flutter=0.0009, drive=1.6, hf=6200, seed=4), 2.4, 0.34, 11),
    "celesta":  lambda x: room(tape(x, wow=0.0026, flutter=0.0013, drive=1.3, hf=9500, seed=5), 3.2, 0.46, 13),
    "cello":    lambda x: room(tape(x, wow=0.0014, flutter=0.0007, drive=1.7, hf=4800, seed=6), 2.2, 0.30, 15),
    "friction": lambda x: room(tape(x, wow=0.0018, flutter=0.0010, drive=1.4, hf=11000, seed=7), 3.0, 0.44, 17),
}
mixed = {k: proc[k](v) for k, v in TR.items()}

# драматургическая огибающая по сценам. Без неё уровень стоит полкой
# и нагнетание не читается: ровная громкость 18 секунд — это монотонность.
# Точки взяты по монтажному листу, а не на глаз.
ARC = np.interp(t_of(N),
                [0.0, 1.63, 3.50, 5.53, 7.57, 9.77, 11.63, 12.83, 14.10, 14.70,
                 14.90, 15.90, 16.33, 17.35, 18.20],
                [0.16, 0.16, 0.30, 0.42, 0.56, 0.68, 0.82, 0.90, 1.00, 1.00,
                 0.00, 0.00, 0.30, 1.00, 1.00])
for v in mixed.values():
    v *= ARC

# срез монтажом, без затухания хвоста (правило 7)
CUT = 18.14
for v in mixed.values():
    v[int(CUT * SR):] = 0.0

# проверка правила «не более четырёх слоёв одновременно»
act = np.zeros(N, dtype=np.int8)
for v in mixed.values():
    e = np.convolve(np.abs(v), np.ones(2400) / 2400, "same")
    act += (e > np.abs(v).max() * 0.02).astype(np.int8)
over = float((act > 4).sum()) / SR

# панорама: пианино и челеста разведены, низ и виолончель в центре
L = (mixed["drone"] + mixed["pulse"] + mixed["cello"]
     + 0.80 * mixed["piano"] + 1.00 * mixed["celesta"] + 0.85 * mixed["friction"])
R = (mixed["drone"] + mixed["pulse"] + mixed["cello"]
     + 1.00 * mixed["piano"] + 0.80 * mixed["celesta"] + 1.00 * mixed["friction"])
R = np.roll(R, 55)

st = np.stack([L, R], axis=1)
st /= np.abs(st).max()
st = np.tanh(st * 1.15) * 0.86

out = sys.argv[1] if len(sys.argv) > 1 else "score.wav"
with wave.open(out, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print(f"{out}  {TOTAL:.2f} с  ударов пульса: {k}  "
      f"превышение 4 слоёв: {over:.2f} с  тишина: {SIL_B - SIL_A:.2f} с")
