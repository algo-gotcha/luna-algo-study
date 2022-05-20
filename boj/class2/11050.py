import sys

N, K = map(int, sys.stdin.readline().split())

if K == 0 or N == K:
    print(1)

else:
    maxK = max(K, N-K) + 1
    minK = min(K, N-K) + 1

    bunmo = N
    for num in range(maxK, N):
        bunmo *= num


    bunza = 1
    for num in range(1, minK):
        bunza *= num


    print(bunmo // bunza)

