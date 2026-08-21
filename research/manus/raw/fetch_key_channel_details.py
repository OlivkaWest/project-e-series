import sys
import json
from pathlib import Path
sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient

channels = [
    ('en', 'https://www.youtube.com/@TheLandofBoggs'),
    ('en', 'https://www.youtube.com/@CatDogDiary-6868'),
    ('en', 'https://www.youtube.com/@ViglooOfficial'),
    ('ru', 'https://www.youtube.com/@yandextaxi'),
    ('ru', 'https://www.youtube.com/@Al-sEriesSS'),
    ('ru', 'https://www.youtube.com/@Animatic-i1d'),
]
client = ApiClient()
results = []
for language, channel in channels:
    try:
        data = client.call_api('Youtube/get_channel_details', query={'id': channel, 'hl': language})
        results.append({'language':language,'channel_input':channel,'data':data})
    except Exception as exc:
        results.append({'language':language,'channel_input':channel,'error':str(exc)})
out = Path('/home/ubuntu/youtube_shorts_market_research/key_channel_details.json')
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Сохранены структурированные карточки {len(results)} каналов: {out}')
