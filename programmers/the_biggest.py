def solution(numbers):
	if sum(numbers) == 0:
		return '0'
	numbers = list(map(str, numbers))
	numbers.sort(key = lambda x: x * 3, reverse = True)
	return ''.join(numbers)

print(solution([6, 10, 2]) == "6210")
print(solution([3, 30, 34, 5, 9]) == "9534330")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210")
print(solution([0, 0, 0, 0]) == "0")
print(solution([0, 1, 0, 0]) == "1000")
