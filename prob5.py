#!/usr/bin/python3
import datetime
name=input("enter your name")
x=datetime.datetime.now()
if x.hour in range(4,12):
        print("good morning",name)
elif x.hour in range(12,17):
	print("good afternoon",name)
elif x.hour in range(17,21):
	print("good evening",name)
else:
	print("good night")
