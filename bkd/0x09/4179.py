import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline().strip()) for _ in range(h)]

info = {}


def init_info(maze, w, h, info):
    for y in range(h):
        for x in range(w):
            if maze[y][x] == 'J':
                info['J'] = (x, y)
            elif maze[y][x] == 'F':
                info['F'] = (x, y)
    return info


info = init_info(maze, w, h, info)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


q = deque()
q.append(('F', info['F']))
q.append(('J', info['J']))
count = 0
while q:
    k, pos = q.popleft()
    x, y = pos
    if k == 'J' and (x == 0 or x >= w - 1 or y == 0 or y >= h - 1):
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if k == 'J':
                if maze[ny][nx] == '.':
                    maze[ny][nx] = 'J'
                    if ny == h - 1 or nx == w - 1:
                        break
                    q.append((k, (nx, ny)))
            elif k == 'F':
                if maze[ny][nx] == '.' or maze[ny][nx] == 'J':
                    maze[ny][nx] = 'F'
                    q.append((k, (nx, ny)))
    # if k == 'J':
    #     count += 1
        init_info['result'] = (nx, ny)
        print()
        print(f"k: {k}, count : {count}")
        for m in maze:
            print(m)

is_alive = False
for m in maze:
    if 'J' in m:
        is_alive = True
        break
if is_alive:
    print(count + 1)
else:
    print("IMPOSSIBLE")
