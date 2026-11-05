#!/usr/bin/env python3
# -*- coding : utf-8 -*-
'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string

print(s)  # with print(), special characters are interpreted, so \n produces new line
print('C:\this\name')  # here \t means tab, \n means newline

print(r'C:\this\name')  # note the r before the quote

x=int(input("please enter an integer:"))
if x<0:
	x=0
	print('Negative changed to zero')
elif x==0:
	print('Zero')
elif x==1:
	print('single')
else:
	print('more')