b = int(input("プログラムを停止させる行を選んでください"))
c = int(input("処理を飛ばす行を選んでください"))

for i in range(1,11):
    if i == c and i == b:
        break
    elif i == c:
        continue
    print(i, end='')
    if i == b:
        break

print("end of program")
