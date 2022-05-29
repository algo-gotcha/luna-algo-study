import sys

K, N = map(int, sys.stdin.readline().split())

lans = [int(sys.stdin.readline().strip()) for _ in range(K)]

start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
