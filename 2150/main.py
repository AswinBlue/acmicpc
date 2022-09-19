# https://www.acmicpc.net/problem/2150
# Strongly Connected Component
from sys import stdin, stdout, setrecursionlimit

MAX_V = 10000
MAX_E = 100000
DEBUG = 0

setrecursionlimit(MAX_V + 10)

def Print(*args):
    if DEBUG:
        print(*args)

def DFS(current):
    global graph, visit, stack, result
    visit[current] = True
    idx = len(stack)  # current node가 stack에 들어간 index
    stack.append(current)

    min_idx = idx  # 자신 및 자식 node에서 stack을 역행했을 때 도달할 수 있는 최소 index 찾기위함. 초기값으로 자신 설정
    for next in graph[current]:
        if not visit[next]:
            min_idx = min(min_idx, DFS(next))  # 자식 node의 결과와 비교해서 최소값을 취함

    # 갈 수 있는 모든 node에 대해 DFS를 수행했다면, SCC 조건 검사
    # stack의 idx 위치에서 [0:idx] node 중 어딘가로 갈 수 있는 edge가 있는지 확인, 즉 DFS 를 통해 왔던 경로를 어디까지 거슬러 올라갈 수 있는지 체크
    # stack에 한개만 남아있고, 더 갈 곳이 없고, 부모 node로도 가지 못하는 경우도 SCC로 취급
    for i in range(0, idx):
        if stack[i] in graph[current]:
            min_idx = min(min_idx, i)
            break

    Print('check', current, graph[current], idx, min_idx)
    if min_idx == idx:
        # 현재 node보다 더 위로 갈 수 없다면, stack[idx:] 를 하나의 SCC로 취급
        Print('push', current, stack[idx:], stack[:idx])
        result.append(stack[idx:])  # 결과에 추가
        stack = stack[:idx]  # stack 에서 제거

    Print('DFS', current, stack, result)
    return min_idx  # 현재 node(idx) 및 자식 node에서 stack[:idx] 중 도달 가능한 최소 지수를 반환

if __name__ == '__main__':
    V, E = map(int, stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for e in range(E):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)

    visit = [False for _ in range(V+1)]  # node 방문 여부를 체크
    stack = []  # 타잔 방식으로 SCC를 찾기 위한 스택. 방문할때마다 push하고, 특정 조건일때 pop함
    result = []  # SCC 결과 그룹의 list
    # 전체 node에 대해 빠짐없이 DFS 수행(순서는 상관없음)
    for i in range(1, V+1):
        if not visit[i]:
            DFS(i)

    # 각 SCC를 오름차순으로 정렬
    for r in result:
        r.sort()
        r.append(-1)
    # 전체 결과 배열을 오름차순으로 정렬
    result.sort()

    # 결과 출력
    out = '{}\n'.format(len(result))
    for r in result:
        out += ' '.join(map(str,r)) + '\n'
    
    stdout.write(out)
