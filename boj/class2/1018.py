import sys

N, M = map(int, sys.stdin.readline().split())

input_chess = [sys.stdin.readline().strip() for _ in range(N)]

chess1 = ['WB' * 4 if i % 2 == 0 else 'BW' * 4 for i in range(N)]

results = []
for i in range(N + 1 - 8):
    for j in range(M + 1 - 8):
        count1 = 0
        count2 = 0
        for y in range(8):
            if y + i >= N:
                break
            for x in range(8):
                if x + j >= M:
                    break
                if input_chess[y + i][x + j] != chess1[y][x]:
                    count1 += 1
                else:
                    count2 += 1
        results.append(min(count1, count2))

print(min(results))
