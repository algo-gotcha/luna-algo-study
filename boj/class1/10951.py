results = []

while True:
	try:
		a, b = map(int, input().split())
		if a == 0 and b == 0:
			break
		results.append(a + b)
	except:
		break

for result in results:
	print(result)