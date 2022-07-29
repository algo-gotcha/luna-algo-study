def solution(people, tshirts):
    people.sort()
    tshirts.sort()
    count = 0
    while people and tshirts:
        if people[-1] <= tshirts[-1]:
            count += 1
            tshirts.pop()
        people.pop()
    return count

print(solution([2, 3], [1, 2, 3]))
print(solution([1, 2, 3], [1, 1]))