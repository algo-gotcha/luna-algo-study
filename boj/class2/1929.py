m, n = map(int, input().split())

result = [i for i in range(m, n + 1)]
for i in range(m, n + 1):
	for j in range(2, m):
		if i % j == 0:
			result.remove(i)
			break

for i in result:
	print(i)