# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

from sys import stdin, stdout

MIN_N = 5
MAX_N = 25

DUMMY_VALUE = 9999

def find_root(group, node):
    ptr = node
    while group[ptr] >= 0:
        ptr = group[ptr]

    root = ptr

    # collapse. skiewed tree 형태에 의해 find가 느려지는걸 방지
    # 동작 효율을 위한 과정으로, 생략해도 결과에는 무방
    ptr = node
    while group[ptr] >= 0:
        tmp = group[ptr]
        group[ptr] = root
        ptr = tmp

    return root

N = int(stdin.readline())
town = [None for _ in range(N)]
for n in range(N):
    town[n] = stdin.readline().strip()

def merge(group, A, B):
    root_a = find_root(group, A)
    root_b = find_root(group, B)

    # root가 같다면 병합 필요없음
    if root_a == root_b:
        return

    # child가 더 많은 쪽이 최종 root가 된다.
    if group[root_a] <= group[root_b]:
        group[root_a] += group[root_b]
        group[root_b] = root_a
    else:
        group[root_b] += group[root_a]
        group[root_a] = root_b



# 그래프를 탐색하며 union find 실행
group = [-1 for _ in range(N*N)]  # 2차원배열 대신 1차원 N * N 배열 사용

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    for j in range(N):
        # 1이 집이 있는곳을 뜻함. 붙어있는 1끼리 그룹을 구해야 한다.
        if town[i][j] == '0':
            # 2차원 배열을 1차원 배열로 폈을 때 index 구하기
            A = i * N + j
            group[A] = DUMMY_VALUE  # 집이 없는곳은 그룹에서 제외
            continue
        for dir in range(4):
            x = i + dx[dir]
            y = j + dy[dir]

            if x >= 0 and x < N and y >= 0 and y < N and town[x][y] == '1':
                # 2차원 배열을 1차원 배열로 폈을 때 index 구하기
                A = i * N + j
                B = x * N + y
                # union find를 위해 병합작업 수행
                merge(group, A, B)

result = []
# union find 최종 결과로 문제에서 원하는 형태 답 출력
for g in group:
    # 음수인 경우가 각 집단의 root이며, 그 절대값은 집단의 크기를 의미한다.
    if g < 0:
        result.append(-g)

# 오름차순으로 정렬
result.sort()

# 출력
stdout.write('{}\n'.format(len(result)))
for r in result:
    stdout.write('{}\n'.format(r))

        
