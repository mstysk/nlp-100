#!/bin/sh
#
#拡張の１コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べる
#
cut -f 1 popular-names.txt | sort | uniq -c | sort -r -n
