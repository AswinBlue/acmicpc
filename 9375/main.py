if __name__ == "__main__":
    TC = int(input())

    for t in range(TC):
        n = int(input())
        clothes = {}

        for i in range(n):
            cloth, kind = map(str, input().split())

            if kind in clothes:
                clothes[kind].append(cloth)
            else:
                clothes[kind] = [cloth]

        num = 1
        for part in clothes:
            num *= (len(clothes[part]) + 1) # also count 'not wearing' case

        print(num - 1) # except 'wear nothing' case


