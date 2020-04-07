import sys

path = sys.argv[1]
N = int(input('N = '))

with open(path) as f:
    for i in range(N):
        print(f.readline(), end='')