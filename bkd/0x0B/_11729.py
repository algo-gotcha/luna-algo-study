import sys


n = int(sys.stdin.readline())

def solution(a, b, n):
    if n == 1:
        print(f"{a} {b}")
        return
    solution(a, 6 - a - b, n - 1)
    print(f"{a} {b}")
    solution(6 - a - b, b, n - 1)
    
print(2 ** n - 1)
solution(1, 3, n)