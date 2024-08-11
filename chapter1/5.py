# n-gram
# 与えられたシーケンス（文字列やリストなど)からn-gram を作る関数を作成せよ、この関数を用い、"I am an NLPer" という文から単語bi-gram, 文字bi-gramを得よ

# 単語bi-gram
#  連続するn個の単語のまとまり

# 文字列bi-gram
#  連続するn個の文字のまとまり

# n = 1 (uni-gram)
# n = 2 (bi-gram)
# n = 3 (tri-gram)

s = "I am an NLPer"

def ngram(s,n):
    r = []
    for i in range(len(s)-n+1):
        r.append(s[i:i+n])
    return r

print(ngram(s.split(), 2))
print(ngram(s, 2))
