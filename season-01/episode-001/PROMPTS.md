# EP01 · «Сорок шестая» · PROMPTS v2

Пересобрано под визуальную систему. Каждый промпт наследует мастер-блок
`bible/VISUAL_LANGUAGE.md` §11 — ниже указаны только отличия конкретного кадра.

**Ни в одном промпте не упоминаются названия чужих сериалов или режиссёров.**
Стиль переведён в язык камеры, света, фактур и движения.

---

## 0. Базовый блок эпизода

```text
STYLE: luxury psychological horror cinematography, photorealistic, physically believable,
       editorial photography composition, clinical institutional imagery,
       late-Soviet apartment building interior, night
COLOR: desaturated institutional palette — dirty milk white #E8E2D4, cold grey #B9B4A8,
       faded beige #C9BEA6, institutional green oil paint #6E7A68, aged brass #8C7A55,
       dark wood #3A2C22, faded burgundy #6E3B3B, deep black #0B0B0C, desaturated skin
GRADE: fine film grain 6%, gentle halation on practicals only, green lift in shadows,
       blacks never crushed below #0B0B0C
FRAMING: vertical 9:16, horizon level, 12% top and 20% bottom safe area
NEGATIVE: monster, creature, gore, jump scare, glowing eyes, plastic skin, airbrushed skin,
          uncanny smooth render, digital glitch, VHS artefacts, chromatic aberration,
          lens flare, vignette, teal and orange grade, red horror lighting without a source,
          drone shot, handheld shake, dutch angle, text, watermark, logo, subtitles,
          extra fingers, deformed hands
```

### IDENTITY LOCK — Прохор Ветлугин (черновик до CP5)

```text
29 year old man, eastern european, short dark brown hair, three-day stubble,
narrow grey-green eyes, straight nose, thin scar through the right eyebrow,
lean build 182cm, tired calm face, desaturated skin with visible pores and slight asymmetry
WARDROBE: dark navy utility work jacket with a small embroidered patch on the left chest,
grey t-shirt, dark jeans, worn work boots, keyring on the right hip
NEVER CHANGE: face shape, eye colour, scar on the right eyebrow, hair length, jacket
```

---

## 1. Master frames — Nano Banana

### sh01 — панель лифта · MACRO
```text
SUBJECT:   an old residential elevator control panel, buttons 1 to 9, brass rings,
           chipped institutional green oil paint, greasy fingerprints
ACTION:    a tenth button is pushing outward through the blank metal below the "9",
           a glowing muted brick red "46"
CAMERA:    static, exactly perpendicular      LENS: 100mm macro
LIGHTING:  cold fluorescent from above with a slight green cast, plus the button's own red glow
COMPOSITION: panel centred, the 46 button in the lower third, blank metal above
MATERIALS: oxidised brass, chipped paint, dust in the button gaps
ATMOSPHERE: completely ordinary — the anomaly is the only strange thing in frame
CONTINUITY: exactly nine original buttons, 46 always BELOW the nine
Seed: TBD · Файл: assets/ep001-sh01.png
```

### sh02 — Прохор и зеркало · WRONG DETAIL
```text
SUBJECT:   <IDENTITY LOCK>, standing in a small elevator cabin beside a scratched mirror
ACTION:    eyes moving down-left, head beginning to turn
CAMERA:    static, eye level                  LENS: 50mm
LIGHTING:  one bulb behind a yellowed plastic ceiling diffuser; the right half of the face
           receives no fill light at all and falls into pure black
COMPOSITION: man in the right third, mirror in the left third, top of his head slightly cropped
MATERIALS: skin pores, stubble, faint perspiration at the temple, knitted collar,
           scratched mirror glass, green oil-painted metal wall
CONTINUITY: jacket patch, keyring on right hip, scar on right eyebrow
Seed: TBD · Файл: assets/ep001-sh02.png
```

### sh03 — палец у кнопки
```text
SUBJECT:   a man's hand, index finger two centimetres from the glowing 46 button
ACTION:    the red glow is fading on its own; floor indicator reads 9
CAMERA:    static frame prepared for a very slow push-in     LENS: 100mm
LIGHTING:  dying red glow, cold green fluorescent taking over, door light entering from the left
MATERIALS: skin of the fingertip in macro, a hangnail, brass
CONTINUITY: the finger never touches the panel
Seed: TBD · Файл: assets/ep001-sh03.png
```

### sh04 — коридор · BEAUTIFUL FRAME / ПОСТЕР
```text
SUBJECT:   an empty ninth-floor corridor of a late-Soviet panel apartment building,
           impossibly long, in strict one-point perspective
ACTION:    a single fluorescent tube mid-corridor; a narrow milk-white sliver of light
           under a white door at the far end
LOCATION:  five leatherette-covered doors on the left, numbers 41 to 45
CAMERA:    static, from inside the open elevator, eye level     LENS: 24mm
LIGHTING:  one fluorescent tube only, green cast; corners of the frame receive no fill;
           warm milk-white #E8E2D4 shaft at the far end
COMPOSITION: perfect symmetry, the white door at the exact centre, headroom for subtitles
MATERIALS: institutional green oil paint to chest height, faded whitewash above,
           bare concrete floor, worn burgundy runner, dust visible in the tube light
ATMOSPHERE: beautiful before it is frightening — this frame is the series poster
CONTINUITY: exactly five doors plus the 46th; corridor length constant across all episodes
Seed: TBD · Файл: assets/ep001-sh04.png
```

