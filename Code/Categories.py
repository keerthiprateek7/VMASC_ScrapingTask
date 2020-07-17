import requests
from bs4 import BeautifulSoup
from dbcreate import connection
#import config


def categories():
    result = requests.get(
        "https://hamptonroadsalliance.com/")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    # finding all categories and making into list
    links = soup.findAll(
        "h3", {"class": "el-title"})
    links_list = [link.getText().strip() for link in links]

    # making key-value pair
    # res = {
    # links_list[i]: "distribution-and-logistics" for i in range(len(links_list))}
    # print(res)

    # making db connection
    path = connection()
    mycursor = path.cursor()  # pointing towards the location

    # making list as column
    query_string = "INSERT INTO categories(category_name) VALUES (%s);"
    for i in range(len(links_list)):
        mycursor.execute(query_string, (links_list[i],))
    path.commit()


categories()
