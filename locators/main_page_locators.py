from selenium.webdriver.common.by import By


class MainPageLocators:

    TOP_ORDER_BUTTON = (
        By.XPATH,
        ".//button[text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class,'Home_FinishButton')]//button"
    )

    SCOOTER_LOGO = (
        By.CLASS_NAME,
        "Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.CLASS_NAME,
        "Header_LogoYandex__3TSOI"
    )

    QUESTIONS_HEADER = (
    By.CLASS_NAME,
    "Home_FAQ__3uVm4"
    )

    @staticmethod
    def question_locator(index):

        return (
            By.ID,
            f"accordion__heading-{index}"
        )

    @staticmethod
    def answer_locator(index):

        return (
            By.ID,
            f"accordion__panel-{index}"
        )
    