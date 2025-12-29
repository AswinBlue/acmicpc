# https://www.acmicpc.net/problem/11438
# LCA 2
from sys import stdin, stdout, setrecursionlimit
import time
import math


MAX_N = 100000
MAX_M = 100000
ROOT = 1  # root node가 1이라고 문제에서 주어짐
setrecursionlimit(MAX_N)

def Print(*args):
    # print(*args)
    return

def DFS(current):
    global parent, visit, graph, depth  # 전역변수 사용
    visit[current] = 1

    for next in graph[current]:
        if visit[next] == 1:
            continue
        parent[next][0] = current  # parent 설정
        depth[next] = depth[current] + 1  # depth 설정
        DFS(next)

start_time = time.time()

N = int(stdin.readline())
limit = math.ceil(math.log2(MAX_N))  # MAX_N에 기반해 DP가 필요한 한계치 설정

graph = [[] for _ in range(N+1)]
parent = [[0 for _ in range(limit+1)] for _ in range(N+1)]  # parent[i][j] 는 i부터 2^j 번 상위 node로 이동했을 때 도착하는 node 값이다. 
depth = [-1 for _ in range(N+1)]
parent[ROOT][0] = 1
depth[ROOT] = 0

# 두 정점간의 간선을 알려준다고 했다. a 와 b 중 어느것이 parent인지는 정해주지 않았음
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
Print('간선', graph)


# 전체 node들을 순회하며 parent를 확정짓고 depth를 측정한다. 
visit = [0 for _ in range(N+1)]  # DFS 순회를 위한 방문 체크
DFS(ROOT)

Print('세팅', parent, depth)

# sparse table 작성
for i in range(1, limit+1):
    for j in range(1, N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

Print('테이블', limit, parent)

# 두 node 입력받아 결과 출력
M = int(stdin.readline())
result = ''
for _ in range(M):
    a, b = map(int, stdin.readline().split())

    # a 가 더 depth가 깊도록 swap
    if depth[a] < depth[b]:
        a, b = b, a 
    diff = depth[a] - depth[b]
    for digit in range(limit, -1, -1):
        if diff & (1 << digit) > 0:
            a = parent[a][digit]  # 2^digit 번 parent로 거슬러 올라간 수를 sparse table에서 참조
            Print('depth', a, diff, digit)

    # 위 과정을 거치면 a, b는 depth가 같아진다. 
    # 이때, a와 b가 같으면 공통부모를 찾은 것
    if a == b:
        result += '{}\n'.format(a)
    else:
        # 공통 부모를 찾지 못했다면, 이후 최소 공통 조상을 찾아 올라감
        # 큰 값부터 거꾸로 시도한다. 2진법으로 모든 수를 표현할 수 있듯이, 2^i 를 더하여 공통 부모까지 거리 x를 찾는 방식이다. 
        for i in range(limit, -1, -1):
            # 값을 확인했을 때, 조상이 같다면 더 낮은 보폭으로 이동하여 확인 필요
            if parent[a][i] != parent[b][i]:
                # Print('climb', a, b)
                # 값을 2^i만큼 이동했을 때, 조상이 다르다면 해당 보폭만큼 이동
                a = parent[a][i]
                b = parent[b][i]
        # 위 과정을 거치면 parent[a][0] 혹은 parent[b][0] 가 결과이다. 즉 a, b는 공통 부모의 child가 되어있다. 
        result += '{}\n'.format(parent[b][0])

stdout.write(result)
end_time = time.time()
Print('elapsed:', end_time - start_time)