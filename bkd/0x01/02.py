#def solution(arr, n):
#	for i, a in enumerate(arr):
#		for j, b in enumerate(arr):
#			if i != j and a + b == 100:
#				return 1
#	return 0

def solution(arr, n):
	numbers = [100 - n for n in range(101)]
	for a in arr:
		if numbers[a] != 50 and numbers[a] in arr:
			return 1
	return 0

print(solution({1, 52, 48}, 3) == 1)
print(solution({50, 42}, 2) == 0)
print(solution({4, 13, 63, 87}, 4) == 1)
