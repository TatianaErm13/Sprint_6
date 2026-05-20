import pytest
import allure

from pages.main_page import MainPage
from data.data import FAQ_DATA


class TestQuestions:

    @allure.title("Проверка раскрытия FAQ вопросов")
    @pytest.mark.parametrize(
        "index, expected_text",
        FAQ_DATA
    )
    def test_questions_dropdown(
            self,
            driver,
            index,
            expected_text
    ):

        page = MainPage(driver)

        page.open()

        # прокрутка до блока FAQ
        page.scroll_to_questions()

        page.click_question(index)

        actual_text = page.get_answer_text(index)

        assert actual_text == expected_text