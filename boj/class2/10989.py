import sys
from collections import deque

loop = int(sys.stdin.readline().rstrip())

hash = [0 for i in range(10001)]

for _ in range(loop):
    number = int(sys.stdin.readline().strip())
    hash[number] += 1

for i, count in enumerate(hash):
    for _ in range(count):
        print(i)
