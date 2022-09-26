# https://www.acmicpc.net/problem/17412
# 도시 왕복하기 1
from sys import stdin, stdout

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

def DFS(current, visit):
    global graph, capacity, START, END

    Print(capacity)
    # 다음 node를 모두 DFS  순차진행
    for i in range(len(graph[current])):
        next = graph[current][i]
        # 마지막점 도달시
        if next == END and capacity[current][next] > 0:
            # 문제에서 한번 사용한 edge는 사용 불가라고 했으므로 capacity가 1로 취급한다. 
            # 현재까지 거쳐온 간선들을 재사용 불가능하도록 처리한다.
            visit[next] = current
            flow = MAX
            ptr = next
            while ptr != START:
                # 최소 유량을 확인한다. 
                a = visit[ptr]  # 기준점
                b = ptr  # 다음노드
                ptr = visit[ptr]
                if capacity[a][b] > 0:
                    flow = min(flow, capacity[a][b])
            
            # capacity를 갱신하고 역방향 flow 를 생성한다. 
            ptr = next
            while ptr != START:
                a = visit[ptr]  # 기준점
                b = ptr  # 다음노드
                ptr = visit[ptr]
                # 그래프 자체를 삭제하는 방법은 시간이 너무 오래 걸린다. capacity만 조작하자
                capacity[a][b] -= flow  # flow 갱신
                capacity[b][a] += flow  # 역방향 flow

            Print('flow', flow)
            return flow  # 종점 도달 가능한 flow를 반환

        elif visit[next] == 0 and capacity[current][next] > 0:
            visit[next] = current
            res = DFS(next, visit)
            # 종점에 도달 가능한 결과가 나왔다면 종료
            if res > 0:
                return res
    # 본 node의 하위 node들로부터 종점에 도달 불가능한 경우, 방문 처리를 취소하고 0을 반환
    # visit[current] = False
    return 0


def solve():
    global graph, capacity, START, END
    
    # DFS 시작, 더이상 종점에 도달 할 수 없을 때 까지 반복
    # 결국 capacity가 모자라 loop가 종료될 것
    count = 0
    while True:
        visit = [0 for _ in range(N+1)]
        # 경로를 따로 배열로 지정하면 메모리 및 시간이 낭비되므로, visit을 parent로 사용한다. 
        res = DFS(START, visit)
        if res == 0:
            break
        else:
            count += res
    return count


START = 1
END = 2
MAX = 9999999999
N, P = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
capacity = [[0 for _ in range(N+1)] for _ in range(N+1)]
for p in range(P):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  # maxflow 알고리즘을 위해 역방향도 추가한다.
    capacity[a][b] += 1  # 같은 간선이 여러번 올 수 있을수도 있으므로 다음과 같이 설정

Print(graph)
Print(capacity)

count = solve()

stdout.write(str(count))