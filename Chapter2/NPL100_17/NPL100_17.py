import sys

path = sys.argv[1]

with open(path) as f:
    s = set()
    for l in f:
        s.add(l.split('\t')[0])

    for e in s:
        print(e)