### sh05 — проход вглубь
```text
SUBJECT:   <IDENTITY LOCK>, seen from behind, walking away from camera
ACTION:    walking steadily toward the far door, glancing up at the flickering tube
CAMERA:    static — the camera does NOT follow him       LENS: 35mm
LIGHTING:  rim light from the door sliver on his shoulders, face never visible
COMPOSITION: figure centred and shrinking, empty corridor behind him
MATERIALS: heavy jacket fabric, worn runner, keyring
Seed: TBD · Файл: assets/ep001-sh05.png
```

### sh06 — брелок · REWATCH DETAIL
```text
SUBJECT:   a small plastic fish keychain hanging on a brass door handle
ACTION:    the keychain hangs still
LOCATION:  white apartment door, "46" in fresh paint, faded burgundy leatherette
CAMERA:    static                                       LENS: 100mm macro
LIGHTING:  warm from below, cold rim from above
COMPOSITION: handle and keychain in the lower third, the number 46 in the upper third
MATERIALS: cheap plastic rubbed white with age, scratches, a small red split ring,
           oxidised brass, quilted leatherette
CONTINUITY: THERE IS NOTHING ELSE ON THE HANDLE — no hair tie, nothing.
            One unique keychain for the whole series
Seed: TBD · Файл: assets/ep001-sh06.png
```

### sh07 — волос · EXTREME DETAIL
```text
SUBJECT:   a single long grey human hair lying at the base of a brass door handle
ACTION:    the hair rests across the metal, dust hanging motionless in the air
CAMERA:    static, 15 cm from the subject               LENS: 100mm macro
LIGHTING:  hard backlight; the hair glows like a thread against dark metal
COMPOSITION: the hair diagonal across frame, brass falling out of focus
MATERIALS: micro-scratches in brass, floating dust motes, the natural kink of the hair
ATMOSPHERE: an intimate, almost beautiful detail that becomes unpleasant on reflection
CONTINUITY: the hair is always Vera's — long, grey, with a bend
Seed: TBD · Файл: assets/ep001-sh07.png
```

### sh08 — лицо, узнавание
```text
SUBJECT:   <IDENTITY LOCK>
ACTION:    recognising something, one caught breath, saying nothing, not looking away
CAMERA:    static                LENS: 85mm, very shallow depth of field
LIGHTING:  hard side light from the door gap on the left; the right half of the face is pure
           black with no fill; the visible eye stays lit
COMPOSITION: face in the lower third, large empty space to the right
MATERIALS: pores, three-day stubble, perspiration at the temple, individual eyelashes
ATMOSPHERE: a man who has just been proven right and is not relieved by it
Seed: TBD · Файл: assets/ep001-sh08.png
```

### sh09 — снятие брелока
```text
SUBJECT:   a man's hand pulling the fish keychain off the door handle
ACTION:    the split ring catches, the skin over the knuckles stretches, the sharp edge
           drags across the palm leaving a thin line
CAMERA:    static                                       LENS: 100mm macro
LIGHTING:  hard warm key, sharp finger shadows
MATERIALS: palm lines, stretched skin over knuckles, brass, worn plastic
CONTINUITY: the scratch is on the LEFT palm and stays visible through EP03
Seed: TBD · Файл: assets/ep001-sh09.png
```

### sh10 — ЦЕНА · два кадра
```text
SUBJECT:   <IDENTITY LOCK> in the near foreground, side-on, not turning around;
           in the depth of frame the door of apartment 44 with a small brass nameplate
ACTION:    the intercom panel beside the white door lights up by itself
CAMERA:    static — the camera does not help the viewer notice
LENS:      35mm, stopped down so BOTH planes stay readable
LIGHTING:  green intercom glow on the near cheek; only the corridor tube in the depth
MATERIALS: engraved brass, grain of the painted door, dust
COMPOSITION: man in the right third foreground, door 44 in the left third of the depth
CONTINUITY: plate reads "ПОСОШКОВЫ" in version A and is blank brass in version B
Seed: TBD · Файлы: assets/ep001-sh10-a.png (с буквами) · assets/ep001-sh10-b.png (без)
```

### sh11 — свет на лице
```text
SUBJECT:   <IDENTITY LOCK>
ACTION:    a horizontal band of milk-white light rising across his eyes, pupils contracting,
           half a step forward
CAMERA:    static                                       LENS: 85mm
LIGHTING:  growing warm band from a door opening two centimetres
COMPOSITION: face centred, the light band horizontal across the eyes
Seed: TBD · Файл: assets/ep001-sh11.png
```

### sh12 — щель · POV
```text
SUBJECT:   a two-centimetre gap of warm morning light between door and frame
ACTION:    inside: the edge of a kitchen table, an overexposed window,
           a glass of milk with a clean untouched surface
CAMERA:    POV, breathing less than one percent         LENS: 50mm
LIGHTING:  milk-white 2700K, blown-out edge, everything else pure black
COMPOSITION: a vertical strip of light centred in the frame
MATERIALS: wooden door frame, tablecloth edge, glass
CONTINUITY: it is ALWAYS morning inside 46; milk there is always fresh
Seed: TBD · Файл: assets/ep001-sh12.png
```

