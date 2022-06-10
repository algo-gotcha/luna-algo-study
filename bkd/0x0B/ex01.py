def solution(n):
    if n == 1:
        print(1)
        return
    solution(n - 1)
    print(n)

solution(10)

def solution_sum(n):
    if n == 1:
        return 1
    return solution_sum(n - 1) + n

print(solution_sum(10))