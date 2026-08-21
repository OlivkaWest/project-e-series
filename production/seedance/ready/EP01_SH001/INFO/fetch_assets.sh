#!/usr/bin/env bash
# Скачивает два кадра EP01_SH001 в UPLOAD/ под правильными именами.
# Запускать на своей машине из папки EP01_SH001.
set -euo pipefail
mkdir -p UPLOAD
curl -fL --retry 3 -o UPLOAD/01_START_FRAME.png "https://d8j0ntlcm91z4.cloudfront.net/user_2wC9fxqVl9PMYHtH6o6vf0HfQ8Y/hf_20260821_160032_c791a9f4-63d9-4518-b625-4c1db5814165.png"
curl -fL --retry 3 -o UPLOAD/02_END_FRAME.png   "https://d8j0ntlcm91z4.cloudfront.net/user_2wC9fxqVl9PMYHtH6o6vf0HfQ8Y/hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png"
ls -l UPLOAD
echo "Готово. Теперь: Upload -> вставить SEEDANCE_PROMPT.txt -> 9:16 -> 5 sec -> 720P -> Generate."
