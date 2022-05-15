x, y, w, h = map(int, input().split())

width = w - x
height = h - y

print(min(x, y, width, height))


