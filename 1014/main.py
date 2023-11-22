# https://www.acmicpc.net/problem/1014
# 컨닝

import math

MAX_N = 10
MAX_M = 10
BROKEN_TABLE = 'x'
AVAILABLE_TABLE = '.'

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args, sep='\n')

# 방법 1. Max Flow
# max flow 알고리즘을 사용하여 최대로 많이 앉을 수 있는 자리 갯수를 구한다.
# MVC(minimum vertex cover) : 최소한의 vertex만을 선택하여 모든 edge들이 포함되게 하는 vertex 조합
# König's Theorem (콰닉 이론) : 이분 그래프

# 컨닝을 할 수 있다면 두 vertex 사이에 edge를 긋는다.
# 이렇게 만들어진 그래프는 이분 그래프가 된다. 
# 이분 그래프란 그래프의 인접한 vertex를 서로 다른 색으로 칠할 때, 두 가지 색으로 모두 색칠이 가능한 그래프이다. (즉, 홀수 사이클이 없음)
# 여기서 vertex를 하나씩 골라 해당 vertex와 그에 붙은 edge를 제거한다. 
# edge가 하나도 없게 되면 컨닝이 불가능한 배치를 의미하므로, edge가 하나도 남지 않을 떄 까지 제거한다. 
# 이러면 남은 vertex의 갯수가 최대 배치 가능한 자리 수가 된다.
# 즉, minimum vertex cover를 구하고, 그 여집합을 구하면 되는 것이다.

# 방법 2. Dynamic programming
# DP만으로는 timeout이 발생할 계산 분량이지만, bit masking을 곁들이면 시간 안에 해결이 가능하다.
# 단서 1. n행까지만 고려하여 최대로 앉을 수 있는 인원 x_n을 찾았다면, n+1행 까지 고려할 때는 n행까지 고려한 결과 x에 얼마를 더 놓을수 있는지 체크하면 된다. (DP로 처리 가능)
# 단서 2. 자리 배치를 행 단위로 끊어 봤을 때, 컨닝을 할 수 있는 자리는 해당 행과 그 이전 행이다. (DP 계산시 n-1만 고려하면 됨)
# 단서 3. 열의 길이는 최대 10이므로, 한 행의 자리 배치를 bit 연산을 사용하여 int 형으로 표현할 수 있다. (bit로 표시 불가능하면 해결 불가)
def method2(N, M, table):
    # 1. 한 행만 고려했을 때, 컨닝을 할 수 없는 배치와 그 배치에서 선택된 책상의 갯수를 저장한다.
    candidate = []
    for i in range(0, 1 << M): # 아무 책상도 선택하지 않은 상태 ~ 모든 책상을 선택한 상태까지 포함
        adjacent = False
        cnt = 0 # 수에 1이 얼마나 들어있는지 체크하기 위한 변수
        for j in range(M-1): # 0 ~ M-2번까지 bitshifting 해가며 
            mask = 3 << j  # 011, 인접한 자리에 붙어있는지 체크하기 위한 마스크
            if (i & mask) == mask: # 인접한 경우
                adjacent = True
                break
            if (i & (1 << j)):
                cnt += 1

        if not adjacent: # 인접하지 않게 배치된 경우
            # 마지막 자리 추가 계산
            if (i & (1 << M-1)):
                cnt += 1
            candidate.append((i, cnt)) # bit표기와 자리의 수를 pair로 저장
    Print('candidate: ', candidate)

    # 2. 부서진 자리도 bitmasking으로 비교하기 위해 입력값을 2차원배열에서 1차원 bit배열로 수정한다.
    mask_table = [0 for _ in range(N)]
    for i in range(N):
        number = 0
        for j in range(M):
            if table[i][j] == BROKEN_TABLE:
                pass  # 부서진 책상은 bit 0으로 표기
            elif table[i][j] == AVAILABLE_TABLE:
                number += (1 << j)  # 사용가능한 책상은 bit 1로 표기
        mask_table[i] = number

    # 3. DP를 수행한다.
    DP = [[0 for _ in range(1 << M)] for _ in range(N)] # DP[i][j] : i행의 배치를 j 형태로 했을 때 0~i행까지 컨닝이 되지 않게 배치할 수 있는 최대 자리
    # i==1인 경우 초기설정
    for current, current_num in candidate:
        if mask_table[0] & current == current : # 부서진 책상에 배치한 경우가 아니라면 ok
            DP[0][current] = current_num
        # 부서진 책상에 배치한 경우라면 skip 

    # i==2인 경우부터 DP 진행
    for i in range(1, N):
        for current, current_num in candidate:  # i번쨰 자리 배치
            if current == 0:  # i번째 행에 하나도 배치하지 않는 경우
                DP[i][current] = max(DP[i-1])  # 이전 배치중 가장 큰 값으로 설정 가능
            elif mask_table[i] & current != current :
                continue  # 부서진 책상에 배치한 경우라면 skip 

            for prev, prev_num in candidate:  # 앞자리 배치
                if mask_table[i-1] & prev != prev :
                    continue  # 부서진 책상에 배치한 경우라면 skip 
                # i번째 행을 current처럼 배치하고, i-1번쨰 행을 prev처럼 배치한 경우, 앞자리 사람을 컨닝 가능한지 체크
                mask_risky = 0 # 컨닝이 가능한 자리를 1로 표시하기 위한 변수

                # 가장자리 앉은사람은 따로 체크
                if current & 1 > 0:
                    mask_risky |= 2 # 2번째 자리는 컨닝 가능(1 << 1)
                if current & (1 << (M - 1)) > 0:
                    mask_risky |= 1 << (M - 2) # M-1번째 자리는 컨닝 가능
                for k in range(1, M - 1):
                    if current & (1 << k) > 0:  # k번째 자리를 선택한 경우라면
                        mask_risky |= (1 << k-1) # k번째 왼쪽자리는 컨닝 가능
                        mask_risky |= (1 << k+1) # k번쨰 오른쪽 자리는 컨닝 가능
                if prev & mask_risky == 0: # 앞자리와 비교 해 봤을 떄 컨닝이 불가능한 배치라면
                    # DP 점화식에 의해 값 결정
                    DP[i][current] = max(DP[i][current], DP[i-1][prev] + current_num)
    
    # 4. 결과 출력
    Print(*DP)
    return max(DP[N-1])



if __name__ == '__main__':
    # get input
    testCase = int(input())
    for i in range(testCase):
        N, M = map(int, input().split())
        table = [None for _ in range(N)]
        for j in range(N):
            A = input()
            table[j] = list(A)
        Print('table: ', *table)
        result = method2(N, M, table)
        print(result)