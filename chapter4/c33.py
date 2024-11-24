from c30 import getSentences

# 33. 「AのB」
## 2つの名詞が「の」で連結されている名詞句を抽出せよ

sentences = getSentences()

for sentence in sentences:
    if sentence["pos"] == "名詞" and sentence["surface"] == "の":
        print(sentence)
