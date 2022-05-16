def get_yoots(sum_yoots):
	if sum_yoots == 3:
		return "A"
	elif sum_yoots == 2:
		return "B"
	elif sum_yoots == 1:
		return "C"
	elif sum_yoots == 0:
		return "D"
	elif sum_yoots == 4:
		return "E"


for _ in range(3):
	yoots = list(map(int, input().split()))
	sum_yoots = sum(yoots)
	print(get_yoots(sum_yoots), end=" ")