### sh13 — экран телефона · SILENCE
```text
SUBJECT:   a phone screen held in a man's hand, a baby-monitor app view
ACTION:    a child's bed, duvet thrown back, the bed empty, a night light on;
           in the TOP RIGHT CORNER of the screen image, the edge of white fabric
           in the nursery doorway
CAMERA:    static                                       LENS: 100mm macro
LIGHTING:  the screen is the only light source, cold on the fingers
COMPOSITION: screen fills 70% of frame
MATERIALS: fingerprints on the glass, pixel grid, skin of the fingers
NOTE:      надпись «ДЕТСКАЯ · 00:46» рисуется в композе шрифтом PT Mono, а не генерацией
Seed: TBD · Файл: assets/ep001-sh13.png
```

### sh14 — рука и резинка · СМЕНА СМЫСЛА
```text
SUBJECT:   a man's hand closing on a brass door handle, knuckles whitening
ACTION:    the grip tightens; the handle does not turn
LOCATION:  door 46. ON THE SAME HANDLE, BESIDE HIS FINGERS, HANGS A THIN CHILD'S HAIR TIE
           WITH A SINGLE BEAD
CAMERA:    static                                       LENS: 85mm
LIGHTING:  warm gap below, cold above
COMPOSITION: hand in the lower third, blank white door plane above
MATERIALS: blanching skin, tendons, brass, elastic fabric of the hair tie, one plastic bead
CONTINUITY: the palm scratch from sh09 must be visible; the hair tie was NOT there in sh06
Seed: TBD · Файл: assets/ep001-sh14.png
```

---

## 2. Seedance — видео по шотам

Промпт описывает последовательность движения и физику, а не настроение.

### sh01
```text
SHOT: ep001-sc1-sh01 · INPUT: assets/ep001-sh01.png · DURATION: 2s · 9:16
SUBJECT: an elevator button panel, no people
ACTION: For the first half second nothing moves. Then the blank metal below the "9" begins to
        bulge outward very slightly, as if pressed from behind. The shape of a button forms.
        Only after the shape is complete does the number 46 light up in muted brick red.
CAMERA MOTION: none, locked off
PHYSICS: the metal deforms slowly and elastically like thin sheet metal, not like rubber;
         no sparks, no smoke, no debris, no melting
LIGHTING: the cold fluorescent stays constant; the red glow rises over 0.4 seconds and holds
FACIAL BEHAVIOR: none
START: blank metal · END: the 46 button formed and glowing steadily
NEGATIVE: camera movement, people, text overlay, sparks, melting metal, flicker of other buttons
```

### sh02
```text
SHOT: ep001-sc1-sh02 · INPUT: assets/ep001-sh02.png · DURATION: 2s · 9:16
ACTION: The man stays completely still for half a second. His eyes move down-left first.
        Only after the eyes have moved does the head begin to turn, about fifteen degrees,
        and stop. THE REFLECTION IN THE MIRROR REPEATS EACH MOVEMENT TWO FRAMES LATER
        THAN THE MAN HIMSELF.
CAMERA MOTION: none
PHYSICS: everything else in the mirror is a correct physical reflection; only the timing differs
LIGHTING: constant; the right half of the face receives no fill and stays pure black
FACIAL BEHAVIOR: no fear, eyebrows do not rise, jaw stays relaxed, one blink maximum
START: looking forward · END: looking at the panel, reflection catching up
CONTINUITY: facial identity, stubble, scar on right eyebrow and jacket completely unchanged
NEGATIVE: head shake, shoulder movement, zoom, monster in the mirror, second person,
          glowing eyes, distorted reflection
```

### sh03
```text
SHOT: ep001-sc1-sh03 · INPUT: assets/ep001-sh03.png · DURATION: 3s · 9:16
ACTION: The finger stays two centimetres away and does not move closer. After one second the
        red glow fades evenly to nothing over 0.8 seconds. One second later, light from the
        opening doors enters the frame from the left.
CAMERA MOTION: extremely slow push-in, no more than 4 percent of frame width across 3 seconds
PHYSICS: the glow fades smoothly, it does not blink or stutter
START: button lit · END: button dark, door light entering
NEGATIVE: hand shake, button press, flicker, fast dolly
```

### sh04
```text
SHOT: ep001-sc2-sh04 · INPUT: assets/ep001-sh04.png · DURATION: 3s · 9:16
ACTION: The corridor is empty and still. At 1.4 seconds the fluorescent tube stutters once
        through its starter — two frames dark, then steady again. The milk-white light under
        the far door widens by about a millimetre and narrows again, slowly, like breathing.
        Dust in the tube light drifts almost imperceptibly.
CAMERA MOTION: none
PHYSICS: the light under the door moves smoothly; the tube flicker is instantaneous;
         dust motes drift with air currents of a still room
START: corridor at rest · END: corridor at rest
NEGATIVE: people, figure appearing, door opening, camera movement, dust storm, fog
```

### sh05
```text
SHOT: ep001-sc2-sh05 · INPUT: assets/ep001-sh05.png · DURATION: 3s · 9:16
ACTION: The man walks away from camera at an even pace, four steps. On the second step he
        raises his eyes to the flickering tube above without stopping, then lowers them.
        The keyring on his hip swings in time with the steps. He becomes visibly smaller.
CAMERA MOTION: none — the camera stays behind and does not follow
PHYSICS: the keyring swings with real weight and lag; jacket fabric shifts on the shoulders;
         perspective scale changes correctly as he moves away
START: first step out of the lift · END: three metres from the door
CONTINUITY: same jacket, same keyring, body proportions unchanged
NEGATIVE: running, turning around, floating gait, morphing legs, camera following
```

