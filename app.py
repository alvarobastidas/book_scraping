import logging
import time
from pages.all_pages_content import AllPagesContent
from menu.book_menu import Menu

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M%:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list ...')


selection = '''
OPTIONS:
        a : See the next book
        b : Select books by price
        c : Select books by rating
        d : Select top ten best books
        e : Select top ten cheapest books
        f : Exit the app
'''

# Synchronous Program that working with request function
start_time = time.time()
web_page_root = 'http://books.toscrape.com/'
content = AllPagesContent(web_page_root).all_content
book_menu = Menu(content)
print(f'This function took {time.time()-start_time}')


user_choices = {
    'a': book_menu.all_books,
    'b': book_menu.by_price,
    'c': book_menu.by_rating,
    'd': book_menu.best_books,
    'e': book_menu.cheapest_books
}

user_input = input(f'{selection}\nplease choose an option: ')

while user_input != 'f':
    if user_input in ('a', 'b', 'c', 'd', 'e'):
        for a in user_choices[user_input]:
            print(a)
    else:
        print('Please choose a valid option!!')
    user_input = input(f'{selection}\nplease choose an option: ')

print('BYE!!!')

