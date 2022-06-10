import sys

n, m = map(int, sys.stdin.readline().split())

from itertools import permutations

nums = [i for i in range(1, n+1)]
results = permutations(nums, m)
for result in results:
    print(*result)