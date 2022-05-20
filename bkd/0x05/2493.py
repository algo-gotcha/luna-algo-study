import sys
from collections import deque

count = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

hash = deque()
hash.append((100000001, 0))

for i, number in enumerate(numbers):
    while hash[-1][0] < number:
        hash.pop()
    print(hash[-1][1], end=' ')
    hash.append((number, i + 1))

