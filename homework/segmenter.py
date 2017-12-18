import sys

text = sys.stdin.read()

segment = text.replace('. ', '.\n')

print(segment) 
