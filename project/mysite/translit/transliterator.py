# -*- coding: utf-8 -*-
import sys

text = str(input('Type text:'))

print('Press \'1\' for transliterate from cyrillic (Karamshoev dictionary) to latin (Zarubin dictionary)')
print('Press \'2\' for transliterate from latin (Zarubin dictionary) to cyrillic (Karamshoev dictionary)')
f = int(input())

tr = {}

fd = open('orthography_table_shugnanskiy.txt', 'r', encoding="utf8")
for line in fd.readlines():
	line = line.strip('\n')
	q = line.split('\t')
	if f == 1:
		tr[q[0]]=q[1]
	elif f == 2:
		tr[q[1]]=q[0]

text_trans = ''

sentence = text.split('\n')

for s in sentence:
	newtranslit = ''
	for orig_smb in s:
		if orig_smb in tr:
			new_smb = tr[orig_smb]
		else:	
			new_smb = orig_smb
		newtranslit = newtranslit + new_smb
	text_trans = text_trans + newtranslit + '\n'

		
sys.stdout.write(text_trans)







