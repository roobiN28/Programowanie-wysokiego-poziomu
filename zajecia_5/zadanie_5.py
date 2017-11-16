import sys
import json


class Library(object):
    books = []

    def toString(self):
        return self.books

    def add(self):
        title = raw_input('Podaj tytul: ')
        isbn = raw_input('Podaj numer ISBN: ')
        author = raw_input('Podaj autora: ')
        self.books.append({
            'title': title,
            'ISBN': isbn,
            'author': author
        })

    def delete(self):
        book = self.findByTitle(raw_input('Podaj tytul: '))
        if book:
            self.books.remove(book)

    def findByTitle(self, title):
        for book in self.books:
            if book.get('title') == title:
                return book

    def writeToFile(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(self.books))
            f.close()

    def readFromFile(self, path):
        with open(path, 'r') as f:
            self.books = json.loads(f.readline())
            f.close()


library = Library()
while True:
    print '1.Wyswietl wszystkie'
    print '2.Dodaj'
    print '3.Usun'
    print '4.Zapisz'
    print '5.Wczytaj'
    print '6.Wyjdz'
    option = input('Podaj opcje: ')
    if option == 1:
        print library.toString()
    elif option == 2:
        library.add()
    elif option == 3:
        library.delete()
    elif option == 4:
        library.writeToFile(sys.argv[1])
    elif option == 5:
        library.readFromFile(sys.argv[1])
    else:
        break
