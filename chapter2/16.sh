#!/bin/sh
#
# ファイルをＮ分割する
#
# 自然数Ｎをコマンドライン引数などの手段でうけとり、入力ふぁいるを行単位でＮ分割せよ、同様の処理をsplitコマンドで実現せよ
#

split -l $1 --additional-suffix=.txt popular-names.txt 
