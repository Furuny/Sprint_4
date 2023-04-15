import locators
import allure
import text_answer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import PageYandexScooter
import locators


class TestQuestions:


    @allure.title('Тест вопроса: Сколько это стоит? И как оплатить?')
    def test_question_how_to_pay(self, driver):
        self.question = locators.Question_how_to_pay
        self.answer = locators.Answer_how_to_pay
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_how_to_pay

    @allure.title('Тест вопроса: Хочу сразу несколько самокатов! Так можно?')
    def test_question_several_scooters(self, driver):
        self.question = locators.Question_several_scooters
        self.answer = locators.Answer_several_scooters
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_several_scooters

    @allure.title('Тест вопроса: Как рассчитывается время аренды?')
    def test_question_rental_time_calculated(self, driver):
        self.question = locators.Question_rental_time_calculated
        self.answer = locators.Answer_rental_time_calculated
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_rental_time_calculated

    @allure.title('Тест вопроса: Можно ли заказать самокат прямо на сегодня?')
    def test_question_order_scooter_today(self, driver):
        self.question = locators.Question_order_scooter_today
        self.answer = locators.Answer_order_scooter_today
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_order_scooter_today

    @allure.title('Тест вопроса: Можно ли продлить заказ или вернуть самокат раньше?')
    def test_question_return_scooter_earlier(self, driver):
        self.question = locators.Question_return_scooter_earlier
        self.answer = locators.Answer_return_scooter_earlier
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_return_scooter_earlier

    @allure.title('Тест вопроса:Вы привозите зарядку вместе с самокатом?')
    def test_question_charging_with_scooter(self, driver):
        self.question = locators.Question_charging_with_scooter
        self.answer = locators.Answer_charging_with_scooter
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_charging_with_scooter

    @allure.title('Тест вопроса:Можно ли отменить заказ?')
    def test_question_cancel_order(self, driver):
        self.question = locators.Question_cancel_order
        self.answer = locators.Answer_cancel_order
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz == text_answer.text_cancel_order

    @allure.title('Тест вопроса:Я жизу за МКАДом, привезёте?')
    def test_question_beyond_MKAD(self, driver):
        self.question = locators.Question_beyond_MKAD
        self.answer = locators.Answer_beyond_MKAD
        main_yandex = PageYandexScooter(driver, self.question, self.answer)
        main_yandex.all_actions_withs_questions()
        texti_iz = main_yandex.match_checking()
        assert texti_iz  == text_answer.text_beyond_MKAD