### sh06
```text
SHOT: ep001-sc2-sh06 · INPUT: assets/ep001-sh06.png · DURATION: 2.5s · 9:16
ACTION: The keychain hangs still for one second, then swings twice — a small pendulum motion
        that damps down naturally and stops. Nothing else in frame moves.
CAMERA MOTION: none
PHYSICS: pendulum with a short period and visible damping; the door and handle stay rigid;
         there is no visible air movement anywhere else in frame
START: keychain still · END: keychain almost still again
NEGATIVE: wind, door movement, hand entering, any additional object on the handle
```

### sh07
```text
SHOT: ep001-sc2-sh07 · INPUT: assets/ep001-sh07.png · DURATION: 1.5s · 9:16
SUBJECT: a single long grey hair on brass, extreme macro
ACTION: The hair lies still for the first second. Then one end lifts about a millimetre and
        settles again. The dust in the air does not move at all during this.
CAMERA MOTION: none
PHYSICS: the hair moves as a very light fibre would, but nothing else responds — there is no
         air current in the frame
START: hair at rest · END: hair displaced by one millimetre
NEGATIVE: hair growing, hair crawling, insect, dust motion, camera movement, any face
```

### sh08
```text
SHOT: ep001-sc3-sh08 · INPUT: assets/ep001-sh08.png · DURATION: 3s · 9:16
ACTION: The face is still. At one second the chest lifts once with a caught breath and the
        nostrils widen slightly. The eyes stay open and do not blink until 2.4 seconds.
        At two seconds the gaze lowers toward the door handle. He does not speak.
CAMERA MOTION: none
FACIAL BEHAVIOR: micro-expression only; no crying, no grimace, no mouth opening
LIGHTING: the unlit half of the face stays completely black throughout
START: neutral · END: eyes lowered, decision made
NEGATIVE: talking, smiling, tears, head tilt, fill light appearing on the dark side
```

### sh09
```text
SHOT: ep001-sc3-sh09 · INPUT: assets/ep001-sh09.png · DURATION: 3s · 9:16
ACTION: The fingers close on the split ring and pull. The ring catches on the handle for half
        a second and resists — the skin over the knuckles stretches visibly. The hand pulls
        harder and the keychain comes free, the sharp edge dragging across the palm.
        A thin line appears on the skin one moment after the contact, not during it.
CAMERA MOTION: none
PHYSICS: the ring is rigid metal and does not bend; resistance is visible before release;
         skin deforms under the metal edge before the line appears
START: fingers touching the ring · END: keychain in the fist, thin scratch on the palm
NEGATIVE: blood spray, extra fingers, rubbery hand, glow, bending metal
```

### sh10
```text
SHOT: ep001-sc3-sh10 · INPUT: assets/ep001-sh10-a.png · END REFERENCE: assets/ep001-sh10-b.png
DURATION: 3s · 9:16
ACTION: The man in the foreground stands still and does not turn around. The intercom panel
        beside the white door lights up by itself at 0.4 seconds. Starting at 1.0 second, deep
        in the frame, the engraved letters on the brass nameplate of door 44 stop existing one
        at a time, from right to left, each taking about a fifth of a second. The engraving does
        not fade like light — the metal surface simply becomes smooth. By 2.4 seconds the plate
        is blank brass. The man never reacts and never turns.
CAMERA MOTION: none
PHYSICS: no particles, no dissolve, no glow, no sparkle — only the disappearance of engraving
LIGHTING: green intercom glow appears on the near cheek; the corridor tube behind stays constant
FOCUS: both planes stay readable throughout; no focus pull toward the nameplate
START: nameplate reads fully · END: nameplate blank
NEGATIVE: turning around, camera push toward the nameplate, focus pull, sparkle, dissolve
          effect, text appearing elsewhere, any figure in the corridor
```

### sh11
```text
SHOT: ep001-sc3-sh11 · INPUT: assets/ep001-sh11.png · DURATION: 2s · 9:16
ACTION: A horizontal band of warm light appears on the lower part of the face and rises slowly
        across the eyes as the door widens off-frame. The pupils contract visibly.
        He shifts his weight forward, half a step, no more.
CAMERA MOTION: none
PHYSICS: the light band moves smoothly and evenly, consistent with a door opening two centimetres
START: face in shadow · END: eyes lit, pupils narrowed
NEGATIVE: full door opening, strong flare, speaking, blinking during the pupil contraction
```

### sh12
```text
SHOT: ep001-sc4-sh12 · INPUT: assets/ep001-sh12.png · DURATION: 3s · 9:16
ACTION: The strip of warm light is steady. At 1.6 seconds a small soft-edged shadow crosses it
        from left to right, quickly, at the height of a child, and is gone. The strip returns
        to steady. The surface of the milk in the glass inside does not move.
CAMERA MOTION: POV breathing, less than one percent of frame
PHYSICS: the shadow is soft-edged and fast, consistent with something passing a few metres inside
START: empty strip · END: empty strip again
NEGATIVE: face appearing, door movement, monster silhouette, hand, eye in the gap
```

