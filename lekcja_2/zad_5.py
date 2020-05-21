from sys import *
a=int(stdin.readline())
b=int(stdin.readline())
c=int(stdin.readline())

if a<=10 and a>0:
    print('liczba a jest w przedziale(0,10>')
if a>b or b>c:
    print('warunki spełnione')
else:
    print('drugi warunek nie spełniony')