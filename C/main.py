#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'C-small-attempt2'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	n = int(s[0])
	low = int(s[1])
	high = int(s[2])
	s = src.pop(0).strip().split(' ')
	freqs = [int(freq) for freq in s]
	
	print 'case %d-%d %s' % (low, high, freqs)
	
	for jf in range(low, high + 1):
		if jf in freqs:
			continue
		f = freqs[:]
		f.append(jf)
		f.sort()
		#print 'try %s' % (f)
		for i in range(n):
			for j in range(n + 1):
				if i == j:
					continue
				if f[j] % f[i] == 0:
					#print 'devide! %d %% %d' % (f[j], f[i])
					break
				#else:
					#print 'error!! %d %% %d' % (f[j], f[i])
			else:
				#print 'pattern end %s' % f
				break
		else:
			print 'Clear %s + %d' % (freqs, jf)
			result += 'Case #%d: %d\n' % (case_count + 1, jf)
			break
	else:
		print 'not Clear'
		result += 'Case #%d: NO\n' % (case_count + 1)
			
		
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()