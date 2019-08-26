#!/usr/bin/python

import pytest

import book


@pytest.fixture()
def books_data():
    bookList = [('book 1', 'author 1'),
                ('book 2', 'author 2'),
                ('book 3', 'author 3'),
                ('book 4', 'author 4')]
    return bookList


def test_BookList(books_data):
    for title, author in books_data:
        theBook = book.Book(title, author)
        assert theBook.getTitle() == title
        assert theBook.getAuthor() == author
