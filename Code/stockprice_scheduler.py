# Used concept of scheduler to get the values for evry 5 seconds

from bs4 import BeautifulSoup
import requests
import sched
import time
s = sched.scheduler(time.time, time.sleep)


def parseprice():
    webpage = "https://finance.yahoo.com/quote/"
    stockname = "TSLA"
    extension = "?p="+stockname+"&.tsrc=fin-srch"
    result = requests.get(
        webpage+stockname+extension)
    src = result.content
    # print(src)
    soup = BeautifulSoup(src, 'html.parser')
    # print(soup)
    price = soup.find(
        'div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    print(price)
    s.enter(5, 0, parseprice)


s.enter(5, 0, parseprice)
s.run()

# parseprice()

# for i in range(10):
#print('current price is:' + parseprice())
