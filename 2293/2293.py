if __name__ == "__main__":
    n, k = input().split()
    n = int(n)
    k = int(k)

    coin = []
    D = [0 for i in range(k + 1)]
    for i in range(n):
        tmp = int(input())
        coin.append(tmp)

    for i in range(n):
        if coin[i] <= k:
            D[coin[i]] += 1
            for j in range(1, k + 1):
                if D[j] > 0 and j + coin[i] <= k:
                    D[j + coin[i]] += D[j]

    print(D[k])
    """
    1111111111
    211111111
    22111111
    2221111
    222211
    22222
    
    11111
    2111
    221
    5
    """