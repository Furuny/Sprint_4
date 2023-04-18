from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('ждем элемент')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('находим элемент')
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step('скроллим к кнопкам')
    def scroll_to_button(self, *locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('скроллим к вопросам')
    def scroll_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)


