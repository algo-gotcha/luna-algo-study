alphabet = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

word = input()

for char in word:
	alphabet[char] += 1

print(*alphabet.values())
