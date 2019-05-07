from turtle import *
def roku(a):
  if a>0:
    fd(100)
    rt(60)
    roku(a-1)
home()
clear()
roku(6)
done()
