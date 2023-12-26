# https://www.acmicpc.net/problem/1086
# 박성원

# [배경지식]
# 나눗셈 연산의 분배법칙을 알아야 문제를 풀 수 있다. 
# 나눈셈 연산은 덧셈, 곱셈, 뺄심에 대해 분배법칙을 적용 할 수 있으며, 각각 아래와 같이 식을 변환할 수 있다. 
# (A + B) % p = ((A % p) + (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p
# (A * B) % p = ((A % p) * (B % p)) % p

# 나눗셈은 굳이 변환하자면 아래와 같다. 
# (A / B) % p = (A * B^(p - 2)) % p = ((A % p) * (B^(p - 2) % p)) % p

# [접근방법]
# 모든 경우의 수를 확인하는 것은 MAX_N! 만큼 시간이 소요되어 불가능하다. 
# 특정 경우간의 상관관계가 있는지 확인하고, 메모이제이션으로 계산 횟수를 줄일 수 있는지 확인하자.
# 1. 목표 확인
# 주어진 N개의 수를 집합 S라 할 때, 우리는 S에서 수를 조합해 만들 수 있는 수 중 K로 나누었을 때 나머지가 0인 수의 갯수를 구해야 한다. 
#
# 2. 연산 최적화
# 집합 S = {1,2,3} 라 하자. S의 원소를 조합해 만들 수 있는 수 중 K로 나누어 떨어지는 수는 몇가지 일까?
# 일단 S로 만들 수 있는 수를 모두 나열해 보면 123, 132, 213, 231, 312, 321 총 6가지이다.
# -> 조합의 갯수는 N!/(숫자1의갯수 * 숫자2의갯수 *숫자3의갯수) 이다.
#    N이 커지면 exhaustive search 접근방식으로는 무조건 시간초과가 발생한다.
#
# 각 수들은 자리수만 달라졌을 뿐 1,2,3으로 구성된 수이므로 각 수들을 k로 나눈 값을 구하되, 자릿수별로 분해하여 본다.
# 숫자 하나를 예를들어 보면
# 123 % k = (100 + 20 + 3) % k
#         = (100%k + 20%k + 3%k)%k
#         = ( ((1 % k) * (100 % k))%k + ((2 % k) * (10 % k))%k + 3%k)%k
# 결국 각 자릿수를 k로 나머지 연산한 값과 10^i 를 k로 나머지 연산한 값들의 합과 곱으로 이루어진다.
# 즉, 우리는 10^i를 k로 나머지 연산한 값과, S의 인자들을 k로 나머지 연산한 값을 알면 된다. 
# -> 앞으로 10^i % k 를 저장한 배열을 L[i] 라 하자. 즉, L[i] = 10^i % k 이다.
#    배열 L에 대해서도 점화식이 성립하여 L[i + 1] = (L[i] * 10 % k) % k 이다. 

# 3. 상관관계 찾기
# 123을 K로 나눈 값은 (12%k * 10%k) + 3%k이다. 
# 그럼 12를 k로 나눈 값은 (1%k * 10%k) + 2%k 이다.
# 즉, S = {A,B,C} 일 때,
#   ABC % K = (AB % K * 10^C_length % K) %K + C % K
#           = (AB * 10^C_length) %K + C % K 
# 가 된다.(C_length는 C의 길이)
# -> P[x]= x를 k로 나눈 나머지라 한다면 P[ABC] = P[AB] * 10^C_length % K+ C % K 이다.
# -> 결국 P[ABC] 를 구하려면 P[AB], L[C_length], P[C] 를 알고 있으면 된다는 뜻이다.
# 
# 1단계 목표확인을 되짚어 보면, 우리가 구해야 하는 값은 '수를 조합하여 순열을 만들었을 때 K로 나누었을 때 나머지가 0인 수의 갯수' 를 구해야 한다. 
# 그렇다면 메모이제이션의 결과값이 '갯수' 가 되는것이 좋겠다.
# 또한, '수를 조합하여' 하나의 수를 만들기 때문에, 사용된 수를 bit로 표현하는것이 좋겠다.
# 그러면 `DP[수의 조합] = 조합으로 만든 수를 K로 나누었을 때 나머지가 0인 수의 갯수` 가 되는 것이 이상적이다.
# 하지만 '수의 조합' 만으로 수를 특정할 수는 없다. (ABC가 될수도, CBA가 될 수도 있기 때문) DP 배열의 상관관계를 통해 점화식을 사용하려면 '실제 수'를 알아야 한다.
# '실제 수'를 추가하여 DP[수의 조합][실제 수] = 조합으로 만든 수를 K로 나누었을 때 나머지가 0인 수의 갯수
#    라고 할 수 있다. 하지만 우리는 (2) 연산최적화 단계에서 수를 K로 나눈 값만 있어도 문제를 풀 수 있다는 것을 확인하였기에,
#    여기서 '실제 수' 대신 '수를 k로 나눈 나머지' 를 사용할 수 있다.
# -> 즉, DP[수의 조합][실제수를 K로나눈 나머지] = 조합으로 만든 수를 K로 나누었을 때 나머지가 0인 수의 갯수
#     형태로 만든다면, 2차원 배열 DP를 통해 메모이제이션을 할 수 있다. 
# -> 또한 모든 '순열'에 대해 계산을 하지 않고, 모든 '조합' * K (나머지가 0 ~ K-1 이 나오는 경우) 번만 연산을 하면 된다. 

