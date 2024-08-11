# 20. JSONデータの読み込jjjjjjjj
# Wikipedia記事のＪＳＯＮファイルを読み込み、「イギリス」に関する記事本文を表示せよ。
# 問題21-29 では、ここで抽出した記事本文にたいして実行せよ

import pandas as pd
import re

filename = "jawiki-country.json"
json = pd.read_json(filename, lines=True)

uk = json[json["title"] == "イギリス"]
uk = uk["text"].values

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ

for c in uk[0].split("\n"):
    if "Category:" in c:
        category = c
        break
print(category)

# 22.カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で)抽出せよ

for c in uk[0].split("\n"):
    if "Category:" in c:
        match = re.search(r'\[\[Category:([^\|\]]+)', c)
        if (match):
            print(match.group(1))
