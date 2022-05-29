from collections import deque
import sys


loop = int(sys.stdin.readline())

nums = deque()
freq = {}
for _ in range(loop):
    num = int(sys.stdin.readline())
    nums.append(num)
    if freq.get(num, 0):
        freq[num] += 1
    else:
        freq[num] = 1


sorted_nums = sorted(nums)
index = len(nums) // 2
print(round(sum(nums) / len(nums)))
print(sorted_nums[index])

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
max_mf = sorted_freq[0][1]
most_freq = deque()
for m in sorted_freq:
    if m[1] == max_mf:
        most_freq.append(m)
    else:
        break

most_freq = sorted(most_freq)

if len(most_freq) > 1:
    print(most_freq[1][0])
else:
    print(most_freq[0][0])

print(sorted_nums[-1] - sorted_nums[0])
