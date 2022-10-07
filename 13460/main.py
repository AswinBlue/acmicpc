# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

from collections import deque
from urllib.parse import MAX_CACHE_SIZE


MIN_N_M = 3
MAX_N_M = 10
MAX_TIME = 10
WALL = '#'
SPACE = '.'
NOT_FOUND = -1
# 상 좌 하 우
DX = [-1, 0, 1, 0]
DY = [0, -1, 0, 1]
def is_red_first(rx, ry, bx, by, dir):
    if dir == 0:
        if rx < bx:
            return True
    elif dir == 1:
        if ry < by:
            return True
    elif dir == 2:
        if rx > bx:
            return True
    elif dir == 3:
        if ry > by:
            return True

N, M = map(int, input().split())
board = [None for _ in range(N)]

# 시작 위치 및 종료위치 저장할 변수
RX = RY = BX = BY = OX = OY = -1

# 입력을 받아 초기 위치 설정
for n in range(N):
    board[n] = input()
    r = board[n].find('R')
    b = board[n].find('B')
    o = board[n].find('O')

    if r >= 0:
        RX = n
        RY = r
        board[n].replace('R', SPACE)  # 공 위치는 기록하지 않는다.
    if b >= 0:
        BX = n
        BY = b
        board[n].replace('B', SPACE)  # 공 위치는 기록하지 않는다.
    if o >= 0:
        OX = n
        OY = o

# 4차원 배열 visit[i][j][k][l] 은 붉은공 (i,j) 푸른공 (k,l) 위치의 상태를 의미
visit = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)] 
visit[RX][RY][BX][BY] = 1
# do BFS
Q = deque()
Q.append((RX, RY, BX, BY, 0))
result_found = False
while Q:
    # print(Q)
    rx, ry, bx, by, move = Q.popleft()
    # 최대 이동 횟수 초과시 검색 안함. BFS이기 때문에 뒤에 올 것들은 MAX_TIME 이상일 것이라 continue가 아니라 break
    if move >= MAX_TIME:
        break
    # 4방향 살펴보며 진행. 어떤 공을 먼저 진행할지 확인 필요
    for dir in range(4):
        dx = DX[dir]
        dy = DY[dir]
        rx2, ry2, bx2, by2 = -1, -1, -1, -1  # 이동 후 공들의 다음 좌표를 저장할 변수
        red_goal = False # 빨간공이 목적지점에 도달했는지 여부
        blue_goal = False # 파란공이 목적지점에 도달했는지 여부

        # 빨강 먼저인 경우
        if is_red_first(rx, ry, bx, by, dir):
            # 빨강 위치 설정
            rx2, ry2 = rx, ry 
            # 가장자리에는 항상 벽이 있으므로 index validation 체크 안함
            while board[rx2 + dx][ry2 + dy] != WALL:
                rx2 += dx
                ry2 += dy
                # 목적지점 도달하는지 체크
                if (rx2, ry2) == (OX, OY):
                    # 목적지점 도달시 더이상 체크 불필요
                    red_goal = True
                    rx2 = ry2 = -1
                    break
            # 파랑 위치 설정
            bx2, by2 = bx , by
            # 빨간 공이 이미 지나가 있는 곳이랑 겹치는지도 체크 필요
            while board[bx2 + dx][by2 + dy] != WALL and (rx2, ry2) != (bx2 + dx, by2 + dy):
                bx2 += dx
                by2 += dy
                # 목적지점 도달하는지 체크
                if (bx2, by2) == (OX, OY):
                    # 목적지점 도달시 더이상 체크 불필요
                    blue_goal = True
                    bx2 = by2 = -1
                    break
        # 파랑 먼저인 경우
        else:
            # 파랑 위치 설정
            bx2, by2 = bx, by
            while board[bx2 + dx][by2 + dy] != WALL:
                bx2 += dx
                by2 += dy
                # 목적지점 도달하는지 체크
                if (bx2, by2) == (OX, OY):
                    # 목적지점 도달시 더이상 체크 불필요
                    blue_goal = True
                    bx2 = by2 = -1
                    break
            # 빨강 위치 설정
            rx2, ry2 = rx, ry
            # 파랑 공이 이미 지나가 있는 곳이랑 겹치는지도 체크 필요
            while board[rx2 + dx][ry2 + dy] != WALL and (rx2 + dx, ry2 + dy) != (bx2, by2):
                rx2 += dx
                ry2 += dy
                # 목적지점 도달하는지 체크
                if (rx2, ry2) == (OX, OY):
                    # 목적지점 도달시 더이상 체크 불필요
                    red_goal = True
                    rx2 = ry2 = -1
                    break

        # 파란공이 목표지점에 들어간 경우
        if blue_goal:
            # 실패 case이므로 더이상 찾지 않음
            continue
        # 파란공이 목표에 들어가지 않고 빨간 공이 목표지점에 들어간 경우
        if red_goal:
            # BFS로 찾았으므로, 가장 먼저 발견된 것이 가장 빠르다.
            print(move + 1)
            Q = None  # 루프 종료를 위한 설정
            result_found = True
            break

        # 방문한 적이 없다면 queue에 공의 위치를 넣고 다음 진행
        if visit[rx2][ry2][bx2][by2] == 0:
            visit[rx2][ry2][bx2][by2] = 1
            Q.append((rx2, ry2, bx2, by2, move + 1))

# BFS를 완료했는데도 결과가 없을 경우
if not result_found:
    print(NOT_FOUND)