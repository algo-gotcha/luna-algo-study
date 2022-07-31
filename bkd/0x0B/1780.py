import sys

N = int(sys.stdin.readline())

result = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def is_full(N, start_pos, start_value):
    x, y = start_pos
    for i in range(N):
        for j in range(N):
            if result[y + j][x + i] != start_value:
                return False
    return True

def get_pos(N, start_pos):
    x, y = start_pos
    return [(x + (N * i)//3, y + (N * j)//3) for i in range(3) for j in range(3)]

paper_count = [0, 0, 0]

def solution(N, paper, paper_count, pos=(0, 0)):
    i, j = pos
    if N == 1 or is_full(N, pos, paper[j][i]):
        paper_count[paper[j][i] + 1] += 1
        return
    else:
        poses = get_pos(N, pos)
        for pos in poses:
            i, j = pos
            solution(N//3, paper, paper_count, pos)
    return
    

solution(N, result, paper_count)
for paper in paper_count:
    print(paper)








