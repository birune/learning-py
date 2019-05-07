import mydir.myclass
#from mydir import myclassでも可

pr = mydir.myclass.Customer("aaa", 10, "090-0000-0000")
#from~で定義しているとmydir.はいらない

print(pr.getName())
print(pr.getTel())