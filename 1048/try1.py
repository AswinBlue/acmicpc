# https://www.acmicpc.net/problem/1048
# 유니콘

# FAIL. 시간초과
# 시간 복잡도가 (30*30) * 50 인줄 알았는데, 
# (30 * 30) ^ 50 이었다.
DEBUG = 1
MOD = 1_000_000_007

def Print(*args):
    if DEBUG:
        print(*args)

# (x1, y1) 에서 (x2, y2) 로 이동가능한지 체크하는 함수
def check(x1, y1, x2, y2):
    if (abs(x1 - x2) > 2 and abs(y1 - y2) > 1)\
        or ((abs(x1 - x2) > 1 and abs(y1 - y2) > 2)):
        return True
    return False

# (current_x, current_y) 좌표에서 index 번 경로의 알파벳이 있는 위치로 이동 가능한지 체크하며 최종 경로의 갯수를 확인하는 함수
def find_case(current_x, current_y, index):
    global full_string, L
    if index == len(full_string):
        return 1  # 끝까지 이동 완료
        
    # 경로 계산 시작
    result = 0
    next_char = full_string[index]
    # 예외처리(밖에서 처리해주지 않을 경우, 에러 방지용)
    if next_char >= L:
        return 0
    
    # Print(f'[{index}]{current_x},{current_y}')
    for new_x, new_y in board[next_char]:
        if index == 0:
            if new_x == current_x and new_y == current_y:
                # index가 0인경우, 시작지점을 찾는 case로, (current_x, current_y)에 'next_char' 알파벳이 있는지 체크해야한다.
                result += find_case(new_x, new_y, index + 1) % MOD  # 끝까지 도달한 case 갯수 저장
        elif (check(current_x, current_y, new_x, new_y)):
            # new_x, new_y 로 이동 가능하다면 다음 가능성 체크
            result += find_case(new_x, new_y, index + 1) % MOD  # 끝까지 도달한 case 갯수 저장
    Print(f'[{index}]{current_x},{current_y}result:{result}')
    return result

if __name__ == '__main__':
    N, M, L = map(int, input().split())
    tmp = list(input())
    full_string = [(ord(c) - ord('A')) for c in tmp]
    board = [[] for _ in range(L)]  # 알파벳을 기준으로 좌표 저장
    for n in range(N):
        for idx, c in enumerate(list(input())):
            board[ord(c) - ord('A')].append((n, idx))  # 좌표 저장
    Print(board)

    result = 0
    # 예외처리: board에 존재하지 않는 알파벳이 있는지 점검
    for s in full_string:
        if s >= L:
            print(result)
            exit(0)  # 추가 계산 안하고 종료

    for i in range(N):
        for j in range(M):
            result += find_case(i, j, 0) % MOD
            Print(f'[0]{i},{j}result:{result}')

    print(result % MOD)

