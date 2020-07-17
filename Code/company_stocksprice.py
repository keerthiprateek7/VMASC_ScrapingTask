import requests
from bs4 import BeautifulSoup
from dbcreate import connection
import config

path = connection()
mycursor = path.cursor()

new_list = []
ids_list = []
query = "select company_id,company_stocksymbol from companies"
mycursor.execute(query)
listing = mycursor.fetchall()
for i in listing:
    ids_list.append(i[0])
    new_list.append(i[1])

insert_sp_query = "insert into company_stocks(company_id, company_stock_price) values (%s,%s);"
print("Stock Prices for all the listed companies")

# checking if the stock has value or not
for i in range(len(new_list)):
    if new_list[i] == 'N/A':
        print(new_list[i]+"--- No Stock Symbol !!!!!")
        continue
    else:
        if i == 36:
            new_list[i] = new_list[i]+".MI"
        # Made a generalized pattern for all links
        webpage = "https://finance.yahoo.com/quote/"
        stockname = new_list[i]
        extension = "?p="+stockname+"&.tsrc=fin-srch"
        result = requests.get(
            webpage+stockname+extension)
        src = result.content
        # print(src)
        soup = BeautifulSoup(src, 'html.parser')
        # print(soup)
        price = soup.find(
            'div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        mycursor.execute(insert_sp_query, (ids_list[i], price))
        print(new_list[i]+"="+price)
path.commit()
