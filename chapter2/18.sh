#!/bin/sh
#
#拡張を３コラム目の数値の降順にソート
#
#各行を３コラム目の数値の逆順で整列せよ（注意：各行の内容は変更せずに並び替えよ）
#確認にはsortコマンドを用いよ(（この問題はコマンドで実行した時の結果とあわなくてもよい ）
#
cat popular-names.txt | sort -k 3r
