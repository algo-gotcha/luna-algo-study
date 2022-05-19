from itertools import combinations

n, m = map(int, input().split())

cards = sorted(list(map(int, input().split())))

result = []
for card in combinations(cards, 3):
	if sum(card) <= m:
		result.append(sum(card))
	
print(max(result))

