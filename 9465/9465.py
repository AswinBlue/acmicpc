
def do_calc():
    N = int(input())
    L = [[] for i in range(2)]
    D = [[0 for i in range(N+1)] for j in range(2)]

    for i in range(2):
        L[i] = input().split()
        L[i] = [0] + [int(t) for t in L[i]]
    D[0][1] = L[0][1]
    D[1][1] = L[1][1]

    for j in range(2, N + 1):
        for i in range(2):
            _i = 0
            if i == 0:
                _i = 1
            else:
                _i = 0
            D[i][j] = max(D[_i][j-2], D[_i][j-1]) + L[i][j]

    print(L[0])
    print(L[1])
    print(D[0])
    print(D[1])
    print(max([D[0][N], D[1][N]]))


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        do_calc()

