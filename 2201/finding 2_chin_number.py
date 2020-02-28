# 이친수를 tree로 나타내면, 순서대로 정렬 하기 쉽다.
# root부터 level이 n인 node까지 경로상의 node들을 합치면 n자리 이친수가 된다.
# node 의 형태는 다음과 같다.
"""
1
0
01
010
010 01
010 01 010
010 01 010 010 01
"""
# 자세히 살펴보면 규칙이 있다.
# n level의 node는 n-1 level의 node에 n-2 level의 node를 붙인 형태이다.
# ex) n=4일 때, 010 01 에서 010은 n-1 level, 01은 n-2 level의 node들이다.
# 이를 이용하여 문제를 푼다.

# node를 다 저장하기엔 용량이 너무 많이 차지하므로, node들의 숫자를 배열에 저장한다.
# 점화식을 이용하여 k보다 값이 커질 때 까지 배열의 다음 원소를 찾아나간다.

if __name__ == '__main__':
    k = int(input())
    # tree의 어떤 node 까지의 경로상의 모든 node들을 이어붙이면 이친수 하나를 나타낸다.
    # node의 탐색 경로가 이친수 하나를 나타내므로, node 하나당 이친수 하나를 나타낸다고 봐도 된다.
    # level이 클수록 이친수의 크기도 크다.
    # level order로 node를 나열하면 이친수의 크기별로 나열할 수 있다.
    # k번째 node가 몇 번째 level에 있는지 먼저 찾고, 그 level에서 위치를 찾는다.

    # tree[i]는 depth
    tree = [1, 1, 2]
    nodes = 0
    depth = 0
    while True:
        if len(tree) <= depth:
            tree.append(tree[-1] + tree[-2])

        if nodes + tree[depth] >= k:
            break
        nodes += tree[depth]
        depth += 1

    # k번째 node는 'depth' 깊이의 'n' 번째 원소이다.
    n = k - nodes

    # tree[depth]의 node들을 직접 구한다.
    # 'depth' 깊이의 node들만 구하면, tree의 모든 node들을 알 수 있다.
    # 'depth' 에 있는 node들을 앞에서 일정 길이만큼 자르면 다른 깊이의 node들이 되기 때문
    C = ''
    C_1 = '0'
    C_2 = '1'
    for i in range(depth):
        C = C_1 + C_2
        C_2 = C_1
        C_1 = C

    # 마지막 digit을 결과에 저장한다.
    # 뒷쪽부터 차례로 집어넣을 것이다.
    result = [C[n]]

    # 현재 level에서 (1의 갯수)만큼 윗 level에서 0이 존재 할 것이며, 현재 level에서 (1의 갯수 - 0의 갯수)만큼 윗 level에서 1이 존재할 것이다.
    # num0 num1는 각각 d 깊이에서 ptr까지의 원소들 중 0, 1의 갯수를 나타낸다.
    # 따라서 윗 level의 num1 + (num0 - num1),즉 num0번째 node에서 현재 level의 ptr번째 node가 생성된 것이다.
    ptr = n
    d = depth
    while d > 1:
        num0 = 0
        # C[0:ptr+1]에서 1의 갯수 세기
        for i in C[0:ptr]:
            if i == '0':
                num0 += 1
        ptr = num0
        result.append(C[ptr-1])
        d -= 1

    # 첫자리 1 추가
    result.append('1')
    result.reverse()
    for i in result:
        print(i, end='')
    print()


# <1차 시도> 메모리 초과
"""
    # tree의 node 하나는 이친수 하나를 나타낸다고 해도 된다.
    # level이 클수록 이친수의 크기도 크다.
    # k번째 node가 몇 번째 level에 있는지 먼저 찾고, 그 level에서 위치를 찾은 후 규칙을 이용해 이친수를 찾아낸다.
    tree = [1, 0, 2]
    nodes = 0
    level = 0
    while True:
        level += 1
        if len(tree) < level:
            tree.append(tree[-1] + tree[-2])

        if nodes + tree[level-1] >= k:
            break
        nodes += tree[level-1]

    # 해당 node는 'level' level의 'n' 번째 원소이다.
    n = k - nodes


    # 찾아낸 'level' + 1 level 까지 점화식을 통해 실제 이친수를 구한다.
    pinary = [[] for i in range(level)]
    pinary[0].append(1)
    pinary[1].append(0)
    for i in range(2,level):
        pinary[i].extend(pinary[i - 1])
        pinary[i].extend(pinary[i - 2])

    # 뒷 자리 부터 거꾸로 찾아간다
    result = [pinary[level-1][n-1]]
    # 자릿수를 가리키는 포인터
    ptr = n
    for i in range(level-1, 0, -1):
        num0 = 0
        num1 = 0
        for j in range(ptr):
            if pinary[i][j] == 0:
                num0 += 1
            # elif pinary[i][j] == 1:
            #    num1 += 1
        # num0 num1은 각각 ptr 번째 앞의 0과 1의 갯수이다. 
        # 현재 level에서 (1의 갯수)만큼 윗 level에서 0이 존재 할 것이며, 현재 level에서 (1의 갯수 - 0의 갯수)만큼 윗 level에서 1이 존재할 것이다.
        # 따라서 윗 level의 num1 + (num0 - num1),즉 num0번째 node에서 현재 level의 ptr번째 node가 생성된 것이다.
        ptr = num0
        result.append(pinary[i-1][ptr-1])

    result.reverse()
    for i in result:
        print(i, end='')
    print()
"""

# <2차 시도>
# tree에 0과 1의 갯수를 따로 저장한다.
"""
tree = [[0, 1], [1, 0], [1, 1]]

nodes = 0
depth = 0
while True:
    # tree의 다음 원소 추가 조건
    if len(tree) <= depth:
        # 0은 이전의 0과 1의 갯수에 비례한다. 1은 이전의 0의 갯수에 비례한다.
        tree.append([tree[-1][0] + tree[-2][0] + tree[-1][1] + tree[-2][1], tree[-1][0] + tree[-2][0]])

    #
    if nodes + tree[depth][0] + tree[depth][1] >= k:
        break
    nodes += tree[depth][0] + tree[depth][1]
    depth += 1

n = k - nodes
# 우리가 찾는 node는 depth + 1 의 깊이를 가진 n 번째 node
# 결과를 아랫 level부터 찾아서 집어넣는다.

# <2차 시도중 실패한 부분> 메모리 초과를 없애려고 실제 tree의 node들을 직접 구하지 않으려 했다.
# 하지만 직접 tree를 구하지 않고는 방법이 너무 복잡해져서 포기한 방법
# 대신 tree의 마지막 level만 구함으로서 메모리를 절약했다.

# 현재 level의 n번째의 node가 result에 들어갔다.
parent = n
for i in range(depth, 0, -1):
    d = i
    # depth -1의 node, 즉 parent를 찾기 위해 사용한 임시 변수 counter
    cnt = parent
    # depth -1의 parent번째의 node를 result에 넣어야 한다.
    parent = 0
    while cnt > 0:
        d -= 1
        if tree[d][0] + tree[d][1] < cnt:
            cnt -= tree[d][0] + tree[d][1]
            parent += tree[d][1]
            # 규칙의 예외, tree[1]에는 1이 없다. tree[2]의 모든 원소는 0으로부터 파생된다.
            if i == 1:
                parent += 1
    result.append(C[parent])
"""