import pandas as pd
import numpy as np
import re
import math
from datetime import date
from pathlib import Path
import matplotlib.pyplot as plt

base = Path('/home/ubuntu/youtube_shorts_market_research')
df = pd.read_csv(base / 'case_registry_100.csv')
snapshot = pd.Timestamp('2026-08-21')
df['published'] = pd.to_datetime(df['date'], errors='coerce')
df['age_days'] = (snapshot - df['published']).dt.days.clip(lower=1)
df['views'] = pd.to_numeric(df['views'], errors='coerce')
df['subs'] = pd.to_numeric(df['subs'], errors='coerce')
df['ratio'] = pd.to_numeric(df['ratio'], errors='coerce')
df['velocity_day'] = df['views'] / df['age_days']

# Normalise channel identity despite inconsistent source formatting.
def channel_key(x):
    x = str(x).lower()
    x = x.split('(')[0].split('—')[0].strip()
    x = re.sub(r'url канала:.*', '', x).strip()
    return x

df['channel_key'] = df['channel'].map(channel_key)

# Series evidence: number of records and known neighbor episodes for the same channel.
group_stats = df.groupby(['language','channel_key']).agg(
    group_cases=('video_url','count'),
    group_views=('views', lambda s: s.notna().sum()),
    median_views=('views','median'),
    max_views=('views','max')
).reset_index()
df = df.merge(group_stats, on=['language','channel_key'], how='left')
df['retention_proxy'] = np.where(
    (df['group_views'] >= 3) & df['max_views'].notna() & (df['max_views'] > 0),
    df['median_views'] / df['max_views'],
    np.nan
)

# Score is a conservative public-data score. Missing public evidence earns zero in that component.
df['score_view_ratio'] = np.where(df['ratio'].notna(), np.minimum(25, 25 * np.log10(np.maximum(1, df['ratio'])) / 2), 0)
df['score_velocity'] = np.where(df['velocity_day'].notna(), np.minimum(15, 15 * np.log10(1 + df['velocity_day']) / 6), 0)
df['has_explicit_episode'] = df['seriality'].str.contains(r'часть|серия|episode|part|эпизод', case=False, na=False)
df['neighbor_known'] = ~df['neighbor'].fillna('').str.contains('не найдено', case=False)
df['score_repeatability'] = np.where(df['group_cases'] >= 3, 20, np.where(df['neighbor_known'] & df['has_explicit_episode'], 15, np.where(df['neighbor_known'], 10, 5)))
df['score_retention'] = np.where(df['retention_proxy'].notna(), np.minimum(15, 15 * df['retention_proxy']), 0)
# Comment-demand cannot be reliably retrieved for most anonymous-page cases, so it stays zero.
df['score_comment_demand'] = 0
df['score_simplicity'] = np.where(df['hook'].fillna('').str.contains('не найдено', case=False), 2, 5)
# Strong emotions inferred only from documented hook/conflict lexical cues.
emotion_text = (df['hook'].fillna('') + ' ' + df['conflict'].fillna('') + ' ' + df['ending'].fillna('')).str.lower()
strong = emotion_text.str.contains(r'страх|ужас|пуга|опас|преда|betray|horror|terrified|тревог|умер|похищ|секрет|исчез|mystery|lost|спас')
medium = emotion_text.str.contains(r'юмор|смеш|игр|любов|роман|family|друж|школ|работ')
df['score_emotion'] = np.select([strong, medium], [10, 7], default=5)
df['viral_score_public'] = (df['score_view_ratio'] + df['score_velocity'] + df['score_repeatability'] + df['score_retention'] + df['score_comment_demand'] + df['score_simplicity'] + df['score_emotion']).round(1)

# Complete data means numeric views, numeric subs, date, hook and available neighbor episode.
df['evidence_fields'] = df[['views','subs','published','hook','neighbor']].notna().sum(axis=1)
df.loc[df['hook'].fillna('').str.contains('не найдено'), 'evidence_fields'] -= 1
df.loc[df['neighbor'].fillna('').str.contains('не найдено'), 'evidence_fields'] -= 1

summary = df.groupby('language').agg(
    cases=('video_url','count'),
    numeric_views=('views',lambda s: s.notna().sum()),
    numeric_subs=('subs',lambda s: s.notna().sum()),
    numeric_ratio=('ratio',lambda s: s.notna().sum()),
    dated=('published',lambda s: s.notna().sum()),
    median_views=('views','median'),
    max_views=('views','max'),
    median_ratio=('ratio','median'),
    median_public_score=('viral_score_public','median')
).reset_index()
summary.to_csv(base/'analysis_market_summary.csv',index=False)

