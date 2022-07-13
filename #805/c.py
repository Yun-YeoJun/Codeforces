import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    __ = input()
    n, k = map(int,input().split())
    stations = deque(map(int,input().split()))

    l1 = {}
    l2 = {} 
    for i in range(k):
        a,b = map(int,input().split())
        if a in l1:
            l1[a].append(i)
        else:
            l1[a] = [i]
        if b in l2:
            l2[b].append(i)
        else:
            l2[b] = [i]
    result = [-1 for i in range(k)]

    while stations:
        p = stations.popleft()
        if p in l1:
            for i in l1[p]:
                if result[i] == -1:
                    result[i] = 1
        if p in l2:
            for i in l2[p]:
                if result[i] == 1:
                    result[i] = 0
    for i in result:
        if i == 0:
            print("YES")
        else:
            print("NO")