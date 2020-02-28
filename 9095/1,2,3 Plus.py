if __name__ == '__main__':
    T = int(input())
    for k in range(T):
        C = [0]
        C.append(1)
        C.append(2)
        C.append(4)

        n = int(input())
        for i in range(4, n+1):
            C.append(C[i-1] + C[i-2] + C[i-3])
        result = C[n]
        print(result)