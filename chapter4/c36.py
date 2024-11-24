from utils import getSentences
import matplotlib.pyplot as plt
import japanize_matplotlib

# 35 頻度上位10語
## 出現頻度が高い10語とその出現頻度をグラフで表示せよ
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

list = sorted(text_d.items(), key=lambda x: x[1], reverse=True)[:10]

plt.bar([k for k, v in list], [v for k, v in list])
plt.show()
