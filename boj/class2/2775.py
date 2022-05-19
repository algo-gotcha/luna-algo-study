count = int(input())

for _ in range(count):
	floors = int(input())
	rooms = int(input())
	result = [[1] for i in range(floors + 1)]
	result[0] = [i for i in range(rooms + 1)]
	for floor in range(1, floors + 1):
		for room in range(1, rooms + 1):
			if room == 1:
				result[floor].append(1)
			else:
				result[floor].append(result[floor - 1][room] + result[floor][room - 1])
	print(result[floors][rooms])


#1	5	15	35	...
#1	4	10	20	35	56	...
#1	3	6	10	15	21	28	36	...
#1	2	3	4	5	6	7	8	...





