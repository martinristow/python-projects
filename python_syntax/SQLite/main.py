import sqlite3

db = sqlite3.connect("books-collection.db") # pravime konekcija so bazata

cursor = db.cursor() # kreirame kursor koj sto ke ni sluzi za da ja kontrolirame bazata

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(2, 'Martin Ristov', 'Martin', '9.3')")
db.commit()