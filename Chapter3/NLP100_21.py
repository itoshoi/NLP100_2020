import NLP100_20
import re

data = NLP100_20.load()
p = re.compile(r'^(.*\[\[Category.*\]\])$', re.MULTILINE)

for l in p.findall(data):
    print(l)