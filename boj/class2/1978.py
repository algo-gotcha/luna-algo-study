from collections import deque
import sys

loop = int(sys.stdin.readline())

numbers = map(int, sys.stdin.readline().split())


def get_sosu(number):
    i = 2
    if number == 1:
        return False
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


count = 0
for number in numbers:
    if get_sosu(number):
        count += 1

print(count)
