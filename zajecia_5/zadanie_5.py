import sys
import json

books = []
id = 1
def add(title, isbn, author):
    global id
    # title = raw_input("Podaj tytul: ")
    # isbn = raw_input("Podaj numer ISBN: ")
    # author = raw_input("Podaj autora: ")
    books.append({
        'id': id,
        'title': title,
        'ISBN': isbn,
        'author': author
    })
    id += 1

with open(sys.argv[1], 'w') as file:
    add("wladca pierscieni", 80932843204, "tolkien")
    print books
    print books[0]
    print books