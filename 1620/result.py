import bisect
n,m = map(int,raw_input().split())
pokemon = [raw_input() for i in xrange(n)]
sort_pokemon = sorted(pokemon)
pokemon_num = sorted([[pokemon[i],str(i+1)] for i in xrange(len(pokemon))], key=lambda x:x[0])

answer = ''
for i in xrange(m):
    name_or_num = raw_input()
    if name_or_num.isdigit():
        answer += pokemon[int(name_or_num)-1]+'\n'
    else:
        answer += pokemon_num[bisect.bisect(sort_pokemon, name_or_num)-1][1]+'\n'
print answer[:-1]


