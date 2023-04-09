import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.question))
        self.driver.find_element(*self.question).click()

    @allure.step('ждем что ответ появился')
    def wait_to_answer(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.answer))

    @allure.step('возвращаем текст ответа')
    def match_checking(self):
        return self.driver.find_element(*self.answer).text


    def all_actions(self):
        self.scroll_to_questions()
        self.click_to_question()
        self.wait_to_answer()

