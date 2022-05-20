count = int(input())

result = []

stack = []
for _ in range(count):
    command = input().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif command[0] == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)


for re in result:
    print(re)
