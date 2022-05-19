room_number = input()

def solution(room_number):
    room_number = str(room_number)
    hash = {}
    for number in room_number:
        if number != '9' and number != '6':
            if hash.get(number, 0) == 0:
                hash[number] = 1
            else:
                hash[number] += 1
    
    sixnine = room_number.count('6') + room_number.count('9')
    if sixnine % 2 != 0:
        sixnine = sixnine // 2 + 1
    else:
        sixnine //= 2
    if len(hash.values()) > 0:
        max_num = max(hash.values())
        if sixnine < max_num:
            return max_num
    return sixnine


# print(solution(9999) == 2 )
# print(solution(122) == 2)
# print(solution(12635) == 1)
# print(solution(888888) == 6)

print(solution(room_number))
