# https://www.acmicpc.net/problem/2629
# 양팔저울
MAX_PEN_NUM = 30
MAX_PEN_WEIGHT = 500
MAX_BEAD_WEIGHT = 40000

N = int(input())  # 추
pendulum = list(map(int, input().split()))
M = int(input())  # 구슬
beads = list(map(int, input().split()))
max_weight = max(beads)

# 양팔 저울은 좌측, 우측 부분이 있다. 구슬(측정 대상)을 좌측에 놓는다고 했을 때, 측정을 위해 올려야 할 추의 무게는 저울 우측의 무게이다.
# 따라서 저울 오른쪽을 기준으로 봤을 때, 추를 좌측에 놓으면 -, 우측에 놓으면 + 가 된다.

# possible[i] 는 추를 1번부터 i+1번(코드에서는 0~N-1 index사용)까지 썼을 때 저울 오른쪽의 무게가 될 수 있는 수들의 집합이다. (중복 제거를 위해)
possible = [set() for _ in range(N)]
# 추를 하나 썼을 때
possible[0].add(0)  # 사용 안했을 때
possible[0].add(pendulum[0])  # 우측에 사용했을 때
possible[0].add(-pendulum[0]) # 좌측에 사용했을 때

# 추를 두개 이상 썼을 때
for i in range(1, N):
    # i-1개의 추를 쓴 결과에 i번째 추를 추가로 썼을 때 결과 갱신
    for p in possible[i-1]:
        possible[i].add(p)  # 사용 안했을 때
        possible[i].add(p + pendulum[i])  # 우측에 사용했을 때
        possible[i].add(p - pendulum[i])  # 좌측에 사용했을 때
# print(possible)
# 모든 구슬들에 대해 구슬 무게만큼 차이가 나게 추를 배분할 수 있는지 확인
result = ''
for b in beads:
    if b in possible[N-1]:
        result += 'Y '
    else:
        result += 'N '
print(result)