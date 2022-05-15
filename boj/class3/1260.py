from collections import deque


n, m, v = numbers = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
	key, value = map(int, input().split())
	graph[key].append(value)
	graph[value].append(key)

for g in graph:
	g.sort()

def dfs(graph, start, visited):
	visited[start] = True
	print(start, end=' ')
	for i in graph[start]:
		if not visited[i]:
			dfs(graph, i, visited)

def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

dfs(graph, v, [False] * (n + 1))
print()
bfs(graph, v, [False] * (n + 1))
print()
#print(graph)