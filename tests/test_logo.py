import allure

from pages.main_page import MainPage
from data.constants import BASE_URL


class TestLogo:

    @allure.title("Проверка перехода по клику на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):

        page = MainPage(driver)

        page.open()

        page.click_scooter_logo()

        assert BASE_URL in page.get_current_url()

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):

        page = MainPage(driver)

        page.open()

        page.click_yandex_logo()

        page.switch_to_yandex_tab()

        page.wait_for_yandex_page_load()

        current_url = page.get_current_url()

        assert (
            "dzen" in current_url
            or "yandex" in current_url
            or "ya.ru" in current_url
        )