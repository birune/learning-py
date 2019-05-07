import csv

f = open("sample3-2.csv", "w")
w = csv.writer(f)

w.writerow(["Tokyo", "eraser"])
w.writerows([["Osaka", "pencil"], ["Kyoto", "ruler"]])