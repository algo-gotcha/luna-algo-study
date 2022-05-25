

from collections import deque
import sys


number = int(sys.stdin.readline())

cards = deque(n for n in range(1, number + 1))

while len(cards) > 1:
	cards.popleft()
	to_move = cards.popleft()
	cards.append(to_move)

print(cards[0])
