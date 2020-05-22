'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''

import sys

path = sys.argv[1]

with open(path) as f:
    print(''.join(sorted(f.readlines(), key=lambda l:int(l.split('\t')[2]), reverse=True)))