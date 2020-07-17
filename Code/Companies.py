from bs4 import BeautifulSoup
import requests
from dbcreate import connection

webpages = ["https://hamptonroadsalliance.com/distribution-and-logistics/",
            "https://hamptonroadsalliance.com/business-shared-services/",
            "https://hamptonroadsalliance.com/advanced-manufacturing/",
            "https://hamptonroadsalliance.com/food-beverage-processing/",
            "https://hamptonroadsalliance.com/information-technology/"]

ddict = {}


for webpage in webpages:
    companies = []
    page = requests.get(webpage)
    # print(page.status_code)
    soup = BeautifulSoup(page.content, 'lxml')
    category = soup.title.text.lstrip().rstrip().split("-")[0].strip()
    category = category.replace("&", "and")
    for company in soup.find_all('h4', class_="el-title uk-h4 uk-margin-top uk-margin-remove-bottom"):
        companies.append(company.text.lstrip().rstrip())

    ddict[category] = companies

# handling this particular webpage differently
page = requests.get(
    "https://hamptonroadsalliance.com/maritime-shipbuilding-repair/")
companies = []
soup = BeautifulSoup(page.content, 'lxml')
category = soup.title.text.lstrip().rstrip().split("-")[0]
category = category.split(":")[1].strip()
category = category.replace("&", "+")

# made a dictionary with category and companies
for company in soup.find_all('h3', class_="el-title uk-margin-top uk-margin-remove-bottom"):
    companies.append(company.text.lstrip().rstrip())
ddict[category] = companies


# print(ddict.keys())
companyNames = []
sql_insert_companies = "insert into companies(company_name,category_id) values (%s,%s)"
path = connection()
mycursor = path.cursor()
# print(ddict.keys())
for key in ddict.keys():
    # print(ddict.get(key))

    # found the id from category table and using the id's of catgeory table inserted companies in companies table
    sql_select_query = "select category_id from categories where category_name = (%s)"
    mycursor.execute(sql_select_query, (key,))
    record = mycursor.fetchall()
    cat_id = record[0][0]
    for j in ddict.get(key):
        print("inserting : ", cat_id, j)
        mycursor.execute(sql_insert_companies, (j, cat_id))


path.commit()
print("insert successful !!!")


# for key in ddict.keys():
# id = "select * from categories"
# addr = (key,)
# mycursor.execute(id)
# records = mycursor.fetchall()
# print(records)
# for row in records:
# print("Id = ", row[0], )
