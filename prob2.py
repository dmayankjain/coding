#!/usr/bin/python3
from googlesearch import search
import time
web=input("search")
url=[]
for i in search(web,stop=10):
	print(i)
time.sleep(2)
url.append(i)
print(url)

