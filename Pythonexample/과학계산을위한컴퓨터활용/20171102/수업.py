'''
m = 'hello'
a = 12
x = 123.123456789
y = 987.98765e-10
print("%s %s %s %s" %(m,a,x,y))
print("Message = ", m, ', liter = ', a, ', x = ', x, ' y = ', y)
print("Message = ", m, ', liter = ', a, ', x = ', x, ' y = ', y, sep ='')
print("Message = " + m + ', liter = ' + str(a) + ', x = ' + str(x) + ' y = ' + str(y))
print('x = {2}, y = {3}, Message = {0}, iter = {1}'.format(m,a,x,y))
print("Message = {}, iter = {}, x = {}, y = {}".format(m,a,x,y))
print("Message = {:10s}, iter = {:10d}, x = {:20f}, y = {:20e}".format(m,a,x,y))
print("Message = {:>10s}, iter = {:10d}, x = {:20.3f}, y = {:20.3e}".format(m,a,x,y))
print("Message = {:^10s}, iter = {:10d}, x = {:20.3f}, y = {:20.3e}".format(m,a,x,y))
print("Message = {:<10s}, iter = {:010d}, x = {:20.3g}, y = {:20.3g}".format(m,a,x,y))
print("x = {2:20.3g}, y = {3:20.3g}, Message = {0:^10s}, iter = {1:10d}".format(m,a,x,y))
'''

'''
def myadd(a, b):
    c = a + b
    return c

def mymul(a, b):
    c = a * b
    return c

def print_val(f, a, b):
    print(f(a, b))

def myaddmul(a,b):
    c = a + b
    d = a * b
    return c, d

def myadd2(a, b):
    c = a + b
    m ='addition'
    return c, m

vala = int(input())
valb = int(input())
print("myadd = %d" %myadd(vala, valb))
print("print_val(myadd) = ", end="")
print_val(myadd, vala, valb)
print("print_val(mynul) = ", end="")
print_val(mymul, vala, valb)
a, b = myaddmul(vala, valb)
print("myaddmul = ", end = "")
print((a, b))
print("myaddmul = ", end = "")
print(myaddmul(vala,valb))
print("myadd2 = ", end = "")
print(myadd2(vala, valb))
print("myadd2 = {}".format(myadd2(vala, valb)))

#import는 한번 하고 다시 하지않음
#따라서 현재를 리셋하고 다시 import해야 한다
'''
#bisection
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 3 + 4 * x ** 2 - 10
while 1:
    a = int(input("a = "))
    b = int(input("b = "))
    if a > b:
        temp = a
        a = b
        b = temp
    elif a == b:
        print('a cannot equal b')
    if f(a) * f(b) > 0:
        print("f(a) and f(b) have same sign")
    else:
        break
while 1:
    TOLinte = int(input("TOL 10^-() = "))
    TOL = 10 ** (-TOLinte)
    if TOL <= 0:
        print('Tolerance must be positive')
    else:
        break
N0 = 100
x = np.linspace(a, b, 100)
y = f(x)