#!/usr/bin/env.python
#._*_.coding:utf -8._*_

'''

i=0
while i < 6:
    print("*"*i)
    i+=1


i=0
while i<6:
    j=0
    while j<i:
        print("*",end='')
        j+=1
    print("\n")
    i+=1


'''
i=5
while i>0:
    j=0
    while j<i:
        print("*",end='\n')
        j+=1
    print("")
    i-=1

#99乘法表
'''
i=1
j=1
while i<10:
    m=i*j
    while j<10:
        print(i+str"x" + j+str"="+m)
        j+=1
    i+=1
'''