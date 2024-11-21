# https://www.acmicpc.net/problem/1048
# 유니콘

DEBUG = 0
MOD = 1_000_000_007

def Print(*args):
    if DEBUG:
        print(*args)

def deep_copy_2d_array(array):
    return [row[:] for row in array]

# (x2, y2) 에서 (x1, y1) 로 이동가능한지 체크하는 함수
def check(x2, y2, x1, y1):
    if (abs(x2 - x1) > 2 and abs(y2 - y1) > 1)\
        or ((abs(x2 - x1) > 1 and abs(y2 - y1) > 2)):
        return True
    return False

# array의 index를 벗어나는 범위라면 보정된 값을 반환하고, 아니면 값을 반환하는 함수
def get_data(array, i, j):
    global N, M
    if i < 0 or j < 0:
        return 0
    i = min(N-1, i)
    j = min(M-1, j)
    return array[i][j]

# 전체 배열의 부분합 구하는 함수
def get_partial_sum(array):
    global N, M
    for i in range(N):
        cnt = 0  # 이번 행에 계산될 count
        for j in range(M):
            cnt = (array[i][j] + cnt) % MOD  # 이번 행의 j열까지 계산된 값
            array[i][j] = (cnt + get_data(array,i-1,j)) % MOD

# (x2,y2) (x1,y1) 두 점 사이의 영역 계산 (x2,y2) < (x1,y1)
def calc_area(array, x1, y1, x2, y2):
    val = get_data(array,x2,y2) - get_data(array,x2,y1-1) - get_data(array,x1-1,y2) + get_data(array,x1-1,y1-1)
    # Print(f'{get_data(array,x2,y2)} - {get_data(array,x2,y1-1)} - {get_data(array,x1-1,y2)} + {get_data(array,x1-1,y1-1)} = {val}')
    return val


if __name__ == '__main__':
    N, M, L = map(int, input().split())
    tmp = list(input())
    full_string = [(ord(c) - ord('A')) for c in tmp]
    alphabet_board = [[] for _ in range(L)]  # 알파벳을 기준으로 좌표 저장
    for n in range(N):
        for idx, c in enumerate(list(input())):
            alphabet_board[ord(c) - ord('A')].append((n, idx))  # 좌표 저장

    Print(alphabet_board)

    result = 0
    # 예외처리: board에 존재하지 않는 알파벳이 있는지 점검
    for s in full_string:
        if s >= L:  # s 는 0~25 사이의 수, L은 1~26 까지 가능
            print(result)
            exit(0)  # 추가 계산 안하고 종료

    # 첫 글자에 대한 처리 (초기설정)
    next_count_board = [[0 for _ in range(M)] for _ in range(N)]
    # 첫 글자와 동일한 셀은 도달 가능 카운트 1로 설정
    for i, j in alphabet_board[full_string[0]]:
        next_count_board[i][j] = 1

    Print(f'[0]:{next_count_board}')
    get_partial_sum(next_count_board)
    Print(f'[0]:{next_count_board}')


    # 두 번째 글자~마지막 글자까지 처리. 규칙에 따른 연산
    # KEY IDEA: board에 저장되는 count에는 누적합을 결과를 계산하고 저장한다. 누적합을 사용함으로서 시간을 단축할 수 있다.
    # board 에는 (0,0) ~ (i,j) 위치에서 (i,j) 위치로 이동할 수 있는 갯수를 저장한다.
    for k in range(1, len(full_string)):
        # 문자열을 2번째 문자부터 순회
        next_char = full_string[k]
        #  start_count_board 는 원본 데이터로 사용하고, next_count_board 에는 k번째 알파벳으로 이동 가능한 경로 갯수가 저장됨
        start_count_board = next_count_board
        next_count_board =  [[0 for _ in range(M)] for _ in range(N)]
        # 보드의 모든 셀을 한 번씩 시작점으로 선정할 필요 없다. 
        # 알파벳이 일치하는 모든 셀에 대해 연산을 수행해도, 부분합을 사용하면 O(1) 시간안에 연산이 가능하다.
        for i, j in alphabet_board[next_char]:
            # (i,j) 에 도달가능한 갯수 연산
            # (0,0) ~ (N-1,M-1) 좌표 중 (i,j) 에 도달 할 수 없는 영역의 부분합을 구한다.
            # board[N-1][M-1] 값에서 위에서 구한 값을 빼면, (i,j) 로 이동 가능한 
            # 중앙 정사각형 + 좌측 직사각형 + 우측 직사각형 + 상단 직사각형 +  하단 직사각형 영역을 더한다. 
            # board[x][y]는 부분합 값이므로, 각 값들을 합하면 해당 영역에서 조건을 만족하는 좌표의 갯수 값이 된다. (알파벳 순서대로 체스말을 움직일 수 있는 좌표)
            
            next_count_board[i][j] = \
                start_count_board[N-1][M-1] - \
                (calc_area(start_count_board, i-2, j-2, i+2, j+2) + calc_area(start_count_board, 0, j-1, i-3, j+1)\
                    + calc_area(start_count_board, i-1, j+3, i+1, M-1) + calc_area(start_count_board, i+3, j-1, N-1, j+1)\
                    + calc_area(start_count_board, i-1, 0, i+1, j-3)
                ) % MOD
        
        Print(f'[{k}]:{next_count_board}')
        get_partial_sum(next_count_board)
        Print(f'[{k}]:{next_count_board}')

    result = next_count_board[N-1][M-1]
    print(result)

