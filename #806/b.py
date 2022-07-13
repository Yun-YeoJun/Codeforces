import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().rstrip())
    l = [0 for i in range(26)]
    for i in s:
        k = ord(i) - 65
        if l[k] == 0:
            l[k] += 2
        else:
            l[k] += 1
    print(sum(l))