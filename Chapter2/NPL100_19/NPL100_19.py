'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''

import sys

path = sys.argv[1]

dict = {}
with open(path) as f:
    for l in f:
        key = l.split('\t')[0]
        dict[key] = dict.get(key, 0) + 1

for key, value in sorted(dict.items(), key=lambda kv: kv[1], reverse=True):
    print(str(value) + ' ' + str(key))