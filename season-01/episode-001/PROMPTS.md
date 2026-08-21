# EP01 · «Сорок шестая» · PROMPTS

Все промпты наследуют `bible/VISUAL_LANGUAGE.md`.
Блок `IDENTITY LOCK` — черновой, финализируется на CHECKPOINT 5 и после этого не меняется.

---

## 0. Общие блоки эпизода

### STYLE BLOCK (вставляется в каждый промпт изображения)

```text
STYLE: cinematic stylized realism, 2.5D, night, worn Soviet-era concrete apartment block interior
PALETTE: #0E1621 cold blue, #1C2B3A graphite, #E3A857 amber accent, #C8332B signal red, #F2EDE4 paper white
GRAIN: fine film grain 6%, gentle halation on light sources, no vignette
FRAMING: vertical 9:16, subject in lower third, 12% top and 20% bottom safe area
NEGATIVE: text, watermark, logo, subtitles, extra fingers, deformed hands, distorted face,
          monster, gore, lens flare, chromatic aberration, VHS effect, drone shot, fisheye,
          modern luxury interior, american apartment, daylight in corridor
```

### IDENTITY LOCK — Кирилл Радченко (черновик до CP5)

```text
29 year old man, eastern european, short dark brown hair, three-day stubble,
narrow grey-green eyes, straight nose, thin scar through the right eyebrow,
lean athletic build 182cm, tired but calm expression,
WARDROBE: dark navy utility work jacket with small embroidered patch on left chest,
grey t-shirt, dark jeans, worn work boots, keyring on right hip
NEVER CHANGE: face shape, eye colour, scar on right eyebrow, hair length, jacket
```

---

## 1. Master frames — Nano Banana

> Порядок: сначала sh01, sh06, sh09, sh12 (холодный тест) → приёмка → остальные девять.

### sh01 — панель лифта
```text
SUBJECT:     elevator control panel, buttons 1 to 9, worn brushed metal, fingerprint smudges
ACTION:      a tenth button is pushing through the blank metal below the "9", glowing red "46"
LOCATION:    interior of a small residential elevator cabin at night
CAMERA:      static, perfectly perpendicular to the panel
LENS:        85mm macro
LIGHTING:    cold overhead cabin light, plus self-emitting red glow #C8332B from the new button
COMPOSITION: panel centred, the "46" button in the lower third, empty metal above
MATERIALS:   scratched aluminium, chipped paint, dust in the button gaps
ATMOSPHERE:  ordinary, almost boring — the anomaly is the only strange thing in frame
IDENTITY LOCK: —
CONTINUITY:  exactly nine original buttons; 46 appears BELOW the nine, never beside it
NEGATIVE:    <общий негатив>
Seed: TBD · Файл: assets/ep001-sh01.png
```

### sh02 — Кирилл в кабине
```text
SUBJECT:     <IDENTITY LOCK Кирилл>
ACTION:      standing in the elevator, turning his head down-left toward the panel, checking not fearing
LOCATION:    small elevator cabin, scratched mirror on the side wall
CAMERA:      static, eye level
LENS:        50mm
LIGHTING:    cold overhead only, face underlit from below, mirror reflection slightly dimmer
COMPOSITION: man in the right third, mirror with his reflection in the left third
MATERIALS:   scratched mirror, graffiti scratches, metal wall panels
ATMOSPHERE:  end of a night shift, routine
CONTINUITY:  work jacket with patch, keyring on right hip, scar on right eyebrow
Seed: TBD · Файл: assets/ep001-sh02.png
```

### sh03 — палец у кнопки
```text
SUBJECT:     a man's hand, index finger two centimetres from the glowing 46 button
ACTION:      the button is fading out on its own, floor indicator reads 9
LOCATION:    elevator panel
CAMERA:      static frame prepared for a slow push-in
LENS:        85mm
LIGHTING:    dying red glow, cold overhead taking over
COMPOSITION: finger entering from the left, button on the right, air between them
CONTINUITY:  the finger NEVER touches the button
Seed: TBD · Файл: assets/ep001-sh03.png
```

