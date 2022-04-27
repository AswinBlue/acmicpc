import sys
sys.setrecursionlimit(10**6)

MAX_VALUE = 9999999999
DEBUG = 0

# fill leaf nodes with inputs
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
# @arg : tree : data structure array
# @arg : target_left : target range start index
# @arg : target_right : target range end index
# @arg : left : left index that current node covers
# @arg : right : right index that current node covers
# @arg : tree_idx : current index in tree
# @arg : input : input array
# @arg : arr_idx : current index in array
# @return : return smallest height
def search_index_tree(target_left, target_right, left, right, idx):
    # set exit condition
    if target_left <= left and target_right >= right:
        # current node is in target range
        return index_tree[idx]
    elif target_left > right or target_right < left:
        # current node isn't in target range
        return -1
    else:
        mid = (left + right) // 2
        # check left
        return_left = search_index_tree(target_left, target_right, left, mid, idx * 2)
        # check right
        return_right = search_index_tree(target_left, target_right, mid + 1, right, idx * 2 + 1)

        if return_left == -1:
            result_left = MAX_VALUE
        else:
            result_left = inputs[return_left]
            
        if return_right == -1:
            result_right = MAX_VALUE
        else:
            result_right = inputs[return_right]
        
        # return index of min value
        if result_left < result_right:
            return return_left
        else:
            return return_right

def find_max_area(length, start, end) :
    # finish condition
    if start == end:
        return inputs[start]
    elif start > end:
        return 0

    # mid =  search_height_tree(height_tree, left, right, left, right, 1)

    # go until meets leaf node
    mid = search_index_tree(start, end, 1, length, 1)
    height = inputs[mid]
    
    if DEBUG:
        print('find max', start, mid, end)

    left_result = find_max_area(length, start, mid - 1)
    right_result = find_max_area(length, mid + 1, end)

    if DEBUG:
        print('find max cmp', start, end, left_result, right_result)

    return  max(left_result, right_result, height * (end - start + 1))


if __name__ == '__main__':
    while True:
        inputs = list(map(int, input().split()))
        # finishing condition
        if inputs[0] == 0 :
            break
        
        length = inputs[0]
        # make binary tree
        index_tree = [MAX_VALUE for x in range(4 * length)]

        # fill leaf nodes
        init_tree(index_tree, 1, length, 1)
        
        # make segment tree with root index '1'
        # fill_tree(height_tree, index_tree, 1, length, 1)

        if DEBUG:
            print(index_tree)

        max_area = find_max_area(length, 1, length)

        # result = get_max_area(height_tree, 1, length, 1, length, 1)
        print(max_area)