import allure
import pytest
from Base_page import BasePage
from locators import SearchLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import PageYandexScooter
from text_answer import TextAnswer


class TestQuestions:
    @pytest.mark.parametrize("question, answer, text_answer", [
        (SearchLocators.question_how_to_pay, SearchLocators.answer_how_to_pay, TextAnswer.text_how_to_pay),
        (SearchLocators.question_several_scooters, SearchLocators.answer_several_scooters, TextAnswer.text_several_scooters),
        (SearchLocators.question_rental_time_calculated, SearchLocators.answer_rental_time_calculated, TextAnswer.text_rental_time_calculated),
        (SearchLocators.question_order_scooter_today, SearchLocators.answer_order_scooter_today, TextAnswer.text_order_scooter_today),
        (SearchLocators.question_return_scooter_earlier, SearchLocators.answer_return_scooter_earlier, TextAnswer.text_return_scooter_earlier),
        (SearchLocators.question_charging_with_scooter, SearchLocators.answer_charging_with_scooter, TextAnswer.text_charging_with_scooter),
        (SearchLocators.question_cancel_order, SearchLocators.answer_cancel_order, TextAnswer.text_cancel_order),
        (SearchLocators.question_beyond_mkad, SearchLocators.answer_beyond_mkad, TextAnswer.text_beyond_mkad)])

    @allure.step('тест всех вопросов')
    def test_question(self, driver, question, answer, text_answer):
        main_yandex = PageYandexScooter(driver)
        main_yandex.perform_all_actions_with_question(question, answer)
        text_iz = main_yandex.get_answer_text(answer)
        assert text_iz == text_answer
