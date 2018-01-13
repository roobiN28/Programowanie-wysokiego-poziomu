import sqlite3


def printAll():
    for row in cursor.execute('SELECT * FROM book'):
        print(row)
    for row in cursor.execute('SELECT * FROM person'):
        print(row)
    for row in cursor.execute('SELECT * FROM lend'):
        print(row)


def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY , title TEXT, author TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY , name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS lend(id INTEGER PRIMARY KEY , book_id INTEGER, person_id INTEGER)')


def insertData():
    cursor.execute('INSERT INTO book VALUES (1,"Harry Potter", "J.R.R. Rowling")')
    cursor.execute('INSERT INTO book VALUES (2,"Wiedzmin", "Andrzej Sapkowski")')
    cursor.execute('INSERT INTO book VALUES (3,"Gringo wsrod dzikich plemion", "Wojciech Cejrowski")')

    cursor.execute('INSERT INTO person VALUES (1,"Krzysztof Jarzyna")')
    cursor.execute('INSERT INTO person VALUES (2,"Zawisza Czarny")')

    cursor.execute('INSERT INTO lend VALUES (1,1,2)')
    cursor.execute('INSERT INTO lend VALUES (1,3,1)')

def deleteData():
    cursor.execute('DELETE FROM book')
    cursor.execute('DELETE FROM person')
    cursor.execute('DELETE FROM lend')


connection = sqlite3.connect('library.db')

cursor = connection.cursor()

createTable()
connection.commit()

insertData()
connection.commit()

printAll()

deleteData()
connection.commit()

connection.close()
