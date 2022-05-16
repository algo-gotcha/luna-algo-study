stars = int(input())

for star in range(stars):
	print(f'{" " * star}{"*" * (stars - star)}')