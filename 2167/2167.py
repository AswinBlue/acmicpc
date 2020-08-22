if __name__ == "__main__":
    N, M = map(int, input().split())

    arr = [[0] for i in range(N+1)]
    arr[0] += [0 for i in range(M)]

    for t in range(1,N+1):
        arr[t] += [int(i) for i in input().split()]

    for i in range(1, N+1):
        for j in range(2, M+1):
            arr[i][j] += arr[i][j - 1]

    for j in range(1, M+1):
        for i in range(2, N+1):
            arr[i][j] += arr[i - 1][j]

    K = int(input())
    for i in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        print(arr[x2][y2] - arr[x2][y1] - arr[x1][y2] + arr[x1][y1])

