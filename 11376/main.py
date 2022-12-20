# https://www.acmicpc.net/problem/11376
# 열혈강호 2
# max flow 알고리즘으로 해결한다.
# 1. 주어진 그래프를 capacity와 edge를 가진 flow로 나타낸다.
# 2. DFS를 수행하며 START에서 END까지 가는 경로를 찾는다.
# 3. 찾아낸 경로에서 흐를 수 있는 최대 유량을 측정한다.
# 4. 3에서 찾은 유량만큼 해당 경로의 capacity를 빼주고, 역방향 capacity에는 더해준다. 
# 5. DFS를 더이상 수행할 수 없을 때 까지 2~4를 반복하며 3에서 얻은 유량값을 누적한다. 
# 6. 5에서 얻은 누적 유량값이 max flow이다. 


MAX_N = 1000
MAX_M = 1000
START = 0
END = MAX_N + MAX_M + 1

DEBUG = 0
def Print(*args, end='\n'):
    if DEBUG:
        print(*args, end=end)

# (2)
def DFS(current, visit):
    global edge, capacity, N, M
    Print('DFS current', current)
    # 현재 node(current) 에서 갈 수 있는 모든 node들 체크
    for next in edge[current]:
        Print('\tDFS next', next, capacity[current][next], visit[next])
        # 기존에 방문하지 않은 다른 node에 도달할 수 있는 경우
        if capacity[current][next] > 0 and visit[next] is None:
            # visit에 경로정보 입력
            visit[next] = current
            
            if next == END:
                # 목적지(END) 도달한 경우
                # (3)
                # 최소 유량을 찾고 역방향 그래프 적용
                flow = 99999
                # 경로를 역으로 되짚어가며 min flow를 찾음
                ptr = END
                Print('\tpath', end=' ')
                while ptr != START:
                    Print('-', ptr, '[', capacity[visit[ptr]][ptr], ']', end=' ')
                    flow = min(flow, capacity[visit[ptr]][ptr])
                    ptr = visit[ptr]
                Print('')
                # (4)
                # 찾은 min flow로 flow 갱신 및 역방향 flow 생성
                ptr = END
                while ptr != START:
                    capacity[visit[ptr]][ptr] -= flow
                    capacity[ptr][visit[ptr]] += flow
                    ptr = visit[ptr]
                Print('\t-> flow', flow)
                return flow
            else:
                # 목적지가 아닌 경우
                # 다음 목적지 검색
                res = DFS(next, visit)
                if res > 0:
                    return res

    # 진행 가능한 경로가 없는 경우는 0을 반환
    return 0


N, M = map(int, input().split())

edge = [[] for _ in range(END + 1)]  # 1부터 N까지는 worker, N+1부터 N+M까지는 work를 의미한다.
capacity = [[0 for _ in range(END + 1)] for _ in range(END + 1)]  # (i,j)로 진입하는 각 edge가 가지는 capacity

# (1)
for i in range(1, N+1):
    tmp = list(map(int, input().split()))[1:]
    for j in tmp:
        edge[i].append(MAX_N + j)
        edge[MAX_N + j].append(i)  # 역방향 그래프도 설정(대신 capacity는 0)
        capacity[i][MAX_N + j] = 1
        # j -> i 는 capacity 0 유지

    # 한 사람당 2개의 일 처리 가능
    edge[START].append(i)
    edge[i].append(START)
    capacity[START][i] = 2

for j in range(MAX_N + 1, MAX_N + M + 1):
    # 각 일은 한번만 처리하면 됨
    edge[j].append(END)
    edge[END].append(j)
    capacity[j][END] = 1

result = 0

# (5)
# 더 이상 DFS 경로를 찾을 수 없을 때 까지 START -> END 로 가는 DFS 찾기.
while True:
    # DFS 한번 할 때 마다 visit은 초기화
    # visit에는 경로를 확인할 수 있게 이전에 방문한 node 번호를 적는다.
    visit = [None for _ in range(END+1)]
    visit[START] = START  # 시작점 visit 처리
    dfs_result = DFS(START, visit)
    # 결과가 0이면 더이상 경로가 없는 것
    if dfs_result == 0:  
        break
    else:
        # (6)
        result += dfs_result

print(result)