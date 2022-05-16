stars = int(input())

for star in range(1, stars + 1):
	print(f"{' ' * (stars - star)}{'*' * (star * 2 - 1)}")