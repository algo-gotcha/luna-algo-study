import sys
from collections import deque

loop = int(sys.stdin.readline())

front = deque()
front.append(0)
back = deque()
back.appendleft(10000001)
for _ in range(loop):
    number = int(sys.stdin.readline())
    if number < front[-1]:
        while front and number < front[-1]:
            back.appendleft(front.pop())
    if back[0] >= number >= front[-1]:
        front.append(number)
        continue
    if number > back[0]:
        while back and number > back[0]:
            front.append(back.popleft())
    if number <= back[0]:
        back.appendleft(number)
        continue

front.popleft()
back.pop()
print()
for f in front:
    print(f)
for b in back:
    print(b)
