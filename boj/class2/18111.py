from collections import Counter
import sys


def make_land(height):
	sec = 0
	for key in land:
		if key < height:
			sec += (height - key) * land[key]
		elif key > height:
			sec += (key - height) * 2 * land[key]
	return sec


n, m, inven = map(int, sys.stdin.readline().split())
land = []
for _ in range(n):
	land += map(int, sys.stdin.readline().rstrip().split())

_sum, _len = sum(land), n * m
land = dict(Counter(land))
height, min_sec = 0, sys.maxsize

for i in range(257):
	if _len * i <= _sum + inven:
		sec = make_land(i)
		if sec <= min_sec:
			min_sec = sec
			height = i

print(min_sec, height)