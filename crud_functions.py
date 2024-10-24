import sqlite3
from desc import *

connestion = sqlite3.connect('product.db')
cursor = connestion.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')


initiate_db()

#for i in range(1, 5):
#    cursor.execute(f'INSERT INTO Products (title, description, price) VALUES(?, ?, ?)',
#                   (f'{name[i - 1]}', f'{noty[i - 1]}', f'{price[i - 1]}'))

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return False
    return True

def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                       (username, email, age, 1000))
    connestion.commit()


connestion.commit()