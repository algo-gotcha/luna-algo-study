import sys

string = sys.stdin.readline().rstrip()

floor = -1
tmp = ''
count = 0
for s in string:
    if s == '(':
        floor += 1
        tmp = s
    elif s == ')':
        if tmp == '(':
            count += floor
        else:
            count += 1
        tmp = s
        floor -= 1

print(count)



# (())
# 2

# ((()))
# 4

# (((())))
# 6

# (()())
# 3

# ((()()))
# 6

# ((()())())
# 3 + 4 = 7


# (((()())()))
# 3 + (3 + 1) + (3 + 1) = 11

# (()()())
# 4

# ((())())
# 5
# 2 + 3

# ((())(()))
# 2 + 2 + 3 = 7

# ((()()))
# 3 + 3 = 6

