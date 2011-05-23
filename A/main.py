#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'A-large'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

class Field:
	def __init__(self, r,c):
		self.r = int(r )
		self.c = int(c )
		self.m = []
		self.blue_count = 0
	def set_line(self, line):
		self.m.append(line)
		self.blue_count += line.count('#')
	def replace(self):
		for i in range(self.r):
			for j in range(self.c):
				if self.m[i][j] == '#':
					if self.m[i][j+1] == '#' and self.m[i+1][j] == '#' and self.m[i+1][j+1] == '#':
						self.set_str(i, j, '/')
						self.set_str(i+1, j, '\\')
						self.set_str(i, j+1, '\\')
						self.set_str(i+1, j+1, '/')
						self.blue_count -= 4
					else:
						return False
		return 0
	def set_str(self, y, x, s):
		self.m[y] = self.m[y][0:x] + s + self.m[y][x+1:]
	def __str__(self):
		return '\n'.join(self.m)
	

case_num = int(src.pop(0))
case_count = 0
result = ''

print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	f = Field(s[0], s[1])
	print 'case %d %d' % (f.r, f.c)
	for i in range(f.r):
		f.set_line(src.pop(0).strip())
	print f
	if f.blue_count % 4 != 0:
		print '%d %% 4 != 0' % f.blue_count
		result += 'Case #%d:\nImpossible\n' % (case_count + 1)
	else:
		f.replace()
		print 'replace end'
		print f
		if f.blue_count == 0:
			print 'replace complete'
			result += 'Case #%d:\n%s\n' % (case_count + 1, f)
		else:
			print 'blue remain'
			result += 'Case #%d:\nImpossible\n' % (case_count + 1)
		
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()