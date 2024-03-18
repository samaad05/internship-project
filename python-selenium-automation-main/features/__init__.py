from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# IDs:
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'continue')
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.ID, 'createAccountSubmit')

# Xpath
driver.find_element(By.XPATH, '//input[@class="a-icon a-icon-logo"]')

driver.find_element(By.XPATH, '//input[@href="/gp/help/customer/display.html/ref'
                              '=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]')

driver.find_element(By.XPATH, '//input[@href="/gp/help/customer/display.html/ref'
                              '=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')

driver.find_element(By.XPATH, '//input[@class="a-expander-prompt"]')


driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, '#continue')
driver.find_element(By.CSS_SELECTOR, 'a[href*="ref=ap_register_notification_privacy_notice"]')
driver.find_element(By.CSS_SELECTOR, 'a[href*="ref=ap_register_notification_condition_of_use"]')
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')