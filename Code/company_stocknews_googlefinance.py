import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'


def get_data(symbol, stockexchnage):
    base_url = 'https://www.google.com/search?q='+stockexchnage+':' + symbol
    print(base_url)
    res = requests.get(url=base_url, headers={'user-agent': user_agent})
    print(res.status_code)
    soup = BeautifulSoup(res.content, 'html.parser')
    current_price = soup.find('span', attrs={'jsname': 'vWLAgc'}).text
    print(current_price)

    news_url = base_url + '&tbm=nws&source=lnms&sa=X'
    news_res = requests.get(url=news_url, headers={'user-agent': user_agent})
    news_soup = BeautifulSoup(news_res.content, 'html.parser')
    news_items = news_soup.find('div', attrs={'id': 'search'}).find_all(
        'div', attrs={'class': 'dbsr'})
    for item in news_items:
        heading = item.find('div', attrs={'role': 'heading'}).text
        news_article_link = item.find('a')['href']
        print(heading)
        print(news_article_link)
        print('_'*50)


exchanges = ['NYSE', 'NASDAQ']
for i in range(len(exchanges)):
    get_data('TSLA', exchanges[i])
