if __name__ == "__main__":
    S = input()
    check = [0 for i in range(200)]
    
    for i, c in (enumerate(S)):
        check[ord(c)] += 1

    for i in range(ord('a'), ord('z') + 1):
        print(check[i], end=' ')
