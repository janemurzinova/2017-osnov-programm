import sys

lines = 0
tokens = 0
characters = 0 
vowels = 0

v = 'aáæeiíoóøuúyý'

for c in sys.stdin.read():
	if c == ' ': 
		tokens = tokens + 1
	if c == '\n': 
		lines = lines + 1
	characters = characters + 1 
	if c in v: 
		vowels = vowels + 1

print(lines,tokens,characters,vowels)
	
