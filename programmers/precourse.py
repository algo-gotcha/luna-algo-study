from collections import Counter, deque


def solution(s1, s2, k):
    answer = []
    graph = { key:[] for key in s2}
    visited = {}
    for dst, src in zip(s2, s1):
        graph[dst].append(src)
        visited[dst] = 0
        visited[src] = 0

    q = deque()
    q.append(k)
    # visited[k] = 1


    last = []

    while q:
        key = q.popleft()
        if not graph.get(key):
            if visited[key] == 0:
                last.append(key)
                visited[key] += 1
            continue
        else:
            for item in graph[key]:
                q.append(item)
        answer.append(key)
        visited[key] = 1
    last.sort()

    return last + answer[::-1]


print(solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"],["G", "C", "G", "F", "J", "E", "B", "F", "B"], "B") == ["D", "H", "E", "C", "F", "B"])
print("answer :", solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"],["G", "C", "G", "F", "J", "E", "B", "F", "B"], "B"))
print(solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"],["G", "C", "G", "F", "J", "E", "B", "F", "B"] ,"G") == ["A", "D", "H", "E", "C", "F", "B", "G"])
print("answer :", solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"],["G", "C", "G", "F", "J", "E", "B", "F", "B"] ,"G"))
# print(solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"],["G", "C", "G", "F", "J", "E", "B", "F", "B"], "G"))

