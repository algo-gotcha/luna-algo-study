import sys


max_num, count = map(int, sys.stdin.readline().split())

numbers = [num for num in range(1, max_num + 1)]

results = map(int, sys.stdin.readline().split())

count = 0
index = 0
for re in results:
	re_index = numbers.index(re)
	if re_index != index:
		move_right = abs(re_index - index)
		move_left = len(numbers) - abs(re_index - index)
		if move_left < move_right:
			count += move_left
			index -= move_left
			if index < 0:
				index += len(numbers)
		else:
			count += move_right
			index += move_right
			if index >= len(numbers):
				index -= len(numbers)
	numbers.pop(re_index)
	index = re_index			

print(count)


