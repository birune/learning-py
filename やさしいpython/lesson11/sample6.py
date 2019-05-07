import urllib.request
from html.parser import HTMLParser

class SampleHTMLParser(HTMLParser):
#派生クラスの定義
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False
    #オーバーライドしていく

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.title = True
    #開始タグの解析

    def handle_data(self, data):
        if self.title is True:
            print("タイトル:", data)
            self.title = False
    #データを取得する


page = urllib.request.urlopen("https://www.python.org/")
#urlを開く

html = page.read()
#読み込む
str = html.decode()
#読み込んだものを文字列にする

p = SampleHTMLParser()
p.feed(str)