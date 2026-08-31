#!/usr/bin/env python3
"""Озвучка EP01. Запускать НА СВОЕЙ МАШИНЕ, не в удалённой сессии.

Причина: в удалённой сессии хост api.elevenlabs.io закрыт политикой
исходящего трафика, 403 на CONNECT. Обходить политику нельзя.

Что делает:
  1. читает ключ и voice id из .env (в репозиторий .env не попадает);
  2. если voice id не заданы — печатает список доступных голосов и выходит,
     чтобы вы выбрали и вписали их в .env;
  3. синтезирует четыре реплики с настройками из VOICE.md;
  4. накладывает обработку, прописанную в режиссуре: домофонная полоса
     300-3400 Гц для Серафимы, приглушение через дверь для Аделаиды;
  5. нормализует речь к -16 LUFS, пик <= -1 dBTP.

Запуск:
    pip install elevenlabs
    python3 integrations/elevenlabs/render_ep01_voice.py            # список голосов
    python3 integrations/elevenlabs/render_ep01_voice.py --render   # синтез
"""
import os, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "season-01/episode-001/assets/voice"


def load_env():
    p = ROOT / ".env"
    if not p.exists():
        sys.exit(".env не найден. Скопируйте .env.example в .env и заполните.")
    for line in p.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.strip().split("=", 1)
            os.environ.setdefault(k, v)


# реплика, персонаж, переменная с voice id, настройки, обработка
CUES = [
    ("v01", "Серафима", "ELEVENLABS_VOICE_SERAFIMA",
     "Не бери. Ты уже платил.",
     dict(stability=0.55, similarity_boost=0.85, style=0.20),
     "highpass=f=300,lowpass=f=3400,acompressor=threshold=-18dB:ratio=3"),
    ("v02", "Прохор", "ELEVENLABS_VOICE_PROHOR",
     "Мам?",
     dict(stability=0.45, similarity_boost=0.80, style=0.30),
     None),
    ("v03", "Аделаида", "ELEVENLABS_VOICE_ADELAIDA",
     "Пап, я тут.",
     dict(stability=0.40, similarity_boost=0.80, style=0.35),
     "lowpass=f=5000,aecho=0.8:0.7:22:0.18"),
    ("v04", "Аделаида", "ELEVENLABS_VOICE_ADELAIDA",
     "Пап.",
     dict(stability=0.40, similarity_boost=0.80, style=0.35),
     "lowpass=f=5000,aecho=0.8:0.7:22:0.18"),
]


def main():
    load_env()
    from elevenlabs.client import ElevenLabs
    client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])

    missing = [var for _, _, var, *_ in CUES if not os.environ.get(var)]
    if missing or "--render" not in sys.argv:
        print("Доступные голоса. Выберите и впишите id в .env:\n")
        for v in client.voices.get_all().voices:
            lb = v.labels or {}
            print(f"  {v.voice_id}  {v.name:24s} {lb.get('gender',''):8s}"
                  f"{lb.get('age',''):12s}{lb.get('accent','')}")
        if missing:
            print("\nНе заполнено в .env:", ", ".join(sorted(set(missing))))
        print("\nПотом: python3 integrations/elevenlabs/render_ep01_voice.py --render")
        return

    OUT.mkdir(parents=True, exist_ok=True)
    for tag, who, var, text, settings, fx in CUES:
        raw = OUT / f"ep001-{tag}.raw.mp3"
        final = OUT / f"ep001-{tag}.wav"
        audio = client.text_to_speech.convert(
            voice_id=os.environ[var],
            model_id="eleven_multilingual_v2",
            text=text,
            voice_settings=settings,
            output_format="mp3_44100_128",
        )
        raw.write_bytes(b"".join(audio))

        chain = [fx] if fx else []
        chain.append("loudnorm=I=-16:TP=-1:LRA=7")
        chain.append("aresample=48000:resampler=soxr")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw),
                        "-af", ",".join(chain), "-ar", "48000",
                        "-c:a", "pcm_s16le", str(final)], check=True)
        raw.unlink()
        print(f"  {tag}  {who:10s} «{text}»  →  {final.relative_to(ROOT)}")

    print("\nГотово. Файлы положить в репозиторий и прислать — вставлю в монтаж.")


if __name__ == "__main__":
    main()
