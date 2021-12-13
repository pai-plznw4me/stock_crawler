from bs4 import BeautifulSoup
import urllib.request

stock_number = '005930'

f = urllib.request.urlopen("https://finance.naver.com/item/sise.naver?code={}".format(stock_number))
s = f.read()
f.close()

soup = BeautifulSoup(s, "html")
strong_tag = soup.find("strong", {"id": "_nowVal"})
text = strong_tag.text
