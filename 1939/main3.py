# collapsing find
def find(tree, A):
    #print('find+', tree)
    res = A
    while tree[res] >= 0:
         res = tree[res]

    tmp = A
    while tree[tmp] >= 0:
        if tree[tmp] != res:
            tmp2 = tree[tmp]
            tree[tmp] = res
            tmp = tmp2
        else:
            tmp = tree[tmp]
    #print('find-', tree)
    return res

# find root of A B, and join them into disjoint set tree
def check(tree, A, B):
    A_root = find(tree, A)
    B_root = find(tree, B)
    # if 'A' 'B' are already in same tree, do nothing
    if A_root == B_root:
        return
    
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
        arr.append((A,B,C))
    start, end = map(int, input().split())

    #print(arr)
    arr.sort(key = lambda arr : arr[2])
    #print(arr)
    tree = [-1 for i in range(N+1)]
    while len(arr) > 0:
        A, B, C = arr.pop()
        check(tree, A, B)
        #print(A, B, C, tree, arr)
        if find(tree, start) == find(tree, end):
            break
    print(C)
