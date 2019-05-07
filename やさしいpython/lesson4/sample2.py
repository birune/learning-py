sale = int(input("売り上げを入力してください\n>>> "))
customer = int(input("客数を入力してください\n>>> "))

if sale >= 100 and customer >=100:
    print("売り上げは盛況です")
elif sale >= 100:
    print("売り上げは順調です")
elif sale >= 50:
    print("売り上げは普通です")
elif sale < 0:
    #処理をしないときには"pass"を記述する
    pass
else :
    print("売り上げは低調です")

print("処理を終了します")    