import sys

A, B, C = map(int, sys.stdin.readline().split())

# answer = A
# for i in range(B):
#     answer = answer * A % C

def solution(A, B, C):
    if B == 1:
        return A % C
    val = solution(A, B // 2, C)
    val = val * val % C
    if B % 2 == 0:
        return val
    return val * A % C

print(solution(A, B, C))





