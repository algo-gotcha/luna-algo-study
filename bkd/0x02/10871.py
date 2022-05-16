count, max_number = map(int, input().split())

numbers = map(int, input().split())

for number in numbers:
	if number < max_number:
		print(number, end=' ')