#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @property
    def page_count(self):
        return self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @title.setter
    def title(self, value):
        if value != "":
           self._title=value
        else:
            raise ValueError("some message")

    @page_count.setter
    def page_count(self, value):
        if type(value) is int:
            self._page_count=value
        else:
            print("page_count must be an integer")


my_book = Book("Hello Weird", 5)
print(f"{my_book.title} is {my_book.page_count} pages long")
my_book.turn_page()