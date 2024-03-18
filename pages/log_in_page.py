from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class LogInPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[id*=email]")
    PASSWORD_FILED = (By.ID, "field")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(@class, 'login-button')]")
    def open_main_page(self):
        self.open("https://soft.reelly.io/sign-in")


    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)


    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_FILED)
        )
        password_field.clear()
        password_field.send_keys(password)



    def click_continue_button(self):
        self.click(*self.CONTINUE_BUTTON)