### sh04 — коридор
```text
SUBJECT:     empty ninth-floor corridor of a panel apartment building, impossibly long
ACTION:      one fluorescent tube flickering mid-corridor; a warm amber sliver of light under a white door at the far end
LOCATION:    residential corridor, five apartment doors on the left, numbers 41 to 45
CAMERA:      static, from inside the open elevator, eye level
LENS:        35mm
LIGHTING:    single flickering tube, cold; amber #E3A857 light leaking under the far door
COMPOSITION: one-point perspective, white door dead centre, headroom above for subtitles
MATERIALS:   painted concrete, chipped skirting, leatherette-covered doors
ATMOSPHERE:  the corridor is longer than the building could possibly be
CONTINUITY:  exactly five doors plus the 46th; corridor length constant across all episodes
Seed: TBD · Файл: assets/ep001-sh04.png
```

### sh05 — проход
```text
SUBJECT:     <IDENTITY LOCK Кирилл>, seen from behind
ACTION:      walking steadily toward the far white door, glancing up at the flickering tube
LOCATION:    the same corridor
CAMERA:      static frame prepared for a slow pull-out
LENS:        35mm
LIGHTING:    rim light from the amber door sliver, cold tube overhead
COMPOSITION: figure centred, door ahead, empty corridor behind him
Seed: TBD · Файл: assets/ep001-sh05.png
```

### sh06 — брелок на ручке
```text
SUBJECT:     a small worn plastic fish keychain hanging on a door handle
ACTION:      the keychain sways gently although there is no draught
LOCATION:    white apartment door, number "46" in fresh paint
CAMERA:      static
LENS:        85mm macro
LIGHTING:    warm from below, cold rim from above
COMPOSITION: handle and keychain in the lower third, the number 46 in the upper third
MATERIALS:   cheap plastic rubbed white with age, small red split ring, leatherette door
ATMOSPHERE:  an ordinary family object in a place it cannot be
CONTINUITY:  ONE unique keychain for the whole series — same shape, wear and red ring every time
Seed: TBD · Файл: assets/ep001-sh06.png
```

### sh07 — лицо, узнавание
```text
SUBJECT:     <IDENTITY LOCK Кирилл>
ACTION:      recognising the object, one breath catching, saying nothing
LOCATION:    dark corridor, door blurred behind him
CAMERA:      static
LENS:        85mm, shallow depth of field
LIGHTING:    warm underlight from the door gap, key light off-frame
COMPOSITION: face in the lower third, gaze angled down-forward
ATMOSPHERE:  a man who has just been proven right and is not relieved by it
Seed: TBD · Файл: assets/ep001-sh07.png
```

### sh08 — снятие брелока
```text
SUBJECT:     a man's hand taking the fish keychain off the door handle
ACTION:      the split ring catches, he pulls, the sharp edge scratches his palm
LOCATION:    door handle, close
CAMERA:      static
LENS:        85mm macro
LIGHTING:    hard warm key, sharp finger shadows
COMPOSITION: hand diagonal across frame, handle in the right third
CONTINUITY:  the scratch is on the LEFT palm and stays visible through EP03
Seed: TBD · Файл: assets/ep001-sh08.png
```

### sh09 — ЦЕНА (ключевой кадр)
```text
SUBJECT:     <IDENTITY LOCK Кирилл> in the near foreground, side-on, not turning around;
             in the background the door of apartment 44 with a small brass nameplate
ACTION:      the intercom panel beside the white door lights up by itself;
             deep in frame the letters on the brass nameplate are going out one by one
LOCATION:    ninth-floor corridor
CAMERA:      static — the camera does not help the viewer notice
LENS:        35mm, stopped down so BOTH planes stay readable
LIGHTING:    green intercom glow on his cheek in front, only the corridor tube in the depth
COMPOSITION: man in the right third foreground, door 44 in the left third of the depth
CONTINUITY:  nameplate reads "СУХОВЫ" at the start of the shot and is blank brass at the end;
             blank in every corridor shot from EP02 onward
NOTE:        собирается из двух генераций (буквы есть / букв нет) + маска перехода
Seed: TBD · Файл: assets/ep001-sh09-a.png (с буквами), assets/ep001-sh09-b.png (без)
```

