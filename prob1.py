#!/usr/bin/python3
import datetime
name=input("enter your name")
age=int(input("enter age"))
x=datetime.datetime.now()
print(name + "will be of 95 year old in:" + str((95-age)+x.year))
