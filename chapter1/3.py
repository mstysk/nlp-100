# 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"  という文字を単語に分解し、各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ


s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

for w in s.replace(",", "").split(" "):
    print(len(w))
