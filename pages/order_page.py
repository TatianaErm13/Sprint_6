from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_first_form(
            self,
            name,
            surname,
            address,
            metro,
            phone
    ):

        self.fill_input(
            OrderPageLocators.NAME,
            name
        )

        self.fill_input(
            OrderPageLocators.SURNAME,
            surname
        )

        self.fill_input(
            OrderPageLocators.ADDRESS,
            address
        )

        self.fill_input(
            OrderPageLocators.METRO,
            metro
        )

        self.click_element(
            OrderPageLocators.metro_station(metro)
        )

        self.fill_input(
            OrderPageLocators.PHONE,
            phone
        )

        self.click_element(
            OrderPageLocators.NEXT_BUTTON
        )

    def fill_second_form(self, date):

        self.fill_input(
            OrderPageLocators.DATE,
            date
        )

        self.find_element(
            OrderPageLocators.DATE
        ).send_keys(Keys.ENTER)

        self.click_element(
            OrderPageLocators.RENT_PERIOD
        )

        self.click_element(
            OrderPageLocators.RENT_PERIOD_OPTION
        )

        self.click_element(
            OrderPageLocators.BLACK_COLOR
        )

        self.click_element(
            OrderPageLocators.ORDER_BUTTON
        )

        self.click_element(
            OrderPageLocators.YES_BUTTON
        )

    def check_order_created(self):

        return self.find_element(
            OrderPageLocators.SUCCESS_MODAL
        ).is_displayed()
    