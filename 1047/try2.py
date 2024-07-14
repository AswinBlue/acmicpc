# 울타리
# https://www.acmicpc.net/problem/1047

# ERROR: MAX_N이 40이므로 40^4회 연산은 시간초과가 걸린다.

DEBUG = 0
def Print(*arg):
    if DEBUG:
        print(*arg)

MAX_N = 40
MIN_N = 2
MAX_VALUE = 1_000_000

def solve(x_sorted, y_sorted, v_sorted, x_left, x_right, y_left, y_right, v_right, lumber, chopped_tree):
    global N, max_chopped_tree
    
    if chopped_tree >= max_chopped_tree:  # not promising
        return

    # 값이 0인 나무는 이미 베었다는 뜻, 다음으로 넘어간다. 
    while x_sorted[x_left][VALUE] == 0 and x_left < x_right:
        x_left += 1
    while x_sorted[x_right][VALUE] == 0 and x_left < x_right:
        x_right -= 1
    while y_sorted[y_left][VALUE] == 0 and y_left < y_right:
        y_left += 1
    while y_sorted[y_right][VALUE] == 0 and y_left < y_right:
        y_right -= 1
    while v_sorted[v_right][VALUE] == 0 and 0 < v_right:
        v_right -= 1

    requiring_lumber = ((x_sorted[x_right][X] - x_sorted[x_left][X]) + (y_sorted[y_right][Y] - y_sorted[y_left][Y])) * 2  # 필요한 목재 계산
        
    Print(f"chopped_tree: {chopped_tree}, max: {max_chopped_tree}, req: {requiring_lumber}, lumber: {lumber}\n{x_sorted}\n{y_sorted}\n{v_sorted}")

    if lumber >= requiring_lumber or chopped_tree + 1 == N:  # finish condition (1. 목재가 울타리에 필요한 양 이상 마련됨. 2. 나무가 하나만 남음)
        if chopped_tree < max_chopped_tree:
            Print('--\t--\t--\t--\tUPDATE_MAX:', chopped_tree)
            max_chopped_tree = chopped_tree
        return
    

    # 가장 promising 한 나무를 찾는다.
    if x_left < x_right:  # 나무가 둘 이상 있어야 비교 가능
        # 최좌측 나무를 잘랐을 떄 얻을 수 있는 기대값(줄어드는 테두리 길이 & 늘어나는 목재)
        acquired_lumber = x_sorted[x_left][VALUE]
        # A 를 자르고 난 뒤 연산 기댓값
        x_sorted[x_left][VALUE] = 0  # A를 잘랐음을 처리
        solve(x_sorted, y_sorted, v_sorted, x_left + 1, x_right, y_left, y_right, v_right, lumber + acquired_lumber, chopped_tree + 1)
        x_sorted[x_left][VALUE] = acquired_lumber  # 하위 연산 후 복구
    if x_left < x_right:
        # 최우측 나무를 잘랐을 떄
        acquired_lumber = x_sorted[x_right][VALUE]
        x_sorted[x_right][VALUE] = 0
        solve(x_sorted, y_sorted, v_sorted, x_left, x_right - 1, y_left, y_right, v_right, lumber + acquired_lumber, chopped_tree + 1)
        x_sorted[x_right][VALUE] = acquired_lumber
    if y_left < y_right:
        # 최상단 나무를 잘랐을 떄
        acquired_lumber = y_sorted[y_left][VALUE]
        y_sorted[y_left][VALUE] = 0
        solve(x_sorted, y_sorted, v_sorted, x_left, x_right, y_left + 1, y_right, v_right, lumber + acquired_lumber, chopped_tree + 1)
        y_sorted[y_left][VALUE] = acquired_lumber
    if y_left < y_right:
        # 최하단 나무를 잘랐을 떄
        acquired_lumber = y_sorted[y_right][VALUE]
        y_sorted[y_right][VALUE] = 0
        solve(x_sorted, y_sorted, v_sorted, x_left, x_right, y_left, y_right - 1, v_right, lumber + acquired_lumber, chopped_tree + 1)
        y_sorted[y_right][VALUE] = acquired_lumber
    if 0 < v_right and v_sorted[v_right][VALUE] > 0:
        # 가장 목재가 많이 나오는 나무를 잘랐을 때
        acquired_lumber = v_sorted[v_right][VALUE]
        v_sorted[v_right][VALUE] = 0
        x = v_sorted[v_right][X]
        y = v_sorted[v_right][Y]
        # 모서리의 나무를 자른 경우에 대비해 한 번 더 체크
        if x == x_sorted[x_left][X]:
            x_left += 1
        if x == x_sorted[x_right][X]:
            x_right -= 1
        if y == y_sorted[y_left][X]:
            y_left += 1
        if y == y_sorted[y_right][X]:
            y_right -= 1

        solve(x_sorted, y_sorted, v_sorted, x_left, x_right, y_left, y_right, v_right - 1, lumber + acquired_lumber, chopped_tree + 1)
        v_sorted[v_right][VALUE] = acquired_lumber

if __name__ == '__main__':
    X = 0
    Y = 1
    VALUE = 2

    N = int(input())
    x_sorted = [None for _ in range(N)]
    y_sorted = [None for _ in range(N)]
    v_sorted = [None for _ in range(N)]
    x_left = x_right = 0
    y_left = y_right = 0
    v_right = 0

    for n in range(N):
        x,y,v = map(int, input().split())
        tree = [x,y,v]  # x좌표, y좌표, 울타리 재료 양
        x_sorted[x_right] = tree
        x_right += 1
        y_sorted[y_right] = tree
        y_right += 1
        v_sorted[v_right] = tree
        v_right += 1

    # 나무의 속성을 배열로 구성하였다. 배열은 mutable 객체이므로 x_sort[] 와 y_sort[] 는 동일한 객체의 주소를 참조하도록 설정된다. 
    x_sorted = sorted(x_sorted, key=lambda t : t[0])  # REF: python sorting
    y_sorted = sorted(y_sorted, key=lambda t : t[1])
    v_sorted = sorted(v_sorted, key=lambda t : t[2])

    Print(f"{x_sorted}\n{y_sorted}\n{v_sorted}")

    x_right = y_right = v_right = N - 1  # 시작 위치 세팅

    #  x,y 축에 대해 각각 sorting 된 두 개의 배열이 존재한다. 
    #  가장 외곽의 나무들에 대해 (1) 나무를 베었을 떄 나오는 울타리의 양, (2) 나무를 베었을 때 줄어드는 테두리 길이 를 구한다.
    #  1과 2를 합산한 값이 가장 큰 나무를 먼저 제거한다.
    #  제거한 나무는 value를 0으로 변경한다. list에서 pop 하는것 보다 리소스가 적게든다.

    max_chopped_tree = MAX_N  # 최대 벌목한 나무
    solve(x_sorted, y_sorted, v_sorted, x_left, x_right, y_left, y_right, v_right, lumber=0, chopped_tree=0) # 보유한 목재 0, 벌목한 나무 0

    print(max_chopped_tree)

