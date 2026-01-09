# https://www.acmicpc.net/problem/1013
# Contact

import sys

# (100+1+ | 01)+ 패턴 매칭 함수. state machine 사용
# state 정의, state 전이 정의, 종료 가능 state 정의 후 state machine 가동

def solve():
    """
    Solves the 'Contact' problem from acmicpc.net/problem/1013
    by implementing an iterative Deterministic Finite Automaton (DFA)
    to recognize the pattern: (100+1+ | 01)+
    """
    
    # DFA state transition table 
    # States are numbered 0 through 9.
    # 0: start, 9: error
    # Transitions[current_state][input_char] = next_state
    # input_char is 0 for '0', 1 for '1'
    transitions = [
        # State 0: idle 상태. 새로운 패턴을 시작할 수 있음. 1 또는 0을 받을 수 있음.
        {'0': 2, '1': 1},
        # State 1: 100+1+ 에서 1을 받고 00을 기다리는 상태 (현재 1)        
        {'0': 3, '1': 9},
        # State 2: 01 패턴에서 0을 받고 1을 기다리는 상태 (현재 0)
        {'0': 9, '1': 8},
        # State 3: 100+1+ 에서 두번째 0을 기다리는 상태 (현재 10)
        {'0': 4, '1': 9},
        # State 4: 100+1+ 에서 추가 0 혹은 첫번째 1을 기다리는 상태 (현재 100)
        {'0': 4, '1': 5},
        # State 5: 100+1+ 에서 추가 1을 기다리는 상태 (현재 1001). [종료 가능]
        {'0': 2, '1': 6},

        # 주의. 여기서부터 다음 n개의 데이터를 확인해야 어떤 패턴인지 결정되는 경우 발생.

        # State 6: 10011 형태. [종료 가능]
        # 1을 받는다면 1) 100+1+ 에서 1을 추가로 받는 경우. 2) 앞선 100+1 을 완료하고 새로운 100+1 패턴의 1이 시작되는 경우
        # 0을 받는다면 1) 새로운 100+1+ 패턴이 시작되는 경우거나 2) 앞선 100+1+ 패턴이 완료되고 새로운 01 패턴이 시작되는 경우
        {'0': 7, '1': 6},
        # State 7: 100110 형태. 
        # 1을 받는다면 앞선 0과 새로운 1이 합쳐져 "01" 패턴 확정
        # 0을 받는다면 새로운 100+1+ 패턴이 시작되는 경우 확정
        {'0': 4, '1': 8},
        # State 8: 01 패턴에서 01을 받은 상태 (현재 01) [종료 가능]
        # 1을 받는다면 새로운 100+1+ 패턴이 시작되는 경우 확정
        # 0을 받는다면 새로운 01 패턴이 시작되는 경우 확정
        {'0': 2, '1': 1},

        # State 9: 에러. 실패
        {'0': 9, '1': 9},
    ]
    
    # A state is accepting if a valid pattern can end there.
    # For (pattern)+, any state that represents the end of a complete sub-pattern is an accepting state.
    # State 5: "100+1" is a complete pattern.
    # State 6: "100+1+" is a complete pattern.
    # State 7: "01" is a complete pattern, or "100+1+" followed by "01".
    accepting_states = {5, 6, 8}

    input = sys.stdin.readline
    try:
        T = int(input())
    except (ValueError, IndexError):
        return
        
    for _ in range(T):
        signal = input().strip()
        current_state = 0
        
        # signal 의 각 문자에 대해 상태 전이 수행
        for idx, char in enumerate(signal):
            current_state = transitions[current_state][char]
            # print(f'[DEBUG] {idx}/{len(signal)} char:{char}, state:{current_state}')
            if current_state == len(transitions) - 1: # Early exit if error state is reached
                break

        # 마지막 state 가 종료 가능 state 인지 확인
        if current_state in accepting_states:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()