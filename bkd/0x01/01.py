def solution(n):
	result = 0
	for number in range(n + 1):
		if number % 3 == 0 or number % 5 == 0:
			result += number
	return result

print(solution(16) == 60)
print(solution(34567) == 278812814)
print(solution(27639) == 178254968)