import random

N = 100000
M = 100000
ROOT = 0  # tree의 root node
NAME_IN = '11438\in4.txt'
NAME_OUT = '11438\out4.txt'

# 입력 파일 생성
f = open(NAME_IN, 'w')
# 정답 파일 생성
# g = open(NAME_OUT)

f.write('{}\n'.format(N))
left = [i for i in range(1, N)]
random.shuffle(left)
parent = [0 for _ in range(N)]

Q = [ROOT]
while Q:
    current = Q.pop(0)
    count = random.randint(1, 3)  # 1~3개 child 랜덤으로 가짐
    # child들에 대해 parent 설정 및 queue에 child들 추가하여 동일작업 반복
    for i in range(count):
        if not left:
            # 더 이상 남은 항목이 없으면
            break
        next = left.pop()
        Q.append(next)
        parent[next] = current

for i in range(1, N):
    f.write('{} {}\n'.format(i+1, parent[i]+1))

f.write('{}\n'.format(M))
for _ in range(M):
    a = random.randint(1, N)
    b = random.randint(1, N)
    f.write('{} {}\n'.format(a, b))  # 입력파일 작성
    # 정답 작성?


f.close()
# g.close()


