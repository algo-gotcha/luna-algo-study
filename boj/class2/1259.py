
while True:
	n = input()
	if n == '0':
		break
	mid = len(n) // 2
	if len(n) % 2 == 0:
		half_front = n[:mid]
		half_back = n[mid:]
	else:
		half_front = n[:mid]
		half_back = n[mid +1:]
	if half_front == half_back[::-1]:
		print("yes")
	else:
		print("no")