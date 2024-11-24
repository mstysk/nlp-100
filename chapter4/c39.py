from utils import getSentences

# Zipf の法則
## 単語の出現頻度順位を横実、その出現頻度を縦実として、両対数グラフをプロットせよ

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

list = sorted(text_d.items(), key=lambda x: x[1], reverse=True)

x = [i + 1 for i in range(len(list))]
y = [v for k, v in list]

import matplotlib.pyplot as plt
import japanize_matplotlib

plt.xscale("log")
plt.yscale("log")
plt.plot(x, y)
plt.show()
