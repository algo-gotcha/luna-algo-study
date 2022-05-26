import sys
from collections import deque

MAX = 10 ** 5
N, K = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(MAX + 1)]
q = deque()
q.append(N)
visited[N] = 1
count = 0
while q:
    x = q.popleft()
    if x == K:
        print(visited[x] - 1)
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and not visited[nx]:
            q.append(nx)
            visited[nx] = visited[x] + 1
