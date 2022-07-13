import sys
input = sys.stdin.readline

t = int(input())
result = ''
for _ in range(t):
    z = input()
    n,k = map(int,input().split())
    l = input().split()
    idx = {}
    for i,j in enumerate(l):
        if not j in idx:
            idx[j] = [i,i]
        else:
            idx[j][1] = i
    for i in range(k):
        a,b = input().split()
        if not a in idx or not b in idx:
            print("NO")
        elif idx[a][0] > idx[b][1]:
            print("NO")
        else:
            print("YES")