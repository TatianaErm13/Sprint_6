import allure

from pages.main_page import MainPage
from data.constants import (
    BASE_URL,
    YANDEX_URL
)


class TestLogo:

    @allure.title("Проверка перехода на главную страницу Самоката")
    def test_scooter_logo_redirect(self, driver):

        page = MainPage(driver)

        page.open()

        page.click_scooter_logo()

        assert page.get_current_url() == BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):

        page = MainPage(driver)

        page.open()

        page.click_yandex_logo()

        page.switch_to_yandex_tab()

        current_url = page.get_yandex_url()

        assert "yandex.ru" in page.get_current_url()
        