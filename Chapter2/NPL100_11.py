import sys

path = sys.argv[1]
with open(path) as f:
    print(f.read().replace('\t', ' '))

# UNIX COMMAND
# sed 's/\t/ /g'