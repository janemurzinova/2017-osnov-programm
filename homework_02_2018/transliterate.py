# -*- coding: utf-8 -*-

import sys

tr = {}

fd = open('translit_new.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	q = line.split('\t')
	tr[q[0]]=q[1]


text = sys.stdin.read()

sentence = text.split('\n')

for s in sentence:
	if '\t' in s:
		token = s.split('\t')
		if not token[0] == 'ID':
			form = token [1]
			translit = token [9]
			newtranslit = 'Translit='
			for smb in tr:
				if len(smb) > 1 and form.find(smb) >= 0:
					form = form.replace(smb, tr[smb])
			for orig_smb in form:
				if orig_smb in tr:
					new_smb = tr[orig_smb]
				else:	
					new_smb = orig_smb
				newtranslit = newtranslit + new_smb
			token [9] = newtranslit
			a=''
			for t in token:
				a = a + t + '\t'
			sys.stdout.write (a[:-1] +'\n')
		else:
			print(s)
	else:		
		print(s)

