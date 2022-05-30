from collections import deque
import sys

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(visited, start, end, building):
    q = deque()
    q.append(start)
    x, y, z = start
    visited[z][y][x] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if visited[nz][ny][nx] == 0 and building[nz][ny][nx] in ['.', 'E']:
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    if nx == end[0] and ny == end[1] and nz == end[2]:
                        return f"Escaped in {visited[z][y][x]} minute(s)."
                    q.append((nx, ny, nz))
    return "Trapped!"


while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0:
        break

    # make building
    building = []
    for _ in range(L):
        b = []
        for _ in range(R + 1):
            input_line = sys.stdin.readline().rstrip()
            if input_line == '':
                continue
            b.append(list(input_line))
        building.append(b)

    # make visited
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    
    # find start and end
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == 'S':
                    start = (x, y, z)
                elif building[z][y][x] == 'E':
                    end = (x, y, z)

    # bfs
    print(bfs(visited, start, end, building))