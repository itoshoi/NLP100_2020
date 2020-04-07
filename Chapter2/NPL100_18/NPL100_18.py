import sys

path = sys.argv[1]

with open(path) as f:
    print(''.join(sorted(f.readlines(), key=lambda l:l.split('\t')[2], reverse=True)))