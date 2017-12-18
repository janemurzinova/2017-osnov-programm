import sys

text = sys.stdin.read()

sentence = text.split('\n')

t_list = []

s_count = 1
for s in sentence:
	t_list.append(['sent_id = ' + str(s_count)])
	t_list.append(['text = ' + s])
	s = s.replace('.',' .')
	s = s.replace(',',' ,')
	s = s.replace(':',' :')
	s = s.replace(';',' ;')
	s = s.replace('!',' !')
	s = s.replace('?',' ?')

	token = s.split(' ')
	t_count = 1
	for t in token:
		t_list.append([t_count, '\t', t, '\t_', '\t_', '\t_', '\t_', '\t_', '\t_', '\t_', '\t_'])
		t_count = t_count + 1
	s_count = s_count + 1
	t_list.append(['\n'])	


for q in t_list:
	print(*q)