### sh13
```text
SHOT: ep001-sc4-sh13 · INPUT: assets/ep001-sh13.png · DURATION: 2s · 9:16
ACTION: The phone screen shows a still empty bed. At one second the camera feed refreshes:
        the image stutters for two frames, compression blocks visibly rebuild, and the bed is
        still empty. The edge of white fabric in the doorway at the top right does not move.
CAMERA MOTION: none
PHYSICS: digital refresh artefact only, no physical motion in the frame
START: screen lit, bed empty · END: refreshed, bed still empty
NEGATIVE: child appearing, ghost, figure moving, glitch aesthetic, hand movement, zoom
```

### sh14
```text
SHOT: ep001-sc4-sh14 · INPUT: assets/ep001-sh14.png · DURATION: 2s · 9:16
ACTION: The hand rests on the handle. Over 1.5 seconds the fingers tighten gradually and the
        knuckles go pale. The handle does not turn. The child's hair tie hanging beside the
        fingers moves once, very slightly, from the pressure transmitted through the metal.
CAMERA MOTION: none
PHYSICS: skin blanches under pressure, tendons lift on the back of the hand;
         the elastic hair tie behaves as light elastic fabric
START: hand resting · END: grip tight, knuckles white
CONTINUITY: the palm scratch from sh09 stays visible; the hair tie stays in frame the whole shot
NEGATIVE: door opening, handle turning, extra fingers, the keychain reappearing
```

---

## 2-бис. Правило текста в кадре

**Генерация не пишет текст. Никогда.**

Любые буквы и цифры, которые должны читаться — латунная табличка, список жильцов, номер
квартиры, домофонное табло, интерфейс телефона, — рисуются в композе шрифтами из
`bible/TYPOGRAPHY.md` поверх сгенерированной поверхности.

В промпт вместо текста идёт описание носителя: «a small engraved brass nameplate, the engraving
illegible at this distance», «a blank enamel plate», «a sheet of paper under scratched glass».
В негатив каждого промпта обязательно: `text, letters, numbers, signage, watermark, caption`.

Исключение — номер «46» на двери: он крупный, простой и генерируется приемлемо,
но проверяется на каждой генерации отдельно.

## 2-тер. Эталонные ассеты (генерируются один раз, дальше только переиспользуются)

| Ассет | Файл | Наследуют |
|---|---|---|
| Дверь 46 целиком | `assets/ref-door46.png` | sh06, sh07, sh09, sh11, sh12, sh13, sh14 |
| Дверная ручка крупно | `assets/ref-handle.png` | sh06, sh07, sh09, sh14 |
| Панель лифта | `assets/ref-panel.png` | sh01, sh03 |
| Коридор целиком | `assets/ref-corridor.png` | sh04, sh05, sh10 |

### Прогон эталонов — 21.08.2026, по два варианта на ассет

| Ассет | Вар. | Seed | Job ID | Выбор |
|---|---|---:|---|---|
| ref-corridor | A | 483256 | `7381976f-1cef-4149-983c-2c364c394b0c` | ⬜ |
| ref-corridor | B | 464751 | `560ce155-e32a-4ee5-8b20-7d3ab392d566` | ⬜ |
| ref-door46 | A | 334247 | `02205f71-cf72-4b9d-9308-e0b4aeb477d3` | ⬜ |
| ref-door46 | B | 991987 | `9d0aa44c-0a87-4b86-b2ac-74e5cee8c643` | ⬜ |
| ref-handle | A | 816535 | `426f191f-d1ab-4ddc-9b12-16d7bf03aeea` | ⬜ |
| ref-handle | B | 624565 | `94ebda73-7d8c-4ad2-afb6-0b64738dd7a0` | ⬜ |
| ref-panel | A | 602796 | `3189cb29-1389-4732-a980-eacda85aa697` | ⬜ |
| ref-panel | B | 674997 | `130d1315-a7ce-4caf-8a33-14b52723ae57` | ⬜ |

### Прогон эталонов v3 — 21.08.2026, позитивные формулировки

| Ассет | Seed | Job ID | Приёмка |
|---|---:|---|---|
| `ref-corridor` | **224379** | `e7388002-70d9-4422-bb8d-c2c3fc0ed1e7` | ⬜ |
| `ref-door46` | **214278** | `77e17ca1-eaf8-4d00-a5ee-e1697760a16b` | ⬜ |
| `ref-handle` | **79713** | `231affca-b76e-4b39-acbc-623eecad2e05` | ⬜ |

Метод изменён после провала v2: вместо перечисления запретов — позитивное описание
того, что должно быть в кадре. Из промптов убрано плёночное зерно: именно оно вызывало
краевую маркировку плёнки. Подробности — `.claude/agents/prompt-director.md`.

### Прогон эталонов v2 — отклонён целиком

Все три забракованы. На ручке появился брелок-рыбка, хотя `fish charm` стоял в негативе;
на двери — оранжевый плёночный код; в коридоре — объявления на стене, оранжевое пятно
вместо полосы света и красный отсвет без источника.

### Прогон эталонов v2 — исходные параметры

| Ассет | Seed | Job ID | Что исправлено | Приёмка |
|---|---:|---|---|---|
| `ref-corridor` | **875293** | `f96159cf-0ac5-405e-954f-bde1ac53333b` | закрытая белая дверь, свет только полосой снизу, молочный вместо оранжевого, холодная трубка | ⬜ |
| `ref-door46` | **393449** | `eada9679-b6a8-412a-a332-30c3dc193484` | **дверь без номера**: цифра рисуется в композе | ⬜ |
| `ref-handle` | **770194** | `54ba34e4-ad69-4619-bb71-47720310d0b9` | ручка пустая, ничего не висит | ⬜ |

