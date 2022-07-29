import sys

def get_sabun(n, r, c):
    medium = 2 ** (n - 1)
    if r < medium and c < medium:
        return 1
    if r < medium and c >= medium:
        return 2
    if r >= medium and c < medium:
        return 3
    if r >= medium and c >= medium:
        return 4

def solution(n, r, c, start):
    if n == 1:
        if r == 0 and c == 0:
            return start
        elif r == 0 and c == 1:
            return start + 1
        elif r == 1 and c == 0:
            return start + 2
        elif r == 1 and c == 1:
            return start + 3
    sabun = get_sabun(n, r, c)
    medium = 2 ** (n - 1)
    start += ((medium ** 2) * (sabun - 1))
    medium = medium
    if sabun == 2:
        c = c - medium
    elif sabun == 3:
        r = r - medium
    elif sabun == 4:
        r = r - medium
        c = c - medium
    return solution(n - 1, r, c, start)

n, r, c = map(int, sys.stdin.readline().split())
print(solution(n, r, c, 0))