# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

import sys
input = sys.stdin.readline

def find_max_area_stack(heights):
    """
    Calculates the largest rectangular area in a histogram using a monotonic stack.
    Time complexity: O(N)
    Space complexity: O(N)
    """
    stack = []  # Stack will store tuples of (index, height)
    max_area = 0
    
    # Append a 0-height bar to flush the stack at the end
    extended_heights = heights + [0]  # 아래 알고리즘에서 stack에 남아있는 값들을 모두 처리하고 시퀀스를 종료하기 위해 끝에 0을 추가

    # 핵심 알고리즘
    # stack 을 이용하여 점진적 계산
    # stack 에는 (idx, height) 가 들어가고, 이는 넓이 연산에 필요한 가로 시작점(index)과 높이(height)를 담고 있다.
    # 0번 index부터 블록을 순회하며 현재 블록이 stack의 top 보다 높이가 높으면 stack에 쌓고, 높이가 낮으면 연산을 진행한다.
    # stack의 top에 있는 높이가 현재 높이보다 낮아질 떄 까지 이 작업을 반복한다. 
    # loop가 완료되면 마지막으로 stack에서 뽑아낸 마지막 index (혹은 stack을 pop 한 적이 없다면 현재의 index) 와 현재 height를 stack에 push 한다.
    for i, h in enumerate(extended_heights):
        start_index = i
        while stack and stack[-1][1] > h:
            # The current bar `h` is the right boundary for the bar at the top of the stack.
            top_index, top_height = stack.pop()
            width = i - top_index
            max_area = max(max_area, top_height * width)
            start_index = top_index # The rectangle can extend to the left
        
        stack.append((start_index, h)) # 'start_index' 이후의 모든 ('i'보다 작은) 블록의 높이가 h 이상임을 보장한다는 뜻(h가 가장 낮음)
        
    return max_area

if __name__ == '__main__':
    while True:
        line = list(map(int, input().split()))
        # finishing condition
        if line[0] == 0:
            break
        
        heights = line[1:]
        max_area = find_max_area_stack(heights)
        print(max_area)