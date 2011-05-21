#!/usr/bin/env python
# -*- coding: utf-8 -*-

IN_FILE = 'A-large.in'
OUT_FILE = '%s_result.txt' % IN_FILE

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

def test_d(n, pd):
	if 100 <= n:
		return True
	result = []
	for i in range(1, n+1):
		for j in range(0, i+1):
			win = j
			if 0 == win * 100 % i and pd == win * 100.0 / i:
				print "found %d%% [%d/%d] < %d" % (pd, win, i, n)
				return True


print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	#n, pd, pg = *s
	n = int(s[0])
	pd = int(s[1])
	pg = int(s[2])
	if test_d(n, pd):
		if pd == pg or (pg != 0 and pg != 100) :
			result += 'Case #%d: Possible\n' % (case_count + 1)
			print '%s Possible' % s
			continue
	result += 'Case #%d: Broken\n' % (case_count + 1)
	print '%s Broken' % s


print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()


