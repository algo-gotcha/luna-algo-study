import sys

count = int(sys.stdin.readline().rstrip())
for _ in range(count):
	a, b = sys.stdin.readline().rstrip().split()
	print(int(a) + int(b))