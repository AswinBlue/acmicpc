from sys import stdin, stdout, setrecursionlimit

MAX_N = 32000
MAX_M = 100000
setrecursionlimit(MAX_N)

# 결과 저장용 stack
result_stack = []
# 동작에 사용할 stack
stack = []
# 그래프를 표현
nodes = None
# 방문 vertex를 기록
visit = None

def iteration(i):
    stack.append(i)  # push

    while len(stack):
        # stack의 top value 가져옴
        current = stack[-1]
        visit[current] = True
        
        # print(current, stack, result_stack)

        cnt = 0  # 다음 node 있는지 체크하기 위한 변수
        # current에서 갈 수 있는 모든 vertex 체크
        for n in nodes[current]:
            if visit[n]:
                continue
            stack.append(n)
            cnt += 1
            break
            
        if cnt != 0:
            # 다음 갈 수 있는 길을 stack에 하나 담았으면 break
            continue
        else:
            # 다음으로 갈 수 있는 vertex가 더 없는경우, stack의 top value를 pop하여 result_stack에 집어넣음
            result_stack.append(stack.pop())  # stack.pop() == current

def recursive(i):
    visit[i] = True
    for n in nodes[i]:
        if visit[n]:
            continue
        recursive(n)
    result_stack.append(i)

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    nodes = [[] for _ in range(N+1)]  # root node 생성, 그래프를 list로 표현. nodes[i]는 i 에서 갈수있는 vertex를 의미
    visit = [False for i in range(N+1)]
    for m in range(M):
        a, b = map(int, stdin.readline().split())
        nodes[a].append(b)
    # print(nodes)

    # 모든 node에 대해 한번이상 수행
    for i in range(1, N+1):
        # 이미 방문했다면 skip
        if visit[i]:
            continue
        # topology sort 실행
        # iteration(i)  # iteration방법
        recursive(i)  # recursive방법
                
    # 결과 작성
    result_stack.reverse()
    result = ' '.join(map(str, result_stack))
    stdout.write(result + '\n')
