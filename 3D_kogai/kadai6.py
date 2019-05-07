from turtle import *
def scroll2(a,c,r):
    pu()
    home()
    clear()
    pd()
    dash = 0
    color(c)
    for _ in range(r):
        dash += 10
        fd(dash)
        rt(a)
scroll2(60,'green',10)
scroll2(88,'blue',20)
scroll2(117,'red',30)
scroll2(144,'yellow',40)
done()
