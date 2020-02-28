max = 10007
if __name__ == '__main__':
    n = int(input())
    C = [0]
    C.append(1)
    C.append(3)
    # C[3] = 5
    # C[4] = 11

    for i in range(3, n+1):
        C.append(C[i-2]*2 + C[i-1])
    result = C[n]%max
    print(result)

