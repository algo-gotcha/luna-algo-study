import sys

n = int(sys.stdin.readline())

result = 1
for i in range(1, n + 1):
    result *= i

result = str(result)[::-1]

count = 0
for r in result:
    if r == '0':
        count += 1
    else:
        break

print(count)