from collections import deque
import sys


n, loop, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(loop):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for line in graph:
    line.sort()

q = deque()
q.append(start)
visited[start] = 1
count = 0
results = [0 for _ in range(n + 1)]
while q:
    x = q.popleft()
    count += 1
    results[x] = count
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)


for result in results[1:]:
    print(result)
