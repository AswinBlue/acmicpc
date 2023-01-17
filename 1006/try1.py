# https://www.acmicpc.net/problem/1006
# 습격자 초라기

# 미구현 try
# 구현중 DFS 순회를 너무 복잡하게 짠 것을 인지하고 새로 구현

MAX_N = 10000
MAX_W = 10000

DEBUG = 1

def Print(*args):
    if DEBUG:
        print(*args)

# DFS 순회시 현재 좌표를 넣으면 다음 순회할 좌표를 반환하는 함수
def next(x, y):
    if x == 0:
        return 1, y
    return 0, y + 1

# 재귀형태로 순환하며 전체 case를 모두 확인하는 함수
def DFS(visit, x, y, result):
    global N, W, sector, min_result

    Print(x, y, visit)
    # 종료 조건, 마지막 sector 체크시
    if y >= N:
        min_result = min(min_result, result)
        Print(min_result)
        return 0
    # 이웃 섹터 visit 체크 및 방문 가능 여부 확인
    
    if visit[x][y] == 0:
        visit[x][y] = 1
        x_, y_ = next(x,y)
        DFS(visit, x_, y_, result + 1)
    elif visit[x][y] == 1:
        if x == 0 and sector[x+1][y] + sector[x][y] <= W:
            visit[x][y] = 2
            visit[x+1][y] = 4
            x_, y_ = next(x,y)
            DFS(visit, x_, y_, result + 1)
            visit[x+1][y] = 0  # DFS 완료 이후 같이 묶은 쌍 원복
        elif y < N-1 and sector[x][y+1] + sector[x][y] <= W:
            # 세로로 묶을 수 없는 경우 바로 우측이랑 묶기 시도
            visit[x][y] = 3
            visit[x][y+1] = 4
            x_, y_ = next(x,y)
            DFS(visit, x_, y_, result + 1)
            visit[x][y+1] = 0  # DFS 완료 이후 같이 묶은 쌍 원복
        elif y == N-1 and visit[x][0] == 1 and sector[x][0] + sector[x][y] <= W:
            # 처음과 끝 sector가 이어져 있으므로, 이를 고려한 것. 서로 묶을 수 있으면 마지막 sector는 비용추가없이 처리 가능
            visit[x][y] = 3
            x_, y_ = next(x,y)
            DFS(visit, x_, y_, result)
        else:
            # 묶기 실패한 경우
            visit[x][y] = 5

    elif visit[x][y] == 2:
        # 가로로 묶기 시도
        if y < N-1 and sector[x][y+1] + sector[x][y] <= W:
            visit[x][y] = 3
            visit[x][y+1] = 4
            x_, y_ = next(x,y)
            DFS(visit, x_, y_, result + 1)
            visit[x][y+1] = 0  # DFS 완료 이후 같이 묶은 쌍 원복
        elif y == N-1 and visit[x][0] == 1 and sector[x][0] + sector[x][y] <= W:
            # 처음과 끝 sector가 이어져 있으므로, 이를 고려한 것. 서로 묶을 수 있으면 마지막 sector는 비용추가없이 처리 가능
            visit[x][y] = 3
            x_, y_ = next(x,y)
            DFS(visit, x_, y_, result)
        else:
            # 묶기 실패한 경우
            visit[x][y] = 5
    elif visit[x][y] == 3:
        visit[x][y] = 5  # 모든 case 완료했다고 처리
    elif visit[x][y] == 4:
        # 이전 sector에서 함께 고려된 경우, skip하고 다음 진행
        x_, y_ = next(x,y)
        visit[x][y] = 3
        DFS(visit, x_, y_, result)
    elif visit[x][y] == 5:
        # 모든 case 다 체크한 경우
        visit[x][y] = 0  # 모든 case 체크 이후 방문정보 원복 (trace back)
        return 0

    # 모든 case가 고려될 때 까지 반복 체크 (visit이 3이 되면 더이상 호출 안됨)
    DFS(visit, x, y, result)

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
