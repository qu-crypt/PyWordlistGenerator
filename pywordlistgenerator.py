#!/usr/bin/python

import itertools

print ("-----------------------------------")
print ("-------PyWordlistGenerator---------")
print ("-----------------------------------")
print ("-------qucrypt@0x3f.dev------------")
print ("-----------------------------------")
print ("")

lwl = 'abcdefghijklmnopqrstuvwxyz'
upl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numb = '1234567890'
spch = '`~!@#$%^&*()_+=-[]{}<>,./?"\|'
ch = ''
flnm = ''

question = raw_input("Do you want lowercase letters? [Y/n] > ")
if question=='y' or question=='':
        ch+=lwl
question = raw_input("Do you want uppercase letters? [Y/n] > ")
if question=='y' or question=='':
        ch+=upl
question = raw_input("Do you want numbers? [Y/n] > ")
if question=='y' or question=='':
        ch+=numb
question = raw_input("Do you want special characters? [Y/n] > ")
if question=='y' or question=='':
        ch+=spch
rep = raw_input("Enter number of characters e.g. 3 > ")

question = raw_input("Type file name or enter for default(dict.txt) > ")
if question=='':
        flnm="dict.txt"
else:
        flnm=question

f=open(flnm, 'w')

print ("Depending on your selections, this may take a while.")
print ("Please be patient...")

for j in range(1,int(rep)+1):
        res = itertools.product(ch, repeat=j) # 3 is the length of your result.
        for i in res: 
                f.write("".join(i)+"\n")

f.close()

print ("Your dictionary is ready!")
