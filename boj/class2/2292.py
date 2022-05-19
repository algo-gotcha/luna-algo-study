number = int(input())

def solution(number):
	n = 1
	while True:
		if number == 1:
			return 1
		if number <= 3 * n * (n + 1) + 1:
			return n + 1
		n += 1

print(solution(number))