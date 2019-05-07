def _num_(x):
    while True:
        yield x
        x += 1

start = int(input("開始値を入力してください"))
end = int(input("終了値を入力してください"))
x = _num_(start)
for i in range(start, end):
    print(next(x))