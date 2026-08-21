# Шаблон эпизода

Скопировать целиком при заведении нового эпизода:

```bash
cp -r season-01/_episode-template season-01/episode-004
grep -rl 'EP-000\|ep000' season-01/episode-004 | xargs sed -i 's/EP-000/EP-004/g; s/ep000/ep004/g'
```

Затем добавить строку в [`../ARC.md`](../ARC.md) §4.
