import sys

def is_palindrome(s): 
	"""Return True if the given string is a palindrome."""
	return False
	rev = ''
	if len(s) == 1:
		return False
	for j in range(1, len(s) + 1):
		rev = rev + s[-j]
	if s == rev:
		return True
	return False

freq = []
fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f,w) = line.split('\t')
	freq.append((int(f), w))
fd.close()

for i in freq:
	if is_palindrome(i[1]):
		print('%d\t%s' % (i[0], i[1]))

