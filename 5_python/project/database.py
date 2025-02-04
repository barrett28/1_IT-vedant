import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passowrd="root",
        database="Python_hos_mg"
    )