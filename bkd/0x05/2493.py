from collections import deque
import sys

count = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

result = deque()
for _ in range(count):
    popped = numbers.pop()
    is_popped = False
    max_index = len(numbers) - 1
    for i in range(max_index + 1):
        if numbers[max_index - i] > popped:
            result.appendleft(max_index - i + 1)
            is_popped = True
            break
    if not is_popped:
        result.appendleft(0)
        
print(*result)


