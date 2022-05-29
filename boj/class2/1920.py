import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
src = list(map(int, sys.stdin.readline().split()))

hash = {i: 1 for i in dist}

for s in src:
    if hash.get(s, 0):
        print(1)
    else:
        print(0)
