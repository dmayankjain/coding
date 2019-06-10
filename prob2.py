#!/usr/bin/python3
from googlesearch import search
import time
web=input("search")
list1=[]
for i in search(web,stop=10):
	print(i)
	time.sleep(2)
	list1.append(i)
print(list1)
f=open('url.txt','a+')
for i in list1:
	f.write(i+'\n')
f.close()