Во всех трёх `enhance_prompt: false` — промпты сохранены дословно, проверено по ответу API.

**Ключевое решение прогона:** номер «46» на двери больше не генерируется. Он попадал
в кадр вместе с мусорным текстом, потому что любое упоминание цифр в промпте открывает
модели дверь к надписям. Теперь дверь генерируется чистой, а «46» наносится в композе
шрифтом из `bible/TYPOGRAPHY.md` — так же, как список жильцов, табличка и домофон.
Правило текста стало сплошным, без исключений.

### Прогон эталонов v1 — отменён

Что исправлено относительно теста v1: свет только узкой полосой снизу двери; лампа холодная
люминесцентная без оранжевого; в негатив добавлены `text, letters, numbers, signage, watermark`;
панель лифта генерируется **без кнопки 46** — она появляется в кадре sh01 как событие;
ручка генерируется **пустой**, брелок и волос добавляются в кадрах sh06 и sh07 с этого эталона.

Правило: кадры, входящие в одну локацию, генерируются **с эталона как reference-медиа**,
а не с нуля по тексту. Иначе в каждом кадре получается другая ручка.

## 2-кватер. Запрет на reference conditioning для кадров с лицом

Проверено 21.08.2026: при передаче референса `soul_2` принудительно переписывает промпт
и разрушает identity lock. Отключить нельзя. Подробности и таблица искажений —
`docs/production-stack/VIDEO_ENGINES.md` §3-бис.

**Кадры с лицом Прохора генерируются только text-to-image** с дословным locked-блоком.
Эталонные ассеты локаций (`ref-*`) референс использовать могут: там нет лица и нечего ломать.

## 3. Порядок производства

```
0. ЭТАЛОНЫ:  ref-door46, ref-handle, ref-panel, ref-corridor   ← добавлено после теста v1
1. Холодный тест v2: sh04, sh06, sh07, sh10-a/b с эталонов
2. Приёмка → остальные 11 мастер-кадров
3. Приёмка всех 15 → генерация 14 клипов
4. Сборка по EDIT.md
```

## 3-бис. Исправленные промпты для прогона v2

### sh04 — коридор (правка света)
Заменить в промпте два фрагмента:

```text
БЫЛО:  a plain white door with a narrow milk-white sliver of warm light spilling out from underneath it
СТАЛО: a plain closed white door, completely dark around its frame, with a single narrow
       milk-white strip of warm light visible ONLY along the very bottom edge, two centimetres high;
       the door frame itself is not glowing and there is no light around its sides or top

БЫЛО:  Lit by a single fluorescent ceiling tube in the middle of the corridor, cold green cast
СТАЛО: Lit by a single old fluorescent tube in the middle of the corridor, cold neutral white
       with a slight green cast, no orange or red glow anywhere in the frame
```
Добавить в негатив: `glowing door frame, portal, orange light, red light, warm ceiling lamp`.

### sh06 — брелок (правка цвета и номера)
```text
БЫЛО:  covered in faded burgundy quilted leatherette, and the number 46 is painted on it in fresh white paint
СТАЛО: covered in heavily faded, dusty, desaturated burgundy leatherette, closer to dull brown-red
       than to true red; the number 46 is painted in small white figures, fully visible with clear
       space around them, occupying no more than one eighth of the frame height
```
Добавить: `the only saturated colour in the frame is the small red split ring of the keychain`.

### sh07 — волос (главная правка)
```text
БЫЛО:  A single long grey human hair lying across the base of an oxidised brass door handle
СТАЛО: Exactly ONE single long grey human hair, one strand only, lying loosely across the base
       of an oxidised brass door handle. There is no lock of hair, no bundle, no cut strands —
       one thin isolated hair and nothing else on the metal
```
Добавить в негатив: `lock of hair, bundle of hair, hair strands, wig, cut hair, many hairs, fur`.

### sh10-a — цена (полная переработка)
```text
Photorealistic cinematic still, vertical 9:16, deep focus.
FOREGROUND, right third, very close to camera: the shoulder, jaw and cheek of a 29 year old
man in a dark navy utility work jacket, seen strictly in profile, facing along the corridor and
away from camera. His eyes are NOT visible. Half of his face is in complete darkness with no fill
light. Faint green light from an intercom panel just off frame touches only his cheekbone.
BACKGROUND, left third, five metres away and clearly readable: an apartment door with a small
engraved brass nameplate; the engraving is illegible at this distance.
The corridor has institutional green oil paint to chest height, faded whitewash above,
lit by one cold fluorescent tube far behind him.
35mm lens, stopped down, both planes sharp, locked-off tripod, no focus pull.
Desaturated institutional palette, natural skin pores, faint perspiration, fine film grain.
NEGATIVE: glowing eyes, green eyes, luminous pupils, eye contact with camera, text, letters,
numbers, caption, watermark, signage, second person, monster, glitch, lens flare,
shallow depth of field, blurred background.
```

Ни один клип не генерируется, пока его мастер-кадр не принят.

## 4. Журнал попыток

**Холодный тест v1 — 21.08.2026.** Модель `soul_2` (text2image_soul_v2), 1152×2048,
style «General», enhance_prompt off.

