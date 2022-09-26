# https://www.acmicpc.net/problem/17412
# 도시 왕복하기 1
from sys import stdin, stdout

def Print(*args):
    if DEBUG:
        print(*args)

DEBUG = 0
START = 1
END = 2
N, P = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for p in range(P):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

S = [(START,0)]  # DFS를 위한 stack
visit = [False for _ in range(N+1)]
count = 0
# DFS 시작
while S:
    current, pos = S.pop()
    Print(current, S)
    visit[current] = True
    # 다음 node를 모두 stack에 push
    has_next = False
    for i in range(pos, len(graph[current])):
        # 마지막점 도달
        if graph[current][i] == END:
            count += 1
            Print(S)
            # 문제에서 한번 사용한 edge는 사용 불가라고 했으므로 제거한다
            for s in range(len(S)-1):
                graph[S[s][0]].remove(S[s+1][0])
                Print('remove', S[s][0], 'to', S[s+1][0])
            graph[current].remove(END)
            # 이후 stack 및 visit 초기화. 처음부터 다시 시작
            visit = [False for _ in range(N+1)]
            S = [(START,0)]
            Print(graph)
            break

        elif not visit[graph[current][i]]:
            S.append((current, i + 1))  # stack의 top 어디까지 확인했는지 설정
            S.append((graph[current][i], 0))
            has_next = True
            break
    # 전체를 다 확인해봐도 방문할 곳이 없으면 방문 처리 취소
    if not has_next:
        visit[current] = False

stdout.write(str(count))