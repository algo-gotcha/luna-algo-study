r = 31
M = 1234567891

slen = int(input())
hash = { c:i + 1 for i, c in enumerate("abcdefghijklmnopqrstuvwxyz") }

s = input()

result = 0
for i, c in enumerate(s):
	result += hash[c] * (r ** i)

print(result % M)