### sh10 — свет на лице
```text
SUBJECT:     <IDENTITY LOCK Кирилл>
ACTION:      half a step forward, a horizontal band of warm light sliding across his eyes
LOCATION:    in front of the door, door itself off-frame
CAMERA:      static
LENS:        85mm
LIGHTING:    growing amber band from the widening door gap
COMPOSITION: face centred, light band horizontal across the eyes
Seed: TBD · Файл: assets/ep001-sh10.png
```

### sh11 — щель (POV)
```text
SUBJECT:     a two-centimetre gap of warm morning light between door and frame
ACTION:      the edge of a kitchen table and morning light are just readable inside
LOCATION:    threshold of apartment 46
CAMERA:      POV, breathing very slightly
LENS:        50mm
LIGHTING:    amber #E3A857, blown-out edge
COMPOSITION: vertical strip of light centred in the frame
CONTINUITY:  it is ALWAYS morning inside 46, whatever the time outside
Seed: TBD · Файл: assets/ep001-sh11.png
```

### sh12 — экран телефона
```text
SUBJECT:     a phone screen held in a man's hand, baby-monitor app
ACTION:      a child's bed, duvet thrown back, the bed empty, night light on
LOCATION:    dark corridor
CAMERA:      static
LENS:        85mm macro
LIGHTING:    the screen is the only light source, cold on the fingers
COMPOSITION: screen fills 70% of frame, app label at the top of the screen
CONTINUITY:  identical app interface in every episode
NOTE:        надпись "ДЕТСКАЯ · 00:46" рисуется в композе, а не генерацией
Seed: TBD · Файл: assets/ep001-sh12.png
```

### sh13 — рука на ручке
```text
SUBJECT:     a man's hand closing on the door handle, knuckles whitening
ACTION:      grip tightening
LOCATION:    door 46
CAMERA:      static
LENS:        85mm
LIGHTING:    warm gap below, cold above
COMPOSITION: hand in the lower third, blank white door plane above it
CONTINUITY:  the palm scratch from sh08 must be visible
Seed: TBD · Файл: assets/ep001-sh13.png
```

---

## 2. Seedance — видео по шотам

Промпт описывает **последовательность движения**, а не настроение.

### sh01
```text
SHOT: ep001-sc1-sh01
MODEL: seedance
INPUT IMAGE: assets/ep001-sh01.png
DURATION: 2s
ASPECT RATIO: 9:16
SUBJECT: an elevator button panel, no people
ACTION: For the first half second nothing moves. Then the blank metal below the "9"
        begins to bulge outward very slightly, as if pressed from behind. The shape of
        a button forms. Only after the shape is complete does the number 46 light up red.
CAMERA MOTION: none, locked off
ENVIRONMENT: interior elevator cabin, night
PHYSICS: the metal deforms slowly and elastically, like thin sheet metal, not like rubber;
         no sparks, no smoke, no debris
LIGHTING: cold overhead stays constant; the red glow rises over 0.4 seconds and then holds steady
FACIAL BEHAVIOR: none
START FRAME: blank metal below the nine
END FRAME: the 46 button fully formed and glowing steadily
CONTINUITY: the nine original buttons never change shape or position
NEGATIVE CONSTRAINTS: no camera movement, no people, no text overlay, no sparks,
                      no melting metal, no flicker of the other buttons
```

### sh02
```text
SHOT: ep001-sc1-sh02
INPUT IMAGE: assets/ep001-sh02.png · DURATION: 2s
ACTION: The man stays completely still for the first half second. His eyes move down-left first.
        Only after his eyes have moved does his head begin to turn. The turn is small,
        about fifteen degrees, and stops.
CAMERA MOTION: none
PHYSICS: the reflection in the scratched mirror follows his movement two frames late
LIGHTING: constant
FACIAL BEHAVIOR: no fear; the eyebrows do not rise; the jaw stays relaxed
START FRAME: looking forward · END FRAME: looking at the panel
CONTINUITY: facial identity, stubble, scar on the right eyebrow and jacket remain completely unchanged
NEGATIVE CONSTRAINTS: no blinking loop, no head shake, no shoulder movement, no zoom
```

