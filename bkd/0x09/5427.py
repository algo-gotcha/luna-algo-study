from collections import deque
import sys

loop = int(sys.stdin.readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def fire_bfs(q, visited, building):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if visited[ny][nx] == 0 and building[ny][nx] != '#':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

def bfs(q, visited, building):
    while q:
        x, y = q.popleft()
        if x == 0 or x == w - 1 or y == 0 or y == h - 1:
            return visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if visited[ny][nx] == 0 and building[ny][nx] == '.' and (fire_visited[ny][nx] == 0 or visited[y][x] + 1 < fire_visited[ny][nx]):
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))
    return "IMPOSSIBLE"


for _ in range(loop):
    w, h = map(int, sys.stdin.readline().split())
    building = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    fire_visited = [[0 for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    fire_q, q = deque(), deque()

    for y in range(h):
        for x in range(w):
            if building[y][x] == '*':
                fire_q.append((x, y))
                fire_visited[y][x] = 1
            elif building[y][x] == '@':
                q.append((x, y))
                visited[y][x] = 1
            
    fire_bfs(fire_q, fire_visited, building)
    print(bfs(q, visited, building))


