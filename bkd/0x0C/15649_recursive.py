import sys

n, m = map(int, sys.stdin.readline().split())

nums = [0 for _ in range(m)]
is_used = [False for _ in range(10)]

def func(k):
    if k == m:
        print(*nums)
        return
    for i in range(1, n + 1):
        if not is_used[i]:
            nums[k] = i
            is_used[i] = True
            func(k + 1)
            is_used[i] = False

func(0)
