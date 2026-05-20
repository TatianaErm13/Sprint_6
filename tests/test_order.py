import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.data import ORDER_DATA


class TestOrder:

    @allure.title("Создание заказа самоката")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, button_type",
        ORDER_DATA
    )
    def test_create_order(
        self,
        driver,
        name,
        surname,
        address,
        metro,
        phone,
        date,
        button_type
    ):

        main_page = MainPage(driver)

        main_page.open()

        main_page.click_top_order_button()

        order_page = OrderPage(driver)

        order_page.fill_first_form(
            name,
            surname,
            address,
            metro,
            phone
        )

        order_page.fill_second_form(date)

        assert order_page.check_order_created()