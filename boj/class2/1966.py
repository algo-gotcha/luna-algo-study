from collections import deque
import sys


loop = int(sys.stdin.readline())
for _ in range(loop):
    n, m = map(int, sys.stdin.readline().split())

    docs = deque(map(int, sys.stdin.readline().split()))
    q = deque(0 for _ in range(n))
    q[m] = True
    i = 0
    while q:
        while max(docs) > docs[0]:
            docs.append(docs.popleft())
            q.append(q.popleft())
        if q[0] == True:
            print(i + 1)
            break
        docs.popleft()
        q.popleft()
        i += 1
