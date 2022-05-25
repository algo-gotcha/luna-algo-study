import sys

loop = int(sys.stdin.readline().rstrip())

count = 0
for _ in range(loop):
    stack = []
    string = sys.stdin.readline().rstrip()
    for s in string:
        if len(stack) > 0 and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if len(stack) == 0:
        count += 1

print(count)

