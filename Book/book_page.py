from bs4 import BeautifulSoup
from locators.book_locator_page import BookPageLocator
from parser.book_parser import BookParser


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def book(self):
        locator = BookPageLocator.BOOK
        return [BookParser(book) for book in self.soup.select(locator)]
