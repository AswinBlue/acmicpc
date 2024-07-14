# 큰 수 만들기
# https://www.acmicpc.net/problem/16496
from functools import cmp_to_key

DEBUG = 0

def Print(*args):
    if DEBUG:
        print(*args)


MAX_N = 1_000_000_000

# REFS: python 비교함수 구문 반환값
# return 음수 : 먼저 들어온 요소가 앞으로 정렬됨
# return 0 : 바뀌지 않음
# return 양수 : 나중에 들어온 요소가 앞으로 정렬됨(먼저들어온 요소보다 앞에 배치됨)
def compare(A, B):
    # AB로 합친 숫자와 BA로 합친 숫자의 크기를 비교한다.
    # 두 숫자끼리 비교하며 전체 항목을 모두 순회할 때, 전체 항목에 대해 순서 정렬이 보장된다. 즉 greedy 전략이 통한다.
    AB = int(''.join([A, B]))
    BA = int(''.join([B, A]))
    if AB > BA:
        return -1
    elif AB < BA:
        return 1
    else:
        # 완전히 동일
        return 0
            
N = int(input())

numbers = list(input().split())
numbers = sorted(numbers, key=cmp_to_key(compare))
Print(numbers)

res = ''.join(numbers)
print(int(res))
# for n in numbers:
