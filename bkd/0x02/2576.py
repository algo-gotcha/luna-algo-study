sum_odd = 0
min_num = 100
for _ in range(7):
	number = int(input())
	if number % 2 == 1:
		sum_odd += number
		if number < min_num:
			min_num = number

if sum_odd == 0:
	print(-1)
else:
	print(sum_odd)
	print(min_num)