### sh03
```text
SHOT: ep001-sc1-sh03
INPUT IMAGE: assets/ep001-sh03.png · DURATION: 3s
ACTION: The finger stays two centimetres away and does not move closer. After one second the
        red glow of the button begins to fade evenly to nothing over 0.8 seconds. One second
        after the glow is gone, light from the opening doors enters the frame from the left.
CAMERA MOTION: very slow push-in, no more than 8 percent of frame width across the full 3 seconds
PHYSICS: the glow fades, it does not blink or stutter
START FRAME: button lit, finger near · END FRAME: button dark, door light entering
CONTINUITY: the finger never touches the panel
NEGATIVE CONSTRAINTS: no hand shake, no button press, no flicker
```

### sh04
```text
SHOT: ep001-sc2-sh04
INPUT IMAGE: assets/ep001-sh04.png · DURATION: 3s
ACTION: The corridor is empty and still. At 1.4 seconds the fluorescent tube flickers once,
        for two frames only, then returns to steady. The amber light under the far door widens
        by a few millimetres and narrows again, slowly, like breathing.
CAMERA MOTION: none
PHYSICS: the light under the door moves smoothly, the flicker of the tube is instant
START FRAME: corridor at rest · END FRAME: corridor at rest, light slightly wider
NEGATIVE CONSTRAINTS: no people, no door opening, no camera movement, no dust particles storm
```

### sh05
```text
SHOT: ep001-sc2-sh05
INPUT IMAGE: assets/ep001-sh05.png · DURATION: 3s
ACTION: The man walks away from camera at an even pace, four steps. On the second step he
        raises his eyes to the flickering tube above without stopping, then lowers them again.
        The keyring on his hip swings in time with the steps.
CAMERA MOTION: very slow pull-out, matching the walk so his size in frame stays almost constant
PHYSICS: the keyring swings with real weight and lag, the jacket fabric shifts on the shoulders
START FRAME: first step out of the lift · END FRAME: three metres from the door
CONTINUITY: same jacket, same keyring, body proportions unchanged
NEGATIVE CONSTRAINTS: no running, no turning around, no floating gait, no morphing legs
```

### sh06
```text
SHOT: ep001-sc2-sh06
INPUT IMAGE: assets/ep001-sh06.png · DURATION: 3s
ACTION: The keychain hangs still for one second, then swings twice — a small pendulum motion
        that damps down naturally. Nothing else in the frame moves.
CAMERA MOTION: none
PHYSICS: pendulum with a short period and visible damping; the door and handle stay rigid
START FRAME: keychain still · END FRAME: keychain almost still again
NEGATIVE CONSTRAINTS: no wind in the frame, no door movement, no hand entering
```

### sh07
```text
SHOT: ep001-sc3-sh07
INPUT IMAGE: assets/ep001-sh07.png · DURATION: 3s
ACTION: The face is still. At one second the chest lifts once with a caught breath and the
        nostrils widen slightly. The eyes stay open. At two seconds the gaze lowers toward
        the door handle. He does not speak.
CAMERA MOTION: none
FACIAL BEHAVIOR: micro-expression only; no crying, no grimace, no mouth opening
START FRAME: neutral · END FRAME: eyes lowered, decision made
CONTINUITY: facial identity unchanged
NEGATIVE CONSTRAINTS: no talking, no smile, no tears, no head tilt
```

### sh08
```text
SHOT: ep001-sc3-sh08
INPUT IMAGE: assets/ep001-sh08.png · DURATION: 3s
ACTION: The fingers close on the split ring and pull. The ring catches on the handle for half
        a second and resists. The hand pulls harder and the keychain comes free, the sharp edge
        dragging across the palm. A thin line appears on the skin.
CAMERA MOTION: none
PHYSICS: the ring is rigid metal and does not bend; the resistance is visible before the release;
         the skin deforms under the metal edge before the line appears
START FRAME: fingers touching the ring · END FRAME: keychain in the fist, thin scratch on the palm
NEGATIVE CONSTRAINTS: no blood spray, no extra fingers, no rubbery hand, no glow
```

