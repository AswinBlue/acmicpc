# https://www.acmicpc.net/problem/24480
# 알고리즘 수업 - 깊이 우선 탐색 2
from collections import deque

MAX_N = 100000
MAX_M = 200000

from sys import stdin, stdout

N, M, START = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]  # 인접 노드를 나타낼 배열
for m in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

for i in range(1, N+1):
    graph[i].sort(reverse=True)  # 오름차순 순으로 정렬(문제 조건)

stack = deque()  # DFS 를 위한 stack
stack.append((START, 0))  # stack에는 (node, adj) 형태가 들어가며, node는 확인할 node, adj는 확인을 시작할 인점 node의 index를 의미한다. 
visit = [0 for _ in range(N+1)]
order = 1  # 방문 순서

while stack:
    current, adj = stack.pop()
    # 현재 node 방문처리
    if visit[current] == 0:
        visit[current] = order
        order += 1
    # print(visit)

    # 다음 방문할 node 검사. adj 다음 index부터 검사
    for n in range(adj, len(graph[current])):
        next = graph[current][n]
        if visit[next] == 0:
            stack.append((current, n+1))
            stack.append((next, 0))
            break
    # 더이상 방문할 node가 없는 경우
result = ''
for i in range(1, N+1):
    result += '{}\n'.format(visit[i])
stdout.write(result)