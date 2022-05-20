import sys

string = list(sys.stdin.readline().rstrip())
count = int(input())
index = len(string) - 1
max_index = index

for _ in range(count):
    command = sys.stdin.readline().rstrip()
    if command[0] == 'P':
        string.insert(index + 1, command[-1])
        index += 1
    elif command[0] == 'B':
        if index >= 0:
            del string[index]
            index -= 1
    elif command[0] == 'L' and index >= 0:
        index -= 1
    elif command[0] == 'D' and max_index:
        index += 1



print()
print()
print(''.join(string))
print()
print()
