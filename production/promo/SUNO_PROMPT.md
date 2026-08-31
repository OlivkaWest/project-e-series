# Suno — партитура EP01

Мотивы и палитра — `bible/SOUND_LANGUAGE.md` §3. Чужие сериалы и фильмы в промптах
не называются (правило из `CLAUDE.md`): звук задаётся инструментами, приёмами и
продакшеном. Ниже описаны ровно те механики, которые дают нужное ощущение.

Режим: **Instrumental** (переключатель обязательно включён). Модель — последняя доступная.

---

## 1. Основной промпт · весь эпизод

**Style of Music:**

```
Instrumental horror film score. 46 BPM, D minor, never resolves.
Prepared piano with felt between the strings: dull, percussive, inharmonic, short decay.
Celesta and a slightly detuned music box in the top octave, out of tune with itself.
Solo cello holding one long note while a second voice sits a semitone above it, beating slowly.
Bowed metal, scraped cymbal, struck brass, dry industrial metallic percussion.
Sub-bass pulse like a slow heartbeat that imperceptibly speeds up.
Heavy analog tape wow and flutter, tape saturation, hiss, reverse swells before each event.
Sparse, dry, close, claustrophobic. Long silences. Dread that grows by density, not by volume.
```

**Exclude Styles:**

```
vocals, choir, drums, drum kit, percussion groove, beat, EDM, synthwave, trailer braams,
orchestral crescendo, epic, jump scare sting, uplifting, resolution, major key, lofi
```

---

## 2. Промпт под DANGER · 12,8–14,7 с

Если основной трек не даёт нужного напряжения в кульминации — сгенерировать отдельно.

```
Instrumental. 46 BPM, D minor. One sustained cello note with a second voice a semitone
above, beating at four hertz. Bowed metal underneath. High tremolo strings entering.
Tape wow and flutter. Everything dry and close. No drums, no melody, no release.
```

---

## 3. Промпт под финал · 16,3–18,1 с

```
Instrumental. Very sparse. A detuned music box plays three descending notes, twice as slow,
almost inaudible, through analog tape. Then total silence. Then one low cello string struck
once and cut off. No reverb tail. No drums.
```

---

## 4. Что прислать

Скачать из Suno в максимальном качестве (WAV, если доступен; иначе MP3 320).
Можно прислать 2–3 варианта — выберу по тому, как ложится на монтаж.

**Класть в `incoming/AUDIO_DUMP/`** либо просто прикрепить в чат.

## 5. Что сделаю дальше

1. Найду в треке участок, который ложится на кривую монтажа: тихое начало,
   нарастание, провал, финал.
2. Порежу под 18,17 с и посажу события на реальные склейки
   (1,63 · 3,50 · 5,53 · 7,57 · 9,77 · 11,63 · 12,83 · 14,70 · 16,33).
3. Обеспечу тишину 14,90–15,90 — правило 4 библии, одна секунда, все слои сняты.
4. Обрежу финал монтажным cut'ом на 18,14 без затухания хвоста — правило 7.
5. Мастеринг: −14 LUFS, истинный пик ≤ −1 dBTP, 48 кГц.

## 6. Чего в промптах намеренно нет

| Не пишем | Почему |
|---|---|
| названия сериалов, фильмов, режиссёров | правило из `CLAUDE.md`, своя IP |
| «scary», «creepy», «horror vibes» | модель отвечает штампами: орган, вой, скример |
| «epic», «cinematic build» | даёт крещендо к громкому удару — у нас нагнетание плотностью |
| «ambient» | даёт подушку без событий, а нам нужны удары и провалы |
