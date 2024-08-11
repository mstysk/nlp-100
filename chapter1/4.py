# 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorne. New Nations Might Also Sign Pease Security Clause. Arthur King Can". 
# とういう文を単語に分解し、1,5,6,7,8,9,15,19番目の単語は先頭の１文字、それ以外の単語は先頭の２文字を取り出し、取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ

s = "Hi He Lied Because Boron Could Not Oxidize Fluorne. New Nations Might Also Sign Pease Security Clause. Arthur King Can"

i = 1;
for w in s.split(" "):
    if (i == 1 
        or i == 5
        or i == 6
        or i == 7
        or i == 8
        or i == 9
        or i == 15
        or i == 19
        ):
        print(w[0])
    else:
        print(w[0:2])
    i += 1
