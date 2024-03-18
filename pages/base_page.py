from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_element_visible(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Element with {by}={value} not visible within {timeout} seconds. Error: {e}")
            return None

    def open(self,url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)

    def wait_element_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element by {locator} is not clickable')

    def wait_element_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message=f'Element by {locator} is not clickable').click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"expected '{expected_text}' but got '{actual_text}'"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"expected '{expected_text}' not in '{actual_text}'"

    def verify_url(self, expected_url, *locator):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"expected '{expected_url}' not in '{actual_url}'"

    def verify_partial_url(self, expected_partial_url, *locator):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f"expected '{expected_partial_url}' not in '{actual_url}'"