'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''

import sys

filepath = sys.argv[1]
with open(filepath) as f:
    print(len(f.readlines()))

# UNIX COMMAND
# wc -l hightemp.txt