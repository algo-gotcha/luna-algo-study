count = int(input())

for _ in range(count):
	numbers, s = input().split()

	numbers = int(numbers)	
	len_s = len(s)

	result = ''
	for i in range(len_s * numbers):
		result += s[i // numbers]

	print(result)