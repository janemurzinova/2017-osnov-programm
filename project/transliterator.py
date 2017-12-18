import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from xlrd import open_workbook

text = raw_input('Type text:')

#while not f == 1 or f == 2
print('Press \'1\' for transliterate from cyrillic (Karamshoev dictionary) to latin (Zarubin dictionary)')
print('Press \'2\' for transliterate from latin (Zarubin dictionary) to cyrillic (Karamshoev dictionary)')
f = input()

rb = open_workbook('orthography_table_shugnanskiy.xls')
sheet = rb.sheet_by_index(0)

cyr = ''
lat = ''

for colnum in range(sheet.ncols):
	col = sheet.col_values(colnum)
	for c_el in col:
		if colnum == 0:
			cyr = cyr + c_el
		elif colnum == 1:
			lat = lat + c_el

text_trans = text

if f == 1:
	mapping = zip(list(cyr),list(lat))
	for k, v in mapping:
		text_trans = text_trans.replace(k, v)
elif f == 2:
	mapping = zip(list(lat),list(cyr))
	for v, k in mapping:
		text_trans = text_trans.replace(v, k)

print(text_trans)







