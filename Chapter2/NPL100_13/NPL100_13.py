'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''

import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

with open(path1) as f1, \
        open(path2) as f2, \
        open('merged.txt', 'w') as fw:
    for l1 in f1:
        fw.write(l1.rstrip('\n') + '\t' + f2.readline())
