FNAME = '2261\in10.txt'
N = 100_000

f = open(FNAME, 'w')
f.write(f'{N}\n')

X = -10_000
Y = -10_000
flag = 1
for n in range(N):
    f.write(f'{X} {Y}\n')
    X += flag
    Y += flag
    flag *= -1
    X *= -1
    Y *= -1

f.close