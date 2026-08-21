import csv
import re
import math
from pathlib import Path

src = Path('/home/ubuntu/verify_youtube_video_candidates.csv')
outdir = Path('/home/ubuntu/youtube_shorts_market_research')

fields = [
    ('channel', r'Канал:\s*(.*?)(?=; URL канала:|; Язык:)'),
    ('channel_url', r'URL канала:\s*(.*?)(?=; Язык:)'),
    ('language', r'Язык:\s*(ru|en|другой)'),
    ('title', r'Заголовок:\s*(.*?)(?=; Дата:)'),
    ('date', r'Дата:\s*(.*?)(?=; Просмотры:)'),
    ('views_raw', r'Просмотры:\s*(.*?)(?=; Подписчики:)'),
    ('subs_raw', r'Подписчики:\s*(.*?)(?=; Длительность_с:)'),
    ('duration_raw', r'Длительность_с:\s*(.*?)(?=; Тип:)'),
    ('format', r'Тип:\s*(.*?)(?=; Серийность:)'),
    ('seriality', r'Серийность:\s*(.*?)(?=; Подходит:)'),
    ('fit', r'Подходит:\s*(да|нет|неясно)'),
    ('hook', r'Хук:\s*(.*?)(?=; Конфликт:)'),
    ('conflict', r'Конфликт:\s*(.*?)(?=; Поворот:)'),
    ('twist', r'Поворот:\s*(.*?)(?=; Финал:)'),
    ('ending', r'Финал:\s*(.*?)(?=; Соседний эпизод:)'),
    ('neighbor', r'Соседний эпизод:\s*(.*)$'),
]

def extract_num(value):
    value = value.strip().lower()
    if 'не найдено' in value or value == '':
        return None
    # supports values like 3,200,000 / 3.2M / 8.25K / 649000
    m = re.search(r'([\d][\d\s,\.]*)(?:\s*([km]))?', value)
    if not m:
        return None
    raw = m.group(1).replace(' ', '').replace(',', '')
    try:
        num = float(raw)
    except ValueError:
        return None
    suffix = m.group(2)
    if suffix == 'k':
        num *= 1_000
    elif suffix == 'm':
        num *= 1_000_000
    return int(num)

def clean_text(value):
    return re.sub(r'\s+', ' ', value or '').strip()

rows = []
with src.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for source_row in reader:
        record = source_row.get('Проверенная запись', '')
        item = {'video_url': source_row.get('Subject', ''), 'sources': source_row.get('Источники', ''), 'quality': source_row.get('Качество проверки', '')}
        for name, pattern in fields:
            match = re.search(pattern, record, re.S)
            item[name] = clean_text(match.group(1)) if match else 'не найдено'
        item['views'] = extract_num(item['views_raw'])
        item['subs'] = extract_num(item['subs_raw'])
        item['duration_seconds'] = extract_num(item['duration_raw'])
        item['is_qualified'] = item['fit'] == 'да' and item['language'] in {'ru','en'}
        item['ratio'] = (item['views'] / item['subs']) if item['views'] and item['subs'] else None
        if item['ratio'] is None:
            item['view_ratio_score'] = None
        else:
            item['view_ratio_score'] = round(min(25, 25 * math.log10(max(1, item['ratio'])) / 2), 1)
        item['data_completeness'] = sum(1 for x in [item['date'], item['views_raw'], item['subs_raw'], item['duration_raw'], item['hook'], item['conflict'], item['ending'], item['neighbor']] if x != 'не найдено')
        rows.append(item)

qualified = [r for r in rows if r['is_qualified']]
for lang in ('en','ru'):
    lang_rows = [r for r in qualified if r['language'] == lang]
    # Include all, but prioritize records with more complete data and with views/subs.
    lang_rows.sort(key=lambda r: ((r['views'] is not None) + (r['subs'] is not None) + (r['ratio'] is not None), r['data_completeness'], r['views'] or 0), reverse=True)
    for i, row in enumerate(lang_rows, start=1):
        row['rank_within_language'] = i
    print(lang, 'qualified:', len(lang_rows), 'with_views:', sum(r['views'] is not None for r in lang_rows), 'with_subs:', sum(r['subs'] is not None for r in lang_rows), 'with_ratio:', sum(r['ratio'] is not None for r in lang_rows))

out_fields = ['rank_within_language','language','channel','channel_url','title','video_url','date','views','subs','duration_seconds','format','seriality','fit','ratio','view_ratio_score','data_completeness','hook','conflict','twist','ending','neighbor','quality','sources']
with (outdir / 'case_registry_all_qualified.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    for language in ('en','ru'):
        for row in sorted([x for x in qualified if x['language'] == language], key=lambda r: r.get('rank_within_language', 9999)):
            writer.writerow({k: row.get(k,'') for k in out_fields})

# Create a 100-case balanced evidence roster: first 50 of each qualified language.
selected = []
for language in ('en','ru'):
    selected.extend(sorted([x for x in qualified if x['language'] == language], key=lambda r: r.get('rank_within_language', 9999))[:50])
with (outdir / 'case_registry_100.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    for row in selected:
        writer.writerow({k: row.get(k,'') for k in out_fields})

# Summary with date values used and metric completeness.
summary = []
for lang in ('en','ru'):
    lr = [r for r in selected if r['language'] == lang]
    summary.append({
        'language': lang,
        'selected_cases': len(lr),
        'cases_with_views': sum(r['views'] is not None for r in lr),
        'cases_with_subs': sum(r['subs'] is not None for r in lr),
        'cases_with_ratio': sum(r['ratio'] is not None for r in lr),
        'cases_with_date': sum(r['date'] != 'не найдено' for r in lr),
        'cases_with_hook': sum(r['hook'] != 'не найдено' for r in lr),
        'cases_with_neighbor': sum(r['neighbor'] != 'не найдено' for r in lr),
    })
with (outdir / 'case_registry_summary.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=summary[0].keys())
    writer.writeheader(); writer.writerows(summary)
print('all qualified:', len(qualified), 'selected:', len(selected))
