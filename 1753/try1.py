# https://www.acmicpc.net/problem/1753
# 최단경로

# cost를 2차원 배열 만들어서 사용하니 메모리 초과 발생
from sys import stdin, stdout

MAX_V = 20000
MAX_E = 300000
INF = MAX_V * MAX_E

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

cost = [[INF for _ in range(V+1)] for _ in range(V+1)]  # cost[i][j] 는 i에세 j로 갈 경우 드는 비용. 초기값은 max값으로 설정
link = [[]for _ in range(V+1)]  # linked list로 표현한 연결관계
for e in range(E):
    u, v, w = map(int, stdin.readline().split())
    cost[u][v] = w
    link[u].append(v)

# Dijkstra 알고리즘으로 접근
# 음수 weight가 없으므로 dijkstra 가능

# dijkstra 초기화
D = [INF for _ in range(V+1)]  # K에서 i node로 로 갈 수 있는 거리를 D[i]에 저장
D[K] = 0  # 시작 node에서 시작 node로 가는 값은 0
# 접근불가 node에 대해서는 따로 처리 필요

visit = set(range(1,V+1))  # 방문해야 할 항목들

# 모든 node x에 대해 해당 node를 거쳐서 다른 node 'next'에 도달했을 때 드는 비용을 반복문을 통해 갱신해 나감
while visit:
    # 아직 방문하지 않은 ndoe 'i' 중에서 D[i]가 가장 작은 node 'i'를 찾는다.
    min_value = INF
    current = -1
    for i in range(1, V+1):
        if min_value > D[i] and i in visit:
            min_value = D[i]
            current = i
    # D[i] 값이 INF 가 아니면서 아직 방문하지 않은 node가 없는 경우,
    # 도달할 수 있는 모든 node들을 모두 확인한 것이므로, 종료한다. 
    Print(visit, current)
    if current == -1:
        break
    
    # 'current' node에 대해 dijkstra 비교 작업을 수행한다.
    visit.remove(current)  # 방문 처리
    # 노드 'current'을 거쳐서 노드 next 까지 도달시 필요한 weight값을 다시 계산한다. 
    # 기존에 찾은 경로와, 'current'를 거쳐 신규로 갈 수 있는 node를 비교해 더 짧은 길 선택
    for next in link[current]:
        if D[next] > D[current] + cost[current][next]:
            D[next] = D[current] + cost[current][next]

# 미방문 node에 대해  D값 변경
for i in range(1, V+1):
    if D[i] == INF:
        D[i] = "INF"
result = '\n'.join(map(str,D[1:]))  # 문제 출력 형식에 맞게 변환
stdout.write(result)