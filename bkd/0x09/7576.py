import sys
from collections import deque

weight, height = map(int, sys.stdin.readline().split())

box = []
for _ in range(height):
	box.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = deque()
for y in range(height):
	for x in range(weight):
		if box[y][x] == 1:
			pos.append((x, y))

q = deque()

def bfs(q):
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= ny < height and 0 <= nx < weight and box[ny][nx] == 0:
				box[ny][nx] = box[y][x] + 1
				q.append((nx, ny))


min_num = 0
bfs(pos)

def get_result(box):
	res = 0
	for b in box:
		for i in b:
			if i == 0:
				return -1
		res = max(res, max(b) - 1)
	return res

print(get_result(box))
	
