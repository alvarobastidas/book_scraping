import logging
from Book.book_page import BookPage
from pages.web_page_locator import BookPageURL

logger = logging.getLogger('scraping.all_books_page')


class AllPagesContent:
    def __init__(self, main_url):
        self.main_url = main_url
        self.pages_number = BookPageURL(main_url).pages_number

    @property
    def all_content(self):
        page_url = ''
        all_pages_content = []
        for n in range(1, self.pages_number + 1):
            web_page = self.main_url + page_url
            web_content = BookPageURL(web_page).page_content
            logger.debug('Creating AllBooksPage from page content.')
            all_pages_content += BookPage(web_content).book
            if n == 1:
                page_url = BookPageURL(web_page).web_url
            elif n == self.pages_number:
                break
            else:
                page_url = 'catalogue/' + BookPageURL(web_page).web_url
        return all_pages_content

