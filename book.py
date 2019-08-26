#!/usr/bin/python


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author


class BookList(object):
    def __init__(self):
        self.bookList = []

    def addBook(self, book):
        if not isinstance(book, Book):
            raise TypeError
        self.bookList.append(book)

    def removeBook(self, book):
        if book not in self.bookList:
            print("Can't remove Book since it is not in the list!!")
            return False
        self.bookList.remove(book)
        return True

    def clearBookList(self):
        self.bookList = []
