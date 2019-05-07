from turtle import *
def tree(x,n):
  pd()
  if n>0:
    fd(x)
    lt(20)
    tree(x,n-1)
    rt(70)
    tree(x,n-1)
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
