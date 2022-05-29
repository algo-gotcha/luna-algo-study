import sys
m, n = map(int, sys.stdin.readline().split())


def is_sosu(n):
    if n == 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
    return True


results = []
for i in range(m, n + 1):
    if is_sosu(i):
        results.append(i)

for i in results:
    print(i)
