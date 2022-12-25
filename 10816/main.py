# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

MAX_NUM = 10000000
MIN_NUM = -10000000
MAX_N = 500000
MAX_M = 500000

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cards.sort()  # 오름차순으로 정렬
card_count = {}  # 카드의 번호를 key, 개수를 value로 하는 map 생성
# 순회하며 같은 숫자인 경우 count를 올림
idx = 0
count = 0
prev_number = cards[idx]
while idx < N:
    # 이전 카드와 현재 카드를 비교한다.
    if prev_number == cards[idx]:
        count += 1
    else:
        card_count[prev_number] = count  # map에 기록
        # count 및 prev_number 초기화
        prev_number = cards[idx]
        count = 1
    idx += 1

card_count[prev_number] = count  # 마지막에 찾은 count도 map에 기록

# 작성된 card_count로 개수 확인
for t in targets:
    if t in card_count:
        print(card_count[t], end=' ')
    else:
        print('0', end=' ')
