# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
from sys import stdin, stdout
import heapq

MAX_N = 800
MAX_E = 200000
MAX_C = 1000
INACCESSIBLE = 99999999
START = 1

def dijkstra(start):
    global graph, N
    D = [INACCESSIBLE for _ in range(N+1)]  # dijkstra 결과값을 저장할 배열. deep copy에 주의
    D[start] = 0
    H = [(0, start)]  # (cost, idx) 형태의 인자가 들어갈 heap
    cnt = N  # dijkstra 최적화를 위해 횟수 count
    while H and cnt > 0:
        cost, current = heapq.heappop(H)
        for next in range(len(graph[current])):
            if graph[current][next] > 0 and D[next] > D[current] + graph[current][next]:
                D[next] = D[current] + graph[current][next]
                heapq.heappush(H, (D[next], next))
        cnt -= 1
    return D


N, E = map(int, input().split())
graph = [[INACCESSIBLE for _ in range(N+1)] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, stdin.readline().split())

# dijkstra
# 1. start from 'START'
d1 = dijkstra(START)
# 2. start from 'v1'
d2 = dijkstra(v1)
# 3. start from 'v2'
d3 = dijkstra(v2)

# 두 경우중 작은 값이 정답
# START -> v1 -> v2 -> N
# START -> v2 -> v1 -> N
result = min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N])
if result >= INACCESSIBLE:
    print(-1)
else:
    print(result)


