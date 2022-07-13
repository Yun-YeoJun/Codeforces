import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().rstrip().upper()
    if s == "YES":
        print("YES")
    else:
        print("NO")