# Exclude low-data singletons from rank. Keep at least date/views or views/subs evidence.
ranked = df[(df['views'].notna()) & (df['subs'].notna())].copy()
ranked = ranked.sort_values(['viral_score_public','ratio','views'], ascending=False)
cols = ['language','channel','title','video_url','date','views','subs','ratio','velocity_day','group_cases','retention_proxy','viral_score_public','score_view_ratio','score_velocity','score_repeatability','score_retention','hook','conflict','ending','neighbor','quality']
ranked.head(40)[cols].to_csv(base/'ranked_public_viral_score.csv',index=False)

# Top ten per segment for inspection.
for lang in ['en','ru']:
    ranked[ranked['language']==lang].head(15)[cols].to_csv(base/f'top15_{lang}_public_score.csv',index=False)

# Channel / mechanism selection table.
mechanism_rows = []
for (lang, chan), g in df.groupby(['language','channel_key']):
    best = g.sort_values(['viral_score_public','views'], ascending=False).iloc[0]
    mechanism_rows.append({
        'language':lang, 'channel':chan, 'cases_in_sample':len(g),
        'best_title':best['title'], 'best_views':best['views'], 'best_ratio':best['ratio'],
        'best_public_score':best['viral_score_public'], 'seriality':best['seriality'],
        'hook':best['hook'], 'video_url':best['video_url']
    })
mechanisms = pd.DataFrame(mechanism_rows).sort_values(['best_public_score','best_ratio'], ascending=False)
mechanisms.to_csv(base/'channel_mechanism_summary.csv',index=False)

# Visual: meaningful anomalies only — require at least 10,000 public views to avoid a tiny-channel denominator artefact.
plot = ranked[ranked['views'] >= 10_000].copy()
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
fig, axes = plt.subplots(1,2,figsize=(16,6),sharex=False)
for ax, lang, color in zip(axes,['en','ru'],['#2E86AB','#C73E1D']):
    s = plot[plot['language']==lang].sort_values('ratio', ascending=True).tail(7)
    labels = [str(x)[:34] for x in s['title']]
    ax.barh(labels, s['ratio'], color=color)
    ax.set_title('Англоязычные кейсы: View Ratio' if lang=='en' else 'Русскоязычные кейсы: View Ratio')
    ax.set_xlabel('Просмотры / подписчики')
    for y, (ratio, score) in enumerate(zip(s['ratio'], s['viral_score_public'])):
        ax.text(ratio, y, f'  {ratio:.1f}× | VS {score:.0f}', va='center', fontsize=8)
fig.suptitle('Массовые аномалии в выборке: только кейсы с ≥10 тыс. публичных просмотров', fontsize=14, fontweight='bold')
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(base/'top_view_ratio_anomalies.png', dpi=180, bbox_inches='tight')

# Markdown analysis brief with direct values.
md = []
md.append('# Вычислительная сводка выборки\n')
md.append('Срез: 21.08.2026. Score ниже — консервативный **Public-data Viral Score**: недоступный из открытых источников компонент получает 0, поэтому показатель сравнивает силу публично зафиксированных доказательств, а не «истинную» алгоритмическую эффективность.\n')
md.append('## Полнота данных\n')
md.append(summary.to_markdown(index=False))
md.append('\n## Топ-20 по консервативному Public-data Viral Score\n')
md.append(ranked.head(20)[['language','channel','title','views','subs','ratio','velocity_day','group_cases','retention_proxy','viral_score_public','video_url']].to_markdown(index=False))
md.append('\n## Условные формулы\n')
md.append('`Viral Score = View Ratio (25) + Velocity (15) + Repeatability (20) + Series Retention (15) + Comment Demand (10) + Simplicity (5) + Emotional Trigger (10)`. Скорость — `текущие публичные просмотры / дни с публикации`; retention — медиана подтверждённых просмотров нескольких выпусков одного канала / максимум этой группы. Comment Demand не начислялся без репрезентативной доступной выборки комментариев.\n')
(base/'analysis_summary.md').write_text('\n'.join(md),encoding='utf-8')
print(summary.to_string(index=False))
print('\nTop public score:')
print(ranked.head(12)[['language','channel','title','views','subs','ratio','velocity_day','viral_score_public']].to_string(index=False))
