if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]

    sum = 0
    for i in range(1, len(P)):
        if P[i-1] < P[i]:
            sum += P[i] - P[i-1]

    print(sum)