### sh09
```text
SHOT: ep001-sc3-sh09
INPUT IMAGE: assets/ep001-sh09-a.png · END REFERENCE: assets/ep001-sh09-b.png · DURATION: 3s
ACTION: The man in the foreground stands still and does not turn around. The intercom panel
        beside the door lights up by itself at 0.4 seconds. Starting at 1.0 second, deep in the
        frame, the letters of the brass nameplate on door 44 go out one at a time from right to
        left, each taking about a fifth of a second. By 2.4 seconds the plate is blank brass.
        The man never reacts.
CAMERA MOTION: none
PHYSICS: the letters do not fade as light; they simply stop being engraved, the surface becoming
         smooth brass. No particles, no dissolve, no glow
LIGHTING: green intercom glow appears on the near cheek; the corridor tube behind stays constant
FACIAL BEHAVIOR: none — he is side-on and does not move
START FRAME: nameplate reads fully · END FRAME: nameplate blank
CONTINUITY: both planes stay in focus; the man's identity and jacket unchanged
NEGATIVE CONSTRAINTS: no turning around, no camera push toward the nameplate, no sparkle,
                      no dissolve effect, no text appearing anywhere else
```

### sh10
```text
SHOT: ep001-sc3-sh10
INPUT IMAGE: assets/ep001-sh10.png · DURATION: 2s
ACTION: A horizontal band of warm light appears on the lower part of his face and rises slowly
        across his eyes as the door widens off-frame. His pupils contract. He shifts weight
        forward, half a step, no more.
CAMERA MOTION: none
PHYSICS: the light band moves smoothly and evenly, matching a door opening two centimetres
START FRAME: face in shadow · END FRAME: eyes lit, pupils narrowed
NEGATIVE CONSTRAINTS: no full door opening, no strong flare, no speaking
```

### sh11
```text
SHOT: ep001-sc4-sh11
INPUT IMAGE: assets/ep001-sh11.png · DURATION: 3s
ACTION: The strip of warm light is steady. At 1.6 seconds a small shadow crosses it from left
        to right, quickly, at the height of a child. The strip returns to steady.
CAMERA MOTION: POV breathing, less than one percent of frame
PHYSICS: the shadow is soft-edged and fast, consistent with something passing a few metres inside
START FRAME: empty strip · END FRAME: empty strip again
NEGATIVE CONSTRAINTS: no face appearing, no door movement, no monster silhouette, no hand
```

### sh12
```text
SHOT: ep001-sc4-sh12
INPUT IMAGE: assets/ep001-sh12.png · DURATION: 2s
ACTION: The phone screen shows a still empty bed. At one second the camera feed refreshes:
        the image stutters for two frames, the compression blocks visibly rebuild, and the bed
        is still empty. Nothing else moves.
CAMERA MOTION: none
PHYSICS: digital refresh artefact only, no physical motion in the frame
START FRAME: screen lit, bed empty · END FRAME: refreshed, bed still empty
NEGATIVE CONSTRAINTS: no child appearing, no ghost, no glitch aesthetic, no hand movement
```

### sh13
```text
SHOT: ep001-sc4-sh13
INPUT IMAGE: assets/ep001-sh13.png · DURATION: 2s
ACTION: The hand rests on the handle. Over 1.5 seconds the fingers tighten gradually and the
        knuckles go pale. The handle does not turn.
CAMERA MOTION: none
PHYSICS: skin blanches under pressure, tendons lift on the back of the hand
START FRAME: hand resting · END FRAME: grip tight, knuckles white
CONTINUITY: the palm scratch from sh08 stays visible
NEGATIVE CONSTRAINTS: no door opening, no turning of the handle, no extra fingers
```

---

## 3. Журнал попыток

| Шот | Версия | Что менял | Результат |
|---|---|---|---|
| | | | |
