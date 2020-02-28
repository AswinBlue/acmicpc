
# <첫번째 시도>
# 계단수를 배열 stair 에 담아 바로 이전 계단수로 다음 계단수를 계산하려 시도
# stair[i] = stair[i-2]*2 - (이전 계단수의 1,8의 갯수) 식을 알아냈지만, (이전 계단수의 1,8의 갯수)를 알 방법을 구하지 못함
"""
    N = int(input())
    maxNum = 1000000000
    stair = [0, 9, 17]

    for i in range(3, N+1):
        stair.append(stair[i-1]*2 - 2*pow(3,i-3))
    print(stair[N] % maxNum)
"""
if __name__ == '__main__':
    N = int(input())
    maxNum = 1000000000

    stair = [[] for i in range(10)]
    stair[0].append(0)
    for i in range(1, 10):
        stair[i].append(1)
    for j in range(1, N):
        for i in range(10):
            tmp = 0
            if i-1 >= 0:
                tmp += stair[i-1][j-1]
            if i+1 <= 9:
                tmp += stair[i+1][j-1]

            stair[i].append(tmp)

    result = 0
    for i in range(10):
        result += stair[i][N-1]
    print(result % maxNum)
