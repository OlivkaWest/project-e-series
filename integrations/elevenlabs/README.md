# ElevenLabs — `NEEDS_KEY`

**Путь доступа:** официальный SDK `elevenlabs==2.18.0` (установлен).

## Что нужно

```bash
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_PROHOR=...
ELEVENLABS_VOICE_SERAFIMA=...
ELEVENLABS_VOICE_ADELAIDA=...
ELEVENLABS_VOICE_HOUSE=...
```

## Что используем

Text-to-speech · timestamps (словные таймкоды → субтитры) · sound effects ·
контроль произношения · переиспользуемые voice ID.

## Правило

Voice ID фиксируется на CHECKPOINT 5 и не меняется до конца сезона.
Ключи и ID живут в `.env` и **никогда** не попадают в репозиторий.

## Резерв

Без ключа доступен `seed_audio` через Higgsfield — только для черновиков.
