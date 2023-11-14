# 주난의 난
# https://www.acmicpc.net/problem/14497

# 1. 시작점을 기점으로 DFS를 수행한다. 
# 2. 현재 위치가 1인 지점을 만날 때 까지 depth를 늘려나가고, 1을 만나면 해당 지점을 marking 하고 back tracing을 한다.
# 3. 갈 수 있는 모든 지점을 다녔는데도 종료지점을 찾지 못했다면 2에서 marking 한 지점부터 다시 2번 과정을 반복하여 DFS를 수행한다.
#    단, visit 처리한 map은 그대로 유지한다. 
# 4. 2번,3번을 반복하여 종료 지점에 도달했을 때, 반복한 횟수를 출력한다. 

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

MAX_N_M = 300
START = '*'
TARGET = '#'
VISITED = 'X'
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solve():
    # DFS 시작
    count = 1  # 파동이 발생한 횟수
    S = [(x1, y1)]  # 현재 단계에서 DFS 수행해야할 배열
    S2 = [] # DFS 하다 1을 만났을 때 위치를 저장할 배열, 다음 단계에서 DFS 수행할 배열
    room[x1][y1] = VISITED

    while True:
        while len(S) != 0:
            x,y = S.pop()
            res = do_dfs(S2, x, y)  # dfs 하고 결과 방문했다면 res에 True가 담김
            for i in range(N):
                Print(room[i])
            Print(count, res)
            if res:
                return count
        S = S2  # '1'이 있는 위치에 대해 다시 
        S2 = []  # 다시 비워준다.
        count += 1  # 횟수 갱신

    return -1

def do_dfs(S2, x, y):
    # 4방향 확인하여 갈 수 있는곳 체크
    for i in range(4):
        x_next = x + dx[i]
        y_next = y + dy[i]
        if x_next < 0 or x_next >= N or y_next < 0 or y_next >= M:
            continue
        if room[x_next][y_next] == TARGET:
            return True
        elif room[x_next][y_next] == '0':
            room[x_next][y_next] = VISITED  # 다음 node 방문했다고 체크
            res = do_dfs(S2, x_next, y_next)  # next 좌표 기준으로 다시 DFS
            if res:
                return True  # 결과가 true라면(종료지점 찾았다면) 종료
        elif room[x_next][y_next] == '1':
            room[x_next][y_next] = VISITED  # 다음 node 방문했다고 체크
            S2.append((x_next, y_next))  # '1'의 위치를 S2 stack에 저장
    return False


if __name__ == '__main__':
    # 변수 선언 및 입력 저장
    N, M = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    room = [None for _ in range(N)]
    for i in range(N):
        A = input()
        room[i] = [c for c in A]
    print(solve())