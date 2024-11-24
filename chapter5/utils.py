import os
import urllib.request
import zipfile

# 第５章: 係り受け解析

# 日本語Wikipediaの「人工知能」に関する記事からテキスト部分を抜き出したファイルがai.ja.zipに収録されている． この文章をCaboChaやKNP等のツールを利用して係り受け解析を行い，その結果をai.ja.txt.parsedというファイルに保存せよ．このファイルを読み込み，以下の問に対応するプログラムを実装せよ．

aiJaUrl = "https://nlp100.github.io/data/ai.ja.zip"# -O ai.ja.zip"

def download():
    if os.path.exists("ai.ja.zip"):
        return
    urllib.request.urlretrieve(aiJaUrl, "ai.ja.zip")

def unzip():
    if os.path.exists("ai.ja.txt"):
        return
    with zipfile.ZipFile("ai.ja.zip", "r") as f:
        f.extractall()

# knp による係り受け解析
def parse():
    if os.path.exists("ai.ja.txt.parsed"):
        return
    os.system("knp ai.ja.txt > ai.ja.txt.parsed")

download()
unzip()
parse()
