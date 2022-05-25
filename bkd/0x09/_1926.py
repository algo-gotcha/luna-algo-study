import sys
from collections import deque

height, weight = map(int, sys.stdin.readline().split())

dohwaji = []
visited = []

for _ in range(height):
	dohwaji.append(list(map(int, sys.stdin.readline().split())))
	visited.append([0 for _ in range(weight)])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs(q, start, visited):
	q.append(start)
	visited[start[1]][start[0]] = 1
	prev = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= ny < height and 0 <= nx < weight:
				if not visited[ny][nx] and dohwaji[ny][nx] == 1:
					q.append((nx, ny))
					prev += 1
					visited[ny][nx] = prev
	return prev

count = 0
max_num = 0
for y in range(height):
	for x in range(weight):
		if visited[y][x] == 0 and dohwaji[y][x] == 1:
			result = bfs(q, (x, y), visited)
			if max_num < result:
				max_num = result
			count += 1

print(count)
print(max_num)

