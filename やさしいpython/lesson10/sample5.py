try:
    f = open("sample5.txt", "r")
except FileNotFoundError as e:
#ファイルが見つからなかった場合の処理
#eにはエラー内容が入る
    print(e)
else:
#何事もなかった時の処理
    lines = f.readlines()
    for line in lines:
        print(line, end="")
    f.close
finally:
#最後に必ずする処理
    print("処理を終了します")