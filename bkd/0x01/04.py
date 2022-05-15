def solution(n):
	result = 2
	while n:
		if result > n:
			result //= 2
			return result
		result *= 2
	return

print(solution(5) == 4)
print(solution(97615282) == 67108864)
print(solution(1024) == 1024)