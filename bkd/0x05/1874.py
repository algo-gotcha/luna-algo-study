
import sys


count = int(sys.stdin.readline().rstrip())


def solution(count):
    result = []
    prev = 0
    stack = []
    index = 1
    for _ in range(count):
        number = int(sys.stdin.readline().rstrip())
        if result == "NO":
            continue
        if prev <= number:
            while index <= number:
                stack.append(index)
                result.append("+")
                index += 1
        if len(stack) > 0:
            popped = stack.pop()
            result.append("-")
            if popped != number:
                result = "NO"
        prev = number
    return result

result = solution(count)
if result == "NO":
    print(result)
else:
    for re in result:
        print(re)




