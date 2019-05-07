def rpast(num, str='*'):
    for i in range(num):
        print(str, end='')

s = input("文字列を入力してください:")
n = int(input("個数を入力してください:"))

rpast(n, s)