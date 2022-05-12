results = []

count = int(input())
for _ in range(count):
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
	results.append(a + b)

for result in results:
	print(result)