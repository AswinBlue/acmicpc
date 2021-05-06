import sys
sys.setrecursionlimit(10**6)

# collapsing find
def find(tree, A):
    if tree[A] < 0:
        return A
    res = find(tree, tree[A])
    if tree[A] != res:
        tree[A] = res
    return res

# find root of A B, and join them into minimum spanning tree
def check(tree, A, B):
    A_root = find(tree, A)
    B_root = find(tree, B)
    if tree[A_root] > tree[B_root]:
        tree[B_root] += tree[A_root]
        tree[A_root] = B_root
    else:
        tree[A_root] += tree[B_root]
        tree[B_root] = A_root

if __name__ == "__main__":
    INF = 1000000001
    N, M = map(int, input().split())
    arr = []

    for i in range(M):
        A, B, C = map(int, input().split())
        arr.append((A-1,B-1,C))
    start, end = map(int, input().split())

    start -= 1
    end -= 1

    #print(arr)
    arr.sort(key = lambda arr : arr[2])
    #print(arr)
    tree = [-1 for i in range(N)]
    while len(arr) > 0:
        A, B, C = arr.pop()
        check(tree, A, B)
        #print(A, B, C, tree)
        if find(tree, start) == find(tree, end):
            print(C)
            break

