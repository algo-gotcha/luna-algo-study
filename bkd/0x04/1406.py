import sys
from collections import deque

front = deque(sys.stdin.readline().rstrip())
count = int(sys.stdin.readline())

back = deque()

for _ in range(count):
    command = sys.stdin.readline().rstrip()
    if command[0] == 'P':
        front.append(command[-1])
    elif command[0] == 'B' and len(front) > 0:
        front.pop()
    elif command[0] == 'L' and len(front) > 0:
        back.appendleft(front.pop())
    elif command[0] == 'D' and len(back) > 0:
        front.append(back.popleft())

string = front + back


print()
print()
print(''.join(string))
print()
print()
