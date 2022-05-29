from collections import deque
import sys


loop = int(sys.stdin.readline())

rgb_map = [list(sys.stdin.readline().rstrip()) for _ in range(loop)]
w = len(rgb_map[0])
visited = [[0 for _ in range(w)] for _ in range(loop)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q, visited, rgb_map, color):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < loop:
                if visited[ny][nx] == 0 and rgb_map[ny][nx] == color:
                    visited[ny][nx] = 1
                    q.append((nx, ny))


def get_count_original(rgb_map, visited):
    count = 0
    for color in ['R', 'G', 'B']:
        for y in range(loop):
            for x in range(w):
                if visited[y][x] == 0 and rgb_map[y][x] == color:
                    q = deque()
                    q.append((x, y))
                    visited[y][x] = 1
                    bfs(q, visited, rgb_map, color)
                    count += 1
    return count

def get_count(rgb_map, visited):
    count = 0
    for color in ['R', 'B']:
        for y in range(loop):
            for x in range(w):
                if visited[y][x] == 0 and rgb_map[y][x] == color:
                    q = deque()
                    q.append((x, y))
                    visited[y][x] = 1
                    bfs(q, visited, rgb_map, color)
                    count += 1
    return count

origin = get_count_original(rgb_map, visited)
for y in range(loop):
    for x in range(w):
        if rgb_map[y][x] == 'G':
            rgb_map[y][x] = 'R'
        visited[y][x] = 0
result = get_count(rgb_map, visited)

print(origin, result)



