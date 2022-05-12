alphabet = {char: -1 for char in "abcdefghijklmnopqrstuvwxyz"}

word = input()
for char in word:
	alphabet[char] = word.index(char)

for value in alphabet.values():
	print(value, end=" ")