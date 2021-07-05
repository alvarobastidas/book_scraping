import re
from locators.book_locators import BookLocator


class BookParser:

    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Book: {self.name}, Price: ${self.price[0]}, Rating: ({self.rating} stars) '

    @property
    def name(self):
        locator = BookLocator.NAME
        return self.parent.select_one(locator).string

    @property
    def price(self):
        locator = BookLocator.PRICE
        return [float(p) for p in re.findall('[0-9/.]+', self.parent.select_one(locator).string)]

    @property
    def rating(self):
        locator = BookLocator.RATING
        rating_classes = [rating for rating in self.parent.select_one(locator).attrs['class'] if rating != 'star-rating']
        rating_number = BookParser.RATING.get(rating_classes[0])
        return rating_number






