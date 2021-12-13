from bs4 import BeautifulSoup
import urllib.request
import datetime


def get_stock_price(ticker_code):
    """
    Description:

    :param ticker_code: str, 종목 코드
    example)
        삼성전자, 006500
        LG전자, 066570
    """
    f = urllib.request.urlopen("https://finance.naver.com/item/sise.naver?code={}".format(ticker_code))
    s = f.read()
    f.close()

    soup = BeautifulSoup(s, "html")
    strong_tag = soup.find("strong", {"id": "_nowVal"})
    text = strong_tag.text
    return text


if __name__ == '__main__':
    time = datetime.datetime.now()
    ss_price = get_stock_price("005930")
    lg_price = get_stock_price("066570")
    print('time : {}, 삼성전자 주가: {}'.format(time, ss_price))
    print('time : {}, LG전자 주가: {}'.format(time, lg_price))
