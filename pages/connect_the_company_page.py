from selenium.webdriver.common.by import By

from pages.base_page import Page


class ConnectTheCompanyPage(Page):

    def verify_connect_page_opened(self):
        self.verify_url('https://soft.reelly.io/book-presentation')
