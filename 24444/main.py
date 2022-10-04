# https://www.acmicpc.net/problem/24444
# 알고리즘 수업 - 너비 우선 탐색 1

from collections import deque
from sys import stdin, stdout
MAX_N = 100000
MAX_M = 200000

N, M, START = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]  # 인접 노드를 기록할 2차원 배열

for m in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  # undirected 이기 때문에 반대 방향도 추가

for n in range(1, N+1):
    graph[n].sort()  # 문제 조건에서 오름차순으로 인접 노드를 방문한다고 했기에, 정렬을 한다. 

# do BFS
Q = deque()
visit = [0 for _ in range(N+1)]  # 단순 true, false가 아닌 몇번째 방문했는지 여부를 기록한다.
Q.append(START)
order = 1  # 몇번째 방문인지 체크
visit[START] = order

while Q:
    current = Q.popleft()
    # 다음 노드 처리
    for next in graph[current]:
        if visit[next] == 0:
            # 방문처리. BFS는 queue에 넣기 전에 방문처리를 하는게 메모리상 유리하며, 본 문제 조건에도 맞다.
            order += 1
            visit[next] = order
            Q.append(next)

result = ''
for i in range(1, N+1):
    result += '{}\n'.format(visit[i])
stdout.write(result)