#!/usr/bin/env python
# -*- coding: utf-8 -*-

'python study'

__author__ = 'Herbert Yu'

#输入和输出练习，英文和中文
'''---------------------------------------------
print 'hello, world'

print u"中文测试正常"

#name = raw_input('please input your name:')

#print 'hello', name
-------------------------------------------------'''

#判断语句练习
'''-----------------------------------------------
age = raw_input('please input your age:')
if int(age) >= 18:
    print 'adult'
elif int(age) >= 6:
    print 'teenager'
else:
    print 'kid'
------------------------------------------------'''

#循环语句练习
'''-----------------------------------------------
names = ['haibo', 'liujia', 'helong']
for person in names:
    print person

sum = 0
for x in (1,2,3,4,5,6,7,8,9,10):
    sum = sum + x
print sum

sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n  
    n = n - 2
print sum
--------------------------------------------------'''

#dict & set
d = {'haibo': 100, 'liujia': 90, 'helong': 80}
print d
print u'请输入你要查找成绩的名字：'
name = raw_input()
if d.get(name, -1) == -1:
    print u'没有这个名字'
else:
    print name, d[name]

