#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python functional program study'

__author__ = 'Herbert Yu'

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

def log_homework(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'begin call %s():' % func.__name__
		func(*args, **kw)
		print 'end call %s():' % func.__name__
		return None
	return wrapper

@log_homework	
def now():
	print '2016-01-28'



if __name__ == '__main__':
	#main()
	now()
	print now.__name__
    
