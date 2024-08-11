# 集合
# "paraparaparadise" と "paragraph" に含まれる文字bi-gramの集合を、それぞれ、XとYとして求め、XとＹの和集合、積集合、差集合を求めよ、さらに、'se'というbi-gramがXおよびYに含まれるかどうか調べよ

s1 = "paraparaparadise"
s2 = "paragraph"

def ngram(s,n):
    r = []
    for i in range(len(s)-n+1):
        r.append(s[i:i+n])
    return r

x = set(ngram(s1, 2))
y = set(ngram(s2, 2))

print(x | y)
print(x & y)
print(x - y)
print("se" in x or "se" in y)

