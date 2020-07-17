import mysql.connector


def connection():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="prateek@database", database="vmasc")
    if(mydb):
        print("connection successful")
        return mydb
    else:
        print("connection unsuccessful")


# connection()
