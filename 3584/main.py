# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상
from sys import stdin, stdout

MAX_N = 10000

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    parent = [None for _ in range(N)]
    depth = [0 for _ in range(N)]
    # 간선 입력받음
    for n in range(N-1):
        a, b = map(int, stdin.readline().split())
        parent[b-1] = a-1
    root = parent.index(None)  # parent가 없는 node는 root
    # depth 계산 O(n*log(n))
    for i in range(0, N):
        ptr = i
        d = 0
        # 이미 계산한 node는 생략
        if depth[ptr] != 0:
            continue
        # 올라가며 depth 계산
        while ptr != None:
            ptr = parent[ptr]
            d += 1
        # 자신 및 부모 node에 depth 적용
        ptr = i
        while ptr != None:
            depth[ptr] = d
            d -= 1
            ptr = parent[ptr]
    
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1


    # 둘의 depth를 같게 만듬
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[a] < depth[b]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    # 결과 출력
    stdout.write('{}\n'.format(a+1))