from collections import deque
import sys


loop = int(sys.stdin.readline())

people = {i:deque() for i in range(1, 201)}

for _ in range(loop):
	age, name = sys.stdin.readline().split()
	people[int(age)].append(name)

for age, name in people.items():
	while name:
		print(age, name.popleft())



