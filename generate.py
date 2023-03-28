import sqlite3
from sqlalchemy import create_engine
# filename to form database
file = "db.db"

try:
    conn = sqlite3.connect(file)
    print("Database Sqlite3.db formed.")
    engine = create_engine('sqlite:///db.db', echo=False)
    engine.execute('''CREATE TABLE news (
	title TEXT, 
	id TEXT, 
	link TEXT, 
	published_parsed TEXT primary key, 
	summary TEXT, 
	classe TEXT
);''')
except:
    print("Database Sqlite3.db not formed.")
