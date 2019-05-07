import sqlite3

conn = sqlite3.connect("pdb.db")
#データベースに接続
c = conn.cursor()
#データを1行ずつ操作するためカーソルを取得
c.execute("DROP TABLE IF EXISTS product")
#表の存在を調べて存在したなら削除する

c.execute("CREATE TABLE product(name CHAR(20), num INT)")
#表の列名、型名を指定している
c.execute("INSERT INTO product VALUES('orange',80)")
c.execute("INSERT INTO product VALUES('strawberry',60)")
c.execute("INSERT INTO product VALUES('apple',22)")
c.execute("INSERT INTO product VALUES('peach',50)")
c.execute("INSERT INTO product VALUES('marron',75)")

conn.commit()

itr = c.execute("SELECT * FROM product")
for row in itr:
    print(row)
print()

itr = c.execute("SELECT * FROM product WHERE num<=30")
for row in itr:
    print(row)
print()

conn.close()

