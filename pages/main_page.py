import allure
from Base_page import BasePage
from locators import SearchLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class PageYandexScooter(BasePage, SearchLocators):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('скролим до вопросов')
    def scroll_to_questions(self, question):
        self.wait_element(question)
        self.scroll_to_element(self.wait_element(question))

    @allure.step('ждем, пока все загрузится и нажимаем на вопрос')
    def click_to_question(self, question):
        self.wait_element(question).click()

    @allure.step('ждем, пока ответ не появится')
    def wait_for_answer(self, answer):
        self.wait_element(answer)

    @allure.step('возвращаем текст ответа')
    def get_answer_text(self, answer):
        return self.find_element(*answer).text

    @allure.step('все действия с вопросами и ответами')
    def perform_all_actions_with_question(self, question, answer):
        self.scroll_to_questions(question)
        self.click_to_question(question)
        self.wait_for_answer(answer)



    @allure.step('находим кнопку в хедере, ожидаем прогрузку и нажимаем на кнопку')
    def find_button_order_scooter_header_and_click(self):

        self.scroll_to_button(*SearchLocators.button_order_header)
        self.wait_element(SearchLocators.button_order_header).click()

    @allure.step(' находим  большую кнопку в центре страницы, ожидаем прогрузку и нажимаем на кнопку')
    def find_big_button_order_scooter_and_click(self):
        self.scroll_to_button(*SearchLocators.big_button_order)
        self.wait_element(SearchLocators.big_button_order).click()

    @allure.step('находим кнопку самоката и жмем. проверяем переход на главную страницу «Яндекса».')
    def click_yandex_button_header_and_check_transition(self):
        self.wait_element(SearchLocators.yandex_button_header).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_element(SearchLocators.button_yandex_search)
        url_yandex = self.driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"
