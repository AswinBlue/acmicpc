#httpswww.acmicpc.netproblem15998
import math
import sys

DEBUG = 1

def gcd(x,y):
    while y > 0:
        x, y = y, x % y

    return x

if __name__ == '__main__':
    N = int(input())
    
    balance = 0  # balance in the account
    M = 0
    M_left = -1  # 'left' value of M

    # rule 1. find GCD of M and 'charged', check it meets the condition
    # rule 2. new M must be smaller than any 'left' when charged
    # rule 3. M can be 1 if 'left' is 0
    for i in range(N):
        spent, left = map(int, sys.stdin.readline().split()) # python fast input

        if DEBUG:
            print("in:", spent, left, balance)
        
        charged = left - spent - balance
        if DEBUG:
            print("charged:", charged, M)
        # 1. check if need to charge
        if balance + spent < 0:  # get budget from other account

            # 2. check how much have to charge
            # 2-1. find the greatest common denominator, get unit of charge
            new_M_candidate = math.gcd(charged, M)

            # 2-2. check if overcharged
            M_left = max(M_left, left)
            if M_left < new_M_candidate:
                M = new_M_candidate  
            else:
                M = -1
                break          

            if DEBUG:
                print("M:", new_M_candidate, M, M_left)

            if M == 1 and M_left != 0:
                M = -1
                break
                
        else:
            # 3. valudate the inputs
            if balance + spent != left:
                M = -1
                break

        balance = left  # update the current balance

    # print result
    if M == 0:
        print(1)
    else:
        print(M)