import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())

tomato_map = []
for _ in range(h):
    tomato_map.append(list(map(int, sys.stdin.readline().split())))

q = deque()
for y in range(h):
    for x in range(w):
        if tomato_map[y][x] == 1:
            q.append((x, y))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < h and 0 <= nx < w and tomato_map[ny][nx] == 0:
            tomato_map[ny][nx] = tomato_map[y][x] + 1
            q.append((nx, ny))


def get_result(tomato_map):
    res = 0
    for tomato_line in tomato_map:
        if 0 in tomato_line:
            return -1
        res = max(res, max(tomato_line) - 1)
    return res


print(get_result(tomato_map))
