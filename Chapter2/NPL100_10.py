import sys

filepath = sys.argv[1]
with open(filepath) as f:
    print(len(f.readlines()))

# UNIX COMMAND
# wc -l hightemp.txt