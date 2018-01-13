from sqlalchemy import Column, Integer, String, select
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Lend(Base):
    __tablename__ = 'lend'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    person_id = Column(Integer)


engine = create_engine('sqlite:///library.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for book in session.query(Book).all():
    lend = session.execute(select([Lend]).where(Lend.book_id == book.id))
    for l in lend:
        person = session.query(Person).filter(Person.id == l.person_id).one()
        print person.name + ' wypozyczyl ' + book.title + ', ' + book.author

