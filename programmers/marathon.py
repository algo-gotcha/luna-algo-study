from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    for name in completion:
        p[name] -= 1
    return max(p, key=p.get)

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo")
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko")
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav")