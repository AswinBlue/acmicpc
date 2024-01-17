# https://www.acmicpc.net/problem/1028
# 다이아몬드 광산

# 1. 조건 확인
# 다이아몬드는 정사각형이 되어야하므로 각 변의 길이가 모두 동일해야 한다.
# 다이아몬드의 꼭지점은 무조건 90도 각도로 인접한 다른 두 1과 연결되어 있어야 한다. 
# 꼭지점을 시작으로 변의 길이가 짧은 다이아몬드의 형태부터 순서대로 찾아본다.

# 2. 순회 방법
# 이떄까지 찾은 가장 큰 다이아의 변의 길이를 기록한다. (이하 max_length)
# (1,1) 부터 (R,C) 까지 순회하며 1을 찾고, 1 옆에 90도 각도로 인접한 1이 있다면, queue에 쌓는다. 
# queue에는 '꼭지점의 좌표', '변의 방향' 을 기록한다.
# ex) 아래와 같이 한 꼭지점에 4 변이 모두 붙어있다면 queue에는 [((2,2),1), ((2,2),2), ((2,2),3), ((2,2),4)] 가 쌓이게 된다.
# 1 0 1
# 0 1 0 
# 1 0 1 
# queue에 들어간 모든 위치에 대해 다이아몬드 크기 측정 단계를 수행한다.
# 다이아몬드 크기 측정은 아래와같이 진행한다.
# 1) 주어진 방향을 따라 1이 있으면 한 쪽 방향으로 진행하며, 갈림길이 나올 때 까지 이동한 길이(이하 length)를 기록한다.
# 2) 갈림길 혹은 꺾어지는 길이 나오면 갈림길로 이동했을 때 다이아몬드가 생성되는지 체크한다. 
#    이때, length 가 max_length 작다면 (non-promising) 갈림길은 무시하고 가던 방향으로 계속 진행한다. 
# ex) (2,3) 에서 시작하였을 때, (3,1)로 이동해서는 다이아몬드를 만들 수 없다. 갈 필요가 없는 길이다.
# 0 0 0 0 0
# 1 0 1 0 0
# 0 1 0 1 0
# 0 0 1 0 0
# 3) 다이아몬드가 생성 될 수 있는(promising) 길이라면 length 만큼 이동이 가능한지 확인한다.
# 4) 3번이 가능하다면 length만큼 이동한 위치에서 갈림길이 있는지 확인한다. 
# 5) 이동한 경로가 이어져 다이아몬드가 생성될 때 까지 2~4를 반복한다. 
# 6) 다이아몬드가 생성되었다면 max_length 를 갱신하고, queue의 다음 인자에 대해 이 과정을 반복한다.

# 3) 갈라진 방향으로 이동하되, 시계방향
# 2) 다른 방향의 1이 나오면 그쪽으로 이동하되, (1) 에서 측정한 만큼 이동할수 있는지 확인한다.
# 3) 시계방향으로만 이동방향을 전환한다.
# 

# 개선1. queue를 사용하면 메모리 초과가 발생한다. 굳이 promising한 지점을 queue에 쌓지 않고도 찾는 즉시 체크를 할 수 있다.
# 개선2. promising 규칙을 강화하여 불필요한 계산 소모를 줄인다. 
# - 최대 길이 이하의 변은 다이아몬드를 체크할 필요가 없다.
# - 시작 꼭지점의 위치부터 남은 공간까지 그을 수 있는 선의 최대 길이를 사용해 promising 여부를 판별한다. 
DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

MAX_SIZE = 750 # R,C의 최댓값
DIAMOND = 1 # 다이아몬드로 표시되는 문자

STATE_LT_TO_RT = 0 # 좌상단에서 시작, 우상단에서 마치는 case
STATE_RT_TO_RB = 1 # 우상단에서 시작, 우하단에서 마치는 case
STATE_RB_TO_LB = 2 # 우하단에서 시작, 좌하단에서 마치는 case
STATE_LB_TO_LT = 3 # 좌하단에서 시작, 좌상단에서 마치는 case

DIR_LT = 0 # ↖
DIR_RT = 1 # ↗
DIR_RD = 2 # ↘
DIR_LD = 3 # ↙

# 좌상,우상,우하,좌하,좌상 으로 이동하기위한 델타값
DX = [-1, -1, 1, 1]
DY = [-1, 1, 1, -1]
# 주어진 방향에 따른 delta값 반환하는 함수
def get_delta(dir):
    return DX[dir % 4], DY[dir % 4]
# 교차점에서 다음 이동해야 할 방향으로 길이 있는지 찾는 함수
# dir : 진행방향, row : 현재 행, col : 현재 열
def check_junction(dir, row, col):
    global field

    dx, dy = get_delta(dir + 1)
    if field[row + dx][col + dy] == DIAMOND:
        return True

# 길이가 length 인 diamond 를 찾는 함수
# state : 어디서 출발해서 어디로 마치는지 정보
# dir : 현재 탐색 진행 방향
# x, y: 현재 위치(꼭지점)의 row, col 좌표
def check_diamond(state, dir, length, x, y):
    global field

    next_dir = (dir + 1) % 4
    if next_dir == state:  # next_dir == state 가 되면, 네방향을 한바퀴 모두 돌아온 것
        return True  # 길이가 length인 diamond가 존재함
    
    # 다이어몬드 검사 수행
    dx, dy = get_delta(next_dir)
    x_ = x
    y_ = y
    for i in range(length-1): # next_dir 방향으로 이동하며 한 변이 length 길이만큼 될 수 있는지 체크
        x_ += dx
        y_ += dy
        if field[x_][y_] != DIAMOND:
            return False
    # 한 변이 다이아몬드 조건을 충족하면, 다음 변을 체크
    return check_diamond(state, next_dir, length, x_, y_)  # 재귀를 사용해 diamond를 검색

# 가능성 있는(promising) 꼭지점에서 시작하여 다이아몬드를 그려보는 함수
# state : 어디서 출발해서 어디로 마치는지 정보
# x, y: 시작 위치(꼭지점) 
def find_diamond_from_promising_point(x, y, state):
    global max_length, field

    Print(f'({x},{y})/{state},max:{max_length}')
    length = 1
    dir = state  # state가 정해질 때, 처음 진행 방향(dir)은 state의 값과 동일하다. 내가 정의할 때 value가 같도록 정의했기 때문이다.
    dx, dy = get_delta(dir) # get delta

    while True:
        # move one click front
        x_ = x + dx
        y_ = y + dy

        if field[x_][y_] == DIAMOND:
            # can go forward
            # update length of diamond's edge
            length += 1
            # update current position
            x = x_
            y = y_
        else:
            break  # if no more way, break

        if check_junction(dir, x, y):  # check proper curved path to make diamond ahead
            # if has a junction
            if max_length < length and check_diamond(state, dir, length, x, y):  # check it is biggest diamond ever
                max_length = length
                Print(f'MAX_UPDATED:{length}')

if __name__ == '__main__':
    R, C = map(int, input().split())
    field = [None for _ in range(R+2)]
    field[0] = [0 for _ in range(C+2)]  # 테두리를 0으로 감싸서 연산이 쉽도록 하기 위함
    field[R+1] = [0 for _ in range(C+2)]  # 테두리를 0으로 감싸서 연산이 쉽도록 하기 위함
    for i in range(1, R+1):
        x = input()
        field[i] = [0 for _ in range(C+2)]  # 테두리를 0으로 감싸서 연산이 쉽도록 하기 위함
        for j, n in enumerate(x):
            field[i][j+1] = int(n)
    Print(field)

    max_length = 0  # biggest edge length of diamond
    for i in range(1, R+1):
        for j in range(1, C+1):
            if field[i][j] == DIAMOND:
                max_length = 1
                break
        if max_length == 1:
            break

    # check is there any diamonds in field

    # 1. find promising vertex (where edge size could be bigger than 1)
    for i in range(1, R+1):
        for j in range(1, C+1):
            if field[i][j] == DIAMOND:
                # check diamond for all promising point & state combination
                if field[i-1][j-1] == DIAMOND and field[i-1][j+1] == DIAMOND \
                    and (i > max_length * 2 and j > max_length and C - j + 1 > max_length): # 현재 꼭지점에서 더 큰 다이아몬드를 찾을 수 있을지 여부
                    find_diamond_from_promising_point(i, j, STATE_LT_TO_RT)
                if field[i-1][j+1] == DIAMOND and field[i+1][j+1] == DIAMOND \
                    and (i > max_length and R - i + 1> max_length and C - j + 1> max_length * 2):
                    find_diamond_from_promising_point(i, j, STATE_RT_TO_RB)
                if field[i+1][j+1] == DIAMOND and field[i+1][j-1] == DIAMOND \
                    and (R - i > max_length * 2 and j > max_length and C - j + 1 > max_length):
                    find_diamond_from_promising_point(i, j, STATE_RB_TO_LB)
                if field[i+1][j-1] == DIAMOND and field[i-1][j-1] == DIAMOND \
                    and (i > max_length and R - i + 1> max_length and j > max_length * 2):
                    find_diamond_from_promising_point(i, j, STATE_LB_TO_LT)

    print(max_length)

