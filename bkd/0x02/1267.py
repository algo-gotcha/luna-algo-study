count = int(input())
call_times = list(map(int, input().split()))

def get_Y(call_times):
	charge = 0
	for call_time in call_times:
		if call_time > 0:
			charge += (call_time // 30 + 1) * 10
	return charge

def get_M(call_times):
	charge = 0
	for call_time in call_times:
		if call_time > 0:
			charge += (call_time // 60 + 1) * 15
	return charge

Y = get_Y(call_times)
M = get_M(call_times)

if M == Y:
	print(f"Y M {Y}")
elif M < Y:
	print(f"M {M}")
else:
	print(f"Y {Y}")

