# 시간복잡도 O(n^2)
"""
if __name__ == '__main__':
    n = int(input())
    seq = []
    for i in map(int,input().split()):
        seq.append(i)

    amount = [1]
    for i in range(1, len(seq)):
        maxAmount = 0
        for j in range(i):
            if maxAmount < amount[j] and seq[j] < seq[i]:
                maxAmount = amount[j]
        amount.append(maxAmount+1)

    print(amount[-1])
"""


# 시간복잡도 O(n*log(n))

# binary search
# find index of 'target' in 'arr'
def search(start, end, arr, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            end = mid
        elif arr[mid] > target:
            start = mid
        # if target destination found
        else:
            return mid
    # if nothing found, return end
    return end


if __name__ == '__main__':
    n = int(input())
    seq = []
    for i in map(int, input().split()):
        seq.append(i)

    check = [seq[0]]
    for i in range(1, len(seq)):
        # if increasing sequence
        if check[-1] < seq[i]:
            check.append(seq[i])
        # if not, find appropriate index for 'i' in 'check'
        else:
            """
            # find from end to front
            for j in range(len(check)-1, -1, -1):
                if check[j] < i:
                    check[j+1] = i
                    break
                elif j == 0:
                    check[0] = i
            """
            check[search(0, i-1, check, seq[i])] = seq[i]

    print(len(check))
