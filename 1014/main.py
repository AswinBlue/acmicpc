# https://www.acmicpc.net/problem/1014
# 컨닝

<<<<<<< HEAD
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
# 컨닝이 가능한 자리의 관계를 그래프로 표현한 후 이분 그래프 방식으로 문제를 푼다. 
# König's Theorem (쾨닉 이론) : MVC(minimum vertex cover) 문제는 이분 그래프로 풀 수 있다는 정리
#     MVC값은 이분 그래프의 최대 유량과 동일하다. (이분 매칭 알고리즘)
# MVC(minimum vertex cover) : 그래프에서 최소한의 vertex만을 선택하여 만든 그룹 S가 있을 때,
#     전체 그래프의 모든 edge들의 두 끝점 중 하나가 S에 포함된 vertex에 맞닿아 있다면,
#     vertex 조합 S는 MVC가 된다. 
# 단서 1. 컨닝 관계를 그래프로 표현한다면 간선이 하나도 없는 vertex들을 최대한 많이 선택하는 문제가 된다.
#         즉, MVC를 구하고, 여집합을 찾아내면 정답이 된다. 
# 단서 2. 쾨닉의 이론에 의해 MVC는 이분 그래프로 풀 수 있다. 컨닝 관계를 그래프로 그리고, 이분 그래프가 나오는지 확인해본다. 
#         서로 간선이 없는 vertex 를 그룹지으면 두 그룹으로 나타낼 수 있다.
#         즉, 홀수열과 짝수열 vertex들이 대칭되는 이분 그래프가 표현되는 것을 알 수 있다.
# [참조] 이분 그래프란 그래프의 인접한 vertex를 서로 다른 색으로 칠할 때, 두 가지 색으로 모두 색칠이 가능한 그래프이다. (즉, 홀수 사이클이 없음)
def method1(N, M, table):
    # 1. 입력을 그래프로 표현한다. (i,j) 위치는 index "M*i+j" 로 표현하며, G[M*i+j]는 (i,j) 에서 컨닝 가능한 위치의 index 집합이다. 
    G = [[] for _ in range(N * M)]
    total_seat = 0  # 부서지지 않은 책상의 갯수도 덤으로 같이 센다
    for i in range(N):
        for j in range(M):
            current = M * i + j
            if table[i][j] == AVAILABLE_TABLE:
                total_seat += 1
            else:
                continue  # 부서진 테이블 생략
            # 부서진 테이블은 간선을 긋지 않는다. 어차피 사람이 앉지 못하므로 컨닝을 고려할 필요가 없기 때문
            # 간선은 짝수열 -> 홀수열 방향으로만 긋는다. (이분 매칭 형태를 만들기 위해)
                
            if i > 0 and j > 0 and table[i-1][j-1] != BROKEN_TABLE:
                if j % 2 == 0:
                    G[current].append(current - M - 1)
                else:
                    G[current - M - 1].append(current)

            if i > 0 and j < M - 1 and table[i-1][j+1] != BROKEN_TABLE:
                if j % 2 == 0:
                    G[current].append(current - M + 1)
                else:
                    G[current - M + 1].append(current)

            if j > 0 and table[i][j-1] != BROKEN_TABLE:
                if j % 2 == 0:
                    G[current].append(current - 1)
                else:
                    G[current - 1].append(current)

            if j < M - 1 and table[i][j+1] != BROKEN_TABLE:
                if j % 2 == 0:
                    G[current].append(current + 1)
                else:
                    G[current + 1].append(current)

    Print(G)
    # 2. 이분 매칭 알고리즘을 정의한다. 
    # G : 그래프
    # visit : 특정 vertex a(in A)와 연결된 b(in B)를 찾을 때, 무한 순회를 막기 위해 먼저 확인한 vertex를 체크하는 용도.
    #         a가 변경되면 visit  배열은 초기화되어야 한다.
    # paired : paired[x] = x와 연결된 vertex의 index
    # return : 짝을 찾았다면 true, 찾지 못헀다면 false 반환
    def bipartite(G, visit, paired, current):
        visit[current] = True  # 무한반복을 막기위한 체크
        result = False  # 결과
        for next in G[current]:  # current에 연결된 vertex들을 체크
            if paired[next] is None:  # 'next' node가 페어링된 적 없다면
                # idx와 페어링
                paired[next] = current
                paired[current] = next
                result = True
                break
            else:
                assigned = paired[next]
                if visit[assigned] == False \
                    and bipartite(G, visit, paired, assigned) == True:  # 'assigned'가 이번 순회에 사용되지 않았고, 다른 자리로 재배치가 가능한 경우
                    paired[next] = current
                    paired[current] = next
                    result = True
                    break
        # 그 외의 경우, 배치 실패
        return result  
    
    # 3. 이분된 vertex 그룹을 A/B라 할 때, 전체 A vertex에 대해 순회하며 B와 짝을 이루도록 이분매칭 알고리즘을 수행한다. 
    paired = [None for _ in range(N * M)]  # A와 매칭된 B의 값
    invalid_seat = 0  # bipartite로 짝 지어진 node들의 갯수
    for i in range(N):
        for j in range(M):
            # 짝수 열을 A, 홀수열을 B로 취급한다.
            if table[i][j] == AVAILABLE_TABLE and j % 2 == 0:  # 부서진 책상을 제외하고 모든 짝수열 책상에 대해 순회한다. 
                idx = i * M + j
                visit = [False for _ in range(N * M)]  # visit은 idx가 바뀔 때 마다 갱신 필요
                if bipartite(G, visit, paired, idx) == True:
                    invalid_seat += 1
                    Print(f"({i},{j}) -> {idx}, {total_seat - invalid_seat}")

        Print(paired)

    return total_seat - invalid_seat


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
        if i % 2 == 0:
            result = method1(N, M, table)
        else:
            result = method2(N, M, table)
        print(result)
