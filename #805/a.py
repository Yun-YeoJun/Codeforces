import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    k = 0
    while not 10 ** k <= m or not 10 ** (k + 1) > m:
        k += 1

    print(m - 10 ** k)