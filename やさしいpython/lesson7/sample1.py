#"def 関数名(引数リスト):
#   return 戻り値

def _sum_(a ,b):
    print("和を格納します")
    c = a + b
    return c

#引数に*をつけるといくつでも引数を呼び出せる
#引数はタプルとして扱われる
def _sumt_(*args):
    print("和を格納します")
    a = 0
    for i in args:
        a += i
    return a

#引数に**をつけるといくつでもキーワード引数を呼び出せる
#引数はディクショナリとして扱われる
def _sumd_(**args):
    print("和を格納します")
    a = 0
    for i in args.values():
        a += i
    return a

sum1 = _sum_(1, 1)
sum2 = _sumt_(1, 1, 1, 1, 1)
sum3 = _sumd_(a=1, b=1, c=1)

print(sum1)
print(sum2)
print(sum3)
