import sys

text = sys.stdin.read()

segment = text.replace('. ', '.\n')

sys.stdout.write(segment) 	
