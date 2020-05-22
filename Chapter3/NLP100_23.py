'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
'''

import NLP100_20
import re

data = NLP100_20.load()

p = re.compile(r'^(=+)\s*(.*?)\s*\1$', re.MULTILINE)

for found in p.findall(data):
    level = len(found[0]) - 1
    print('{indent}{section}({level})'.format(indent='\t' * (level - 1), section=found[1], level=level))