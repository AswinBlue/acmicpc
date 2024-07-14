# 큰 수 만들기
# https://www.acmicpc.net/problem/16496
from functools import cmp_to_key

DEBUG = 1

def Print(*args):
    if DEBUG:
        print(*args)


MAX_N = 1_000_000_000

# REFS: python 비교함수 구문 반환값
# return 음수 : 먼저 들어온 요소가 앞으로 정렬됨
# return 0 : 바뀌지 않음
# return 양수 : 나중에 들어온 요소가 앞으로 정렬됨(먼저들어온 요소보다 앞에 배치됨)
def compare(A, B):
    len_A = len(A)
    len_B = len(B)
    for i in range(min(len_A, len_B)):
        # 같은 자리에 더 큰숫자가 있다면 우위
        if A[i] > B[i]:
            Print(f"{A} > {B}")
            return -1
        elif A[i] < B[i]:
            Print(f"{A} < {B}")
            return 1
        # 현재 자리의 숫자가 같다면
        else:
            # 끝까지 확인한게 아니라면 다음 자릿수 추가 확인 필요
            # 한 숫자의 마지막 자릿수 까지 모두 확인 한 것이라면, 
            if i == len_A - 1:
                # A의 첫 자리와 B의 다음 자리를 비교한다. 
                # 이 조건에 해당된다는 것은 A[:i+1] 과 B[:i+1] 은 숫자가 모두 같은 경우이다.
                # A가 우위에 있으려면 AB 순서대로 합쳐서 수를 만들 때 숫자가 BA 순서로 합친 결과보다 더 커야한다.
                # 첫자리가 A[0]보다 큰 숫자들은 이미 앞에서 다 걸러졌고(A[i] > B[i] 조건으로 걸러짐)
                # AB 가 BA보다 크려면 A[0]이 B[i+1:]의 모든 수 보다 작아야 한다. <-- [조건1]
                # 예를 들면 A=3 B=334 라 하자
                # i=0일 때 A[0] (3) == B[i+1] (3), A[0] (3) < B[i+1] (4)이 된다.
                # 때문에 [조건1] 을 성립하지 못하게 되고, A보다 B가 우위에 있게 된다. 
                # 실제로 AB = 3 334, BA = 334 3 으로 BA > AB 이다. 

                # ERROR: 100, 10010011 의 경우 B가 먼저 나오는게 맞다. 하지만 이런 경우까지 모두 비교하려면 A[0]뿐 아니라 A의 모든 자릿수에대한 연산이 필요
                for j in range(i + 1, len_B):
                    if B[j] > A[0]:
                        Print(f"{i}, {A} < {B}")
                        return 1
                    elif B[j] < A[0]:
                        Print(f"{i}, {A} > {B}")
                        return -1
                # B[i+1:] 의 모든 수가 A[0] 보다 같거나 작기 때문에 A가 우위
                Print(f"{i}, {A} > {B}")
                return 0
            elif i == len_B - 1:
                Print(i, A,B)
                for j in range(i + 1, len_A):
                    if A[j] > B[0]:
                        Print(f"{i}, {A} > {B}")
                        return -1
                # A[i+1:] 의 모든 수가 B[0] 보다 같거나 작기 때문에 B가 우위
                Print(f"{i}, {A} < {B}")
                return 1
    # 완전히 동일
    return 0
            
N = int(input())

numbers = list(input().split())
numbers = sorted(numbers, key=cmp_to_key(compare))
Print(numbers)

res = ''.join(numbers)
print(int(res))
# for n in numbers:
