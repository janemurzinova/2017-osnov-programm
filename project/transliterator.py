# -*- coding: utf-8 -*-
import sys
from xlrd import open_workbook

text = str(input('Type text:'))

print('Press \'1\' for transliterate from cyrillic (Karamshoev dictionary) to latin (Zarubin dictionary)')
print('Press \'2\' for transliterate from latin (Zarubin dictionary) to cyrillic (Karamshoev dictionary)')
f = int(input())

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
        trans = str.maketrans(cyr,lat)
        text_trans = text.translate(trans)
elif f == 2:
        trans = str.maketrans(lat,cyr)
        text_trans = text.translate(trans)

print(text_trans)







