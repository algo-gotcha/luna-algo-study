
def get_graph(tickets):
    graph = {}
    for src, dst in tickets:
        if not graph.get(src, []):
            graph[src] = [dst]
        else:
            graph[src].append(dst)
    for k in graph:
        graph[k] = sorted(graph[k], reverse=True)
    return graph

def solution(tickets):
    answer = []
    graph = get_graph(tickets)

    stack = ["ICN"]
    # answer.append("ICN")
    while stack:
        popped = stack.pop()
        if graph.get(popped, None):
            dst = graph[popped].pop()
            if graph.get(dst, None):
                answer.append(dst)
    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "ICN"], ["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "ICN"]]))
print(solution([["ICN", "BBC"], ["ICN", "ABC"], ["BBC", "ICN"]]))
