import locators
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_order_scooter import OrderScooter
from pages.main_page import ButtonInManePage


class TestOrder:
    @allure.title('Тест создания заказа по  большой кнопке в центре сайта и вторым набором данных')
    def test_order_from_big_button(self, driver):


        name = 'имя первый'
        surname = "фамилияПервая"
        address = "адрес первый 154 кв 6"
        stantions = "Лубянка"
        number_phone = "89161234567"
        date = "15.04.2023"
        comment = "первый комментарий курьеру"

        orders_forms = OrderScooter(driver)
        button_from_main = ButtonInManePage(driver)
        button_from_main.find_button_order_scooter_header_and_click()
        orders_forms.all_order(self, name, surname, address, stantions, number_phone, date, comment)
        button_from_main.click_yandex_button_header_and_check_transition()


    @allure.title('Тест создания заказа по кнопке в хедере и первым набором данных')
    def test_order_from_button_order_header(self, driver):
        name = 'второе имя'
        surname = "фамилияВторого"
        address = "адрес второй 6 кв 444"
        stantions = "Черкизовская"
        number_phone = "89276874324"
        date = "12.00.2023"
        comment = " второй комментарий курьеру"

        orders_forms = OrderScooter(driver)
        button_from_main = ButtonInManePage(driver)
        button_from_main.find_button_order_scooter_header_and_click()
        orders_forms.all_order(self, name, surname, address, stantions, number_phone, date, comment)
        button_from_main.click_yandex_button_header_and_check_transition()
