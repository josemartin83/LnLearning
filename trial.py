import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
(Title TEXT,Director TEXT, Year INT)''')
