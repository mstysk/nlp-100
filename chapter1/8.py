# 暗号文
# 与えられた文字列の各文字を、以下の仕様で変換するcipher を実装せよ

# - 英小文字ならば (219 - 文字コード) の文字に変換
# - その他の文字はそのまま出力
# - この暗号文を英語のメッセージとして解読せよ.

def cipher(s):
    r = ""
    for c in s:
        if c.islower():
            r += chr(219 - ord(c))
        else:
            r += c
    return r

s = 'I like cryptography.'
c = cipher(s)
d = cipher(c)
print(s)
print(c)
print(d)

