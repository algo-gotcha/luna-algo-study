from math import sqrt

def solution(n):
	if sqrt(n) == int(sqrt(n)):
		return 1
	return 0

print(solution(17) == 0)
print(solution(9) == 1)
print(solution(693953651) == 0)
print(solution(756580036) == 1)