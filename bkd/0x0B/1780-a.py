import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

paper_count = [0, 0, 0]

def solve(x, y, z):
    if check(x, y, z):
        paper_count[paper[x][y] + 1] += 1
        return
    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * n, y + j * n, n)

solve(0, 0, N)

for paper in paper_count:
    print(paper)