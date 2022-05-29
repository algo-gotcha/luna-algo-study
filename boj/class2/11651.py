import sys
from collections import deque

loop = int(sys.stdin.readline())

q = deque()
for _ in range(loop):
    x, y = map(int, sys.stdin.readline().split())
    q.append((x, y))

sorted_q = sorted(q, key=lambda x: (x[1], x[0]))

for p in sorted_q:
    print(p[0], p[1])
