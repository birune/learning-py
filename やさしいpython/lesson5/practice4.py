city = ['東京', '名古屋', '大阪', '京都', '福岡']
tempH = [38, 28, 27, 26, 27]
tempL = [25, 21, 20, 19, 22]
for c, h, l in zip(city, tempH, tempL):
    print(c, "の最高気温は", h, "、最低気温は", l, "です")