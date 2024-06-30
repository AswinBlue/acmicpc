# https://www.acmicpc.net/problem/1533
# 길의 개수

#####
# 접근 방법 : 그래프의 연결 상태를 표현한 행렬의 곱을 n번 수행하면, 그 결과는 i에서 j로 갈 수 있는 길의 갯수를 의미한다.
# 모든 길의 길이가 1이라면, T번 곱을 수행하면, 결과로 나오는 행렬의 각 인자는 i 에서 j 로 T 거리만큼 걸려서 이동할 수 있는 길의 갯수를 의미하게 된다.
# 길의 길이가 최대 5이므로, 길을 길이 1 단위로 나누어 생각한다.(길이가 5인 길은 그 사이에 4개의 node가 더 있다고 생각하고, 이를 행렬로 표현한다.)

DEBUG = 1
MAX_N = 10
MAX_LEN = 5
MAX_T = 1_000_000_000
RESULT_MOD = 1_000_003

def Print(*args):
    if DEBUG:
        print(*args)

if __name__ == '__main__':
    N, S, E, T = map(int, input().split())

    # graph 생성 및 초기화
    graph = [[0 for _ in range(N * MAX_LEN)] for _ in range(N * MAX_LEN)]
    # i * MAX_N 이 실제 node에 해당 (i_0)
    # 그 외 node 들은 i 에 도착하기 까지 떨어진 거리에 따라 i_1, i_2, i_3, i_4 로 표현함
    # i_1 에서 i_0, i_2 에서 i_1, ... i-(n-1) 에서 i_(n-2) 까지 이동 가능하다고 처리
    for i in range(N * MAX_LEN):
        if i + 1 < N * MAX_LEN and (i + 1) % MAX_LEN != 0:
            graph[i + 1][i] = 1

    for i in range(N):
        line = input()
        for j, c in enumerate(line):
            if int(c) > 0:
                # 이동 거리에 따라 알맞은 위치로 이동
                Print(f"({i},{j}): {j * MAX_LEN + (int(c) - 1)}")
                graph[i * MAX_LEN][j * MAX_LEN + (int(c) - 1)] = 1
                # graph[i * MAX_LEN][j * MAX_LEN + x] 은 i로부터 j까지 x-1 번만에 이동 가능하다는 뜻
    
    for i in range(N * MAX_LEN):
        Print(graph[i])


    # 행렬 곱 계산
    # ERROR: 아래와 같이 행렬 곱을 수행하면 T 회 수행하는 게 아니라 2**T 회 수행하는 값이 된다.
    flag_use_graph2 = False
    graph2 = [[0 for _ in range(N * MAX_LEN)] for _ in range(N * MAX_LEN)]
    for t in range(T - 1):
        Print(t)
        if flag_use_graph2:
            for i in range(N * MAX_LEN):
                for j in range(N * MAX_LEN):
                    result = 0
                    for k in range(N * MAX_LEN):
                        result += graph2[i][k] * graph2[k][j]
                    graph[i][j] = result
                Print(f"1-{i}", graph[i])
        else:
            for i in range(N * MAX_LEN):
                for j in range(N * MAX_LEN):
                    result = 0
                    for k in range(N * MAX_LEN):
                        result += graph[i][k] * graph[k][j]
                    graph2[i][j] = result
                Print(f"2-{i}", graph2[i])
        flag_use_graph2 = not flag_use_graph2

    if flag_use_graph2:
        graph = graph2

    for i in range(N * MAX_LEN):
        Print(i, graph[i])

    print(graph[(S - 1) * MAX_LEN][(E - 1) * MAX_LEN])


