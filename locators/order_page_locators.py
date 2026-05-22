from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (
        By.XPATH,
        ".//input[@placeholder='* Имя']"
    )

    SURNAME = (
        By.XPATH,
        ".//input[@placeholder='* Фамилия']"
    )

    ADDRESS = (
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO = (
        By.CLASS_NAME,
        "select-search__input"
    )

    PHONE = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        ".//button[text()='Далее']"
    )

    DATE = (
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD = (
        By.CLASS_NAME,
        "Dropdown-control"
    )

    BLACK_COLOR = (
        By.ID,
        "black"
    )

    ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"
    )

    YES_BUTTON = (
        By.XPATH,
        ".//button[text()='Да']"
    )

    SUCCESS_MODAL = (
        By.XPATH,
        ".//div[contains(text(),'Заказ оформлен')]"
    )

    @staticmethod
    def metro_station(station_name):
        return (
            By.XPATH,
            f".//div[text()='{station_name}']"
        )

    RENT_PERIOD_OPTION = (
        By.XPATH,
        ".//div[text()='сутки']"
    )