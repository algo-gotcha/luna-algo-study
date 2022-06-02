from collections import deque
import sys

count = int(sys.stdin.readline())
loop = int(sys.stdin.readline())

computers = [[] for _ in range(count + 1)]
visited = [0 for _ in range(count + 1)]

for _ in range(loop):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    computers[x].append(y)
    computers[y].append(x)

q = deque()
q.append(1)
visited[1] = 1
count = 0
while q:
    x = q.popleft()
    for i in computers[x]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)
            count += 1

print(count)




