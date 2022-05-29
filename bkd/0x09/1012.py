from collections import deque
import sys


loop = int(sys.stdin.readline())


for _ in range(loop):
    M, N, K = map(int, sys.stdin.readline().split())
    pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
    visited = [0 for _ in range(K)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[0 for _ in range(M)] for _ in range(N)]

    ground = [[0 for _ in range(M)] for _ in range(N)]
    for x, y in pos:
        ground[y][x] = 1
    
    def bfs(q, visited, ground):
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if ground[ny][nx] == 1 and visited[ny][nx] == 0:
                        q.append((nx, ny))
                        visited[ny][nx] = 1
    count = 0
    for p in pos:
        x, y = p
        if visited[y][x] == 0:
            q = deque()
            q.append((x, y))
            visited[y][x] = 1
            bfs(q, visited, ground)
            count += 1
    print(count)

