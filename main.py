import logging
import time
import asyncio
import aiohttp
import async_timeout
import numpy as np
from pages.web_page_locator import BookPageURL
from menu.book_menu import Menu
from Book.book_page import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M%:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list ...')

loop = asyncio.get_event_loop()

selection = '''
OPTIONS:
        a : See the next book
        b : Select books by price
        c : Select books by rating
        d : Select top ten best books
        e : Select top ten cheapest books
        f : Exit the app
'''

# Asynchronous Program with asyncio and aiohttp


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(20):
        async with session.get(url) as response:
            print(f'Page took {time.time()-page_start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

start_time = time.time()
web_page_root = 'http://books.toscrape.com/'
number_of_pages = BookPageURL(web_page_root).pages_number
urls = [f'{web_page_root}catalogue/page-{page_num+1}.html' for page_num in range(number_of_pages)]
web_pages_content = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'This function took {time.time()-start_time}')
all_content = [BookPage(web_content).book for web_content in web_pages_content]
content = np.array(all_content).ravel()  # convert matrix to array
book_menu = Menu(content)


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










