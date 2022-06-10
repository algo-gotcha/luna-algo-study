import sys

a, b, c = map(int, sys.stdin.readline().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    value = solution(a, b // 2, c)
    value = value * value % c
    if b % 2 == 0:
        return value
    return value * a % c

print(solution(a, b, c))
