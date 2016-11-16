import string
import random


class SearchHelper:
    def __init__(self, app):
        self.app = app

    def enter_search_phrase(self, search):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector( "ul.nav.navbar-nav.navbar-right.no-shadow li.dropdown-grid a.dropdown-toggle span.caret").click()
        wd.find_element_by_xpath("//div[@id='dfx_navbar']/ul[2]/li/div/div/form/div/input").click()
        wd.find_element_by_xpath("//div[@id='dfx_navbar']/ul[2]/li/div/div/form/div/input").clear()
        wd.find_element_by_xpath("//div[@id='dfx_navbar']/ul[2]/li/div/div/form/div/input").send_keys(search.phrase)
        wd.find_element_by_xpath("//div[@id='dfx_navbar']/ul[2]/li/div/div/form/div/span/button").click()

    #def open_first_return_result(self):
        #wd = self.app.wd
        #result = wd.find_elements_by_css_selector("div.gsc-webResult.gsc-result div.gs-webResult.gs-result div.gsc-thumbnail-inside div.gs-title a.gs-title")
        #if result.is_displayed is True:
            #result.click()
        #else:
            #print ("No results")


    #def random_phrase(self):
        #wd = self.app.wd
        #symbols = string.ascii_letters + string.digits + string.punctuation + " " * 2
        #return "".join([random.choice(symbols) for i in range(10)])

