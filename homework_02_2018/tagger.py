import sys

wt = {}
mostfreqtag = {}
mft_list = []

a = open (sys.argv[1])
model = a.readlines()
a.close()

for line in model:
	if '\t' not in line:
		continue
	if line [0] == '#':
		continue
	row = line.split('\t')
	if len(row) != 4:
		continue
	form = row[3]
	form = form.strip('\n')
	tag = row[2]
	tag = tag.strip('\n')
	n = row[1]
	p = row [0]
	p = float (p)

	if form != '_':
		tp_counter = 0
		if form not in wt:
			wt[form] = tag
			tp_counter = p
		else:
			if p >= tp_counter:
				wt [form] = tag
			else:
				continue
	else:
		if tag not in mostfreqtag:
			mostfreqtag[tag] = n

for t in mostfreqtag:
	mft_list.append ((int(mostfreqtag[t]), t))
mft_list.sort(reverse = True)
mft = mft_list[0][1]

doc = sys.stdin.readlines()

for line in doc:
	if '\t' in line:
		row = line.split('\t')
		if len(row) != 10:
			continue
		if '#' in row[0]:
			sys.stdout.write(line)
		else:
			if row[3] != '_':
				sys.stdout.write(line)
			else:
				n = row [0]
				w = row[1]
				t = row [3]
				translit = row [9]
				newt = '!'
				if w in wt:
					newt = wt[w]
				else:
					newt = mft
				tagged_line = n+'\t'+ w +'\t'+ '_'+'\t'+newt+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+'_'+'\t'+translit
				sys.stdout.write (tagged_line)	
	else:
		sys.stdout.write (line)
