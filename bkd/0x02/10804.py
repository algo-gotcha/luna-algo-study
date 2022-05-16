ranges = [tuple(map(int, input().split())) for _ in range(1)]

cards = [i for i in range(1, 21)]

result = cards[:]
for idx in ranges:
	if idx[0] != idx[1]:
		result = result[:idx[0]-1] + result[idx[0]-1:idx[1]] + result[idx[1]:]

for number in result:
	print(number, end=' ')


