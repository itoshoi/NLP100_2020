'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''

import NLP100_20
import re

data = NLP100_20.load()
p = re.compile(r'^.*\[\[Category:(.*?)(?:\|.*)?\]\]$', re.MULTILINE)

for l in p.findall(data):
    print(l)