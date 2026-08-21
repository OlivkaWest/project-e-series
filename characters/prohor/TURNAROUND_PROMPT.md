# TURNAROUND — Прохор

Семь ракурсов с одним сидом и одним светом. Генерируются **после** приёмки hero reference.

| # | Файл | Ракурс | Отличие в промпте |
|---:|---|---|---|
| 1 | `references/hero-canonical.png` | эталон, 3/4 слева | базовый промпт |
| 2 | `references/front.png` | строго фас | `camera directly front-on, symmetrical` |
| 3 | `references/profile-left.png` | профиль слева | `strict left profile, nose bridge bump clearly readable` |
| 4 | `references/profile-right.png` | профиль справа | `strict right profile, the scar through the right eyebrow clearly visible` |
| 5 | `references/three-quarter-right.png` | 3/4 справа | `turned 45 degrees to the right` |
| 6 | `references/back.png` | со спины | `seen from behind, head and shoulders, no face visible` |
| 7 | `references/full-body.png` | в рост | `full body standing, 35mm, base wardrobe` |

## Общее для всех ракурсов

```text
LIGHTING: identical single hard source from the left, no fill on the shadow side
BACKGROUND: neutral dark grey, out of focus
EXPRESSION: neutral in all seven
CONTINUITY: identical wardrobe, identical hair length, identical stubble density
```

**Правило:** ракурсы генерируются одной пачкой, с одного сида, в одну сессию.
Разбитые на разные дни — расходятся.
