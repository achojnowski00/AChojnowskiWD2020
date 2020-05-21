from sys import *
h=int(input())
spc1=int(h/2)
x=1
for i in range(1,h+1):
    if(i<=h/2):
        stdout.write(" "*spc1)
        print('|'*x)
        spc1-=1
        x += 2
    else:
        stdout.write(" " * spc1)
        print('|'*x)
        spc1+=1
        x-=2