| Шот | Версия | Seed | Job ID | Результат |
|---|---|---:|---|---|
| sh04 коридор | v1 | 932055 | `0766db94-0479-4f85-98e6-087365eece53` | 🟨 почти принят, две правки света |
| sh06 брелок | v1 | 364660 | `383f0bb0-668c-414e-ba1b-3e1183fb50a1` | 🟨 лучший кадр теста, две правки |
| sh07 волос | v1 | 346868 | `fd8716cd-d3d4-460a-bec2-9c9522c2fa1f` | 🟥 переделать: прядь вместо одного волоса |
| sh10-a цена | v1 | 967287 | `5dfdad32-95c2-4559-a033-4f714bda5d55` | 🟥 переделать: светящиеся глаза, мусорный текст, нет глубины |

### Разбор теста v1

**sh04 — коридор.** Попадание по палитре, симметрии и фактуре. Два нарушения:
свет идёт по всему периметру двери и читается как портал, хотя по библии это узкая полоса
только снизу; потолочная лампа даёт оранжево-красное свечение, хотя у нас холодная
люминесцентная трубка, а красный обязан иметь сюжетный источник.

**sh06 — брелок.** Лучший кадр теста: дерматин, потёртая латунь, вытертая до белизны рыбка,
красное как единственный акцент. Правки: дверь слишком насыщенная — нужен выцветший бордовый
`#6E3B3B`, сейчас она почти красная и спорит с правилом редкого красного; номер «46» обрезан
верхом кадра, должен читаться целиком в верхней трети и быть мельче.

**sh07 — волос.** Свет, чёрный фон и макро-фактура отличные, но в кадре **прядь**, а не один
волос. Прядь читается как отрезанные волосы — это чужой, более дешёвый символ. Нужен ровно
один волос: мотив построен на том, что материя сохранила от человека минимум.

**sh10-a — цена.** Отклонён по трём причинам: **светящиеся зелёные глаза** — прямой запрет
библии, дешёвый хоррор; **мусорный текст поверх кадра**; отсутствие глубины — дверь с табличкой
оказалась на переднем плане вплотную к герою, хотя приём требует читаемого второго плана далеко
позади. Плюс лицо освещено фронтально, а нужна половина в чистом чёрном.

**Сквозная проблема.** В трёх кадрах три разные дверные ручки. До следующего прогона нужен
эталон: одна дверь 46 и одна ручка, от которых наследуются все остальные кадры.

**Вывод про текст.** Модель не пишет кириллицу: на табличке получилась абракадабра,
плюс модель самовольно добавила надпись поверх кадра. Правило зафиксировано ниже.

> Файлы не скачаны в репозиторий: домен выдачи `d8j0ntlcm91z4.cloudfront.net`
> закрыт политикой исходящего трафика этой сессии. Кадры доступны в галерее генерации.
> Seed каждого принятого кадра переносится в этот журнал и больше не меняется.

---

## 5. Эталонные ассеты: четыре прогона

Задача прогонов — получить три эталона (коридор, дверь, ручка), от которых
наследуются все остальные кадры EP01. Отдельная задача, потому что в тесте v1
в трёх кадрах оказались три разные дверные ручки.

### v2 — 21.08.2026, `soul_2`, отклонён целиком

| Ассет | Что пришло | Диагноз |
|---|---|---|
| ручка | на накладке висит брелок-рыбка | `fish charm, keychain` стояло в негативе |
| дверь | серая вместо белой, оранжевый код по краю | «film grain» в позитиве |
| коридор | объявления на стене, оранжевое пятно, красный отблеск | негатив + «film grain» |

Из этого выведены два правила промптинга — см. `.claude/agents/prompt-director.md`.

### v3 — 21.08.2026, `soul_2`, отклонён целиком

Метод исправлен наполовину: позитив переписан утвердительно, но короткий негатив
(`film border, timecode, watermark`, `hanging object, chain, cord`) остался.

| Ассет | Seed | Что пришло | Вердикт |
|---|---|---:|---|
| дверь | 214278 | поверхность чистая, белая, полоса света только снизу, накладка гладкая — **но** оранжевые плёночные коды по левому краю и световой засвет | 🟥 |
| коридор | 224379 | палитра верная: зелёный/кремовый, бордовая дорожка, холодная трубка — **но** доска объявлений слева, оранжево-розовая лужа света вместо узкой молочной полосы, таймкоды в углах | 🟥 |
| ручка | 79713 | геометрия ближе — **но** на накладке цепочка с подвеской «ENPIIERIT» и коды по правому краю | 🟥 |

**Вывод.** Правило подтвердилось на собственном браке: каждое существительное,
оставленное в негативе, вернулось в кадр. Половинчатое применение метода
не работает — негатив нужно опустошать целиком, а не сокращать.

### v4 — 21.08.2026, негатив пустой

Метод применён полностью: негативного списка нет вообще. Всё, чего в кадре быть
не должно, сформулировано утверждением о том, что там есть:

- вместо `notices, posters` → «поверхность покрашена, ровная и непрерывная от пола до потолка»;
- вместо `hanging object, chain` → «рычаг гладкий по всей длине и заканчивается скруглённым концом в открытом воздухе»;
- вместо `film grain` → «цифровой снимок, мелкий сенсорный шум».

Ручка после трёх провалов переведена на другой движок, как и было обещано.

