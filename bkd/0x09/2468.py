from collections import deque
import sys


loop = int(sys.stdin.readline())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(loop)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(q, area, visited, rain):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < loop and 0 <= ny < loop:
                if visited[ny][nx] == 0 and area[ny][nx] > rain:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
    return 1


max_height = 0
for rain in range(1, 100):
    q = deque()
    count = 0
    visited = [[0] * loop for _ in range(loop)]
    for y in range(loop):
        for x in range(loop):
            if visited[y][x] == 0 and area[y][x] > rain:
                q.append((x, y))
                visited[y][x] = 1
                count += bfs(q, area, visited, rain)

    if max_height < count:
        max_height = count

print(max(1, max_height))

