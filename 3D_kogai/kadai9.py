from turtle import *
def tree(x,n):
  pd()
  if n>0:
    fd(x)
    lt(20)
    tree(x*1.2,n-1)
    rt(70)
    tree(x*0.7,n-1)
    lt(50)
    bk(x)
  pu()
home()
clear()
N = int(input())
speed(1)
lt(90)
tree(50,N)
done()
