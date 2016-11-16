from selenium import webdriver
from fixture.search import SearchHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome("C:/chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.search = SearchHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://www.dailyfx.com/")

    def destroy(self):
        self.wd.quit()
