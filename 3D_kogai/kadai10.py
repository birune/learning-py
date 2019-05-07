from turtle import *
def koch0(l):
    pd()
    fd(l/3)
    lt(60)
    fd(l/3)
    rt(120)
    fd(l/3)
    lt(60)
    fd(l/3)
    pu()

home()
clear()
L = int(input())
speed(1)
pu();bk(L/2);pd()
koch0(L)
done()