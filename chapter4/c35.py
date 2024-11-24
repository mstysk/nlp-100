# 35. 単語の出現頻度
## 文章中の出現する単語とその出現頻度を求め、出現頻度の高い順に並べ

from utils import getSentences

sentences = getSentences()
text_d = {}

for sentence in sentences:
    text = sentence["surface"]
    if (text == ""):
        continue
    if (text in text_d):
        text_d[text] += 1
    else:
        text_d[text] = 1

print(sorted(text_d.items(), key=lambda x: x[1], reverse=True))

