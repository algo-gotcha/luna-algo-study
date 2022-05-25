import sys


loop = int(sys.stdin.readline())
def solution():
	stack = []
	ps = sys.stdin.readline()
	for p in ps:
		if p == '(':
			stack.append(p)
		elif p == ')':
			if len(stack) <= 0:
				return "NO"
			if stack[-1] != '(':
				return "NO"
			stack.pop()
	return "YES" if len(stack) == 0 else "NO"


for _ in range(loop):
	print(solution())

