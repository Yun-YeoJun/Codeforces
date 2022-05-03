from sys import stdin

t = int(stdin.readline())

dic = {}
idx = 1

for i in range(97,123):
    for j in range(97,123):
        if i == j:
            continue
        a = chr(i)
        b = chr(j)
        dic[a + b] = idx
        idx += 1

for tc in range(t):
    i = stdin.readline().rstrip()
    print(dic[i])

    