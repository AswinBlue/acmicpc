# https://www.acmicpc.net/problem/9935
# 문자열 폭발

NOT_FOUND = 'FRULA'
MAX_LEN = 1000000
MAX_TARGET_LEN = 36

text = input()
target = input()
length = len(target)

S = [None for _ in range(len(text))]  # stack
top = 0
ptr = 0
for t in text:
    S[top] = t  # 일단 스택에 추가
    top += 1
    # 마지막에 추가한 문자가 목표 문자열의 마지막과 같다면
    if S[top-1] == target[-1]:
        # 스택의 top에서부터 length만큼의 문자가 목표 문자열과 일치하는지 확인
        for i in range(length):
            if target[i] == S[top - length + i]:
                # 목표 문자열이 stack에 존재할 때
                if i == length-1:
                    # 문자열만큼 stack에서 pop
                    top -= length
            # 문자열이 다르다면 skip
            else:
                break

# 남은 문자열이 없는 경우
if top == 0:
    print(NOT_FOUND)
else:
    print(''.join(S[:top]))
