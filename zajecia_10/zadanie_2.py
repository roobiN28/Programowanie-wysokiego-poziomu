import sqlite3


def printAll():
    for row in cursor.execute('SELECT * FROM book'):
        print(row)

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS book(id integer, title text, author text)')

cursor.execute('INSERT INTO book VALUES (1,"Harry Potter", "J.R.R. Rowling")')

connection.commit()

printAll()

cursor.execute('UPDATE book SET title = "Wiedzmin", author = "Andrzej Sapkowski" WHERE id = 1')
connection.rollback()
printAll()

cursor.execute('DELETE FROM book')
connection.commit()

printAll()

connection.close()

