import sys
from collections import deque

loop, gap = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

mins = deque()

for i in range(loop):
	while mins and mins[-1] > numbers[i]:
		mins.pop()
	mins.append(numbers[i])
	if i >= gap and mins[0] == numbers[i - gap]:
		mins.popleft()
	print(mins[0], end=' ')


