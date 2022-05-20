import sys
from collections import deque

count = int(sys.stdin.readline())
for _ in range(count):
    string = deque(sys.stdin.readline().rstrip())
    front = deque()
    back = deque()
    for char in string:
        if char == '<':
            if len(front) > 0:
                back.appendleft(front.pop())
        elif char == '>':
            if len(back) > 0:
                front.append(back.popleft())
        elif char == '-':
            if len(front) > 0:
                front.pop()
        else:
            front.append(char)

    print(''.join(front + back))
