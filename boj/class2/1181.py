import sys

count = int(sys.stdin.readline().rstrip())
N = 20001
hash = [set() for _ in range(N)]

for _ in range(1, count + 1):
    string = sys.stdin.readline().rstrip()
    hash[len(string)].add(string)

for i in range(N):
    hash[i] = sorted(hash[i])
    for s in hash[i]:
        print(s)
