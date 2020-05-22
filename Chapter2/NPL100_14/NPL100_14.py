'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''

import sys

path = sys.argv[1]
N = int(input('N = '))

with open(path) as f:
    for i in range(N):
        print(f.readline(), end='')

with open(path) as f:
    i = 0
    for l in f:
        i += 1
        if N < i:
            break
        else:
            print(l, end='')