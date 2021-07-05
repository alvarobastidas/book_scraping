import requests
import re
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')


class BookWebPageLocator:
    WEB_PAGE_NUMBER = 'div ul.pager li.current'
    WEB_PAGE_URL = 'div ul.pager li.next a'


class BookPageURL:
    def __init__(self, web_link):
        logger.debug('Parsing page content with BeautifulSoup HTML parser. ')
        self.web_link = web_link
        self.page_content = requests.get(self.web_link).content
        self.soup = BeautifulSoup(self.page_content, 'html.parser')

    @property
    def web_url(self):  # Return part of URL /page-2.html
        return self.soup.select_one(BookWebPageLocator.WEB_PAGE_URL).attrs['href']

    @property
    def pages_number(self):  # Return an integer the total pages numbers
        logger.debug('Finding all number of catalogue pages available...')
        return int(re.findall('[0-9]+', self.soup.select_one(BookWebPageLocator.WEB_PAGE_NUMBER).string)[1])
