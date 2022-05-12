numbers = [int(input()) for _ in range(9)]

max_number = max(numbers)
max_index = numbers.index(max_number)
print(max_number)
print(max_index + 1)