# 4. 반복문 구성
# DP[0011][a]를 구하기 위해서는 DP[0001][b], DP[0010][c] 가 필요하다.
# DP[0111][a]를 구하기 위해서는 (DP[0011][b], DP[0010][c]) 혹은 (DP[0110][d], DP[0001][e]) 또는 (DP[0101][f], DP[0010][g]) 가 필요하다.
# 즉, 선택한 수의 갯수가 적은 경우부터 먼저 구해지도록 반복문을 구성하면 된다.
# 반대로 DP[0001][a]를 알 때, 우리는 DP[0011][b], DP[0101][c] 를 계산할 수 있다.
# 즉, 알고있는 수 뒤에 다른 수 하나를 더붙인 경우를 계산할 수 있다. 
# 정리하면 아래 pseudo code가 나온다.
# ```
# for i in range 1<<N
#   for j in range N
#       if i & (1 << j) == 0
#           for l in K:  # [핵심] 모든 K에 대해 수행 (O(순열) 연산량 대신 O(조합)*k 횟수로 해결 가능)
#              find_DP()  # 현재 상태 'i' 뒤에 'j'번째 숫자를 추가로 더 붙이는 경우를 계산

    
import math

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

MAX_N = 15
MAX_K = 100
MAX_LENGTH = 50

# string 형태의 수를 받아 (K로 나눈 나머지, 원래길이) pair 로 치환하는 함수
def string_to_number_mod(number, index, K):
    long_number = number[index]
    s = len(long_number)
    number_after_mod = int(long_number[0]) % K
    for i in range(1, s):
        number_after_mod = (number_after_mod * 10 + int(long_number[i])) % K
        
    number[index] = (number_after_mod, s)

if __name__ == '__main__':
    N = int(input())
    number = [0 for _ in range(N)]
    for i in range(N):
        tmp = input()
        number[i] = [c for c in tmp] # string to char array
    K = int(input())

    # 입력받은 수들은 길기 때문에, string 형태로 받고 K로 나눈 나머지를 배열에 저장하도록 한다.
    for i in range(N):
        string_to_number_mod(number, i, K)

    # L 배열을 구한다. L[i] = (10^i) % K
    L = [0 for _ in range(MAX_LENGTH + 1)]
    L[0] = 1 % K
    for i in range(1, MAX_LENGTH + 1):
        L[i] = (L[i-1] * 10) % K
    Print(f'L:{L}')

    # DP 배열을 구한다.
    DP = [[0 for _ in range(K)] for _ in range(1 << N)] # (2^MAX_N) by K 배열
    DP[0][0] = 1  # 초기화

    for current in range(1 << N):
        for i in range(N):
            if current & (1 << i) == 0:
                next = current | (1 << i)
                # [핵심] 나머지만 구하면 된다는 사실을 사용하여 순열 연산을 조합 연산으로 변경
                for j in range(K):
                    moded_number, length = number[i]
                    k_next = (j * L[length] + moded_number) % K  # 현재 나머지가 j였으므로, 뒤에 moded_number 가 붙은 수에 K를 나눈 나머지를 구한다. 
                    DP[next][k_next] += DP[current][j]
                Print(f'{current} {next} {i}')
    Print(f'{DP}')

    A = DP[(1 << N) - 1][0]
    B = math.factorial(N)
    gcd = math.gcd(A,B)
    print(f'{A // gcd}/{B // gcd}')