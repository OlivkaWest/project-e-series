"""Расчёт Viral Score форматов по весам ТЗ.

Веса (сумма 100):
  hook 15, view_sub 10, repeat 15, retention 15, cliffhanger 10,
  emotion 10, prod_scalability 10, ai_compat 10, ru_opportunity 5

Оценки по каждому критерию — 0..10, выставлены по данным реестра
research/manus/raw/case_registry_100.csv и разборам роликов.
Обоснование каждой оценки — в FORMAT_RANKING.md.
"""

WEIGHTS = {
    "hook": 15, "view_sub": 10, "repeat": 15, "retention": 15,
    "cliff": 10, "emotion": 10, "prod": 10, "ai": 10, "ru": 5,
}

FORMATS = [
    # name, hook, view_sub, repeat, retention, cliff, emotion, prod, ai, ru
    ("Бытовая мистика: правило мира + сквозной долг", 9.5, 6.0, 9.0, 8.0, 9.5, 9.0, 8.5, 9.5, 9.0),
    ("Каталог правил выживания (аномалия №N)",        9.0, 7.0, 9.5, 6.5, 6.0, 7.5, 9.5, 9.5, 6.0),
    ("Социальная микродрама: маскировка + разоблачение", 8.5, 8.0, 8.0, 9.0, 7.0, 9.0, 5.0, 5.5, 6.0),
    ("Игровая анимационная сериализация (Minecraft/Roblox)", 8.0, 9.0, 9.5, 5.0, 8.0, 6.0, 9.0, 7.0, 5.0),
    ("Комедийный дуэт с ролевой асимметрией",         8.5, 4.0, 10.0, 8.0, 3.0, 7.0, 9.0, 8.5, 7.0),
    ("Катастрофа/постапокалипсис, длинный эпизод",    9.0, 5.0, 7.0, 7.0, 9.0, 8.5, 4.0, 5.5, 7.0),
    ("Интерактивная развилка «что ты выберешь»",      8.5, 3.0, 10.0, 6.0, 4.0, 5.5, 9.5, 9.0, 4.0),
    ("Институциональная абсурд-антиутопия",           8.0, 8.0, 9.0, 5.0, 3.0, 6.5, 8.5, 7.5, 5.0),
    ("Вертикальная мелодрама (CEO/измена/месть)",     8.0, 4.0, 9.0, 8.0, 9.0, 9.0, 3.0, 4.0, 3.0),
    ("Дневник отношений (животные/дуэт без слов)",    8.0, 9.5, 9.5, 3.0, 2.0, 9.5, 4.0, 3.0, 5.0),
]

KEYS = ["hook", "view_sub", "repeat", "retention", "cliff", "emotion", "prod", "ai", "ru"]


def score(row):
    return sum(row[i + 1] * WEIGHTS[k] for i, k in enumerate(KEYS)) / 10.0


def main():
    ranked = sorted(FORMATS, key=score, reverse=True)
    head = "| # | Формат | Hook | V/S | Повтор | Retention | Cliff | Эмоция | Произв. | AI | RU | **Viral Score** |"
    print(head)
    print("|" + "---|" * 12)
    for i, row in enumerate(ranked, 1):
        vals = " | ".join(f"{v:.1f}" for v in row[1:])
        print(f"| {i} | {row[0]} | {vals} | **{score(row):.1f}** |")


if __name__ == "__main__":
    main()