| Ассет | Модель | Seed | Job ID |
|---|---|---:|---|
| коридор | `soul_2` | 41194 | `f4f4b689-7ff1-43dd-803b-246352af539a` |
| дверь | `soul_2` | 939398 | `dac7546f-fc78-412b-977f-bbf82ea66a55` |
| ручка | `nano_banana_pro` (`nano_banana_2`) | — | `e79996c1-5d64-48cc-a059-2659e9a57cd2` |

Проверка №0 пройдена: `params.prompt` во всех трёх заданиях совпал с отправленным
дословно, `enhance_prompt: false` у обоих `soul_2`.

**Вердикт — за владельцем:** кадры выдаются на CDN, который закрыт политикой
исходящего трафика сессии, поэтому увидеть их я не могу. Политика не обходится.

### Разбор v4 — 21.08.2026

| Ассет | Модель | Вердикт |
|---|---|---|
| ручка | `nano_banana_pro` | 🟩 **ПРИНЯТА** |
| дверь | `soul_2` | 🟥 свет по всему периметру + бурое пятно на филёнке |
| коридор | `soul_2` | 🟥 фотоаппарат на штативе посреди кадра, палитра ушла в тёплое |

**Что метод дал.** Пустой негатив снял оба хронических артефакта разом: во всех
трёх кадрах нет ни плёночных кодов по краям, ни мусорного текста, ни подвески
на ручке. Правило подтверждено — негатив опустошается целиком.

**Ручка — эталон.** Цельный латунный рычаг, гладкая накладка на двух винтах,
скол краски слева, холодный свет, конец в открытом воздухе. Ровно то, что
описывала библия. Задание `e79996c1-5d64-48cc-a059-2659e9a57cd2`, `nano_banana_pro`.
Seed модель не отдаёт — воспроизводимость держится на дословном промпте,
он записан в задании.

**Дверь.** Свет пробивается по всему периметру и читается как портал — та же
ошибка, что в v1 у варианта B. По библии щель только внизу: дом не светится,
дом подтекает. Плюс на филёнке появилось бурое прямоугольное пятно — вторая
неправильная деталь, а их должно быть ровно ноль на эталоне.

**Коридор — ошибка промптера, не модели.** В промпте стояло
`camera on a tripod at chest height` — описание точки съёмки. Модель нарисовала
фотоаппарат на штативе. Отсюда третье правило: **модель рисует каждое
существительное независимо от его роли в предложении.** Записано в
`.claude/agents/prompt-director.md`.

Уцелевшее из v4-коридора: полоса света под дальней дверью получилась именно
такой, как нужно — узкой, холодной, единственным светлым пятном.

### v5 — 21.08.2026

Точка съёмки задана без техники: `static locked-off view, eye level`.
Пустота кадра закрыта утверждением: `the corridor is deserted and the floor is
clear along its whole length`. Дверь запечатана утверждением:
`sealed along the top and both sides, so those three edges read as thin dark hairlines`.
Дверь переведена на движок, который взял ручку.

| Ассет | Модель | Seed | Job ID |
|---|---|---:|---|
| дверь | `nano_banana_pro` | — | `07543c3f-014d-4b4d-917d-81db7fb9e57f` |
| коридор | `nano_banana_pro` | — | `7c9c1518-7f6b-49d0-9d89-29b78805c5cd` |
| коридор (страховка) | `soul_2` | 900901 | `c5ede92a-d94a-49f8-a819-951656968582` |

### Разбор v5 — 21.08.2026. Эталоны закрыты

| Ассет | Модель | Job ID | Вердикт |
|---|---|---|---|
| коридор | `nano_banana_pro` | `7c9c1518-7f6b-49d0-9d89-29b78805c5cd` | 🟩 **ПРИНЯТ** |
| дверь | `nano_banana_pro` | `07543c3f-014d-4b4d-917d-81db7fb9e57f` | 🟩 **ПРИНЯТА** |
| коридор (страховка) | `soul_2` | `c5ede92a-d94a-49f8-a819-951656968582` | 🟥 не нужен |

**Коридор.** Симметрия по осевой, холодная серо-зелёная панель до пояса, меловой
верх, серый линолеум, тёмно-винная дорожка по центру, закрытая дверь в торце,
узкая полоса света под ней, холодная трубка под потолком, углы и передний план
в чёрном. Ни объявлений, ни техники, ни текста, ни кодов по краям.

**Дверь.** Филёнчатая, цвета грязного молока, прилегает плотно: верх и бока —
тонкие тёмные линии, свет пробивается только по низу узкой холодной полосой.
Латунная накладка с рычагом на уровне руки справа. Поверхность чистая.

**Страховочный `soul_2`.** Перспектива поплыла — стены выгибаются, пол уходит
в широкоугольную бочку, палитра ушла в тёплый беж. Подтверждает запись в
`VIDEO_ENGINES.md`: длинные коридоры и архитектуру ведёт `nano_banana_pro`.

**Итог по методу.** Три эталона получены за пять прогонов. Все три ошибки были
в промпте, не в модели:

1. существительное в негативе притягивает предмет;
2. `film grain` притягивает краевую разметку плёнки;
3. служебное слово о камере рисуется как предмет.

Общее правило одно: **модель рисует каждое существительное, где бы оно
ни стояло.** Кадр задаётся только утверждениями о том, что в нём есть.
