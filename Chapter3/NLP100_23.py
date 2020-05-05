import NLP100_20
import re

data = NLP100_20.load()

r'''
p = re.compile(r'^(==.*==)$', re.MULTILINE)

for l in p.findall(data):
    name = re.findall(r'^=+\s*(.*?)\s*=+$', l)[0]
    eqs = re.findall(r'^(=+).*', l)[0]
    level = len(eqs) - 1
    print('{indent}{section}({level})'.format(indent='\t' * (level - 1), section = name, level = level))
'''

p = re.compile(r'^(=+)\s*(.*?)\s*\1$', re.MULTILINE)

for found in p.findall(data):
    level = len(found[0]) - 1
    print('{indent}{section}({level})'.format(indent='\t' * (level - 1), section=found[1], level=level))