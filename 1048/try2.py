# https://www.acmicpc.net/problem/1048
# 유니콘

# 시간초과 발생
# 1. 모든 가능한 이동을 탐색: 경로를 검증하는 과정에서 check 함수 호출을 통해 모든 가능한 이동을 확인하고 있습니다. 이는 불필요한 계산을 유발합니다.
# 2. 매번 깊은 복사 사용: deep_copy_2d_array를 반복적으로 호출하여 데이터를 복사하는 과정에서 많은 비용이 발생합니다.
# 3. 중복 연산 방지 미흡: 동일한 상태와 이동 경로에 대해 중복된 연산이 수행되고 있습니다.


DEBUG = 0
MOD = 1_000_000_007

def Print(*args):
    if DEBUG:
        print(*args)

def deep_copy_2d_array(array):
    return [row[:] for row in array]

# (x1, y1) 에서 (x2, y2) 로 이동가능한지 체크하는 함수
def check(x1, y1, x2, y2):
    if (abs(x1 - x2) > 2 and abs(y1 - y2) > 1)\
        or ((abs(x1 - x2) > 1 and abs(y1 - y2) > 2)):
        return True
    return False

if __name__ == '__main__':
    N, M, L = map(int, input().split())
    tmp = list(input())
    full_string = [(ord(c) - ord('A')) for c in tmp]
    board = [[] for _ in range(L)]  # 알파벳을 기준으로 좌표 저장
    for n in range(N):
        for idx, c in enumerate(list(input())):
            board[ord(c) - ord('A')].append((n, idx, 0))  # 좌표 및 count 저장

    Print(board)

    result = 0
    # 예외처리: board에 존재하지 않는 알파벳이 있는지 점검
    for s in full_string:
        if s >= L:  # s 는 0~25 사이의 수, L은 1~26 까지 가능
            print(result)
            exit(0)  # 추가 계산 안하고 종료

    # 첫 글자에 대한 처리 (초기설정)
    next_board = deep_copy_2d_array(board)
    for idx1, alphabets in enumerate(next_board):
        # 첫 글자와 동일한 셀은 도달 가능 카운트 1로 설정
        if idx1 == full_string[0]:
            for idx2, cell in enumerate(alphabets):
                start_i, start_j, start_cnt = cell
                next_board[idx1][idx2] = (start_i, start_j, 1)

    Print(f'[0]:{next_board}')

    # 두 번째 글자~마지막 글자까지 처리. 규칙에 따른 연산
    for k in range(1, len(full_string)):
        # 문자열을 2번째 문자부터 순회
        next_char = full_string[k]

        #  start_board 는 원본 데이터로 사용하고, next_board 에는 k번 이동했을 때 이동 가능한 경로 갯수가 저장됨
        start_board = next_board
        next_board = deep_copy_2d_array(board)
        # 보드의 모든 셀을 한 번씩 시작점으로 선정할 때 결과 계산
        for alphabets in start_board:
            for start_i, start_j, start_cnt in alphabets:
                # 알파벳이 일치하는 모든 셀에 대해
                for idx, cell in enumerate(next_board[next_char]):  # 도착점은 start_board 대신 next_board 를 사용한다. 
                    end_i, end_j, end_cnt = cell
                    # 시작점에서 해당 셀로 이동 가능한지 좌표 체크
                    if (check(start_i, start_j, end_i, end_j)):
                        # Print(f'{chr(next_char + ord("A"))}')
                        # Print(f'##[({start_i, start_j})->({end_i, end_j})]:{end_cnt + start_cnt}')
                        next_board[next_char][idx] = (end_i, end_j, end_cnt + start_cnt)  # cnt 증가해서 다시 저장
        Print(f'[{k}]:{next_board}')

    # result 계산
    for i, j, cnt in next_board[full_string[-1]]:
        result = (result + cnt) % MOD # 마지막 데이터들에 대해 합산
    
    
    print(result)

