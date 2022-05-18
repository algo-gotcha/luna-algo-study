number = input()

place = len(number)

number = int(number)


if number > place * 9:
	min_num = number -  place * 9
else:
	min_num = 1

def solution(number):
	for num in range(min_num, number):
		answer = num
		result = num
		while num > 0:
			result += num % 10
			num //= 10
		if result == number:
			return answer
	return 0

print(solution(number))