import sys
from collections import deque

loop = int(sys.stdin.readline())

q = deque()

for _ in range(loop):
	command = sys.stdin.readline().split()
	if command[0] == 'push_front':
		q.appendleft(command[1])
	elif command[0] == 'push_back':
		q.append(command[1])
	elif command[0] == 'pop_front':
		print(-1 if len(q) == 0 else q.popleft())
	elif command[0] == 'pop_back':
		print(-1 if len(q) == 0 else q.pop())
	elif command[0] == 'size':
		print(len(q))
	elif command[0] == 'empty':
		print(1 if len(q) == 0 else 0)
	elif command[0] == 'front':
		print(-1 if len(q) == 0 else q[0])
	elif command[0] == 'back':
		print(-1 if len(q) == 0 else q[-1])
	

	



