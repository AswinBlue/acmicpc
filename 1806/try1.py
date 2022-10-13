# https://www.acmicpc.net/problem/1806
# 부분합
from sys import setrecursionlimit

DEBUG = 0
MAX_N = 100000
MAX_S = 100000000
setrecursionlimit(MAX_N)  # log(n)회 반복 발생 가능
def Print(*args):
    if DEBUG:
        print(*args)

# list의 부분합을 tree 형태로 나타내는 작업 수행
def init_tree(start, end, idx):
    global nums, tree

    if start == end:
        tree[idx] = nums[start]
        return tree[idx]  # left node 도달시, 현재 node 작성 후 현재값 반환
    elif start > end:
        return 0  # error
    
    # start < end 인 경우 아래 수행

    mid = (start + end) // 2
    left = init_tree(start, mid, idx*2)
    right = init_tree(mid+1, end, idx*2+1)
    tree[idx] = left + right  # 현재 node 값 설정
    return tree[idx]  # 현재 값 반환

# @brief    : tree에서 지정된 범위의 부분합에 해당하는 부분을 찾아 반환
# @param    list_start  : 현재 node가 커버하는 부분합의 좌측 범위
# @param    list_end    : 현재 node가 커버하는 부분합의 우측 범위
# @param    target_start: 찾고자하는 범위 좌측부분
# @param    target_end  : 찾고자하는 범위 우측부분
# @param    idx         : tree에서 현재 node의 index
def find_partial_sum(list_start, list_end, target_start, target_end, idx):
    global nums, tree
    Print(list_start, list_end, target_start, target_end, idx)

    # case 1, 현재 node가 전체범위를 커버하는 경우
    if target_start <= list_start and list_end <= target_end:
        return tree[idx]  # 현재 node의 값 반환
    # case 2, 현재 node가 범위를 커버하지 못하는 경우
    elif list_end < target_start or target_end < list_start:
        return 0
    # case 3, 현재 node가 일부 범위를 커버하는 경우
    else:
        mid = (list_start + list_end) // 2
        # 다시 좌우로 나눠서 확인, case 1이나 2가 될때까지 게속 반복
        left = find_partial_sum(list_start, mid, target_start, target_end, idx*2)
        right = find_partial_sum(mid+1, list_end, target_start, target_end, idx*2+1)
        Print('sum:',left, right)
        return left + right

################################################################
# main 로직 시작
N, S = map(int, input().split())

nums = list(map(int, input().split()))

# tree 형태로 부분합을 지정한다.
length = len(nums)
tree = [0 for _ in range(length * 4)]  # complete binary tree, leaf node가 length개라면, 전체 node는 length * 4개면 충분

# complete binary tree 형태의 부분합 저장
init_tree(0, length-1, 1)  # tree의 root는 1
Print(tree)

# 길이를 1부터 늘려가며 부분합이 S 이상이 나올 때 까지 검사
found = False
for l in range(1, length+1):
    for start in range(0, length):
        end = start + l - 1
        # 범위 초과시 종료
        if end >= length:
            break
        result = find_partial_sum(0, length-1, start, end, 1)
        Print(result)
        # 길이가 가장 짧으면서 합이 S 이상인값 찾음 
        if result >= S:
            # 일단 이중 반복문을 한번 탈출하고, 밖에서 출력후 종료
            found = True
            break
    if found:
        print(l)  # 결과 출력
        # 탐색 종료
        break
# 발견못한 경우 0 출력
if not found:
    print(0)