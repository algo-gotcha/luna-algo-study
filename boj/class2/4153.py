from random import triangular

triangles = []

while True:
	input_values = list(map(int, input().split()))
	if sum(input_values) == 0:
		break
	triangles.append(sorted(input_values))



for triangle in triangles:
	# Pythagorean theorem
	a, b, c = triangle
	if a ** 2 + b ** 2 == c ** 2:
		print("right")
	else:
		print("wrong")
	
	