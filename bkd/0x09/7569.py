from collections import deque
import sys


M, N, H = map(int, sys.stdin.readline().split())

tomatos = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

pos = deque()

# find position of tomato
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 1:
                pos.append((x, y, z))

# bfs
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(q, tomatos):
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H:
                if tomatos[nz][ny][nx] == 0:
                    q.append((nx, ny, nz))
                    tomatos[nz][ny][nx] = tomatos[z][y][x] + 1

bfs(pos, tomatos)

def get_result(tomatos):
    max_tomato = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatos[z][y][x] == 0:
                    return -1
                if max_tomato < tomatos[z][y][x]:
                    max_tomato = tomatos[z][y][x]
    return max_tomato - 1

print(get_result(tomatos))