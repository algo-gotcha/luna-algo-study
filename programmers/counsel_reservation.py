from collections import deque

# 0보다 크면 time2가 더 빨리 옴
# 0보다 작으면 time2가 더 늦게 옴
def get_time_priority(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    return m1 - m2 if h1 == h2 else h1 - h2

def get_time(time, minute=1):
    h, m = map(int, time.split(':'))
    m += minute
    if m >= 60:
        h += 1
        m -= 60
    return f"{h}:{m}"

def get_start_time(booked, unbooked):
    return unbooked[0] if get_time_priority(booked[0][0], unbooked[0][0]) > 0 else booked[0]

def solution(booked, unbooked):
    answer = []
    booked = deque(booked)
    unbooked = deque(unbooked)
    t, _ = get_start_time(booked, unbooked)
    while booked and unbooked:
        if get_time_priority(t, booked[0][0]) >= 0:
            answer.append(booked.popleft()[1])
            t = get_time(t, 10)
        elif get_time_priority(t, unbooked[0][0]) >= 0:
            answer.append(unbooked.popleft()[1])
            t = get_time(t, 10)
        else:
            t = get_time(t)
    
    if len(booked) > 0:
        for _, name in booked:
            answer.append(name)
    elif len(unbooked) > 0:
        for _, name in unbooked:
            answer.append(name)
    return answer


# print(solution([["10:11", "b"], ["12:14", "d"], ["14:16", "f"], ["16:18", "h"]], [["10:11", "a"], ["12:13", "c"], ["14:15", "e"], ["16:17", "g"]]))
# print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:00", "bae"]]))
# print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:00", "bae"]]) == ["kim", "lee", "bae"])
# print(solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]]))
# print(solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]]) == ["hae", "jee", "hee", "eom"])
# print(solution([["09:01", "bae"]], [["09:00", "lee"], ["09:01", "kim"]] ))

# print(solution([ ["09:05", "bae"], ["09:15", "bbae"], ["09:17", "bbbae"]], [["09:00", "lee"], ["09:10", "kim"], ["09:11", "kkim"]],))
print(solution([ ["09:00","ycha"], ["09:13", "chlim"]], [["08:50", "jy"], ["09:01", "sooyoon"]]))
