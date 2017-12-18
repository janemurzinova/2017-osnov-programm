# -*- coding: utf-8 -*-

import sys

tr = {}

fd = open('transcription.csv', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	q = line.split(',')
	tr[q[0]]=q[1]



text = sys.stdin.read()

sentence = text.split('\n')

for k, v in tr.items():
	trans_text = text.replace(k,v)

print(trans_text)

