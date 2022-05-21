import sys

count = int(sys.stdin.readline().rstrip())

n = 666
while count > 0:
    if '666' in str(n):
        count -= 1
        n += 1
    else:
        n += 1

print(n - 1)
