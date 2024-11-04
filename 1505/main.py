# https://www.acmicpc.net/problem/1505
# 불 켜기

from collections import deque

MAX_N = 8

DEBUG = 0
def Print(*arg):
    if DEBUG:
        print(*arg)

# 8방향 이동 (중앙, 위, 아래, 왼쪽, 오른쪽, 대각선)
directions = [(0,0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def binary_string_to_int(s):
    # '*'을 '1'로, '.'을 '0'으로 변환
    binary_string = s.replace('*', '1').replace('.', '0')
    
    # 변환된 이진 문자열을 정수로 변환
    return int(binary_string, 2)

def toggle(current_board, x, y, N, M):
    # 현재 위치 및 인접한 8방향의 전구 상태를 반전
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            current_board ^= 1 << (nx * M + ny)  # 전구 반전
    return current_board
N, M = map(int, input().split())
# board 의 형태를 하나의 int 형으로 표현해 저장 할 것이다. string 으로 표현하면 메모리 초과 발생
now = ''
for n in range(N):
    now += input()
now = binary_string_to_int(now)  # int 형으로 전환
Print(f'now:{now:0b}')


goal_state = (1 << (N * M)) - 1
Print(f'goal_state: {goal_state:0b}')
# queue 에 값이 남아있을 때 까지 수행
# KEY IDEA: 모든 경우의 수를 다 확인하면 시간/메모리 초과가 발생한다. 첫번째 행/열에 대해서만 전체 state를 구하고, 
# 이후 (N,M) 까지 한번의 순차진행으로 결과를 확인 할 것이다. 
# (1,1) 부터 (N,M) 까지 순회하며 모든 버튼을 (x-1, y-1) 위치의 전구가 켜짐 상태가 되는지 체크하며 진행한다. (greedy)

result = -1

for row_state in range(1 << M):  # row_state = 0번째 행에서 선택뒨 bit의 불을 끔
    for col_state in range(1 << (N-1)):  # col_state = 0번째 열에서 선택뒨 bit의 불을 끔
        # 첫 행/열을 state에 맞게 구성
        current_board = now  # 값 복사(int)

        cnt = 0
        # 첫 행에 대해 row_state  반전
        for i in range(M):
            if row_state & (1 << i) > 0:
                cnt += 1
                current_board = toggle(current_board, 0, i, N, M)
        # 첫 열에 대해 열상태 반전. 단, (0,0) 은 행을 처리할 떄 진행되었으므로 제거
        for j in range(N):
            if col_state & (1 << j) > 0:
                cnt += 1
                current_board = toggle(current_board, j+1, 0, N, M)

        Print(f'stae:{row_state:0b},{col_state:0b}')
        Print(f'current:{current_board:0b}')
        for x in range(1, N):
            for y in range(1, M):
                Print(f'{x},{y},{current_board & (1 << ((x-1)*M + (y-1)))}')
                # (N,M) 까지 (x-1, y-1) 을 지표삼아 진행
                if current_board & (1 << ((x-1)*M + (y-1))) == 0:
                    # (x-1, y-1) 위치에 불이 꺼져있다면, (x,y) 를 무조건 선택해야함 (이후에는 다시 불을 켤 기회가 없음)
                    current_board = toggle(current_board, x, y, N, M)
                    cnt += 1
        # 완료후 cnt 비교
        Print(f'next:{current_board:0b}')

        if current_board == goal_state and (result < 0 or cnt < result):
            result = cnt
        Print(f'{current_board}/{goal_state}, result:{result}')


print(result)


# BFS로 찾아야 할 문제를 greedy하게 변환하는 아이디어가 핵심

'''
# 메모리초과 발생

# BFS 초기 세팅
queue = deque([(now, 0, 0)])  # BFS 를 위한 queue (현재 불 상태, step, 현재 visit)
# KEY IDEA: 같은 자리를 두 번 이상 껐다 켜면, 상태를 반복하는 것이다. 순서에 상관없이 한 자리는 최대 한 번만 변환해야 중복이 발생하지 않는다.
visited = {0}  # 상태를 이미 거쳤는지 체크할 Dictionary. queue에 넣을떄 방문처리. string을 사용할 시 메모리초과 발생하여 bit manipulation 적용


while queue:
    current_board, steps, current_visit = queue.popleft()  # queue로 활용하기위해 좌측에서 pop
    Print(f'current:{current_board:0b}')
    # 종료 조건
    if current_board == goal_state:
        result = steps
        break

    for x in range(N):
        for y in range(M):
            if x > 0:
                # 이전 행의 전등이 꺼져있어 현재 줄에서 스위칭이 필요한 경우에만 수행
                if x > 0 and y > 0 and current_board & (1 << (x-1)*M + (y-1)) != 0:
                    continue
            next_board = toggle(current_board, x, y, N, M)  # 현재 전구와 인접 전구 반전 (배열형태)
            
            next_visit = current_visit ^ (1 << (x * M + y))
            if next_visit not in visited:
                visited.add(next_visit)  # queue에 넣기 전 visit 체크
                queue.append((next_board, steps + 1, next_visit))  # queue로 활용하기위해 우측에서 삽입
    Print(f'[{steps}]queue:{len(queue)}, visited:{len(visited)}, result:{result}')
'''