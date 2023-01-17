# https://www.acmicpc.net/problem/1006
# 습격자 초라기

# 시간초과가 걸린 해결 방법
# broute force는 prominence를 고려해도 시간초과다.
# dynamic programming으로 접근 필요

from sys import setrecursionlimit
setrecursionlimit(10000)

MAX_N = 10000
MAX_W = 10000

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)

# DFS 순회시 현재 좌표를 넣으면 다음 순회할 좌표를 반환하는 함수
def next(visit, x, y):
    x_, y_ = 0, 0
    if x == 0:
        x_, y_ = 1, y
    else:
        x_, y_ = 0, y + 1
    
    if visit[x_][y_] == 0:
        return x_, y_
    else:
        return next(visit, x_, y_)

# 재귀형태로 순환하며 전체 case를 모두 확인하는 함수
def DFS(visit, x, y, result):
    global N, W, sector, min_result

    Print(x, y, visit)
    # 종료 조건, 마지막 sector 체크시
    if y >= N:
        min_result = min(min_result, result)
        Print(min_result)
        return 0
    
    # 후보의 가능성이 없는 case는 더이상 탐색하지 않음
    if result >= min_result:
        return 0

    # 1. 현재 구역만 커버하는 경우
    visit[x][y] = 1
    x_, y_ = next(visit,x,y)
    DFS(visit, x_, y_, result + 1)

    # visit 복구
    visit[x][y] = 0

    # 2. 현재구역 + 아래쪽 커버하는 경우
    if x == 0 and sector[x+1][y] + sector[x][y] <= W:
        visit[x][y] = 2
        visit[x+1][y] = -2
        x_, y_ = next(visit,x,y)
        DFS(visit, x_, y_, result + 1)

        # visit 복구
        visit[x][y] = 0
        visit[x+1][y] = 0
    
    # 3. 현재구역 + 우측 커버하는 경우
    if y < N-1 and sector[x][y+1] + sector[x][y] <= W:
        visit[x][y] = 3
        visit[x][y+1] = -3
        x_, y_ = next(visit,x,y)
        DFS(visit, x_, y_, result + 1)

        # visit 복구
        visit[x][y] = 0
        visit[x][y+1] = 0

    elif y == N-1 and visit[x][0] == 1 and sector[x][0] + sector[x][y] <= W:
        # 처음과 끝 sector가 이어져 있으므로, 이를 고려한 것. 
        # 0번 index의 sector가 단독으로 처리되었고, 마지막 sector와 서로 묶을 수 있으면 마지막 sector는 비용추가없이 처리 가능
        visit[x][y] = 3
        visit[0][y] = -3
        x_, y_ = next(visit,x,y)
        DFS(visit, x_, y_, result)

        # visit 복구
        visit[x][y] = 0
        visit[0][y] = 0


T = int(input())
for t in range(T):
    N, W = map(int, input().split())

    sector = [None, None]
    sector[0] = list(map(int, input().split()))
    sector[1] = list(map(int, input().split()))

    # >> 접근 전략
    # 1. 인접 섹터 비교하여 한번에 공략 가능한지 여부 판단
    # 2. 가능하다면 해당 case를 선택하고 다음 섹터 확인
    # 3. 가능한 case들을 모두 고려하여 모든 case 순회, 최소값 채택
    min_result = 99999
    visit = [[0 for _ in range(N+1)], [0 for _ in range(N+1)]]  # 방문 여부를 기록하는 배열
    # 0 : 방문안함 / 1 : 현재 한칸만 선택한 경우까지 확인 / 2 : 현재 + 아래칸 선택한 경우까지 확인 / 3 : 현재 + 우측칸 선택한 경우까지 확인 
    # DFS는 (0,0), (1,0), (0,1), (1,1) ... 순으로 진행한다. 

    DFS(visit, 0, 0, 0)
    

    print(min_result)
