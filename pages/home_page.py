from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):
    CONNECT_THE_COMPANY_BUTTON = (By.XPATH, '//div[text()="Connect the company"]')



    def click_connect_company_button(self):
        self.wait_element_clickable_click(*self.CONNECT_THE_COMPANY_BUTTON)

