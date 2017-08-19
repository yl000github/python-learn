#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.common import  log
from lib.file import  fileRead,fileWrite

# def log(title,msg=""):
	# print("====={}====={}".format(title,msg))
	# return

# def fileWrite(path,content):
	# fo = open("path", "w")
	# fo.write( content);
	# fo.close()
	
# def fileRead(path):
	# fo = open("path", "r")
	# str=fo.read();
	# fo.close()
	# return str
# 输出
log( "基本输出" )
print("hello")
print("你好")
# 条件
log( "条件" )
if 1>=0 :
	print("true")
else :
	print("false")

if 1<=0 :
	print("true")
elif 33==22 :
	print("false")
else :
	print("no")
# 循环
log( "循环" )
list=[1,2,3,4]
for i in list:
	print("current value:"+str(i))
for i in range(len(list)):
	print("current value:"+str(list[i]))
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
	print i,j

urls = ['http://mmjpg.com/mm/{cnt}'.format(cnt=cnt) for cnt in range(0, 1)]
print "urls:",urls

	
count=1
while count<9:
	print "count:",count
	count=count+1
else:
	print "count false:",count
	
	
# 函数
log( "函数" )
# 数组
log( "数组" )
list= range(1,10)
print "list:",list

list=[1,2,'3']
print "list:",list

print "list[1]:",list[1]

print "list[-1]:",list[-1]

del list[1]
print "after delete list:",list

# 文件
log( "文件" )
fileWrite("f:/foo.txt","fuck you")

print "str in file:",fileRead("f:/foo.txt")

# 模块
log( "模块" )
