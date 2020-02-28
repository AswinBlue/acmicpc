if __name__ == '__main__':
    n, k = map(int, input().split())
    seq = []
    maxNum = 5000000
    for i in map(int, input().split()):
        seq.append(i)

    check = [[seq[0], 1]]
    num = 0
    for i in range(1, len(seq)):
        # if increasing sequence
        if check[-1][0] < seq[i]:
            check.append([seq[i], 1])
            if len(check) >= k-1:
                mult = 1
                for l in range(len(check)):
                    if check[l][1] > 1:
                        mult *= check[l][1]

                combination = 0
                div = 1
                for l in range(k - 1):
                    combination += (len(check) - 1 - k)
                    div *= k + 1
                num += combination * mult / div

        # if not, find appropriate index for 'i' in 'check'
        else:
            # find from end to front
            for j in range(len(check)-1, -1, -1):
                if check[j][0] < i:
                    check[j+1][0] = i
                    check[j+1][1] = 1

                    if j+1 >= k-1:
                        # new item added in 'check[j+1]'
                        # combination from 0 ~ j
                        mult = 1
                        for l in range(j+1):
                            if check[l][1] > 1:
                                mult *= check[l][1]

                        combination = 0
                        div = 1
                        for l in range(k-1):
                            combination += (j+2-k)
                            div *= k+1
                        num += combination * mult / div
                    break
                elif check[j][0] == i:
                    check[j][1] += 1
                elif j == 0:
                    check[0][0] = i
                    check[0][1] = 1

    print(num)