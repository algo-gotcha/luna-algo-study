from collections import deque

def solution(rows, columns, max_virus, queries):
    medium = [[0 for _ in range(columns)] for _ in range(rows)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    for i, query in enumerate(queries):
        visited = [[0 for _ in range(columns)] for _ in range(rows)]
        y, x = query
        q.append((x - 1, y - 1))
        visited[y - 1][x - 1] = 1
        while q:
            x, y = q.popleft()
            if medium[y][x] == max_virus:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= ny < rows and 0 <= nx < columns and visited[ny][nx] == 0:
                        q.append((nx, ny))
                        visited[ny][nx] = 1
            else:
                medium[y][x] += 1

    return medium

print(solution(3, 4, 2, [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]) == [[0, 2, 1, 1], [2, 2, 2, 1], [2, 2, 2, 1]])

print(solution(3, 4, 2, [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]))


