#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'B-small-attempt1'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

def sean(d_list, l_list, index):
	points = 0
	word = d_list[index]
	w_len = len(word)
	choices = filter(lambda w: len(w) == w_len, d_list)
	print '### Question %s in %s' % (word, choices)
	for l in l_list:
		if len(choices) == 1:
			break
		s = set(''.join(choices))
		if l in s:
			print 'Sean try %s' % l
			if l in word:
				print 'Sean wins'
				# Sean wins
				for i in range(w_len):
					if word[i] == l:
						choices = filter(lambda w: w[i] == word[i], choices)
						print 'Choices change %s' % choices
			else:
				print 'Sean loses'
				points += 1
		
	print '### Point %s %s' % (word, points)
	return points
	
	
	
	



case_num = int(src.pop(0))
case_count = 0
result = ''

print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	d_num = int(s[0])
	l_num = int(s[1])
	d_list = []
	l_list = []
	for i in range(d_num):
		d_list.append(src.pop(0).strip())
	for i in range(l_num):
		l_list.append(src.pop(0).strip())
	
	
	result += 'Case #%d:' % (case_count + 1)
	for i in range(l_num):
		max = -1
		ans = ''
		for j in range(d_num):
			p = sean(d_list, l_list[i], j)
			if p > max:
				print '### new answer %s' % d_list[j]
				ans = d_list[j]
				max = p
		result += ' ' + ans
	result += '\n'
	
	print d_list
	print l_list
	#result += 'Case #%d: Possible\n' % (case_count + 1)
	

print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


