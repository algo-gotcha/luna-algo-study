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
def bfs(q, visited, dohwaji):
	count = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= ny < height and 0 <= nx < weight:
				if dohwaji[ny][nx] == 1 and visited[ny][nx] == 0:
					q.append((nx, ny))
					count += 1
					visited[ny][nx] = 1
	return count


count = 0
size = 0
for y in range(height):
	for x in range(weight):
		if visited[y][x] == 0 and dohwaji[y][x] == 1:
			count += 1
			q.append((x, y))
			visited[y][x] = 1
			result = bfs(q, visited, dohwaji)
			if size < result:
				size = result

print(count)
print(size)
