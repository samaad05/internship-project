from pages.base_page import Page
from pages.home_page import HomePage
from pages.log_in_page import LogInPage
from pages.connect_the_company_page import ConnectTheCompanyPage



class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.home_page = HomePage(driver)
        self.log_in_page = LogInPage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)


