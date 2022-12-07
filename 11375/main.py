# https://www.acmicpc.net/problem/11375
# 열혈강호

# 모든 경우의 수를 다 고려 해 보아야 한다.
# 순회 방법으로 이분 매칭 알고리즘을 사용 가능하다.
# 이분 매칭 알고리즘은 max flow 알고리즘의 특수 케이스이다. 
# 조건1) 모든 간선들이 A 그룹에서 B 그룹으로 향하는 단방향
# 조건2) A 그룹에서 B 그룹으로 가는 flow들의 capacity가 모두 1
# 조건3) 모든 B 그룹의 node들은 단 하나의 간선만 수용 가능
# 조건4) 모든 A그룹의  node들은 단 하나의 간선만 활성화 가능

from sys import setrecursionlimit
setrecursionlimit(10000)

DEBUG = 0
def Print(*argv):
    if DEBUG:
        print(*argv)

# 이분 매칭 알고리즘 핵심 로직
def find_proper_work(worker, check):
    global N, M, ability, assigned, assigned_to
    check[worker] = True  # 방문 처리

    result = False  # 일 할당 가능한지 여부

    # 직원이 처리 가능한 모든 일들을 순회하며 확인
    for work in ability[worker]:
        Print(worker, work)
        # 일에 배정된 직원이 없을 경우
        assigned_worker_for_current_work = assigned_to[work]
        if assigned_worker_for_current_work is None:
            assigned_to[work] = worker  # 일에 직원을 배정
            assigned[worker] = True  # 직원이 일을 배정받았다고 체크
            result = True  # 처리 성공
            Print('assigned to empty work')
            break
        # 배정된 직원이 있는 경우
        else:
            # 기존에 해당된 직원이 다른 일을 하도록 이동시켜본다.
            # 단, 무한 순회를 피하기 위해 이미 한번 고려된 (check) 직원은 반복해서 시도하지 않는다.
            # worker를 check 하든, work를 check하든 상관없다.
            if not check[assigned_worker_for_current_work] \
                and find_proper_work(assigned_worker_for_current_work, check) == True:
                # 이동이 가능하면 이동된 결과로 내용 설정
                assigned_to[work] = worker
                assigned[worker] = True
                result = True  # 처리 성공
                Print('changed previous schedule')
                break
            else:
                Print('continued')
                continue  # 다른 work를 할당 가능한지 확인

    return result


if __name__ == '__main__':
    MAX_N = 1000
    MAX_M = 1000

    N, M = map(int, input().split())  # 직원의 수, 일의 수
    ability = [None for _ in range(N + 1)]  # 각 직원이 처리할 수 있는 일 list
    assigned_to = [None for _ in range(M + 1)]  # 일에 배정된 직원

    # 입력값 저장
    for idx in range(1, N + 1):
        works = list(map(int, input().split()))[1:]
        ability[idx] = works
    Print(ability)

    # 순회하며 정답 찾기
    assigned = [False for _ in range(N + 1)]  # worker에 일이 배정되었는지 체크
    total_assigned_works = 0  # 할당된 일의 총 갯수
    for i in range(1, N+1):
        Print(assigned_to, assigned)
        # 이미 처리한 직원은 생략
        if assigned[i]:
            continue

        check = [False for _ in range(N + 1)]  # 이번 순회 때 worekr가 사용되었는지 확인

        # 직원이 처리 가능한 일들을 둘러보며 어떤 일을 배정할지 확인
        if find_proper_work(i, check) == True:
            total_assigned_works += 1

    print(total_assigned_works)

