from collections import deque
import sys


loop = int(sys.stdin.readline())

people = deque()
for _ in range(loop):
    w, h = map(int, sys.stdin.readline().split())
    people.append((w, h))

rating = deque([] for _ in range(loop))

for i, spec in enumerate(people):
    rank = 1
    for a_spec in people:
        if spec[0] < a_spec[0] and spec[1] < a_spec[1]:
            rank += 1
    print(rank, end=" ")
