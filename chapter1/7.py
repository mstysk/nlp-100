# テンプレートによう文生成
# 引数x,yを受け取り「x時のyは」という文字列を返す関数を実装せよ.さらに,x=12,y="気温", z=22.4として,実行結果を確認せよ.

def template(x,y,z):
    return "{x}時の{y}は{z}".format(x=x, y=y, z=z)

print(template(12, "気温", 22.4))
