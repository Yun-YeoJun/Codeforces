import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = deque(input().rstrip())
    temp = set()
    result = 0
    while len(s) != 0:
        w = s.popleft()
        temp.add(w)
        if len(temp) == 4:
            s.appendleft(w)
            result += 1
            temp = set()
    if len(temp) != 0:
        result += 1
    print(result)