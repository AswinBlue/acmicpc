# https://www.acmicpc.net/problem/5719
# 거의 최단경로

import heapq

MAX_N = 500
MAX_M = 10000
INVALID = -1

DEBUG = 1
def Print(*arg):
    if DEBUG == 1:
        print(*arg)

def dijkstra(graph, parent, cost):
    global N, M, S, D
    H = [(0, S)]  # dijkstra 알고리즘 연산 중 S로 부터의 거리가 최소인 node를 찾기 위한 heap
    while H:
        disitance, node = heapq.heappop(H)
        for next in range(N):

            # node 에서 next 까지 이동이 가능하다면
            if graph[node][next] != INVALID:
                # S 에서 node 까지 거리와 node 에서 next 까지 거리를 더한 값과 S 에서 next 까지 거리 비교
                if (cost[next] == INVALID) or (cost[node] + graph[node][next] < cost[next]):
                    # 값 갱신
                    cost[next] = cost[node] + graph[node][next]
                    heapq.heappush(H, (cost[next], next))  # heap 에 값 갱신. 어차피 기존보다 더 작은 값이 들어가기 때문에 기존 값을 제거하지 않아도 됨
                    parent[next] = node  # 경로 저장

if __name__ == '__main__':

    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break
        graph = [[INVALID for _ in range(N)] for _ in range(N)]

        S, D = map(int, input().split())
        for m in range(M):
            u, v, p = map(int, input().split())
            graph[u][v] = p
        
        parent = [None for _ in range(N)]  # 경로를 저장할 배열
        cost = [INVALID for _ in range(N)]  # 거리를 저장할 배열
        parent[S] = INVALID
        cost[S] = 0
        dijkstra(graph, parent, cost)

        Print(f'S:{S}, D:{D}')
        Print(f'parent:{parent}')
        Print(f'cost:{cost}')

        min_length = cost[D]

        # 최단경로가 여러개 존재 할 경우를 위해 반복
        while True:
            # 종료조건 1. 경로가 없는 경우 종료
            if cost[D] == INVALID:
                break

            # 최단경로 제거
            node1 = parent[D]
            node2 = D
            # S 에 도달할 때 까지 반복. parent[S] == INVALID 로 설정되어 있음
            while node1 != INVALID:
                graph[node1][node2] = INVALID  # 경로 제외
                node2 = node1
                node1 = parent[node1]

            # dijkstra 한번 더 동작
            parent = [None for _ in range(N)]  # 경로를 저장할 배열
            cost = [INVALID for _ in range(N)]  # 거리를 저장할 배열
            parent[S] = INVALID
            cost[S] = 0
            dijkstra(graph, parent, cost)
            Print(f'parent2:{parent}')
            Print(f'cost2:{cost}')
            
            # 종료조건 2. '최단경로'인지 '거의 최단경로'(최단경로 보다 긴 경로 중 가장 짧은 경로) 인지 체크
            if min_length < cost[D]:
                break

        print(cost[D])  # 최종 결과 출력