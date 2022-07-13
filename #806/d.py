import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = [0 for i in range(n)]
    result = 0
    l = [[] for i in range(9)]
    for i in range(n):
        s = input().rstrip()
        l[len(s)].append((s,i))
    
    length = [0 for i in range(9)]
    for i in range(1,9):
        length[i] = length[i - 1] + len(l[i])

    l = sum(l,[])
    for i in range(n):
        leni = len(l[i][0])
        for j in range(0,length[leni - 1]):
            lenj = len(l[j][0])
            tf = False
            for k in range(length[leni - lenj - 1], length[leni - lenj]):
                # if lenj + len(l[k][0]) > 8:
                #     break
                # if leni != lenj + len(l[k][0]):
                #     continue
                if l[i][0] == ''.join([l[j][0], l[k][0]]):
                    result += 2 ** (n - l[i][1] - 1)
                    tf = True
                    break
            if tf:
                break
    result = str(bin(result))[2:]
    for i in range(n - len(result)):
        print('0',end='')
    print(result)

# for _ in range(t):
#     n = int(input())
#     l = [0 for i in range(n)]
#     for i in range(n):
#         l[i] = input().rstrip()
#     plus = [0 for i in range(n * n)]
#     result = ['0' for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if len(l[i]) + len(l[j]) > 8:
#                 continue
#             plus[n * i + j] = l[i] + l[j]
#     for i in range(n):
#         if l[i] in plus:
#             result[i] = '1'
#     print(''.join(result))

# for _ in range(t):
#     n = int(input())
#     l = [0 for i in range(n)]
#     result = ['0' for i in range(n)]
#     for i in range(n):
#         l[i] = input().rstrip()
#     for i in range(n):
#         leni = len(l[i])
#         if leni > 16:
#             continue
#         for j in range(n):
#             lenj = len(l[j])
#             if lenj >= 8:
#                 continue
#             if lenj >= leni:
#                 continue
#             for k in range(n):
#                 lenk = len(l[k])
#                 if lenk >= leni:
#                     continue
#                 if leni != lenj + lenk:
#                     continue
#                 if l[i] == l[j] + l[k]:
#                     result[i] = '1'
#                     break
#             if result[i] == '1':
#                 break

#     print(''.join(result))

# for _ in range(t):
#     n = int(input())

#     l = [[] for i in range(9)]
#     for i in range(n):
#         s = input().rstrip()
#         l[len(s)].append((s,i))

#     l = sum(l,[])

#     result = ['0' for i in range(n)]

#     for i in range(1,9):
#         for j in l[i]:
#             for k in range(1,i):
#                 for a in l[k]:
#                     for b in l[i - k]:
#                         if a[0] + b[0] == j[0]:
#                             result[j[1]] = '1'
#                             continue
#                     if result[j[1]] == '1':
#                         continue
#                 if result[j[1]] == '1':
#                     continue

