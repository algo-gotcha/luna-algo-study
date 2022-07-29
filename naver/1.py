def solution(N):
    largest = 0
    shift = 0
    temp = N
    largest = N
    for i in range(1, 30):
        index = (temp & 1)
        temp = (temp >> 1) | (index << 29)
        if (temp > largest):
            largest = temp
            shift = i
    return shift

print(solution(9736) == 11)
print(solution(1) == 1)
print(solution(2) == 2)
print(solution(8) == 4)
print(solution(4) == 3)
print(solution(5) == 3)
print(solution(9) == 4)
print(solution(809500676) == 0)
print(solution(4868) == 10)
print(solution(2434) == 9)
print(solution(1217) == 8)
print(solution(268435760) == 6)