=======
BROKEN = 'x'
EMPTY = '.'

DEBUG = 1
def Print(*args):
    if DEBUG:
        print(*args)
    
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    desk = []
    for n in range(N):
        desk.append(input())

    # >접근 전략
    # Dynamic programming으로 모든 경우를 고려한다.
    # DP[i][j][0] 에는 (i, j), (i-1, j) 영역에 사람이 없을 경우 iXj 크기의 영역에서 얻을 수 있는 최대값을 저장한다.
    # DP[i][j][1] 에는 (i, j) 또는 (i-1, j) 영역에 사람이 있을 경우 iXj 크기의 영역에서 얻을 수 있는 최대값을 저장한다.

    DP = [[[0, 0] for _ in range(M)] for _ in range(N)]
    # 초기값 세팅
    if desk[0][0] == EMPTY:
        DP[0][0][1] = 1

    # (i,0) 열 세팅
    for i in range(1, N):
        DP[i][0][0] = max(DP[i-1][0][1], DP[i-1][0][0])
        if desk[i][0] == EMPTY:
            DP[i][0][1] = max(DP[i-1][0][1] + 1, DP[i][0][0])
        else:
            DP[i][0][1] = DP[i][0][0]
    # (0,j) 행 세팅  

    for j in range(1, M):
        DP[0][j][0] = max(DP[0][j-1][0], DP[0][j-1][1])
        if desk[0][j] == EMPTY:
            DP[0][j][1] = max(DP[0][j-1][0] + 1, DP[0][j][0])
        else:
            DP[0][j][1] = DP[0][j][0]

    # 나머지 값 순회
    for i in range(1, N):
        for j in range(1, M):
            DP[i][j][0] = max(DP[i][j-1][0], DP[i][j-1][1], DP[i-1][j][0])

            A = max(DP[i-1][j]) - max(DP[i-1][j-1])
            B = max(DP[i][j-1]) - max(DP[i-1][j-1])
            C = max(A, B) + max(DP[i-1][j-1])

            if desk[i][j] == EMPTY:
                DP[i][j][1] = C + 1


            # if desk[i][j] == EMPTY and desk[i-1][j] == EMPTY:
            #     DP[i][j][1] = max(DP[i][j][0], DP[i][j-1][0] + 2, DP[i][j-1])
            #     Print(i, j, '+2')
            # elif desk[i][j] == EMPTY:
            #     DP[i][j][1] = max(DP[i][j][0], DP[i][j-1][0] + 1)
            #     Print(i, j, '+1')
            # elif desk[i-1][j] == EMPTY:
            #     DP[i][j][1] = max(DP[i][j][0], DP[i][j-1][0] + 1)
            #     Print(i, j, '+1_')
            # else:
            #     DP[i][j][1] = DP[i][j][0]
            #     Print(i, j, '+0')
            
    Print('\tTC {} : {}'.format(t+1,  DP))
    
>>>>>>> a7d0eec (12904 / A와 B)
