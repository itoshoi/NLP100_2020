'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
'''

import sys

path = sys.argv[1]
N = int(input('N = '))

with open(path) as f:
    lines = f.readlines()
    print(''.join(lines[-N:]), end='')