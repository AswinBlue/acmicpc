# 울타리
# https://www.acmicpc.net/problem/1047

DEBUG = 1
def Print(*arg):
    if DEBUG:
        print(*arg)

MAX_N = 40
MIN_N = 2
MAX_VALUE = 1_000_000



def solve(x_sorted, y_sorted, x_left, x_right, y_left, y_right, lumber, chopped_tree, requiring_lumber):
    global N, max_chopped_tree
    
    if chopped_tree >= max_chopped_tree:  # not promising
        return
    
    if lumber >= requiring_lumber:  # finish condition
        if chopped_tree < max_chopped_tree:
            max_chopped_tree = chopped_tree
        return
    Print(f"chopped_tree: {chopped_tree}, max: {max_chopped_tree}, req: {requiring_lumber}, lumber: {lumber}\n{x_sorted}\n{y_sorted}")

    # 값이 0인 나무는 이미 베었다는 뜻, 다음으로 넘어간다. 
    while x_sorted[x_left][VALUE] == 0 and x_left < x_right:
        x_left += 1
    while x_sorted[x_right][VALUE] == 0 and x_left < x_right:
        x_right -= 1
    while y_sorted[y_left][VALUE] == 0 and y_left < y_right:
        y_left += 1
    while y_sorted[y_right][VALUE] == 0 and y_left < y_right:
            y_right -= 1

    # 가장 promising 한 나무를 찾는다.
    # ERROR: 가장 가쪽에서부터 나무를 베어나가는 방법은, 놓치는 부분이 있다.
    #        greedy 한 방법으로는 해결이 불가능하다.
    #        in.txt 경우가 이 방법을 사용할 수 없는 반례이다.
    
    if x_left < x_right:  # 나무가 둘 이상 있어야 비교 가능
        # A나무(최좌측 나무)를 잘랐을 떄 얻을 수 있는 기대값(줄어드는 테두리 길이 & 늘어나는 목재)
        decreased_length = (x_sorted[x_left + 1][X] - x_sorted[x_left][X]) * 2 
        acquired_lumber = x_sorted[x_left][VALUE]
        # A 를 자르고 난 뒤 연산 기댓값
        x_sorted[x_left][VALUE] = 0  # A를 잘랐음을 처리
        solve(x_sorted, y_sorted, x_left + 1, x_right, y_left, y_right, lumber + acquired_lumber, chopped_tree + 1, requiring_lumber - decreased_length)
        x_sorted[x_left][VALUE] = acquired_lumber  # 하위 연산 후 복구
    if x_left < x_right:
        decreased_length = (x_sorted[x_right][X] - x_sorted[x_right - 1][X]) * 2 
        acquired_lumber = x_sorted[x_right][VALUE]
        x_sorted[x_right][VALUE] = 0
        solve(x_sorted, y_sorted, x_left, x_right - 1, y_left, y_right, lumber + acquired_lumber, chopped_tree + 1, requiring_lumber - decreased_length)
        x_sorted[x_right][VALUE] = acquired_lumber
    if y_left < y_right:
        decreased_length = (y_sorted[y_left + 1][Y] - y_sorted[y_left][Y]) * 2
        acquired_lumber = y_sorted[y_left][VALUE]
        y_sorted[y_left][VALUE] = 0
        solve(x_sorted, y_sorted, x_left, x_right, y_left + 1, y_right, lumber + acquired_lumber, chopped_tree + 1, requiring_lumber - decreased_length)
        y_sorted[y_left][VALUE] = acquired_lumber
    if y_left < y_right:
        decreased_length = (y_sorted[y_right][Y] - y_sorted[y_right - 1][Y]) * 2 
        acquired_lumber = y_sorted[y_right][VALUE]
        y_sorted[y_right][VALUE] = 0
        solve(x_sorted, y_sorted, x_left, x_right, y_left, y_right - 1, lumber + acquired_lumber, chopped_tree + 1, requiring_lumber - decreased_length)
        y_sorted[y_right][VALUE] = acquired_lumber

        # result = max(A,B,C,D)
        # Print("A,B,C,D,result:", A,B,C,D,result)
        # if result == A:
        #     lumber += x_sorted[x_left][VALUE]
        #     x_sorted[x_left][VALUE] = 0
        # elif result == B:
        #     lumber += x_sorted[x_right][VALUE]
        #     x_sorted[x_right][VALUE] = 0
        # elif result == C:
        #     lumber += y_sorted[y_left][VALUE]
        #     y_sorted[y_left][VALUE] = 0
        # elif result == D:
        #     lumber += y_sorted[y_right][VALUE]
        #     y_sorted[y_right][VALUE] = 0

        # chopped_tree += 1
        # requiring_lumber = (x_sorted[x_right][X] - x_sorted[x_left][X]) + (y_sorted[y_right][Y] - y_sorted[y_left][Y])  # 필요한 목재 갱신
        # Print("chopped_tree:", chopped_tree, "lumber:", lumber, "requiring_lumber:", requiring_lumber)


if __name__ == '__main__':
    X = 0
    Y = 1
    VALUE = 2

    N = int(input())
    x_sorted = [None for _ in range(N)]
    y_sorted = [None for _ in range(N)]
    x_left = x_right = 0
    y_left = y_right = 0

    for n in range(N):
        x,y,v = map(int, input().split())
        tree = [x,y,v]  # x좌표, y좌표, 울타리 재료 양
        x_sorted[x_right] = tree
        x_right += 1
        y_sorted[y_right] = tree
        y_right += 1

    # 나무의 속성을 배열로 구성하였다. 배열은 mutable 객체이므로 x_sort[] 와 y_sort[] 는 동일한 객체의 주소를 참조하도록 설정된다. 
    x_sorted = sorted(x_sorted, key=lambda t : t[0])  # REF: python sorting
    y_sorted = sorted(y_sorted, key=lambda t : t[1])

    Print(f"{x_sorted}\n{y_sorted}")

    x_right = y_right = N - 1  # 시작 위치 세팅

    #  x,y 축에 대해 각각 sorting 된 두 개의 배열이 존재한다. 
    #  가장 외곽의 나무들에 대해 (1) 나무를 베었을 떄 나오는 울타리의 양, (2) 나무를 베었을 때 줄어드는 테두리 길이 를 구한다.
    #  1과 2를 합산한 값이 가장 큰 나무를 먼저 제거한다.
    #  제거한 나무는 value를 0으로 변경한다. list에서 pop 하는것 보다 리소스가 적게든다.

    max_chopped_tree = MAX_N  # 최대 벌목한 나무
    requiring_lumber = (x_sorted[x_right][X] - x_sorted[x_left][X]) + (y_sorted[y_right][Y] - y_sorted[y_left][Y])  # 필요한 목재
    solve(x_sorted, y_sorted, 0, N-1, 0, N-1, lumber=0, chopped_tree=0, requiring_lumber=requiring_lumber) # 보유한 목재 0, 벌목한 나무 0
    

    print(max_chopped_tree)

