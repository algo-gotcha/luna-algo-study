from collections import defaultdict

hash = defaultdict(int)

size = input()
input_numbers = input().split()
answer = int(input())

numbers = map(int, input_numbers)


for number in numbers:
    hash[number] += 1
    hash[answer - number] += 1

count = 0
for value in hash.values():
    if value > 1:
        count += 1

print(count // 2)


