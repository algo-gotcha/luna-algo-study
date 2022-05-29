import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline().strip()) for _ in range(h)]
visited_fire = [[0 for _ in range(w)] for _ in range(h)]
visited_J = [[0 for _ in range(w)] for _ in range(h)]

# find pos of fire and J
pos_J = None
pos_fire = None
fire_q = deque()
J_q = deque()

for y in range(h):
    for x in range(w):
        if maze[y][x] == 'J':
            pos_J = (x, y)
            J_q.append(pos_J)
            visited_J[y][x] = 1

        elif maze[y][x] == 'F':
            pos_fire = (x, y)
            fire_q.append(pos_fire)
            visited_fire[y][x] = 1

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def fire_bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < h and 0 <= nx < w:
                if maze[ny][nx] in ['.', 'J'] and visited_fire[ny][nx] == 0:
                    fire_q.append((nx, ny))
                    visited_fire[ny][nx] = visited_fire[y][x] + 1

fire_bfs()

def J_bfs():
    while J_q:
        x, y = J_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= h or 0 > nx or nx >= w:
                return visited_J[y][x]
            if pos_fire and visited_fire[ny][nx] <= visited_J[y][x] + 1:
                continue
            if maze[ny][nx] in ('.', 'J') and visited_J[ny][nx] == 0:
                J_q.append((nx, ny))
                visited_J[ny][nx] = visited_J[y][x] + 1
                    

result = J_bfs()

if w == 1 and h == 1:
    if maze[0][0] == 'J':
        print(1)
    else:
        print("IMPOSSIBLE")
else:
    print(result) if result else print("IMPOSSIBLE")


