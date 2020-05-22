'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''

import NLP100_20
import re

data = NLP100_20.load()

p = re.compile(r'ファイル:(.+?)(?:\||\])')

for l in p.findall(data):
    print(l)