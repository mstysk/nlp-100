from utils import getSentences

# 34 名詞の連接
## 名詞の連接(連続して出現する名詞 ） を最長一致で抽出せよ

sentences = getSentences()
text_d = {}
text = ""
for sentence in sentences:
    if sentence["pos"] == "名詞":
        text += sentence["surface"]
    else:
        text_d[text] = len(text)
        text = ""

print([k for k, v in text_d.items() if v == max(text_d.values())])
