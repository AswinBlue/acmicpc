f = open('17298\in4.txt','w')
N = 1000000
f.write('{}\n'.format(N))
a = [i for i in range(N)]
A = ' '.join(map(str, a))
f.write(A)
f.close()
