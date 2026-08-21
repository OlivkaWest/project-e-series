# Motion base (image → video)

**Модель:** TBD · **Длительность:** 5 сек · **Дата проверки:** TBD

```
INPUT IMAGE: references/ref-34.png
MOTION: <одно движение: subtle head turn left / slow blink / step forward>
CAMERA: <одно движение: static | slow push-in | slight handheld>
DURATION: 5s
NEGATIVE: morphing face, changing clothes, extra limbs, background warping, text
```

Правила:
- одно движение персонажа + одно движение камеры, не больше;
- лицо крупнее среднего плана — камера статична;
- сцены дольше 5 секунд собираются склейкой, а не одной длинной генерацией.
