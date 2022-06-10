import sys


n, x, y = map(int, sys.stdin.readline().split())

def solution(n, x, y):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    if x < half and y < half:
        return solution(n - 1, x, y)
    if x < half and y >= half:
        return half * half + solution(n - 1, x, y - half)
    if x >= half and y < half:
        return 2 * half * half + solution(n - 1, x - half, y)
    return 3 * half * half + solution(n - 1, x - half, y - half)

print(solution(n, x, y))