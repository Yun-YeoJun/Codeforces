import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dic1 = {}
dic2 = {}

for i in range(26):
    dic1[chr(97 + i)] = i + 1
    dic2[i + 1] = chr(97 + i)

for _ in range(t):
    idx = {}
    for i in range(26):
        idx[i + 1] = deque()
    w = list(input().rstrip())
    p = int(input())
    for i in range(len(w)):
        w[i] = dic1[w[i]]
        idx[w[i]].append(i)
    s = sum(w)
    for i in reversed(range(1,27)):
        for j in idx[i]:
            if s <= p:
                break
            w[j] = 0
            s -= i
        if s <= p:
            break
    l = []
    for i in range(len(w)):
        if w[i] != 0:
            l.append(dic2[w[i]])
    print(''.join(i for i in l))