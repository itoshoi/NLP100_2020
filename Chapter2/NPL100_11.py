'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''

import sys

path = sys.argv[1]
with open(path) as f:
    print(f.read().replace('\t', ' '))

# UNIX COMMAND
# sed 's/\t/ /g'