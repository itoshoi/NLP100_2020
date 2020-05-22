'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ
'''

import sys

path = sys.argv[1]
with open(path) as f, \
    open('col1.txt', 'w') as c1, \
    open('col2.txt', 'w') as c2:
    for line in f:
        line_sp = line.split('\t')
        c1.write(line_sp[0] + '\n')
        c2.write(line_sp[1] + '\n')