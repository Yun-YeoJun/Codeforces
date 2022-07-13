import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())
graph = [[] for i in range(n + 1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start,finish,n):
    distance = [INF for i in range(n + 1)]
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance[finish]

v1, v2 = map(int,input().split())

v1v2 = dijkstra(v1,v2,n)
v1_1 = dijkstra(v1,1,n)
v1_n = dijkstra(v1,n,n)
v2_1 = dijkstra(v2,1,n)
v2_n = dijkstra(v2,n,n)

result = v1v2

if v1_1 + v2_n > v2_1 + v1_n:
    result += v2_1 + v1_n
else:
    result += v1_1 + v2_n

if result == INF:
    result = -1

print(result)