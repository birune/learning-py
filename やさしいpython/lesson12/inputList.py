i = 0
num = []
while True:
    add = int(input(">>>"))
    
    num.append(add)

    if num[i] == -1:
        num.remove(-1)
        break
    i = i + 1

print(num)