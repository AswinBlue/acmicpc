# https://www.acmicpc.net/problem/1006
# 습격자 초라기

MAX_N = 10000
MAX_W = 10000

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

# Dynamic Programming으로 문제를 해결하는 함수
# param[out] target : 함수 return값으로 반환할 DP 배열의 index 
def solve_DP(target):
    global N, W, sector

    DP = [[0 for _ in range(3)] for _ in range(N)]  # N by 3 배열
    # 초기값 세팅
    DP[0][0] = 1 if sector[0][0] + sector[1][0] <= W else 2
    DP[0][1] = 1
    DP[0][2] = 1

    if N > 1:
        DP[1][0] = DP[0][0] + 2  # max값 설정
        # 가로 case 고려
        if sector[0][0] + sector[0][1] <= W and sector[1][0] + sector[1][1] <= W:
            # 가로로 두개
            DP[1][0] = min(2, DP[1][0])
        elif sector[0][0] + sector[0][1] <= W or sector[1][0] + sector[1][1] <= W:
            # 가로하나 개별 두개
            DP[1][0] = min(3, DP[1][0])

        # 세로 case 고려
        if sector[0][1] + sector[1][1] <= W:
            # 1번 열이 세로로 묶을 수 있을 경우
            DP[1][0] = min(DP[1][0], DP[0][0] + 1)

        DP[1][1] = DP[0][2] + 1 if sector[0][0] + sector[0][1] <= W else DP[0][0] + 1
        DP[1][2] = DP[0][1] + 1 if sector[1][0] + sector[1][1] <= W else DP[0][0] + 1

    for i in range(2, N):
        # (1) 위아래 모두 채우는 case
        # 1. 위아래 모두 개별
        DP[i][0] = DP[i-1][0] + 2
        # 2. 위아래 모두 가로
        if sector[0][i-1] + sector[0][i] <= W and sector[1][i-1] + sector[1][i] <= W:
            DP[i][0] = min(DP[i-2][0] + 2, DP[i][0])
        # 3. 위쪽만 가로, 아래쪽은 개별
        if sector[0][i-1] + sector[0][i] <= W:
            DP[i][0] = min(DP[i-1][2] + 2, DP[i][0])
        # 4. 아래쪽만 가로, 위쪽은 개별
        if sector[1][i-1] + sector[1][i] <= W:
            DP[i][0] = min(DP[i-1][1] + 2, DP[i][0])
        # 5. 위아래 세로
        if sector[0][i] + sector[1][i] <= W:
            DP[i][0] = min(DP[i-1][0] + 1, DP[i][0])
        
        # (2) 위쪽만 채우는 case
        # 가로로 길게 vs 단일
        DP[i][1] = DP[i-1][0] + 1
        if sector[0][i-1] + sector[0][i] <= W:
            DP[i][1] = min(DP[i-1][2] + 1, DP[i][1])

        # (3) 아래쪽만 채우는 case
        # 가로로 길게 vs 단일
        DP[i][2] = DP[i-1][0] + 1
        if sector[1][i-1] + sector[1][i] <= W:
            DP[i][2] = min(DP[i-1][1] + 1, DP[i][2])

    Print(DP)
    return DP[target]


T = int(input())
for t in range(T):
    N, W = map(int, input().split())

    sector = [None, None]
    sector[0] = list(map(int, input().split()))
    sector[1] = list(map(int, input().split()))

    # >> 접근 전략
    # 1. 섹터가 가로 1, 세로 2 크기인 경우부터 가로 N인 경우까지 점점 늘려가며 최소 투입 부대를 구한다.
    # 2. Dynamic programming을 이용해 구할 것이며, DP[N][3] 배열을 사용할 것이다.
    #    DP[n][0]은 n번째 열 위아래를 모두 처리한 경우(단일이든 개별이든)
    #    DP[n][1]은 n번째 열 위쪽만 처리하고, 아래쪽은 보류한 경우
    #    DP[n][2]는 n번째 열 아래쪽만 처리하고 위쪽은 보류한 경우를 의미한다.
    #    이 세가지 경우만 있으면 블럭을 놓을 수 있는 모든 경우에 대해 메모이제이션이 가능하게 된다.
    # 3. 이때 각각 DP[N][0], DP[N][1], DP[N][2] 을 구하고 섹터 배치가 순환형인것을 고려한 후 최소값을 취한다.
    
    # sector는 원형으로 이루어져 있어 순환형으로 처음과 끝 만나는 부분 처리가 필요하다.
    # 처음과 끝부분이 (1) 둘다 안 겹치는 경우 (2) 위쪽이 가로로 겹치는 경우 (3) 아래쪽이 가로로 겹치는 경우 (4) 둘다 겹치는 경우 를 고려한다.

    min_result = 9999999999  # 최종 결과

    # (1) 둘다 안 겹치는 경우
    Print('case1')
    result = solve_DP(N-1)
    min_result = min(min_result, result[0])
    
    # (2) 위쪽이 가로로 겹치는 경우 고려
    if N > 1:
        if sector[0][0] + sector[0][N-1] <= W:
            Print('case2')
            tmp1 = sector[0][0]
            tmp2 = sector[0][N-1]
            sector[0][0] = sector[0][N-1] = W  # N-1과 0은 이미 묶여있다고 가정한다. 다른 sector와 묶이지 않도록 값 변경
            result = solve_DP(N-1)
            # 다음 계산을 위해 배열값 원상복구
            sector[0][0] = tmp1
            sector[0][N-1] = tmp2

            min_result = min(min_result, result[2])
        
        # (3) 아래쪽이 가로로 겹치는 경우 고려
        if sector[1][0] + sector[1][N-1] <= W:
            Print('case3')
            tmp1 = sector[1][0]
            tmp2 = sector[1][N-1]
            sector[1][0] = sector[1][N-1] = W  # N-1과 0은 이미 묶여있다고 가정한다. 다른 sector와 묶이지 않도록 값 변경
            result = solve_DP(N-1)
            # 다음 계산을 위해 배열값 원상복구
            sector[1][0] = tmp1
            sector[1][N-1] = tmp2

            min_result = min(min_result, result[1])

        # (4) 둘 다 겹치는 경우 고려
        if sector[0][0] + sector[0][N-1] <= W and sector[1][0] + sector[1][N-1] <= W:
            Print('case4')
            sector[0][0] = sector[0][N-1] = sector[1][0] = sector[1][N-1] = W  # N-1과 0은 이미 묶여있다고 가정한다. 다른 sector와 묶이지 않도록 값 변경
            result = solve_DP(N-2)
            
            min_result = min(min_result, result[0])

    print(min_result)