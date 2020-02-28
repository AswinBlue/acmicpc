if __name__ == '__main__':
    N = int(input())
    maxNum = 1000000000
    # <첫 번째 시도>
    # stair[A][B][C]
    # A : digit(0,1,2,3) at the end of the number
    # B : length of number
    # C : binary flag that marks digits in the number
    # stair = [[[] for i in range(N+1)]for j in range(10)]
    # 메모리 초과로 실패

    # <두 번째 시도>
    # stair[A][B][C]
    # A : digit(0,1,2,3) at the end of the number
    # B : length of number
    # C : binary flag that marks digits in the number

    all_in = (1 << 10)

    stair = [[[0 for k in range(all_in)] for i in range(N+1)]for j in range(10)]
    # initiate array when N=1
    for i in range(1, 10):
        stair[i][1][1 << i] += 1

    for j in range(2, N+1):
        for i in range(10):
            if i-1 >= 0:
                for k in range(all_in):
                    stair[i][j][k | (1 << i)] += stair[i-1][j-1][k]
            if i+1 <= 9:
                for k in range(all_in):
                    stair[i][j][k | (1 << i)] += stair[i+1][j-1][k]

    result = 0

    for i in range(10):
        result += stair[i][N][all_in-1]

    print(result % maxNum)
