import sys

path = sys.argv[1]
with open(path) as f, \
    open('col1.txt', 'w') as c1, \
    open('col2.txt', 'w') as c2:
    for line in f:
        line_sp = line.split('\t')
        c1.write(line_sp[0] + '\n')
        c2.write(line_sp[1] + '\n')