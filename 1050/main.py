# https://www.acmicpc.net/problem/1050
# 물약

import re

DEBUG = 0
def Print(*args):
    if DEBUG:
        print(*args)

MAX_PRICE = 100
MAX_LENGTH = 50
MAX_N = 50
MAX_M = 50
MAX_PRICE = 1_000_000_000
ABOVE_MAX_PRICE = 1_000_000_001
INVALID = -1

def compare(A, B):
    if A == INVALID:
        return B
    elif B == INVALID:
        return A
    else:
        return min(A,B)


N, M = map(int, input().split())
price_list = {'LOVE' : INVALID}  # 가격 저장
recipe = []  # 제작법 저장. 겹치는 제작법이 있을 수 있어서 map 보다 list 사용
idx = -1  # recipe index

for n in range(N):
    name, price = input().split()
    price = int(price)
    price_list[name] = price

for m in range(M):
    total_price = 0
    production = input().replace('+',' ').replace('=',' ').split()
    idx += 1
    recipe.append((production[0], []))
    for item in production[1:]:
        num, name = re.findall(r'[a-zA-Z]+|\d+', item)  # REF : 문자와 숫자 분리하는법, 정규식 사용
        recipe[idx][1].append((num, name))  # 제작법 저장
        if name not in price_list:
            price_list[name] = INVALID # 재료 획득방법 없음
            total_price = INVALID  # 아직 못만듬
            continue  # recipe 완성해야해서 일단 끝까지 다 돌아야함

        if price_list[name] == INVALID:  # 재료를 못구하는 경우
            total_price = INVALID  # 아직 못만듬

        if total_price != INVALID and price_list[name] != INVALID:  # 제조 가능한 경우만 합산
            total_price += int(num) * price_list[name]

    if production[0] in price_list:    
        price_list[production[0]] = compare(total_price, price_list[production[0]])
    else:
        price_list[production[0]] = INVALID

    if price_list[production[0]] > MAX_PRICE:
        price_list[production[0]] = ABOVE_MAX_PRICE

# 전체 재료들이 한 번 이상 등장하였다. 이후로 새로운 재료가 등장하지는 않음이 보장된다.
# 전체 재료 갯수만큼 재료 구하기를 반복한다.
# MAX_N, MAX_M 제한이 50이라서 가능하다. :: (MAX_N * MAX_N * MAX_LENGTH) < (시간제한)
total_num = len(price_list)
Print(price_list) # debugging
Print(recipe) # debugging
for n in range(total_num):
    for k, v in recipe:  # REFS: dictionary 형태 자료형 순회
        # 반복 순회하며 값 갱신
        total_price = 0
        for num, name in v:
            # 조합법 대로 제조
            if price_list[name] == INVALID:  # 재료를 못구하는 경우
                total_price = INVALID  # 아직 못만듬
                break

            total_price += int(num) * price_list[name]

        # 제조후 가격 갱신
        price_list[k] = compare(total_price, price_list[k])
        if price_list[k] > MAX_PRICE:
            price_list[k] = ABOVE_MAX_PRICE

Print(price_list) # debugging
Print(recipe) # debugging

if price_list['LOVE'] == INVALID:
    price_list['LOVE'] = -1  # 문제에서 요구하는 값으로 변환
print(price_list['LOVE'])

