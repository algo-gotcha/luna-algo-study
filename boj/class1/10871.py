limit, max_num = map(int, input().split())

numbers = list(map(int, input().split()))

result = ''
for number in numbers:
	if number < max_num:
		result += f"{number} "

print(result)