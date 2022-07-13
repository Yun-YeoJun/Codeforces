import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n):
        bi, command = input().split()
        bi = int(bi)
        command = list(command)
        for j in command:
            if j == 'D':
                if l[i] == 9:
                    l[i] = 0
                else:
                    l[i] += 1
            if j == 'U':
                if l[i] == 0:
                    l[i] = 9
                else:
                    l[i] -= 1
    for i in l:
        print(i,end = ' ')
    print()
