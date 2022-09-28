FNAME = '11378\in7.txt'
N = 10
M = 10
K = 0

f = open(FNAME, 'w')
f.write('{} {} {}\n'.format(N, M, K))

# case 1
for i in range(1, N+1):
    f.write('{} '.format(i))
    for j in range(1, i+1):
        f.write('{} '.format(j))
    f.write('\n')

# # case 2
# for i in range(1, N+1):
#     f.write('1 {}\n'.format(i))

