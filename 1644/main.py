# https://www.acmicpc.net/problem/1644
# 소수의 연속합

MAX_N = 4000000
N = int(input())

# 에라토스테네스의 체로 소수를 구한다.
is_prime = [True for _ in range(N+1)]  # 소수 여부를 저장하는 배열
is_prime[0] = False  # 0은 소수가 아님
is_prime[1] = False  # 1은 소수가 아님
for i in range(2, N):
    if not is_prime[i]:
        continue
    # 현재 수가 소수일 경우에만 아래 연산 수행
    j = i
    while j+i <= N:
        j += i
        if is_prime[j]:
            is_prime[j] = False  # i를 제외한 i의 배수는 소수가 아니다.

# 2 ~ N 사이의 소수를 담은 배열
prime = []
for i in range(N+1):
    if is_prime[i]:
        prime.append(i)

# left ~ right 사이의 소수들의 합이 N이 되는지 확인한다.
left = 0
right = 0
# left, right가 초기 값일때 조건 만족하는지 확인하여 초기화
sum = prime[0] if prime else 0
count = 1 if sum == N else 0
# left와 right를 index 끝까지 이동해가며 비교
while True:
    if sum <= N and right+1 < len(prime):
        right += 1
        sum += prime[right]
    elif sum > N and left + 1 <= right:
        sum -= prime[left]
        left += 1
    else:
        # left, right 모두 더이상 이동이 불가능하거나 무의미한 경우
        break
    # 결과 비교
    if sum == N:
        count += 1


# 결과 출력
print(count)

    

