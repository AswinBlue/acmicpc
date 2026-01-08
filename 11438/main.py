# https://www.acmicpc.net/problem/11438
# LCA 

# Python/PyPy3 최적화를 위한 import
from sys import stdin, stdout, setrecursionlimit
from collections import deque
import math

# Python의 재귀 깊이 제한을 문제의 최대 노드 수에 맞게 설정
setrecursionlimit(100001)

# BFS 함수 최적화
# - PyPy3에서 더 효율적으로 JIT 컴파일되도록 함수 인자로 필요한 변수들을 명시적으로 전달
def BFS(n, graph, parent, depth):
    # '방문' 배열을 리스트 컴프리헨션 대신 곱셈으로 초기화하여 약간의 속도 향상
    visit = [0] * (n + 1)
    
    # 큐(Queue) 초기화 및 루트 노드(1) 설정
    queue = deque([1])
    visit[1] = 1
    depth[1] = 0

    while queue:
        current = queue.popleft()
        
        # 현재 노드의 깊이에 1을 더한 값을 미리 계산
        d = depth[current] + 1
        # 현재 노드에 연결된 이웃 노드들을 순회
        for next_node in graph[current]:
            # 아직 방문하지 않은 노드라면
            if visit[next_node] == 0:
                visit[next_node] = 1
                parent[next_node][0] = current  # 직계 부모 설정
                depth[next_node] = d            # 깊이 설정
                queue.append(next_node)

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

def solution():
    # 매번 sys.stdin.readline을 호출하는 대신, 지역 변수에 할당하여 조회 속도 향상
    input = stdin.readline

    N = int(input())
    
    # 트리의 최대 깊이는 N을 넘지 않으므로, log2(N)을 통해 희소 배열의 크기를 계산
    limit = math.ceil(math.log2(N))

    # 그래프, 부모 배열, 깊이 배열 초기화
    graph = [[] for _ in range(N + 1)]
    # parent[i][j]: i의 2^j 번째 조상
    parent = [[0] * (limit + 1) for _ in range(N + 1)]
    depth = [-1] * (N + 1)

    # N-1개의 간선 정보를 입력받아 그래프 구성
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # BFS를 실행하여 각 노드의 깊이와 직계 부모(parent[][0])를 계산
    BFS(N, graph, parent, depth)

    # 희소 배열(Sparse Table) 채우기 (Dynamic Programming)
    # 점화식: parent[j][i] = parent[parent[j][i-1]][i-1]
    # 의미: j의 2^i번째 조상은 (j의 2^(i-1)번째 조상)의 (2^(i-1)번째 조상)이다.
    for i in range(1, limit + 1):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

    M = int(input())
    results = []
    for _ in range(M):
        a, b = map(int, input().split())

        # 항상 a가 더 깊은 노드가 되도록 swap
        if depth[a] < depth[b]:
            a, b = b, a

        diff = depth[a] - depth[b]

        # a와 b의 깊이를 맞추는 과정 (Binary Lifting)
        # 깊이 차이를 2의 거듭제곱의 합으로 분해하여 점프
        for i in range(limit, -1, -1):
            if diff >= (1 << i):
                a = parent[a][i]
                diff -= 1 << i

        # 깊이를 맞춘 후, a와 b가 다르다면 공통 조상을 찾아 위로 이동
        # 큰 값부터 거꾸로 시도한다. 2진법으로 모든 수를 표현할 수 있듯이, 2^i 씩 이동하며 공통 부모까지 거리 x를 찾는 방식이다. 
        # 큰 보폭(2^limit)부터 시작해서, 두 노드의 조상이 다를 때만 이동
        # 조상이 같다면? -> LCA보다 더 위에 있다는 뜻이므로 이동하지 않고 보폭을 줄여서 더 아래쪽(LCA에 가까운 쪽)을 탐색
        # 조상이 다르다면? -> 2^i ~ 2^(i+1) 사이에 LCA가 있다는 뜻. 기준점을 2^i 위치로 이동하고(a = parent[a][i]) i-1 -> 1 까지 2의 배수로 보폭을 세팅하며(for i in range(limit, -1, -1)) 위 과정 반복
        if a != b:
            for i in range(limit, -1, -1):
                # 조상이 같아지기 직전까지 두 노드를 함께 이동
                if parent[a][i] != parent[b][i]:
                    a = parent[a][i]
                    b = parent[b][i]
            # 마지막으로 한 칸 더 올라가면 최소 공통 조상(LCA)
            a = parent[a][0]
        
        results.append(str(a))

    # 최종 결과를 한 번에 출력하여 입출력 오버헤드 최소화
    stdout.write('\n'.join(results))

if __name__ == "__main__":
    solution()