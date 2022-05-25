import sys

def solution(string):
    for s in string:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if len(stack) == 0:
                   return "no"
                else:
                    popped = stack.pop()
                    if popped != '(':
                       return "no"
            elif s == ']':
                if len(stack) == 0:
                   return "no"
                else:
                    popped = stack.pop()
                    if popped != '[':
                       return "no"
            elif s == '.':
                if len(stack) == 0:
                   return "yes"
                return "no"
            


while True:
    stack = []
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break
    print(solution(string))

