from turtle import *
def scroll(a):
    pu()
    home()
    clear()
    pd()
    dash = 0
    for _ in range(30):
        dash += 10
        fd(dash)
        rt(a)
scroll(60)
scroll(88)
scroll(117)
scroll(144)
done()
