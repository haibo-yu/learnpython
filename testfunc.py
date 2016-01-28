#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python function study'

__author__ = 'Herbert Yu'

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x

import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x - 1)


if __name__ == '__main__':
	#print my_abs(55)
	#print my_abs(-3)
	#print move(100, 100, 60, math.pi / 6)
	#print power(2)
	#print power(5,3)
	#print calc(1,2)
	#num1 = [1,2,3]
	#print calc(*num1)
	#num2 = (4,5)
	#print calc(*num2)
	print fact(5)
	print fact(1)
	#main()

