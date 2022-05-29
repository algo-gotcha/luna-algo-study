from collections import deque
import sys

loop = int(sys.stdin.readline())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(q, visited, dist):
    while q:
        x, y = q.popleft()
        if x == dist[0] and y == dist[1]:
            return visited[y][x] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

for _ in range(loop):
    I = int(sys.stdin.readline())
    src = tuple(map(int, sys.stdin.readline().split()))
    dist = tuple(map(int, sys.stdin.readline().split()))

    visited = [[0 for _ in range(I)] for _ in range(I)]

    q = deque()
    q.append(src)
    visited[src[1]][src[0]] = 1
    print(bfs(q, visited, dist))

                

