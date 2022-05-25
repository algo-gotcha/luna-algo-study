import sys
from collections import deque

def get_numbers(number_string):
	tmp = 0
	numbers = deque()
	if number_string[1] == ']': return numbers
	for number in number_string:
		if number == ',' or number == ']':
			numbers.append(tmp)
			tmp = 0
		if number.isdigit():
			tmp = tmp * 10 + int(number)
	return numbers

loop = int(sys.stdin.readline())

def solution(numbers, functions):
	is_front = True
	if len(numbers) == 0 and 'D' in functions:
		return "error"
	for fn in functions:
		if fn == 'R':
			is_front = not is_front
		elif fn == 'D':
			if len(numbers) > 0:
				if is_front:
					numbers.popleft()
				else:
					numbers.pop()
			else:
				return "error"
	return numbers if is_front else reversed(numbers)


def get_results(r):
	if r == "error":
		return "error"
	else:
		r = ','.join(map(str, r))
	return f"[{r}]"

results = []
for _ in range(loop):
	functions = sys.stdin.readline()
	len_numbers = int(sys.stdin.readline())
	number_string = sys.stdin.readline()
	numbers = get_numbers(number_string)
	results.append(solution(numbers, functions))

for re in results:
	print(get_results(re))

