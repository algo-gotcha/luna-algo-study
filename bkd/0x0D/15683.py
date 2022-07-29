import sys

h, w = map(int, sys.stdin.readline().split())

office = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

CCTV = [1, 2, 3, 4, 5]

for o in office:
    print(o)

count = 0
for y in range(h):
    for x in range(w):
        # if office[y][x] == 6:
        #     count += 1
        if office[y][x] == 1:
            # count += 1
            count_arr = []
            if y > h//2 and x > w//2:
                step_y = y
                step_count = 0
                while step_y:
                    if office[step_y][x] == '6':
                        break
                    step_y -= 1
                    step_count += 1
                count_arr.append(step_count)
                step_x = x
                step_count = 0
                while step_x:
                    if office[y][step_x] == '6':
                        break
                    step_x -= 1
                    step_count += 1
                count_arr.append(step_count)
            if y > h//2 and x <= w//2:
                step_y = y
                step_count = 0
                while step_y:
                    if office[step_y][x] == '6':
                        break
                    step_y -= 1
                    step_count += 1
                count_arr.append(step_count)
                step_x = x
                step_count = 0
                while step_x < w:
                    if office[y][step_x] == '6':
                        break
                    step_x += 1
                    step_count += 1
                count_arr.append(step_count)
            if y <= h//2 and x > w//2:
                step_y = y
                step_count = 0
                while step_y < h:
                    if office[step_y][x] == '6':
                        break
                    step_y += 1
                    step_count += 1
                count_arr.append(step_count)
                step_x = x
                step_count = 0
                while step_x:
                    if office[y][step_x] == '6':
                        break
                    step_x -= 1
                    step_count += 1
                count_arr.append(step_count)
            if y <= h//2 and x <= w//2:
                step_y = y
                step_count = 0
                while step_y < h:
                    if office[step_y][x] == '6':
                        break
                    step_y += 1
                    step_count += 1
                count_arr.append(step_count)
                step_x = x
                step_count = 0
                while step_x < w:
                    if office[y][step_x] == '6':
                        break
                    step_x += 1
                    step_count += 1
                count_arr.append(step_count)
            
            print(count_arr)
            count += max(count_arr)

print(count)
print(w * h - count)

