count = int(input())

answers = [input() for _ in range(count)]


for answer in answers:
	i = 0
	count = 0
	for o in answer:
		if o == 'O':
			i += 1
		else:
			i = 0
		count += i
	print(count)