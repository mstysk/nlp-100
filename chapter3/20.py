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

print('\n')
# 23. セクション構造
# 記事中にふくまれるセクション名とそのレベル（例えば"==セクション名=="なら1) を表示せよ
for line in uk[0].split("\n"):
    if "==" in line:
        stripped_line = line.lstrip("=")
        level = len(line) - len(stripped_line) - 1
        content = stripped_line.strip("=").strip(" ")
        print(level, content)
print("\n")

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ

for line in uk[0].split("\n"):
    if "ファイル:" in line:
        match = re.search(r'\[\[ファイル:([^\|\]]+)', line)
        if (match):
            print(match.group(1))

print("\n")

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出せし、辞書オブジェクトとして格納せよ

dict = {}
for line in uk[0].split("\n"):
    match = re.search("\|(.+?)\s=\s(.+)", line)
    if (match):
        dict[match.group(1)] = match.group(2)

print(dict)

# 26. 強調マークアップの除去
# 25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調のすべて）を除去してテキストに変換せよ
## ''他との区別'' // 弱い強調
## '''強調'''     // 強調
## ''''斜体と強調'''' // 強い強調

for key,value in dict.items():
    if "\'" in value:
        dict[key] = value.replace("'", "")

print(dict)

# 27. 内部リンクの除去
# 26の処理に加えて、テンプレートの値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ

## [[記事名]]
## [[記事名|表示文字]]
## [[記事名#節名|表示文字]]

for key,value in dict.items():
    match = re.search(r'\[\[(.+?)\]\]', value)
    if (match):
        if "|" in match.group(1):
            dict[key] = match.group(1).split("|")[1]
        else:
            dict[key] = match.group(1)


print(dict)

# 28. MediaWikiマークアップの除去
# 27の処理に加えて、テンプレートの値からMediaWikiマークアップを可能な限り除去し、国の基本情報を整形せよ

# 27で対応した

# 29. 国旗画像のURLを取得せよ
# テンプレートの内容を利用し、国旗画像のURLを取得せよ

print("\n")

import requests

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File: " + dict["国旗画像"],
    "iiprop": "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])
