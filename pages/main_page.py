from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.constants import BASE_URL
import allure

class MainPage(BasePage):

    URL = BASE_URL

    def open(self):

        self.open_url(self.URL)

    def click_top_order_button(self):

        self.click_element(
            MainPageLocators.TOP_ORDER_BUTTON
        )

    def click_bottom_order_button(self):

        self.click_element(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

    def click_scooter_logo(self):

        self.click_element(
            MainPageLocators.SCOOTER_LOGO
        )

    def click_yandex_logo(self):

        self.click_element(
            MainPageLocators.YANDEX_LOGO
        )

    def click_question(self, index):

        self.click_element(
            MainPageLocators.question_locator(index)
        )

    def get_answer_text(self, index):

        return self.get_text(
            MainPageLocators.answer_locator(index)
        )

    def scroll_to_questions(self):

        element = self.find_element(
            MainPageLocators.QUESTIONS_HEADER
        )

        self.scroll_to_element(element)

    def switch_to_yandex_tab(self):

        self.wait_for_new_window()

        self.switch_to_window(1)

        self.wait_for_url_change()

    def get_yandex_url(self):

        return self.get_current_url()
    