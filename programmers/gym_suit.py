def solution(n, lost, reserve):
    set_r = set(reserve)
    set_l = set(lost)
    r_set = set_r - set_l
    l_set = set_l - set_r

    for i in r_set:
        if i - 1 in l_set:
            l_set.remove(i - 1)
        elif i + 1 in l_set:
            l_set.remove(i + 1)
    return n - len(l_set)

print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(3, [3], [1]) == 2)