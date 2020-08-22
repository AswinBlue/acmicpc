if __name__ == "__main__":
    N, M = input().split()
    N = int(N)
    M = int(M)

    D  = [[0 for i in range(301)] for i in range(301)]
    # to make D[1][1] = 0 without using 'if' in 'for' statement
    D[1][0] = -1

    for i in range(1, N+1):
        for j in range(1, M+1):
            if i>j:
                D[i][j] = D[int(i/2)][j] + D[i - int(i/2)][j] + 1
                #print('(',int(i/2), j,')')
            else:
                D[i][j] = D[i][int(j/2)] + D[i][j - int(j/2)] + 1
                #print('(',i, int(j/2),')')

    print(D[N][M])