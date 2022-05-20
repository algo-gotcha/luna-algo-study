import sys
from math import ceil

A, B, V = map(int, sys.stdin.readline().split())

real = A - B
goal = V - B

print(ceil(goal / real))