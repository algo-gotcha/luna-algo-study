import sys

loop, gap = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

for i, _ in enumerate(numbers):
	start_index = i - gap + 1
	if start_index < 0:
		start_index = 0
	
	print(min(numbers[start_index:i+1]), end=' ')


