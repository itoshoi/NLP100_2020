import sys

path = sys.argv[1]
N = int(input('N = '))

with open(path) as f:
    for i in range(N):
        print(f.readline(), end='')

with open(path) as f:
    i = 0
    for l in f:
        i += 1
        if N < i:
            break
        else:
            print(l, end='')