# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from sys import setrecursionlimit
setrecursionlimit(10000)

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

MAX_MOVE = 5
EMPTY = 0

LEFT  = 0
RIGHT = 1
UP    = 2
DOWN  = 3

def move_board_left(current_board):
    next_board = [[0 for _ in range(N)] for _ in range(N)]

    # 이동시 num_A와 num_B가 인접하게 되고, 만약 숫자가 같다면 합쳐지게 된다. 
    for i in range(N):
        num_A = 0
        num_B = 0
        idx = 0  # 이동 후 num_A가 놓일 위치. num_B는 num_A와 합쳐지거나 그 다음에 놓인다.
        for j in range(N):
            if current_board[i][j] == EMPTY:
                continue

            if num_A == 0:
                # num_A를 먼저 찾는다.
                num_A = current_board[i][j]
                continue
            else:
                # num_A를 찾았다면 num_B도 찾는다.
                num_B = current_board[i][j]
                if num_A == num_B:
                    # 숫자가 같다면 합쳐짐
                    next_board[i][idx] = num_A * 2
                    num_A = num_B = 0
                    idx = idx + 1
                else:
                    # 숫자가 다르다면 쌓임
                    next_board[i][idx] = num_A 
                    # B를 A로 치환
                    num_A = num_B
                    num_B = 0
                    idx = idx + 1
            
        # 마지막 남은 num_A를 대입
        if num_A != 0:
            next_board[i][idx] = num_A

    return next_board

def move_board_right(current_board):
    next_board = [[0 for _ in range(N)] for _ in range(N)]

    # 이동시 num_A와 num_B가 인접하게 되고, 만약 숫자가 같다면 합쳐지게 된다. 
    for i in range(N):
        num_A = 0
        num_B = 0
        idx = N - 1  # 이동 후 num_A가 놓일 위치. num_B는 num_A와 합쳐지거나 그 다음에 놓인다.
        for j in range(N - 1, -1, -1):
            if current_board[i][j] == EMPTY:
                continue
            if num_A == 0:
                # num_A를 먼저 찾는다.
                num_A = current_board[i][j]
                continue
            else:
                # num_A를 찾았다면 num_B도 찾는다.
                num_B = current_board[i][j]
                if num_A == num_B:
                    # 숫자가 같다면 합쳐짐
                    next_board[i][idx] = num_A * 2
                    num_A = num_B = 0
                    idx = idx - 1
                else:
                    # 숫자가 다르다면 쌓임
                    next_board[i][idx] = num_A 
                    num_A = num_B
                    num_B = 0
                    idx = idx - 1
            
        # 남은 수 대입
        if num_A != 0:
            next_board[i][idx] = num_A

    return next_board
    
def move_board_down(current_board):
    next_board = [[0 for _ in range(N)] for _ in range(N)]

    # 이동시 num_A와 num_B가 인접하게 되고, 만약 숫자가 같다면 합쳐지게 된다. 
    for j in range(N):
        num_A = 0
        num_B = 0
        idx = 0  # 이동 후 num_A가 놓일 위치. num_B는 num_A와 합쳐지거나 그 다음에 놓인다.
        for i in range(N):
            if current_board[i][j] == EMPTY:
                continue
            if num_A == 0:
                # num_A를 먼저 찾는다.
                num_A = current_board[i][j]
                continue
            else:
                # num_A를 찾았다면 num_B도 찾는다.
                num_B = current_board[i][j]
                if num_A == num_B:
                    # 숫자가 같다면 합쳐짐
                    next_board[idx][j] = num_A * 2
                    num_A = num_B = 0
                    idx = idx + 1
                else:
                    # 숫자가 다르다면 쌓임
                    next_board[idx][j] = num_A 
                    num_A = num_B
                    num_B = 0
                    idx = idx + 1
            
        # 남은수 대입
        if num_A != 0:
            next_board[idx][j] = num_A

    return next_board

def move_board_up(current_board):
    next_board = [[0 for _ in range(N)] for _ in range(N)]

    # 이동시 num_A와 num_B가 인접하게 되고, 만약 숫자가 같다면 합쳐지게 된다. 
    for j in range(N):
        num_A = 0
        num_B = 0
        idx = N - 1  # 이동 후 num_A가 놓일 위치. num_B는 num_A와 합쳐지거나 그 다음에 놓인다.
        for i in range(N - 1, -1, -1):
            if current_board[i][j] == EMPTY:
                continue
            if num_A == 0:
                # num_A를 먼저 찾는다.
                num_A = current_board[i][j]
                continue
            else:
                # num_A를 찾았다면 num_B도 찾는다.
                num_B = current_board[i][j]
                if num_A == num_B:
                    # 숫자가 같다면 합쳐짐
                    next_board[idx][j] = num_A * 2
                    num_A = num_B = 0
                    idx = idx - 1
                else:
                    # 숫자가 다르다면 쌓임
                    next_board[idx][j] = num_A 
                    num_A = num_B
                    num_B = 0
                    idx = idx - 1
            
        # 남은 수 대입
        if num_A != 0:
            next_board[idx][j] = num_A

    return next_board
    
def get_max_number(current_board):
    max_num = 0
    for i in range(N):
        max_num = max(max_num, max(current_board[i]))
    return max_num

def move_and_find_max_number(current_board, depth):
    # 판을 이동하며 recursive하게 동작한다.
    Print(current_board)
    result = [0, 0, 0, 0]
    if depth < MAX_MOVE:
        next_board = move_board_left(current_board)
        result[LEFT] = move_and_find_max_number(next_board, depth + 1)
        next_board = move_board_right(current_board)
        result[RIGHT] = move_and_find_max_number(next_board, depth + 1)
        next_board = move_board_up(current_board)
        result[UP] = move_and_find_max_number(next_board, depth + 1)
        next_board = move_board_down(current_board)
        result[DOWN] = move_and_find_max_number(next_board, depth + 1)
        Print(f"depth:{depth} result:{result}")
        return max(result)  # 가장 큰 값을 반환
    elif depth == MAX_MOVE:
        # 최종 이동한 결과 중 가장 큰 값을 반환
        return get_max_number(current_board)

if __name__ == '__main__':
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        line = map(int, input().split())
        for j, num in enumerate(line):
            board[i][j] = num

    print(move_and_find_max_number(board, 0))

