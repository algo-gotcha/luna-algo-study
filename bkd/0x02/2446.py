stars = int(input())

for star in range(stars):
	print(f"{' ' * star}*{'*' * (stars - (star + 1)) * 2}")
for star in range(1, stars):
	print(f"{' ' * (stars - (star + 1))}*{'*' * star * 2}")
