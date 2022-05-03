from sys import stdin

t = int(stdin.readline())

for tc in range(t):
    x, y = map(int,stdin.readline().split())
    tf = False
    for b in range(1, 100):
        for a in range(1,6):
            if b ** a == y / x:
                tf = True
                print(a, b)
                break
        if tf == True:
            break
    if tf == False:
        print(0,0)