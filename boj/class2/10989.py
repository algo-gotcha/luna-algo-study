import sys
from collections import deque

loop = int(sys.stdin.readline())

MAX = 10 ** 4
hash = [0 for _ in range(MAX + 1)]
for _ in range(loop):
    hash[int(sys.stdin.readline())] += 1

for i in range(1, MAX + 1):
    if hash[i] != 0:
        for _ in range(hash[i]):
            print(i)

# pypy로 하면 통과가 안되는데 python3으로 하면 통과가 됨
