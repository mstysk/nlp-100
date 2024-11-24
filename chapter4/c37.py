from utils import getSentences
import matplotlib.pyplot as plt
import japanize_matplotlib

# 37 「猫」と共起頻度の高い上位10語
## 「猫」とよく共起する110語とその出現頻度をグラフで表示せよ

sentences = getSentences()

text_d = {}

for sentence in sentences:
    if "猫" in sentence["base"]:
        if (sentence["surface"] not in text_d):
            text_d[sentence["surface"]] = 1
        else:
            text_d[sentence["surface"]] += 1

list = sorted(text_d.items(), key=lambda x: x[1], reverse=True)[:10]

plt.bar([k for k, v in list], [v for k, v in list])
plt.show()
