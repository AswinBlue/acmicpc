# https://www.acmicpc.net/problem/1533
# 길의 개수

#####
# 접근 방법 : 그래프의 연결 상태를 표현한 행렬의 곱을 n번 수행하면, 그 결과는 i에서 j로 갈 수 있는 길의 갯수를 의미한다.
# 모든 길의 길이가 1이라면, T번 곱을 수행하면, 결과로 나오는 행렬의 각 인자는 i 에서 j 로 T 거리만큼 걸려서 이동할 수 있는 길의 갯수를 의미하게 된다.
# 길의 길이가 최대 5이므로, 길을 길이 1 단위로 나누어 생각한다.(길이가 5인 길은 그 사이에 4개의 node가 더 있다고 생각하고, 이를 행렬로 표현한다.)

import copy

DEBUG = 0

MAX_N = 10
MAX_LEN = 5
MAX_T = 1_000_000_000
RESULT_MOD = 1_000_003

def Print(*args):
    if DEBUG:
        print(*args)

# matrix : 행렬 곱을 수행할 행렬
# powed : 'matrix'가 원본 행렬(graph)에서 몇번 곱해져서 생성된 것인지
def matmul(matrix, powed):
    global N, MAX_LNE, T

    if powed * 2 <= T:
        # do multiplicate
        matrix_2 = [[0 for _ in range(N * MAX_LEN)] for _ in range(N * MAX_LEN)]
        for i in range(N * MAX_LEN):
            for j in range(N * MAX_LEN):
                result = 0
                for k in range(N * MAX_LEN):
                    result = (result + matrix[i][k] * matrix[k][j]) % RESULT_MOD
                matrix_2[i][j] = result

        # recursive, 제곱으로 연산 가능한 부분은 연산 속도를 위해 제곱으로 묶어서 처리
        res_matrix, res_powed = matmul(matrix_2, powed * 2)

        # 나머지 부분들 연산
        while res_powed + powed <= T:
            Print(f"do {(T - res_powed) / powed} times more")
            # do multiplicate
            # matrix_2 = [[0 for _ in range(N * MAX_LEN)] for _ in range(N * MAX_LEN)]  # 결과 담는용으로 재활용하므로 초기화 필요 없음
            for i in range(N * MAX_LEN):
                for j in range(N * MAX_LEN):
                    result = 0
                    for k in range(N * MAX_LEN):
                        # result = (result + matrix[i][k] * res_matrix[k][j]) % RESULT_MOD
                        result = (result + res_matrix[i][k] * matrix[k][j]) % RESULT_MOD
                    matrix_2[i][j] = result

            # deep copy가 아니라 shallow copy로 포인터만 바꿔 연결해서 계속 재활용 한다.
            tmp = res_matrix
            res_matrix = matrix_2  # 결과값 갱신
            matrix_2 = tmp
            res_powed += powed
                
        Print(f"{powed}: done to {res_powed}")
        for i in range(N * MAX_LEN):
            Print(i, res_matrix[i])

        return res_matrix, res_powed  # 결과 반환
    
    # 더 곱할 수 없는 경우 받은 내용 그대로 반환
    Print(powed, "return without mul")
    res_matrix = [None for _ in range(N * MAX_LEN)]  # REF: 새로운 객체 생성하여 return 필요하다. matrix는 배열이고, python에서 mutable 객체이기 때문에
    # matrix 를 그대로 반환하면 의도한 대로 동작하지 않는다. 참조: https://wikidocs.net/16038#google_vignette
    for i in range(N * MAX_LEN):
        res_matrix[i] = copy.deepcopy(matrix[i])
        Print(i, matrix[i])
    return res_matrix, powed
        

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
        Print("INIT", i, graph[i])

    # 행렬 곱 계산
    res_matrix, res_powed = matmul(graph, 1)

    for i in range(N * MAX_LEN):
        Print("FIN",i, res_matrix[i])

    print(res_matrix[(S - 1) * MAX_LEN][(E - 1) * MAX_LEN])