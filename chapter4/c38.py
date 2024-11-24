from utils import getSentences
import matplotlib.pyplot as plt
import japanize_matplotlib

# 38. ヒストグラム
# 単語の出現頻度のヒストグラムを描け、ただし、横軸は出現頻度を表し、１から単語の出現頻度の最大値までの線形目盛りとする。
# 縦軸はx軸で示される出現頻度となった単語の異なる（種類数)である

sentences = getSentences()

text_d = {}

# 出現頻度
# 単語: 出現回数
for sentence in sentences:
    text = sentence["surface"]
    if (text == ""):
        continue
    if (text in text_d):
        text_d[text] += 1
    else:
        text_d[text] = 1

## x 軸で示される出現頻度
## y 軸で示される単語の種類数

frequency_counts = {}

for word, freq in text_d.items():
    if freq in frequency_counts:
        frequency_counts[freq] += 1
    else:
        frequency_counts[freq] = 1

x = list(frequency_counts.keys())
y = list(frequency_counts.values())

plt.figure(figsize=(10, 6))
plt.bar(x, y)
plt.xlabel("出現頻度")
plt.ylabel("単語の種類数")
plt.grid(axis='y')
plt.xlim(0,10)
plt.show()
