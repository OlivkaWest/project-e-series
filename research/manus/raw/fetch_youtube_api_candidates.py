import sys
import json
from pathlib import Path

sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient

out = Path('/home/ubuntu/youtube_shorts_market_research/youtube_api_discovery.json')
queries = [
    ('en', 'US', 'vertical short drama episode 1'),
    ('en', 'US', 'Roblox horror story part 1 shorts'),
    ('en', 'US', 'animated story episode shorts'),
    ('en', 'US', 'AI animated story episode shorts'),
    ('en', 'US', 'rescue kitten puppy story series'),
    ('en', 'US', 'POV story part 1 shorts'),
    ('ru', 'RU', 'вертикальный мини сериал'),
    ('ru', 'RU', 'сериал часть 1 shorts'),
    ('ru', 'RU', 'майнкрафт сериал серия shorts'),
    ('ru', 'RU', 'мистика часть 1 shorts'),
    ('ru', 'RU', 'ИИ сериал shorts'),
    ('ru', 'RU', 'скетчи серия shorts'),
]

client = ApiClient()
all_results = []
for language, country, query in queries:
    try:
        response = client.call_api('Youtube/search', query={'q': query, 'hl': language, 'gl': country})
        items = []
        for content in response.get('contents', []):
            if content.get('type') == 'video':
                v = content.get('video', {})
                items.append({
                    'videoId': v.get('videoId'), 'title': v.get('title'),
                    'channelTitle': v.get('channelTitle'), 'channelId': v.get('channelId'),
                    'channelUrl': v.get('channelUrl'), 'published': v.get('publishedTimeText'),
                    'views': v.get('viewCountText'), 'duration': v.get('lengthText') or v.get('lengthSeconds'),
                    'description': v.get('descriptionSnippet'), 'badges': v.get('badges', [])
                })
        all_results.append({'language': language, 'country': country, 'query': query, 'estimatedResults': response.get('estimatedResults'), 'items': items})
    except Exception as exc:
        all_results.append({'language': language, 'country': country, 'query': query, 'error': str(exc), 'items': []})

out.write_text(json.dumps(all_results, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Saved {len(all_results)} query results to {out}')
for block in all_results:
    print(block['language'], block['query'], len(block['items']))
