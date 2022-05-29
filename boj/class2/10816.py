from collections import deque
import sys

N = int(sys.stdin.readline())
cards = deque(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
ns = deque(map(int, sys.stdin.readline().split()))

pockets = {}
for c in cards:
    if pockets.get(c, 0):
        pockets[c] += 1
    else:
        pockets[c] = 1

for n in ns:
    print(pockets.get(n, 0), end=' ')
