import sys

path = sys.argv[1]

dict = {}
with open(path) as f:
    for l in f:
        key = l.split('\t')[0]
        dict[key] = dict.get(key, 0) + 1

for key, value in sorted(dict.items(), key=lambda kv: kv[1], reverse=True):
    print(str(value) + ' ' + str(key))