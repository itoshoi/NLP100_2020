'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
'''

import sys

path = sys.argv[1]

with open(path) as f:
    s = set()
    for l in f:
        s.add(l.split('\t')[0])

    for e in s:
        print(e)