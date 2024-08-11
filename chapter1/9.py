#  Typoglycemia
# スペースで区切られた単語に対して、各単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並べ替えるプログラムを作成せよ。ただし、長さが４以下の単語は並び替えない事とする。適当な英語の文(例えば、
#"I couldn't believe that I could actually understand what I was reading: the phenomenal power of the human mind."
# を与え、その実行結果を確認せよ. 

import random

s = "I couldn't believe that I could actually understand what I was reading: the phenomenal power of the human mind."

def typoglycemia(s):
    words = s.split(" ")
    l = []
    for word in words:
        if len(word) <= 4:
            l.append(word)
            continue
        else:
            r = list(word[1:-1])
            random.shuffle(r)
            l.append(
                word[0] + "".join(r) + word[-1]
            )   
    return " ".join(l)

print(typoglycemia(s))
