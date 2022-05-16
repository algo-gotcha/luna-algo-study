import sys

input = sys.stdin.readline

card = list(range(1, 21))

for _ in range(10):
	i, j = map(int, input().split())
	reverse_card = card[i-1:j]
	card = card[:i-1] + reverse_card[::-1] + card[j:]

print(*card)


