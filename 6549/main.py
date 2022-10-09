# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

import sys
sys.setrecursionlimit(10**6)

MAX_VALUE = 9999999999
DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

# fill leaf nodes with inputs
# complete binary tree를 배열로 표현할 때, leaf node들을 초기화하는 함수
# index_tree[i]에는 index_tree[i*2], index_tree[i*2+1] 중 더 작은 값이 들어감
def init_tree(index_tree, start, end, idx):
    if start == end:
        # height_tree[idx] = inputs[start]
        index_tree[idx] = start
        return index_tree[idx]

    mid = (start + end) // 2

    # go through leaf node
    left_idx = init_tree(index_tree, start, mid, idx * 2)
    right_idx = init_tree(index_tree, mid + 1, end, idx * 2 + 1)

    left_height = inputs[left_idx]
    right_height = inputs[right_idx]

    # calculate non-leaef nodes
    if left_height < right_height:
        index_tree[idx] = left_idx
    else:
        index_tree[idx] = right_idx

    return index_tree[idx]

# @desc: searching tree
# @arg : target_left : target range start index
# @arg : target_right : target range end index
# @arg : left : left index that current node covers
# @arg : right : right index that current node covers
# @arg : idx : current index in tree
# @return : return smallest height
def search_index_tree(target_left, target_right, left, right, idx):
    global inputs, index_tree
    # set exit condition
    if target_left <= left and target_right >= right:
        # current node is in target range
        return index_tree[idx]
    elif target_left > right or target_right < left:
        # current node isn't in target range
        return -1
    else:
        # current node has intersection of target area
        # 일부는 포함되고, 일부는 포함되지 않은 경우 계속 좌우로 쪼개서 확인하다 보면 결국 목표 영역 값만 얻을 수 있다.
        mid = (left + right) // 2
        # check left
        return_left = search_index_tree(target_left, target_right, left, mid, idx * 2)
        # check right
        return_right = search_index_tree(target_left, target_right, mid + 1, right, idx * 2 + 1)

        result_left = inputs[return_left]
        result_right = inputs[return_right]
        
        # return index of min value
        if result_left < result_right:
            return return_left
        else:
            return return_right

# 문제에서 요구하는 답을 구하는 함수
def find_max_area(length, start, end) :
    # finish condition
    if start == end:
        return inputs[start]
    elif start > end:
        return 0

    # find index of min height over 'start' ~ 'end'
    min_idx = search_index_tree(start, end, 1, length, 1)
    height = inputs[min_idx]
    
    Print('find max', start, min_idx, end)

    # 최소 높이를 기점으로 좌 우 영역에서 형성 가능한 최대 넓이를 살펴본다.
    left_result = find_max_area(length, start, min_idx - 1)
    right_result = find_max_area(length, min_idx + 1, end)

    Print('find max cmp', start, end, left_result, right_result)

    # 'start'~'end' 영역에서 만들 수 있는 최대 넓이의 사각형은
    # 좌측 영역 결과 : 우측 영역 결과 : 현재 영역 결과  를 비교한 결과이다. 
    return  max(left_result, right_result, height * (end - start + 1))


# 문제 접근법:
# i ~ j 까지 index의 히스토그램에서 가장 큰 사각형의 크기를 memoization 으로 해결하려 접근한다. 
# DP를 이용해 2차원배열로 memoization 할 수도 있지만, 메모리 사용량이 초과된다.
# 대신 부분합을 이용하면 연산 시간을 단축하고, 메모리 사용량도 초과하지 않는다.
# 부분합은 tree 형태로 저장하여 기록한다. 
if __name__ == '__main__':
    while True:
        inputs = list(map(int, input().split()))
        # finishing condition
        if inputs[0] == 0 :
            break
        
        length = inputs[0]
        inputs.append(MAX_VALUE)  # search_index_tree() 에서 계산 편의를 위해 추가
        # make segment tree with root index '1'
        # 부분합을 저장할 배열 생성
        index_tree = [MAX_VALUE for x in range(4 * length)]

        # fill leaf nodes
        # tree의 leaf node에 입력으로 받은 데이터들을 기입한다.
        # index_tree의 leaf node에는 각 히스토그램의 높이가 들어가고, 그 부모 node에는 두 자식 node중 더 작은 높이의 index가 기입된다.
        init_tree(index_tree, 1, length, 1)
        
        Print(index_tree)

        max_area = find_max_area(length, 1, length)

        print(max_area)