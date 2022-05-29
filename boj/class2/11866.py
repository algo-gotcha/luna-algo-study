from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

q = deque([i for i in range(1, N + 1)])

print("<", end="")
while q:
    for i in range(K - 1):
        q.append(q.popleft())
    print(q.popleft(), end="")
    if q:
        print(", ", end="")
print(">")
