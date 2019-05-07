from turtle import *
def tree(x,n):
  pd()
  if n>0:
    fd(x)
    lt(30)
    tree(x,n-1)
    rt(60)
    tree(x,n-1)
    lt(30)
    bk(x)
  pu()
home()
clear()
N = int(input())
speed(1)
lt(90)
tree(50,N)
done()
