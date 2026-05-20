from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.constants import BASE_URL
import allure

class MainPage(BasePage):

    URL = BASE_URL
    @allure.step("Открыть главную страницу")
    def open(self):

        self.open_url(self.URL)

        self.find_element(
            MainPageLocators.TOP_ORDER_BUTTON
        )

    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_question(self, index):
        locator = (
            By.ID,
            f"accordion__heading-{index}"
        )
        self.click_element(locator)

    def get_answer_text(self, index):
        locator = (
            By.ID,
            f"accordion__panel-{index}"
        )
        return self.get_text(locator)
    
    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_questions(self):
        element = self.find_element(MainPageLocators.QUESTIONS_HEADER)
        self.scroll_to_element(element)

    def switch_to_yandex_tab(self):

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        self.driver.switch_to.window(
            self.driver.window_handles[1]
        )

    def wait_for_yandex_page_load(self):

        WebDriverWait(self.driver, 15).until(
            lambda d: d.current_url != "about:blank"
        )

    def get_current_url(self):

        return self.driver.current_url