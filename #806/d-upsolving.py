import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    dic = {}
    n = int(input())
    l = [0 for i in range(n)]
    result = ['0' for i in range(n)]
    for i in range(n):
        s = input().rstrip()
        dic[s] = True
        l[i] = s
    for idx,s in enumerate(l):
        for i in range(1,len(s)):
            pre,post = s[:i],s[i:len(s)]
            if pre in dic and post in dic:
                result[idx] = '1'
                break
    print(''.join(result))