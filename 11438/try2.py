# https://www.acmicpc.net/problem/11438
# LCA 2
from sys import stdin, stdout, setrecursionlimit
from collections import deque
import math
import time

MAX_N = 100000
MAX_M = 100000
ROOT = 1  # root node가 1이라고 문제에서 주어짐
setrecursionlimit(MAX_N)

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

def DFS(current, current_depth, graph, parent, depth, visit):
    # 현재 구현된 재귀 기반의 DFS는 Python에서 함수 호출 오버헤드가 커서 시간 초과를 유발하는 주원인입니다.
    # 특히 N=100,000일 때 트리가 한쪽으로 길게 늘어지면 재귀 깊이가 깊어져 매우 느려집니다.
    # 해결책: **BFS (너비 우선 탐색)** 알고리즘을 사용하여 반복문(while)으로 구현이 필요합니다.
    # collections.deque를 사용하여 큐를 구현하고, 부모와 깊이(depth)를 설정하면 훨씬 빠르고 안정적입니다.
    visit[current] = 1
    depth[current] = current_depth

    for next in graph[current]:
        if visit[next] == 1:
            continue
        parent[next][0] = current  # parent 설정
        DFS(next, current_depth + 1, graph, parent, depth, visit)

def BFS(start, graph, parent, depth):
    global N
    queue = deque([start])
    visit = [0 for _ in range(N+1)]  # BFS 순회를 위한 방문 체크
    visit[start] = 1
    depth[start] = 0

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if visit[next] == 0:
                visit[next] = 1
                parent[next][0] = current  # parent 설정
                depth[next] = depth[current] + 1  # depth 설정
                queue.append(next)

'''
핵심 아이디어
[BFS]
1. 사용 이유:
    Python의 재귀 깊이 제한과 함수 호출 오버헤드 문제를 피하기 위해 DFS 대신 BFS를 사용합니다.
    BFS는 큐를 사용하여 반복문으로 구현되므로, 깊은 트리 구조에서도 안정적으로 작동합니다.
2. 원리:
    BFS는 시작 노드에서부터 인접한 노드들을 차례로 방문하며, 각 노드의 부모와 깊이를 설정합니다.

[Sparse Table (희소 배열)]
1. 사용 이유:
    일반적인 LCA 알고리즘은 부모를 한 칸씩 거슬러 올라가므로 최악의 경우 O(N)이 걸립니다.
    쿼리가 많을 경우(M=100,000) 전체 시간 복잡도가 O(NM)이 되어 시간 초과가 발생합니다.
    희소 배열을 사용하면 2^i 칸씩 점프하여 조상을 찾을 수 있어, 각 쿼리를 O(log N)에 처리할 수 있습니다.
2. 원리 (Dynamic Programming):
    점화식: parent[j][i] = parent[parent[j][i-1]][i-1]
    설명: "2^i번째 조상"은 "2^(i-1)번째 조상"의 "2^(i-1)번째 조상"과 같습니다. (예: 8번째 조상 = 4번째 조상의 4번째 조상)
'''

if __name__ == "__main__":
    global N
    N = int(stdin.readline())
    limit = math.ceil(math.log2(N))  # N에 기반해 DP가 필요한 한계치 설정

    graph = [[] for _ in range(N+1)]
    parent = [[0 for _ in range(limit+1)] for _ in range(N+1)]  # parent[i][j] 는 i부터 2^j 번 상위 node로 이동했을 때 도착하는 node 값이다. 
    depth = [-1 for _ in range(N+1)]

    start_time = time.time()

    # 두 정점간의 간선을 알려준다고 했다. a 와 b 중 어느것이 parent인지는 정해주지 않았음
    for _ in range(N-1):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 전체 node들을 순회하며 parent를 확정짓고 depth를 측정한다. 
    BFS(ROOT, graph, parent, depth)

    # sparse table 작성, 2^i 만큼 올라갔을 때의 조상을 미리 저장
    # parent[j][i]는 j의 2^i번째 조상. 해당 위치에 조상이 없으면 0
    # parent[ROOT][0]은 0(기본값)으로 유지해야 recursion에 의한 오류 발생을 막을수 있다.
    for i in range(1, N+1):
        Print(f'[{i}] {parent[i]}')

    for i in range(1, limit+1):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

    Print('limit:', limit, "\nparent:")
    for i in range(1, N+1):
        Print(f'[{i}] {parent[i]}')

    # 두 node 입력받아 결과 출력
    M = int(stdin.readline())
    results = []
    for _ in range(M):
        a, b = map(int, stdin.readline().split())

        # a 가 더 depth가 깊도록 swap
        if depth[a] < depth[b]:
            a, b = b, a 
        diff = depth[a] - depth[b]
        Print(f'diff:{diff}, a:{a}, b:{b}')

        # 공통부모를 찾기 위해 a와 b의 depth가 동일해 질 때 까지 a를 a의 2^i번째 조상으로 교체한다
        for i in range(limit, -1, -1):
            if diff >= (1 << i):
                a = parent[a][i]
                diff -= (1 << i)

        # 위 과정을 거치면 a, b는 depth가 같아진다.
        # 이때, a와 b가 같으면 공통부모를 찾은 것
        if a == b:
            results.append(str(a))
            Print(f'LCA found:{results}')
        else:
            # 공통 부모를 찾지 못했다면, 이후 최소 공통 조상을 찾아 올라감
            # 큰 값부터 거꾸로 시도한다. 2진법으로 모든 수를 표현할 수 있듯이, 2^i 를 더하여 공통 부모까지 거리 x를 찾는 방식이다. 
            # 큰 보폭(2^limit)부터 시작해서, 두 노드의 조상이 다를 때만 이동
            # 조상이 같다면? -> LCA보다 더 위에 있다는 뜻이므로 이동하지 않고 보폭을 줄여서 더 아래쪽(LCA에 가까운 쪽)을 탐색
            # 조상이 다르다면? -> 아직 LCA에 도달하지 못했다는 뜻이므로 해당 보폭만큼 위로 이동
            for i in range(limit, -1, -1):
                # 2^i만큼 이동했을 때 조상이 다르다면, 두 노드 모두 이동
                Print(f'i:{i}, a:{a}, b:{b}, parent[a][i]:{parent[a][i]}, parent[b][i]:{parent[b][i]}')
                if parent[a][i] != parent[b][i]:
                    a = parent[a][i]
                    b = parent[b][i]
            # 위 과정을 거치면 parent[a][0] 혹은 parent[b][0] 가 결과이다. 즉 a, b는 공통 부모의 child가 되어있다. 
            results.append(str(parent[a][0]))
            Print(f'LCA found:{results}')

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")

    stdout.write('\n'.join(results))