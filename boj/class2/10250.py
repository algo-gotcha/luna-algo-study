count = int(input())

informations = [list(map(int, input().split())) for _ in range(count)]


for floor, rooms, guest in informations:
	real_floor = guest % floor
	if real_floor == 0:
		real_floor = floor
	count = 0
	while guest > 0:
		guest -= floor
		count += 1
	
	if (len(str(count)) == 1):
		print(f"{real_floor}0{count}")
	else:
		print(f"{real_floor}{count}")
	
	
	
