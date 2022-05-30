from collections import deque
import sys


M, N, K = map(int, sys.stdin.readline().split())

square = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            square[y][x] += 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(q, square, x, y):
    q.append((x, y))
    square[y][x] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if square[ny][nx] == 0:
                    square[ny][nx] = 1
                    count += 1
                    q.append((nx, ny))
    return count

count = 0
results = []
for y in range(M):
    for x in range(N):
        if square[y][x] == 0:
            q = deque()
            results.append(bfs(q, square, x, y))
            count += 1

print(count)
print(*sorted(results))