from bs4 import BeautifulSoup
import requests
from dbcreate import connection

path = connection()
mycursor = path.cursor()

new_list = []
ids_list = []
row_list = []
query = "select company_id,company_stocksymbol from companies"
mycursor.execute(query)
listing = mycursor.fetchall()
for i in listing:
    ids_list.append(i[0])
    new_list.append(i[1])

insert_news_query = "insert into company_news(company_id, company_stocknews,company_stocklink) values (%s,%s,%s);"
print("Stock News for all the listed companies")

for i in range(len(new_list)):
    if new_list[i] == "N/A":
        continue
    else:
        if i == 36:
            new_list[i] = new_list[i]+".MI"
        print('-> fetching news for : ', i, ' ', new_list[i])
        webpage = "https://finance.yahoo.com/quote/"
        stockname = new_list[i]
        extension = "?p="+stockname
        # print(webpage+stockname+extension)
        page = requests.get(webpage+stockname+extension)
        soup = BeautifulSoup(page.content, 'lxml')
        news_container = soup.find(
            'ul', attrs={'class': 'My(0) Ov(h) P(0) Wow(bw)'})
        news_items = news_container.findAll(
            'a', attrs={'class': 'not-isInStreamVideoEnabled'})[:2]
        for item in news_items:
            # row_list.append(item.get('href')+","+item.text)
            mycursor.execute(insert_news_query,
                             (ids_list[i], item.text, item.get('href')))

path.commit()
print('--> records inserted')
# for ul in soup.findAll('ul', attrs={'class': 'My(0) Ov(h) P(0) Wow(bw)}):
# for link in ul.findAll('a', attrs={"class": "not-isInStreamVideoEnabled"})[:5]:
# print(link.get('href'))
# print(link.text)
# print("------------------")


#news = soup.find_all('u', class_="StretchedBox").next_sibling.next_sibling
# print(news)
