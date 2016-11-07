#!/usr/bin/python

import itertools

print ("-----------------------------------")
print ("-------PyWordlistGenerator---------")
print ("-----------------------------------")
print ("-------teravice@rawsocket.io-------")
print ("-----------------------------------")
print ("")

lwl = 'abcdefghijklmnopqrstuvwxyz'
upl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numb = '1234567890'
spch = '`~!@#$%^&*()_+=-[]{}<>,./?"\|'
ch = ''

question = input("Do you want lowercase letters? [Y/n] > ")
if question=='y' or question=='':
	ch+=lwl
question = input("Do you want uppercase letters? [Y/n] > ")
if question=='y' or question=='':
	ch+=upl
question = input("Do you want numbers? [Y/n] > ")
if question=='y' or question=='':
	ch+=numb
question = input("Do you want special characters? [Y/n] > ")
if question=='y' or question=='':
	ch+=spch
rep = input("Enter number of characters e.g. 3 > ")

question = input("Type file name or enter for default(dict.txt) > ")
if question=='':
	flnm="dict.txt"

f=open(flnm, 'w')

print ("Depending on your selections, this may take a while.")
print ("Please be patient...")

for j in range(1,int(rep)+1):
	res = itertools.product(ch, repeat=j) # 3 is the length of your result.
	for i in res: 
		f.write("".join(i)+"\n")

f.close()

print ("Your dictionary is ready!")
