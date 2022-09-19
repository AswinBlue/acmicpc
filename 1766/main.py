# https://www.acmicpc.net/problem/1766
# 문제집
# 먼저 나온 문제가 나중에 나오는 문제보다 어렵다는 조건을 뺀다면
# 1. 문제를 풀수록 다음 문제는 난이도가 쉬워진다. depth가 깊은 route부터 모두 해결해야 한다.(like DFS)
# 2. 한 node를 root로 하는 tree 형태로 문제를 본다면, 한 문제에 depth가 깊게 child들이 달리는 경우와, depth가 얕게 child들이 달리는 경우가 있다. \
# depth를 고려해서 문제를 해결해야 한다. depth는 그래프 생성 후 DFS를 수행하며 결정하고, 결정된 depth를 이용해 

import heapq
from sys import stdin, stdout
MAX_N = 32000
MAX_M = 100000

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(args)

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())

    # compose graph
    graph = [[] for _ in range(N+1)]  # 순서를 나타내는 그래프
    graph_in = [0 for _ in range(N+1)]

    for M in range(M):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph_in[b] += 1

    # start topological sort
    Q = []
    for i in range(1, N+1):
        if graph_in[i] == 0:
            heapq.heappush(Q, i)

    result = []  # 결과 담을 list
    Print('graph:', graph)
    while Q:
        # 문제에서 index가 낮을수록 우선순위가 높다고 했으므로 i는 1부터 시작
        current = heapq.heappop(Q)
        result.append(current)
        Print('while loop:', current, graph_in, Q, result)
        
        # 간선 갯수에서 현재 node와 연결된 간선 제거
        for next in graph[current]:
            graph_in[next] -= 1
            # 연결된 간선 0개인 node들 추가
            Print(next, graph_in[next])
            if graph_in[next] == 0:
                heapq.heappush(Q, next)

    stdout.write(' '.join(map(str, result)))  # 결과 출력