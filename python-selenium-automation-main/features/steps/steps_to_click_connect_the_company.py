from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@given('Open the log in page')
def open_login_page(context):
    context.app.log_in_page.open_main_page()


@when('Input {email} in email field')
def input_email(context, email):
    context.app.log_in_page.enter_email(email)


@then('Input {password} in password field')
def input_password(context, password):
    context.app.log_in_page.enter_password(password)


@then('Click on continue button')
def click_continue_button(context):
    context.app.log_in_page.click_continue_button()


@then('Click on “Connect the company”')
def click_company_button(context):
    context.app.home_page.click_connect_company_button()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.home_page.switch_to_new_window()


@then('Verify “Connect the company” page is opened')
def verify_connect_company_page(context):
    context.app.connect_the_company_page.verify_connect_page_opened()