if __name__ == '__main__':
    N = int(input())
    P = [0]
    for Pi in map(int, input().split()):
        P.append(Pi)

    C = [0]
    for i in range(1,N+1):
        cost = 0
        for j in range(i):
            if C[j] + P[i-j] > cost:
                cost = C[j] + P[i-j]
        C.append(cost)

    print(C[N])
