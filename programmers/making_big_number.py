from collections import deque

def solution(number, k):
	number = deque(number)
	results = []
	for num in number:
		while results and results[-1] < num and k > 0:
			results.pop()
			k -= 1
			if not results or k <= 0:
				break
		results.append(num)
		
	return ''.join(results[:len(number) - k])


print(solution('1924', 2) , '94')
print(solution('1231234', 3) , '3234')
print(solution('4177252841', 4) , '775841')
print(solution('1111', 2), '11')
print(solution('1919', 2), '9')
print(solution('29', 1), '2')
