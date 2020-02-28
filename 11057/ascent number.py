if __name__ == '__main__':
    N = int(input())
    maxNum = 10007
    # dynamic programming
    ascent = [[0 for j in range(N)] for i in range(10)]
    # initialization
    for i in range(10):
        ascent[i][0] = 1
    # iteratively fill the array
    for j in range(1,N):
        for i in range(10):
            for k in range(i+1):
                ascent[i][j] += ascent[k][j-1]
    # find the answer
    result = 0
    for i in range(10):
        result += ascent[i][N-1]

    print(result % maxNum)