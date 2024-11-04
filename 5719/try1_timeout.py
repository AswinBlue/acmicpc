# https://www.acmicpc.net/problem/5719
# 거의 최단경로

import heapq

MAX_N = 500
MAX_M = 10000
INVALID = -1

DEBUG = 0
def Print(*arg):
    if DEBUG == 1:
        print(*arg)

def dijkstra(graph, parent, cost):
    global N, M, S, D
    cost[S] = 0
    H = [(0, S)]  # dijkstra 알고리즘 연산 중 S로 부터의 거리가 최소인 node를 찾기 위한 heap
    visit = [False for _ in range(N)]
    while H:
        Print(f'heap:{H}')
        distance, node = heapq.heappop(H)

        # node 에 방문했는지 체크
        if visit[node]:
            continue
        visit[node] = True

        # node 에 방문한 적이 없다면 진행

        for next in range(N):
            # node 에서 next 까지 이동이 가능하다면
            if graph[node][next] != INVALID:
                # S 에서 node 까지 거리와 node 에서 next 까지 거리를 더한 값과 S 에서 next 까지 거리 비교
                new_cost = cost[node] + graph[node][next]
                if cost[next] == INVALID or new_cost < cost[next]:
                    # 값 갱신
                    cost[next] = new_cost
                    heapq.heappush(H, (cost[next], next))  # heap 에 값 갱신. 어차피 기존보다 더 작은 값이 들어가기 때문에 기존 값을 제거하지 않아도 됨
                    parent[next] = [node]  # 경로 저장
                elif new_cost == cost[next]:  # 최단 경로가 여러 개일 경우
                    parent[next].append(node)
                
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
        
        parent = [[] for _ in range(N)]  # 경로를 저장할 배열
        cost = [INVALID for _ in range(N)]  # 거리를 저장할 배열
        dijkstra(graph, parent, cost)

        Print(f'S:{S}, D:{D}, len:{cost[D]}')
        Print(f'parent:{parent}')
        Print(f'cost:{cost}')

        min_length = cost[D]

        # 최단경로가 여러개 존재 할 경우를 위해 반복
        while True:
            # 종료조건 1. 경로가 없는 경우 종료
            if cost[D] == INVALID:
                break

            # 최단경로 제거
            stack = [D]
            while stack:
                node = stack.pop()
                for prev in parent[node]:
                    if graph[prev][node] != INVALID:
                        graph[prev][node] = INVALID
                        stack.append(prev)

            # dijkstra 한번 더 동작
            parent = [None for _ in range(N)]  # 경로를 저장할 배열
            cost = [INVALID for _ in range(N)]  # 거리를 저장할 배열
            dijkstra(graph, parent, cost)
            Print(f'\nlen:{cost[D]}')
            Print(f'parent:{parent}')
            Print(f'cost:{cost}')
            
            # 종료조건 2. '최단경로'인지 '거의 최단경로'(최단경로 보다 긴 경로 중 가장 짧은 경로) 인지 체크
            if min_length < cost[D]:
                break

        print(cost[D])  # 최종 결과 출력
