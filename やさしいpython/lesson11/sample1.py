import sqlite3

conn = sqlite3.connect("pdb.db")
#データベースに接続
c = conn.cursor()
#データを1行ずつ操作するためカーソルを取得
c.execute("DROP TABLE IF EXISTS product")
#表の存在を調べて存在したなら削除する

c.execute("CREATE TABLE product(name CHAR(20), price INT)")
#表の列名、型名を指定している
c.execute("INSERT INTO product VALUES('pencil',80)")
c.execute("INSERT INTO product VALUES('eraser',50)")
c.execute("INSERT INTO product VALUES('ruler',200)")
c.execute("INSERT INTO product VALUES('kompass',300)")
c.execute("INSERT INTO product VALUES('pen',100)")

conn.commit()
#データ更新を確定させる
itr = c.execute("SELECT * FROM product")
#データをすべて取り出す
#*の部分は表示する列を表す
print("all items")
for row in itr:
    print(row)
print()

print("under 200yen")
itr = c.execute("SELECT * FROM product WHERE price<=200")
for row in itr:
    print(row)
print()

print("pencil")
itr = c.execute("SELECT * FROM product WHERE name = 'pencil'")
for row in itr:
    print(row)
print()

print("include \"pen\"")
itr = c.execute("SELECT * FROM product WHERE name LIKE '%pen%'")
for row in itr:
    print(row)
print()

print("ascending")
itr = c.execute("SELECT * FROM product ORDER BY price")
for row in itr:
    print(row)
print()

print("descending")
itr = c.execute("SELECT * FROM product ORDER BY price DESC")
for row in itr:
    print(row)
print()


conn.close()


