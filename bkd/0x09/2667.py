from collections import deque
import sys


loop = int(sys.stdin.readline())

jido = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(loop)]
visited = [[0 for _ in range(loop)] for _ in range(loop)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(visited, jido, x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = 1
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < loop and 0 <= ny < loop:
                if jido[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                    count += 1
    return count

count = 0
results = []
for y in range(loop):
    for x in range(loop):
        if jido[y][x] == 1 and visited[y][x] == 0:
            count += 1
            results.append(bfs(visited, jido, x, y))

print(count)
results = sorted(results)
for result in results:
    print(result)
