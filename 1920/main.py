def binary_search(start, end, target, A):
    # terminate condition
    if start > end:
        return 0

    mid = (start + end) // 2
    # print('start', start, 'end',  end, 'mid', mid, 'target', target, 'A[mid]',  A[mid])
    if A[mid] == target:
        # found target
        return 1
    elif A[mid] > target:
        return binary_search(start, mid - 1, target, A)
    elif A[mid] < target:
        return binary_search(mid + 1, end, target, A)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    numbers = list(map(int, input().split()))

    # print(A, numbers)

    A.sort()
    
    for n in numbers:
        print(binary_search(0, N - 1, n, A))

