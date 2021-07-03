from seleniumpagefactory import *
from selenium.webdriver.common.by import *


class GoogleSearchPage(object):
    _search_box = find_by(how=By.NAME, using='q')

    _search_button = find_by(name='btnK')

    def __init__(self, driver):
        self._driver = driver

    def search(self, keywords):
        self._search_box().click()
        self._search_box().send_keys(keywords)
        self._search_button().click()