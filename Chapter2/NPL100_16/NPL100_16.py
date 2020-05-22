'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''

import sys

path = sys.argv[1]
N = int(input('N = '))

# n分割目のファイルの行の始まりを計算
def linestart(lines, n):
    # n分割目 * 1ファイル当たりの行数 + 端数
    return n * int(len(lines) / N) + min(len(lines) % N, n)


with open(path) as f:
    lines = f.readlines()
    for n in range(N):
        with open('output' + str(n), 'w') as w:
            w.write(''.join(lines[linestart(lines, n): linestart(lines, n + 1)]))