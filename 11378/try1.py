# https://www.acmicpc.net/problem/11378
# 열혈강호 4

MAX_N = 1000
DEBUG = 0

def Print(*args, end='\n'):
    if DEBUG:
        print(*args, end=end)

def max_flow():
    global START, END, capacity, graph

    Q = [START]
    visit = [None for _ in range(END+1)]
    count = 0  # 수행 가능한 일의 개수
    while Q:
        Print('DFS', Q, visit)
        current = Q.pop(0)
        for next in graph[current]:
            if visit[next] == None and capacity[current][next] > 0:  # 방문여부, 용량 체크
                visit[next] = current  # 방문기록
                Q.append(next)  # 다음 후보로 추가

                if next == END:  # 종료지점일 경우
                    count += 1  # 결과 추가
                    # ** flow 갱신 **
                    # min_flow 값 찾기
                    ptr = END
                    min_flow = 99999 
                    Print('find min')
                    while ptr != START:
                        Print(ptr, end=' ')
                        a = visit[ptr]
                        b = ptr
                        if capacity[a][b] > 0 and capacity[a][b] < min_flow:
                            min_flow = capacity[a][b]
                        ptr = visit[ptr]  # 다음 찾기
                    Print('<= route')

                    # capacity 갱신
                    Print('update cap')
                    ptr = END
                    while ptr != START:
                        Print(ptr, end=' ')
                        a = visit[ptr]
                        b = ptr
                        capacity[a][b] -= min_flow  # 순방향 그래프 감소
                        capacity[b][a] += min_flow  # 역방향 그래프 증가
                        ptr = visit[ptr]  # 다음 찾기
                    Print('<= route')

                    # Q 및 visit 초기화 후 다시 동작
                    Q = [START]
                    visit = [None for _ in range(END+1)]
                    break

    # 계산 완료 후 결과값 반환
    return count


# 문제 접근 방식:
# START -> MID_LAYER -> WORKER_LAYER -> WORK_LAYER -> END 형태로 그래프가 형성된다고 생각한다. 
# START -> MID 까지는 1개의 edge만 존재하며, capacity는 K + N이다. 
# MID -> WORKER 상의 edge는 MID에서 모든 WORKER(N개)에 대해 존재하며, capacity 는 무한이다.
# WORKER -> WORK 상의 edge는 문제에서 주어진 조건에 따라(can_do) 결정되며 capacity 는 항상 1이다.
# WORK -> END 상의 edge는 모든 WORK(M개)에서 END로 존재하며, capacity 무조건 1이다. 

# 단, 위와같이 설정하면 일을 안하는 직원이 생길수도 있다.(한명이 N+K 개의 일을 수행할 수도 있게됨) 모든 직원이 하나 이상의 일은 해야 하므로,
# 1차로 MID -> WORKER 로 가는 capacity를 모두 1로 설정하고, START -> MID 로 가는 capacity를 N으로 설정한다. 
# 이후 Max Flow 알고리즘을 이용해서 한번 계산을 해 주고, capacity를 수정해 준다. 
# 2차로 Max Flow 알고리즘을 수정된 capacity를 이용해 다시 수행한다. 이때, MID -> WORKER 상의 capacity를 모두 무한으로 설정하고, START -> MID 의 capacity를 K 로 설정한다.

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    START = N + M
    MID = N + M + 1
    END = N + M + 2

    graph = [[] for _ in range(END+1)]  # directed graph 정의 [:N] 까지는 START -> WORKER, [N:M] 까지는 WORKER -> WORK, 이후 START, MID, END 를 의미
    # 간선 설정
    graph[START].append(MID)
    graph[MID].append(START)
    for n in range(N):
        graph[MID].append(n)
        graph[n].append(MID)
    for m in range(M):
        graph[N+m].append(END)
        graph[END].append(N+m)

    # 용량 설정
    capacity = [[0 for _ in range(END+1)] for _ in range(END+1)]  # M+N by M+N 배열을 생성한다. [:N] 까지는 START -> WORKER, [N:M] 까지는 WORKER -> WORK, 이후 START, MID, END 를 의미
        
    capacity[START][MID] = N  # 벌점 없이도 직원이서 각자 1개의 일 수행

    for n in range(N):
        capacity[MID][n] = 1  # 1차로 값을 1로 제한
    for m in range(M):
        capacity[N+m][END] = 1  # 일은 한번만 수행하면 되므로 1로 설정

    # 입력값을 받아와 간선 및 용량 추가 설정 (WORK -> WORKER 구간)
    for n in range(N):
        can_do = list(map(int, input().split()))  # n번 직원이 할수있는 일을 받아옴
        for c in can_do[1:]:
            c -= 1  # index를 0부터 설정
            capacity[n][N+c] += 1  # 직원은 0부터 시작하고, 일은 N부터 시작하므로, n 번 직원이 c 번 (index는 N+c)의 일을 할 수 있음을 표현
            graph[n].append(N+c)  # 간선 설정
            graph[N+c].append(n)  # 역방향도 설정

    Print('capacity:', capacity)
    Print('graph:', graph)
    result = 0
    # 1차 Max Flow 알고리즘 적용
    result += max_flow()
    # 2차 Max Flow 알고리즘 적용
    # capacity 재설정
    capacity[START][MID] = K # 벌점 K 만큼 추가 일 가능
    for n in range(N):
        capacity[MID][n] = 99999  # 1차로 값을 무한으로 설정

    result += max_flow()

    print(result)