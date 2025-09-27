# https://www.acmicpc.net/problem/2533
# 사회망 서비스(SNS)

import sys
from collections import deque
DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

# 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6 + 10)

def solve_dp(current, parent, friends, dp):
    """
    DFS를 이용하여 트리 DP를 수행합니다.
    dp[node][0]: node가 얼리 어답터가 아닐 때, 해당 서브트리의 최소 얼리 어답터 수
    dp[node][1]: node가 얼리 어답터일 때, 해당 서브트리의 최소 얼리 어답터 수
    """
    dp[current][1] = 1  # leaf node인 경우, 현재 노드가 얼리 어답터일 경우, DP값은 1. leaf node가 아닐경우 아래에서 계산됨

    for neighbor in friends[current]:
        if neighbor != parent:  # 부모 노드는 건너뜀
            solve_dp(neighbor, current, friends, dp)
            # leaf node가 아닐 경우 dp 값 추가 계산
            # case 1. 현재 노드가 얼리 어답터가 아니면, 모든 자식은 반드시 얼리 어답터여야 함
            dp[current][0] += dp[neighbor][1]
            # case 2. 현재 노드가 얼리 어답터이면, 자식은 얼리 어답터이거나 아니거나 상관없음 (둘 중 최솟값 선택)
            dp[current][1] += min(dp[neighbor][0], dp[neighbor][1])

if __name__ == '__main__':
    # get inputs and create tree
    # 빠른 입력을 위해 sys.stdin.readline 사용
    N = int(sys.stdin.readline())
    friends = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = map(int, sys.stdin.readline().split())
        friends[x].append(y)
        friends[y].append(x)

    # DP 테이블 초기화
    dp = [[0, 0] for _ in range(N + 1)]

    # 임의의 노드(1)를 루트로 하여 DP 시작
    root = 1
    solve_dp(root, 0, friends, dp) # 부모가 없는 루트의 부모는 0으로 가정
    
    print(min(dp[root][0], dp[root][1]))
