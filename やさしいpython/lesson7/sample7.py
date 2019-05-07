def calc(*args):
    s = 0
    for i in args:
        s += i
    a = s/len(args)
    #sとaを要素とするタプルを返す
    return s, a

#アンパックして受け取る
S, A = calc(1, 2, 3, 4, 5)
print(S)
print(A)