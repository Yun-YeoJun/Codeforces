from sys import stdin
import math

q = int(stdin.readline())

for tc in range(q):
    s = stdin.readline().rstrip()
    t = stdin.readline().rstrip()

    tf = True
    
    for i in t:
        if i == 'a':
            if len(t) != 1:
                tf = False
                print(-1)
                break
    
    if len(t) == 1 and t[0] == 'a':
        print(1)
        tf = False

    if tf == True:
        result = 1
        n = len(s)
        for i in range(1,len(s) + 1):
            result += math.factorial(n) // (math.factorial(n-i)*math.factorial(i))

        print(result)