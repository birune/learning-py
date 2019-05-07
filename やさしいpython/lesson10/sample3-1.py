import csv

f = open("sample3-1.csv", "r")
rd = csv.reader(f)
#リーダ(csvファイルの各行を返すイテレータ)を返す

for row in rd:
#行を取り出す
    for col in row:
    #列を取り出す
        print(col, end=",")
    print()
f.close()