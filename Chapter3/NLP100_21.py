'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''

import NLP100_20
import re

data = NLP100_20.load()
p = re.compile(r'^(.*\[\[Category.*\]\])$', re.MULTILINE)

for l in p.findall(data):
    print(l)