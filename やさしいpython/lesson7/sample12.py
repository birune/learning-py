a = 0

def func():
    global a
    #グローバル変数に指定する
    b = 0

    print(a, '/', b)

    a += 1
    b += 1

for i in range(5):
    func()