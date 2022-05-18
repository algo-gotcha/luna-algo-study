A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
hash = { num:0 for num in range(10)}
while mul > 0:
	hash[mul % 10] += 1
	mul //= 10

for value in hash.values():
	print(value)