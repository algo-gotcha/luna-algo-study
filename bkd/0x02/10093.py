numbers = list(map(int, input().split()))

numbers.sort()
if numbers[0] == numbers[1]:
	print(0)
else:
	print(numbers[1] - numbers[0] - 1)
for number in range(numbers[0] + 1, numbers[1]):
	print(number, end=" ")