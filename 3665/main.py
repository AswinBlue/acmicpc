# https://www.acmicpc.net/problem/3665
# 최종순위
from sys import stdin, stdout
DEBUG = 0
def Print(*args):
    if DEBUG:
        print(args)

def topological(edges, edges_in, N):
    Q = []  # queue
    result = []  # 결과

    # 진입 edge가 하나도 없는 node부터 시작
    for i in range(1, N+1):
        if edges_in[i] == 0:
            # 모든 node들의 순서가 확정된다면, Queue의 크기는 2 이상이 될 수 없다.
            if len(Q) > 0:
                return "?"  #  데이터 부족
            Q.append(i)
            # break

    while len(Q):
        Print(Q, result, edges_in)
        current = Q.pop(0)
        result.append(current)  # 결과에 추가
        edges_in[current] = -1  # 한번 결과로 처리하면 -1로 변경하여 visit 처리

        # current 에서 나온 edge들을 모두 카운트에서 제거
        for e in edges[current]:
            edges_in[e] -= 1

        # 다시 진입 edge가 하나도 없는 node 검색
        for i in range(1, N+1):
            if edges_in[i] == 0:
                # 모든 node들의 순서가 확정된다면, Queue의 크기는 2 이상이 될 수 없다.
                if len(Q) > 0:
                    return "?"  #  데이터 부족
                Q.append(i)
    
    # 결과 판단
    if len(result) < N:
        # cycle이 있어서 진입edge가 하나도 없는 node를 찾지 못한 경우
        return "IMPOSSIBLE"
    else:
        # 끝까지 다 찾은 경우
        return ' '.join(map(str, result))

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    edges = [[] for _ in range(N+1)]  # i 에서 나가는 edge
    # edges_in = [[] for _ in range(N)]  # i 로 들어오는 edge
    edges_in = [0 for _ in range(N+1)]  # i 로 들어오는 edge

    prev_order = list(map(int, stdin.readline().split()))
    # 모든 vertex들에 대해 순서 설정
    for i in range(N):
        for j in range(i+1, N):
            a = prev_order[i]
            b = prev_order[j]
            edges[a].append(b)
            edges_in[b] += 1

    M = int(stdin.readline())  # 변경할 edge 개수
    for m in range(M):
        a, b = map(int, stdin.readline().split())
        # a, b 두 vertex에 대해 순서 변경
        # a에서 b로 가는 edge를 찾고, 없으면 반대 방향을 찾음
        if b in edges[a]:
            idx = edges[a].index(b)
            edges[a].pop(idx)
            edges[b].append(a)
            edges_in[a] += 1
            edges_in[b] -= 1
        else:
            idx = edges[b].index(a)
            edges[b].pop(idx)
            edges[a].append(b)
            edges_in[a] -= 1
            edges_in[b] += 1

    Print(edges)
    Print(edges_in)
    # 들어오는 edge가 0인 node 찾아 topological sort 시작
    result = topological(edges, edges_in, N)
    stdout.writelines(result+'\n')
