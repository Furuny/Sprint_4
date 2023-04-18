import allure
from selenium import webdriver
from test_data import FIRST_ORDER_DATA, SECOND_ORDER_DATA
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_order_scooter import OrderScooter
from pages.main_page import PageYandexScooter

class TestOrder():

    @allure.title('Тест создания заказа по  большой кнопке в центре сайта и вторым набором данных')
    def test_order_from_big_button(self, driver):

        orders_forms = OrderScooter(driver)
        button_from_main = PageYandexScooter(driver,)
        button_from_main.find_big_button_order_scooter_and_click()
        orders_forms.all_order(self, **FIRST_ORDER_DATA)
        button_from_main.click_yandex_button_header_and_check_transition()


    @allure.title('Тест создания заказа по кнопке в хедере и первым набором данных')
    def test_order_from_button_order_header(self, driver):


        orders_forms = OrderScooter(driver)
        button_from_main = PageYandexScooter(driver)
        button_from_main.find_button_order_scooter_header_and_click()
        orders_forms.all_order(self,  **SECOND_ORDER_DATA)
        button_from_main.click_yandex_button_header_and_check_transition()
