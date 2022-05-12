numbers = [int(input()) for _ in range(3)]

decimal_nums = [ 0 for _ in range(10)]

mul_num = 1
for number in numbers:
	mul_num *= number

while mul_num > 0:
	mod = mul_num % 10
	decimal_nums[mod] += 1
	mul_num //= 10

for num in decimal_nums:
	print(num)

