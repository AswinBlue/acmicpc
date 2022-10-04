# https://www.acmicpc.net/problem/2606
# 바이러스

from sys import stdin, stdout

MAX_N = 100
START = 1

def DFS(current):
    global graph, visit
    visit[current] = True

    count = 0  # 현재 노드에서 신규로 방문한 인접노드의 갯수 체크
    for next in graph[current]:
        if not visit[next]:
            count += 1
            count += DFS(next)  # 자식 노드에서 반환한 결과도 추가
    
    return count  # 현재 및 자식 노드에서 신규로 방문한 인접 노드들의 총 개수


N = int(stdin.readline())
M = int(stdin.readline())
graph = [[]for _ in range(N+1)]  # 인접노드를 위한 2차원 배열
# 인접노드표 작성
for m in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(N+1)]
result = DFS(START)
stdout.write(str(result))

