import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_s = heapq.heappop(scoville)
        if min_s < K:
            second_min_s = heapq.heappop(scoville)
            heapq.heappush(scoville, min_s + (second_min_s * 2))
            answer += 1
    if scoville and scoville[0] < K:
        return -1
    return answer

print(solution([1,2,3,9,10,12], 7))
print(solution([5, 4, 3, 1, 2, 7, 8], 2))
print(solution([1, 2, 200], 1000))
print(solution([10, 12], 35))