#!/bin/sh
#
# １列目の文字列の異なり
#
# １列目の文字列の種類 （異なる文字列の個数）を求めよ
# 確認にはcut,sort,uniqコマンドを用いよ

cat popular-names.txt | cut -f 1 | sort | uniq | wc -l
