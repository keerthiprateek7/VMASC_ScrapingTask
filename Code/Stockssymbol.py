# output not clear

from bs4 import BeautifulSoup
import requests
from dbcreate import connection

webpage = "https://www.google.com/search?q="

companies = ["PRAA"]
#
stockDiv = "zloOqf PZPZlf"
googleFinance = "&tbm=fin"
for company in companies:
    company = company.replace(" ", "%20")
    page = requests.get(webpage+company+googleFinance)
    soup = BeautifulSoup(page.content, 'lxml')
    print(soup.title.text)
    body = soup.find(id="main")
    rs = body.findAll('div')
    ab = body.findAll('span', class_='r0bn4c rQMQod')
    print(ab)
    #infoDiv = soup.find_all('div', class_="mod")
    # print(infoDiv)
    # print(soup.body)
