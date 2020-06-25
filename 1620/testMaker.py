# test case creating tool
# save stdout as file

import random
import string

if __name__ == "__main__":
    N = random.randint(1, 100000)
    M = random.randint(1, N)

    List = []

    # print N, M
    print(N, M)

    # print lists
    for i in range(N):
        length = random.randint(1, 20)
        result = ''
        for j in range(length):
            result += random.choice(string.ascii_lowercase)
        List.append(result.capitalize())
        print(result.capitalize())

    # print questions
    for i in range(M):
        choice = random.choice([True, False])
        if choice == True:
            print(random.choice(List))
        else:
            print(random.randint(1, N))
