# Seedance — основной video engine

Формат промпта (один шот = один файл или один блок):

```text
SHOT:
MODEL:
INPUT IMAGE:
DURATION:
ASPECT RATIO: 9:16
SUBJECT:
ACTION:
CAMERA MOTION:
ENVIRONMENT:
PHYSICS:
LIGHTING:
FACIAL BEHAVIOR:
START FRAME:
END FRAME:
CONTINUITY:
NEGATIVE CONSTRAINTS:
```

Критично: промпт описывает **последовательность движения**, а не настроение.

Плохо:
```text
cinematic mysterious scary atmosphere
```

Хорошо:
```text
The man initially remains completely still.
During the first second his eyes move toward the doorway.
He slowly turns his head.
Only after his head begins turning, the shadow behind him starts moving.
Camera performs a very slow push-in.
The character's facial identity, beard, clothing and body proportions remain completely unchanged.
```

Физику (скорость, масса, инерция, контакт, разрушение, порядок событий) описываем явно.
AI не решает физику сцены сам.
