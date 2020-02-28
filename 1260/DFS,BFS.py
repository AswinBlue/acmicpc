# node for adjacency list
class Node:
    def __init__(self,start,end,next=None):
        self.start = start
        self.end = end
        self.next = next


# recursive part in dfs
# can occur runtime error if code recursively
"""
def _dfs(G, ptr, visit):
    # check if visited
    if visit[ptr.start - 1] == 0:
        # mark as visited
        visit[ptr.start - 1] = 1
        print(ptr.start, end=' ')

    # go to next node
    if G[ptr.end - 1].next is not None:
        if visit[ptr.end-1] == 0:
            _dfs(G, G[ptr.end - 1].next, visit)

    # check next edge
    if ptr.next is not None:
        _dfs(G, ptr.next, visit)
"""


def dfs(n, G, start):
    visit = [0 for i in range(n)]
    stack = [start]

    while len(stack) > 0:
        num = stack.pop()
        # need to check visited before print, because multiple items can exist in the stack
        if visit[num-1] == 0:
            print(num, end=' ')
            visit[num-1] = 1

        ptr = G[num-1].next
        edge = []
        while ptr is not None:
            if visit[ptr.end-1] == 0:
                # gather all nodes connected to 'num' node
                edge.append(ptr.end)
            ptr = ptr.next
        # sort nodes and push to the stack
        edge.sort(reverse=True)
        stack.extend(edge)
    # recursive method
    """
    ptr = G[start - 1].next
    while ptr is not None:
        _dfs(G, ptr, visit)
        ptr = ptr.next
    """
    print()


def bfs(n, G, start):
    visit = [0 for i in range(n)]
    queue = [start]
    visit[start-1] = 1

    while len(queue) > 0:
        num = queue.pop(0)
        print(num, end=' ')

        ptr = G[num-1].next
        edge = []
        while ptr is not None:
            # to make queue size smaller, you'd better check & mark visited when pushing
            # if check & mark visited when popping, queue will have many duplicated item
            if visit[ptr.end - 1] == 0:
                edge.append(ptr.end)
                # mark as visited when pushing
                visit[ptr.end - 1] = 1
            ptr = ptr.next
        edge.sort()
        queue.extend(edge)
    print()


if __name__ == '__main__':
    # Make Graph with adjacency list
    # 1) get input
    n, m, v = map(int,input().split())
    G = [Node(0,0) for i in range(n)]
    endp = [0 for i in range(n)]
    for i in range(n):
        endp[i] = G[i]

    # 2) make adjacency list with inputs
    # unweighted undirected graph
    for i in range(m):
        start, end = map(int, input().split())
        tmp = Node(start, end)
        endp[start-1].next = tmp
        endp[start-1] = tmp
        tmp = Node(end,start)
        endp[end-1].next = tmp
        endp[end-1] = tmp

    # 3) do dfs
    dfs(n, G, v)
    # 4) do bfs
    bfs(n, G, v)
