def func(a, b):#仮引数
    print("a:", a)
    print("b:", b)

func(1, 2)#実引数
print()
func(b=2, a=1)

#Q:実引数で仮引数の名前を指定すれば実引数の順番は影響しないのか
#A:しない