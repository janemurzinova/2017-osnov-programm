import sys

text = sys.stdin.read()

sentence = text.split('\n')
#print(sentence)

sentence.pop()
#print(sentence)

t_list = []

s_count = 1
for s in sentence:
	if len(s) > 0:
		t_list.append('# sent_id = ' + str(s_count) + '\n')
		t_list.append('# text = ' + s + '\n')
		t_list.append('ID'+'\t'+'FORM'+'\t'+'LEMMA'+'\t'+'UPOSTAG'+'\t'+'XPOSTAG'+'\t'+'FEATS'+'\t'+'HEAD'+'\t'+'DEPREL'+'\t'+'DEPS'+'\t'+'MISC' + '\n')
		s = s.replace('.',' .')
		s = s.replace(',',' ,')
		s = s.replace(':',' :')
		s = s.replace(';',' ;')
		s = s.replace('!',' !')
		s = s.replace('?',' ?')
		s = s.replace(')',' )')
		s = s.replace('(','( ')
		s = s.replace('[','[ ')
		s = s.replace(']',' ]')
		s = s.replace('{','{ ')
		s = s.replace('}',' }')
		s = s.replace('\"',' \" ')
		s = s.replace('\'',' \' ')

		token = s.split(' ')
		t_count = 1
		for t in token:
			if not t == '':
				t_list.append(str(t_count) +'\t' + t +'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_' + '\n')
				t_count = t_count + 1
		s_count = s_count + 1
		t_list.append('\n')	

for q in t_list:
	sys.stdout.write(q)

