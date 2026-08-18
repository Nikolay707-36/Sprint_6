import allure
import pytest

from data import FAQData
from pages.main_page import MainPage
from urls import Urls

@allure.feature("FAQ")
class TestFAQ:
    @allure.title("Проверка ответа на вопрос #{number}")
    @pytest.mark.parametrize("number,expected_answer", FAQData.value)
    def test_question_and_answer(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        _, answer_text = main_page.get_question_and_answer(number)
        assert answer_text == expected_answer, (
            f"Неверный ответ для вопроса #{number}\n"
            f"Ожидаемый: {expected_answer}\n"
            f"Фактический: {answer_text}"
        )
