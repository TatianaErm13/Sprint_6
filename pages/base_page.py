from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):

        element = self.find_element(locator)

        self.scroll_to_element(element)

        element.click()

    def fill_input(self, locator, text):

        self.find_element(locator).send_keys(text)

    def get_text(self, locator):

        return self.find_element(locator).text

    def open_url(self, url):

        self.driver.get(url)

    def scroll_to_element(self, element):

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    def wait_for_new_window(self):

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

    def switch_to_window(self, index):

        self.driver.switch_to.window(
            self.driver.window_handles[index]
        )

    def wait_for_url_change(self):

        WebDriverWait(self.driver, 15).until(
            lambda d: d.current_url != "about:blank"
        )

    def get_current_url(self):

        return self.driver.current_url
    