import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
q = deque()
count = 0
q.append(N)
visited = [0 for _ in range(MAX + 1)]
while q:
    x = q.popleft()
    if x == K:
        print(visited[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and not visited[nx]:
            visited[nx] = visited[x] + 1
            q.append(nx)
