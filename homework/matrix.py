import sys

rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for w1 in rus: 
	if w1 not in m: 
		m[w1] = {}
	for w2 in eng:
		m[w1][w2] = 0

print(m)
