import sys

print ('#P', 'count', 'tag', 'form', sep = '\t')

tagsfreq = {}
formfreq = {}
counter = 0
wt = {}

for line in sys.stdin.readlines():
	if line [0] == '#':
		continue
	if line [:2] == 'ID':
		continue
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	form = row[1]
	tag = row[3]
	if tag == '_':
		continue
	if form not in wt:
		wt[form] = {}
	if tag not in wt[form]:
		wt[form][tag] = 0
	wt[form][tag] = wt[form][tag] + 1

	if tag not in tagsfreq:
		tagsfreq[tag] = 0
	tagsfreq[tag] = tagsfreq[tag] + 1

	if form not in formfreq:
		formfreq[form] = 0
	formfreq[form] = formfreq[form] + 1
	
	counter = counter + 1

for tag in tagsfreq:
	print ('%.3f'%(tagsfreq[tag]/counter), tagsfreq[tag], tag, '_', sep = '\t')

for frm in wt:
	for tg in wt[frm]:
		print ('%.3f'% (wt[frm][tg]/formfreq[frm]), wt[frm][tg], tg, frm, sep = '\t') 

