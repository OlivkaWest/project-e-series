"""Комп SH010: гаснущие буквы на табличке квартиры 44.

Это VISUAL REVEAL первой серии и единственное место, где показано правило
мира «дом отдаёт — дом стирает». `SHOTLIST.md` sh10 прямо говорит: табличка
генерируется гладкой латунью, буквы ставятся и гасятся в композе.

Табличка в кадре — 21 на 48 пикселей, вертикальная. Поэтому фамилия набирается
повёрнутой на 90 градусов вдоль пластины, а не поперёк. Буквы гравированные:
тёмный штрих плюс светлый блик снизу, как на настоящей латуни.

Гасят их не разом, а справа налево — по букве, как записано в CONTINUITY:
«буквы перестают быть выгравированными... латунь становится гладкой».
"""
import subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont

SRC = "incoming/VIDEO_DUMP/EP01_SH010_v1.mp4"
DST = "incoming/VIDEO_DUMP/EP01_SH010_v1_comp.mp4"
FONT = "assets/fonts/Oswald.ttf"
TEXT = "ПОСОШКОВЫ"

# углы таблички в кадре 720x1280, снято с увеличенного кропа
TL, TR, BR, BL = (164, 464), (185, 468), (185, 511), (164, 515)
K = 8                      # рисуем в восемь раз крупнее и уменьшаем — сглаживание

FADE_FROM, FADE_TO = 1.15, 2.85   # окно гашения внутри исходника


def build_overlay(path):
    w = int((TR[0] - TL[0]) * K)
    h = int((BL[1] - TL[1]) * K)
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    # текст рисуем горизонтально на длинной стороне, потом поворачиваем
    strip = Image.new("RGBA", (h, w), (0, 0, 0, 0))
    d = ImageDraw.Draw(strip)
    size = int(w * 0.52)
    f = ImageFont.truetype(FONT, size)
    try: f.set_variation_by_axes([500])
    except Exception: pass
    # ужимаем кегль, пока фамилия не влезет в пластину с полями:
    # без этого верхняя буква вылезает за край таблички на дверь
    while size > 4 and d.textlength(TEXT, font=f) > h * 0.80:
        size -= 1
        f = ImageFont.truetype(FONT, size)
        try: f.set_variation_by_axes([500])
        except Exception: pass
    tw = d.textlength(TEXT, font=f)
    x = (h - tw) / 2
    y = (w - size) / 2 - size * 0.10
    # гравировка: тёмный штрих и светлый блик на пиксель ниже
    d.text((x, y + K * 0.9), TEXT, font=f, fill=(214, 198, 160, 90))
    d.text((x, y), TEXT, font=f, fill=(38, 30, 18, 205))

    img.paste(strip.rotate(90, expand=True), (0, 0), strip.rotate(90, expand=True))
    img = img.resize((w // K, h // K), Image.LANCZOS)
    img.save(path)
    return img.size


def main():
    ov = pathlib.Path("/tmp/sh010_plate.png")
    size = build_overlay(ov)
    x, y = TL[0], TL[1]
    # гашение справа налево: маска-градиент по горизонтали, ползущая по кадру
    vf = (
        f"[1:v]format=rgba,"
        f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':"
        f"a='alpha(X,Y)*clip(({FADE_TO}-T)/({FADE_TO}-{FADE_FROM})*1.9-(1-Y/H)*0.9,0,1)'[o];"
        f"[0:v][o]overlay={x}:{y}:format=auto"
    )
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", SRC, "-loop", "1", "-i", str(ov),
                    "-filter_complex", vf, "-map", "0:a?", "-shortest",
                    "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                    "-pix_fmt", "yuv420p", DST], check=True)
    print(f"табличка {size[0]}x{size[1]} px, гашение {FADE_FROM}-{FADE_TO} с → {DST}")


if __name__ == "__main__":
    main()
