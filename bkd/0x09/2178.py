import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

maze = [list(map(int, list(sys.stdin.readline().rstrip())))
        for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


q = deque()
result = 0
q.append((0, 0))
visited[0][0] = True
while q:
    if visited[h - 1][w - 1] is True:
        break
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] == 1 and visited[ny][nx] is False:
            maze[ny][nx] = maze[y][x] + 1
            result = maze[ny][nx]
            visited[ny][nx] = True
            q.append((nx, ny))

print(result)
