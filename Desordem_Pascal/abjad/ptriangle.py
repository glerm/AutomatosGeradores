# -*- coding: utf-8 -*- 
#from abjad import *
import sys
from abjad import *

num=int(sys.argv[1])


def triangle(n):
	import numpy
	x=[[1]]
	op=[[1]]
	for i in range(n-1):
		x.append(list(map(sum,zip([0]+x[-1],x[-1]+[0]))))
		op.append([ ((n%12)) for n in x[i+1]]) #operação sobre os numeros
	return op

def tritonos(n):
	import numpy
	x=[[1]]
	op=[[1]]
	for i in range(n-1):
		x.append(list(map(sum,zip([0]+x[-1],x[-1]+[0]))))
		op.append([ ((n*3)%18) for n in x[i+1]]) #operação sobre os numeros
	return op


def sierpinski(n):
	import numpy
	x=[[1]]
	op=[[1]]
	for i in range(n-1):
		x.append(list(map(sum,zip([0]+x[-1],x[-1]+[0]))))
		op.append([ ((n%2)) for n in x[i+1]]) #operação sobre os numeros
	return op

 


tri=tritonos(num)
Spascal=sierpinski(num)
pascal=triangle(num)
pascal_reverse=(triangle(num))[::-1]
RvSpascal=(sierpinski(num))[::-1]
pascalist=[]

for p in pascal:
	for pp in p:
		pascalist.append(pp )



############## abjad
'''
integers = pascalist
denominator = 8
durations = [Duration(i,denominator) for i in integers]

notes = notetools.make_notes(["c'"], durations)
staff = Staff(notes)
show(staff)
'''



#####################################
for row in tri:
	print row


print " --------\n "
print tri


