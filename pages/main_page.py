import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class PageYandexScooter():

    def __init__(self, driver, question, answer):
        self.driver = driver
        self.question = question
        self.answer = answer

    @allure.step('скролим до вопросов')
    def scroll_to_questions(self):
        element = self.driver.find_element(*self.question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('ждем что все прогрузилось и нажимаем на вопрос')
    def click_to_question(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.question))
        self.driver.find_element(*self.question).click()

    @allure.step('ждем что ответ появился')
    def wait_to_answer(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.answer))

    @allure.step('возвращаем текст ответа')
    def match_checking(self):
        return self.driver.find_element(*self.answer).text


    def all_actions_withs_questions(self):
        self.scroll_to_questions()
        self.click_to_question()
        self.wait_to_answer()


class ButtonInManePage():

    def __init__(self, driver):
        self.driver = driver
        self.button_order_header = locators.button_order_header
        self.big_button_order = locators.big_button_order
        self.yandex_button_header = locators.yandex_button_header
        self.button_yendex_search = locators.Button_yandex_search


    @allure.step('находим кнопку в хедере, ожидаем прогрузку и нажимаем на кнопку')
    def find_button_order_scooter_header_and_click(self):

        element = self.driver.find_element(*self.button_order_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.button_order_header))
        self.driver.find_element(*self.button_order_header).click()

    @allure.step(' находим  большую кнопку в центре страницы, ожидаем прогрузку и нажимаем на кнопку')
    def find_button_order_scooter_header_and_click(self):

        element = self.driver.find_element(*self.big_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.big_button_order))
        self.driver.find_element(*self.big_button_order).click()

    @allure.step('находим кнопку самоката и жмем. проверяем переход на главную страницу «Яндекса».')
    def click_yandex_button_header_and_check_transition(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.yandex_button_header)).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.button_yendex_search))
        url_yandex = self.driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"
