from collections import deque
import sys


F, S, G, U, D = map(int, sys.stdin.readline().split())

MAX_FLOOR = 1000000
visited = [0 for _ in range(F + 1)]

dx = [U, -D]

def bfs(start, visited):
	q = deque()
	q.append(start)
	visited[start] = 1
	while q:
		x = q.popleft()
		if x == G:
			return visited[x] - 1
		for i in range(2):
			nx = x + dx[i]
			if 1 <= nx <= F and not visited[nx]:
				q.append(nx)
				visited[nx] = visited[x] + 1
	return "use the stairs"

print(bfs(S, visited))



