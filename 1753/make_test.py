V = 20000
E = 300000
START = V

f = open('1753\in5.txt', 'w')
f.write('{} {}\n{}\n'.format(V, E, START))
begin = 1
target = 2
for i in range(1, E+1):
    f.write('{} {} 1\n'.format(begin, target))
    if target+1 <= V :
        target += 1
    else:
        if begin+1 <= V:
            begin += 1
        else:
            begin = 1

        target = begin + 1


# f.write('1 2 1\n')
# f.write('2 3 1\n')
# f.write('3 4 1\n')
# f.write('4 5 1\n')
# f.write('5 6 1\n')

f.close()