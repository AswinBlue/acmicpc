# https://www.acmicpc.net/problem/11066
# 파일 합치기
from sys import stdin, stdout

MAX_FILE_SIZE = 10000
MAX_K = 500
MAX = 9999999999

T = int(stdin.readline())
for t in range(T):
    K = int(stdin.readline())
    # DP[i][j] 는 j부터 시작하는 길이가 i인 소설 조합의 최소 비용이다. 
    cost = [[0 for _ in range(K+1)] for _ in range(K+1)]
    # 길이 값은 부분합으로 갖고 있는다.
    lengths = list(map(int,stdin.readline().split()))
    for i in range(1, len(lengths)):
        lengths[i] += lengths[i-1]
    lengths.insert(0, 0) # 1부터 시작하도록 dummy 데이터 추가


    # 폭이 width 인 조합의 최소비용을 dynamic programming으로 계산
    for width in range(2, K+1):
        for idx in range(1, K-width+2):
            min_val = MAX
            for left_width in range(1, width):
                right_width = width - left_width
                # [left][right] 조각을 서로 더했을 때를 비교한다.
                # 모든 [idx:idx+left] + [idx+left:idx+width] 의 경우 중 min 값을 취한다.
                min_val = min(cost[left_width][idx] + cost[right_width][idx+left_width] + (lengths[idx+width-1] - lengths[idx-1]), min_val)

            cost[width][idx] = min_val
    # print(cost)

    result = cost[K][1]
    stdout.write('{}\n'.format(result))