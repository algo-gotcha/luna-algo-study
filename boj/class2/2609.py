import sys

a, b = map(int, sys.stdin.readline().split())


# def get_gcd(a, b):
#     if b == 0:
#         return a
#     return get_gcd(b, a % b)

def get_gcd(a, b):
    n = 2
    yaksoo = 1
    while n <= a:
        if a % n == 0 and b % n == 0:
            yaksoo = n
        n += 1
    return yaksoo

gcd = get_gcd(a, b)

print(gcd)
print(a * b // gcd)



