numbers = list(map(int, input().split()))

unique_number = 0
for number in numbers:
	unique_number += number ** 2

print(unique_number % 10)