n = int(input())

def solution(n):
	count = 0
	while n > 0:
		if n % 5 == 0:
			n -= 5
			count += 1
		elif n % 3 == 0:
			n -= 3
			count += 1
		elif n > 5:
			n -= 5
			count += 1
		else:
			return -1
	return count

print(solution(n))

