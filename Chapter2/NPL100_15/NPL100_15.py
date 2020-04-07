import sys

path = sys.argv[1]
N = int(input('N = '))

with open(path) as f:
    lines = f.readlines()
    print(''.join(lines[-N:]), end='')