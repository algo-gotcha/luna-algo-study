s = input().lower()

result = []

if not s:
	print()

for i, _s in enumerate(s):
    if s.index(s[i]) < i:
        result[s.index(s[i])] += 1
    else:
        result.append(1)

max_result = 0
if len(result) > 0:
	max_result = max(result)

count = 0
for i in result:
		
	if i == max_result:
		count += 1

if max_result:
	if count > 1:
		print("?")
	else:
		print(s[result.index(max_result)].upper())
