import sys

string = sys.stdin.readline().rstrip()

result = 0
results = []
stack = []
tmp = ''
hash = {'(': 2, '[': 3, ')': 2, ']': 3}
open = ['(', '[']
close = [')', ']']

for s in string:
    if s == '(':
        stack.append(hash[s])

    elif s == '[':
        stack.append(hash[s])
    elif s == ']':
        if tmp == '[':
            result += stack.pop()
        else:
            results.append(result)
            result = 0
    elif s == ')':
        if tmp == '(':
            result += stack.pop()
        else:
            results.append(result)
            result = 0
    tmp = s
for i in results:
    result *= i

print("stack", stack)
print("result", result)
print("results", results)


# 2 + 2
# 2 * 2


# print(result)
# 2, 2,
# 2 * 2
# # ()()
# (())
# 2+
# ()
# ()()
# (())

# ([]())()[()]

# 2 * 2 * (2 + 2)
# ((()()))

# (()())()
# stack이 0이 되면 result에 더해준다.

# 2 * (2 + 2) + 2

# [[()()]][](((())))
# (((()()())))

1: 3
2: 3 + 2

(()[[]])([])




1: 3
2: 2 + 3
[[]()]()
3 * ( 3 + 2) + 2
index = 0

if s == [:
    index += 1
    hash[index] = hash.get(index, 0) + 3
    stack.append(s)
elif s == ]:
    stack.pop()
    if len(stack) == 0:
        for i in hash.values():
            result *= i
        results.append(result)
        result = 0

print(sum(results))

() : 2

[] : 3

()() : 4

()()() : 6

(()) : 4

((())) : 8

((()())) : 16

((())[]) : 14

([]())()[()] : 18

2 * (3 + 2) + 2 + 2 * 3

stack = []

[]
2 * 5 = 10

6 + 4 = 10
results = [10,]

# 2 * (2 + 3 * 3) + 2 * 3
