# https://www.acmicpc.net/problem/11378
# 열혈강호 4
from collections import deque
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10000)

MAX_N = 1000
DEBUG = 0

def Print(*args, end='\n'):
    if DEBUG:
        print(*args, end=end)

def max_flow():
    # result = BFS()
    result = DFS()
    return result

def do_dfs(current, visit):
    global START, END, capacity, graph

    for next in graph[current]:
        if capacity[current][next] > 0 and visit[next] == None:
            visit[next] = current

            # 마지막점 도달시
            if next == END:
                # 지나온 경로의 최소 유량 검색
                min_flow = 99999 
                ptr = END
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
                Print('update cap:', min_flow)
                ptr = END
                while ptr != START:
                    Print(ptr, end=' ')
                    a = visit[ptr]
                    b = ptr
                    capacity[a][b] -= min_flow  # 순방향 그래프 감소
                    capacity[b][a] += min_flow  # 역방향 그래프 증가
                    ptr = visit[ptr]  # 다음 찾기
                Print('<= route')

                # 끝점에 도달한 유량 반환
                return min_flow

            res = do_dfs(next, visit)
            # 끝점에 도달한 경우, 반환값이 0이 아님
            if res > 0:
                # 처음부터 다시 시작을 위해 현재 함수 종료
                return res

    # 다음으로 이동할 node가 없을 경우 0 반환
    return 0    

def DFS():
    global START, END
    count = 0
    while True:
        visit = [None for _ in range(END+1)]
        res = do_dfs(START, visit)
        count += res
        if res == 0:
            break
    return count

def BFS():
    global START, END, capacity, graph
    Q = deque([START])
    visit = [None for _ in range(END+1)]
    count = 0  # 수행 가능한 일의 개수
    while Q:
        Print('BFS', Q, visit)
        current = Q.popleft()
        for next in graph[current]:
            if visit[next] == None and capacity[current][next] > 0:  # 방문여부, 용량 체크
                visit[next] = current  # 방문기록
                Q.append(next)  # 다음 후보로 추가

                if next == END:  # 종료지점일 경우
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
                    Print('update cap:', min_flow)
                    ptr = END
                    while ptr != START:
                        Print(ptr, end=' ')
                        a = visit[ptr]
                        b = ptr
                        capacity[a][b] -= min_flow  # 순방향 그래프 감소
                        capacity[b][a] += min_flow  # 역방향 그래프 증가
                        ptr = visit[ptr]  # 다음 찾기
                    Print('<= route')

                    count += min_flow  # 결과 추가
                    # 조기 종료조건 (주어진 일을 모두 완료한 경우)
                    if count >= M:
                        return count

                    # Q 및 visit 초기화 후 다시 동작
                    Q = deque([START])
                    visit = [None for _ in range(END+1)]
                    break

    # 계산 완료 후 결과값 반환
    return count


# 문제 접근 방식:
# START -> WORKER_LAYER -> WORK_LAYER -> END 형태로 그래프가 형성된다고 생각한다. 
# START -> WORKER 상의 edge는 START 에서 모든 WORKER(N개)에 대해 존재하며, capacity 는 1 이다. (벌점이 없어도 1개의 일은 수행 가능하기 때문)
# WORKER -> WORK 상의 edge는 문제에서 주어진 조건에 따라(입력) 결정되며 capacity 는 항상 1이다. (일은 한번만 수행하면 되기 때문)
# WORK -> END 상의 edge는 모든 WORK(M개)에서 END로 존재하며, capacity 무조건 1이다. (일은 한번만 수행하면 되기 때문)
# 여기서 추가로 START -> MID -> WORKER_LAYER 를 두고, capacity를 K로 설정하여 벌점(K) 에 대한 경우를 추가로 고려한다.

if __name__ == '__main__':
    N, M, K = map(int, stdin.readline().split())

    START = N + M
    MID = N + M + 1
    END = N + M + 2

    graph = [[] for _ in range(END+1)]  # directed graph 정의 [:N] 까지는 START -> WORKER, [N:M] 까지는 WORKER -> WORK, 이후 START, MID, END 를 의미
    # 간선 설정
    graph[START].append(MID)
    graph[MID].append(START)
    # 용량 설정
    capacity = [[0 for _ in range(END+1)] for _ in range(END+1)]  # M+N by M+N 배열을 생성한다. [:N] 까지는 START -> WORKER, [N:M] 까지는 WORKER -> WORK, 이후 START, MID, END 를 의미
    capacity[START][MID] = K  # 벌점 K 만큼 추가 capacity를 설정한다.

    # START -> WORKER 구간
    for n in range(N):
        # 간선 설정
        graph[MID].append(n)
        graph[n].append(MID)
        graph[START].append(n)
        graph[n].append(START)
        # 용량 설정
        capacity[START][n] = 1  # 모든 사람은 벌점 없이도 1개의 일을 할수 있다.
        capacity[MID][n] = K  # 벌점을 몰아주면 한사람이 최대 K의 양만큼 일할 수 있다. 
        # 입력값을 받아와 간선 및 용량 추가 설정 (WORK -> WORKER 구간)
        can_do = list(map(int, stdin.readline().split()))  # n번 직원이 할수있는 일을 받아옴
        for c in can_do[1:]:
            c -= 1  # index를 0부터 설정
            capacity[n][N+c] += 1  # 직원은 0부터 시작하고, 일은 N부터 시작하므로, n 번 직원이 c 번 (index는 N+c)의 일을 할 수 있음을 표현
            graph[n].append(N+c)  # 간선 설정
            graph[N+c].append(n)  # 역방향도 설정

    # WORK -> END 구간
    for m in range(M):
        # 간선 설정
        graph[N+m].append(END)
        graph[END].append(N+m)
        # 용량 설정
        capacity[N+m][END] = 1  # 일은 한번만 수행하면 되므로 1로 설정

    Print('capacity:', capacity)
    Print('graph:', graph)
    # Max Flow 알고리즘 적용
    result = max_flow()
    stdout.write(str(result))