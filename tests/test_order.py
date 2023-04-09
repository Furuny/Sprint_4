import locators
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_scooter import OrderScooter


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Тест создания заказа по кнопке в хедере и первым набором данных')
    def test_order_from_big_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.button_order = locators.big_button_order
        self.form_who_scooter_fo = locators.form_who_scooter_fo
        self.input_name = locators.input_name
        self.input_surname = locators.input_surname
        self.input_address = locators.input_address
        self.input_metro = locators.input_metro
        self.input_number_phone = locators.input_number_phone
        self.button_next = locators.button_next
        self.about_rent = locators.about_rent
        self.delivery_date = locators.delivery_date
        self.lease_term_field = locators.lease_term_field
        self.rental_period = locators.rental_period
        self.scooter_color = locators.scooter_color
        self.comment_field = locators.comment_field
        self.end_order_button = locators.end_order_button
        self.confirmation_form = locators.confirmation_form
        self.successful_order_window = locators.successful_order_window
        self.order_has_been_created = locators.order_has_been_created
        self.skooter_button_header = locators.skooter_button_header
        self.yandex_button_header = locators.yandex_button_header



        name = 'имя первый'
        surname = "фамилияПервая"
        address = "адрес первый 154 кв 6"
        stantions = "Лубянка"
        number_phone = "89161234567"
        date = "15.04.2023"
        comment = " первый комментарий курьеру"

        main_yandex = OrderScooter(self.driver, self.button_order,self.form_who_scooter_fo,self.input_name,
                                   self.input_surname, self.input_address, self.input_metro, self.input_number_phone,
                                   self.button_next, self.about_rent, self.delivery_date, self.lease_term_field,
                                   self.rental_period, self.scooter_color, self.comment_field, self.end_order_button,
                                   self.confirmation_form, self.successful_order_window, self.order_has_been_created,
                                   self.skooter_button_header, self.yandex_button_header)
        main_yandex.all_order(name, surname, address, stantions, number_phone, date, comment)


    @allure.title('Тест создания заказа по  большой кнопке в центре сайта и вторым набором данных')
    def test_order_from_button_order_header(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        self.button_order = locators.button_order_header
        self.form_who_scooter_fo = locators.form_who_scooter_fo
        self.input_name = locators.input_name
        self.input_surname = locators.input_surname
        self.input_address = locators.input_address
        self.input_metro = locators.input_metro
        self.input_number_phone = locators.input_number_phone
        self.button_next = locators.button_next
        self.about_rent = locators.about_rent
        self.delivery_date = locators.delivery_date
        self.lease_term_field = locators.lease_term_field
        self.rental_period = locators.rental_period
        self.scooter_color = locators.scooter_color
        self.comment_field = locators.comment_field
        self.end_order_button = locators.end_order_button
        self.confirmation_form = locators.confirmation_form
        self.successful_order_window = locators.successful_order_window
        self.order_has_been_created = locators.order_has_been_created
        self.skooter_button_header = locators.skooter_button_header
        self.yandex_button_header = locators.yandex_button_header



        name = 'второе имя'
        surname = "фамилияВторого"
        address = "адрес второй 6 кв 444"
        stantions = "Черкизовская"
        number_phone = "89276874324"
        date = "12.00.2023"
        comment = " второй комментарий курьеру"

        main_yandex = OrderScooter(self.driver, self.button_order,self.form_who_scooter_fo,self.input_name,
                                   self.input_surname, self.input_address, self.input_metro, self.input_number_phone,
                                   self.button_next, self.about_rent, self.delivery_date, self.lease_term_field,
                                   self.rental_period, self.scooter_color, self.comment_field, self.end_order_button,
                                   self.confirmation_form, self.successful_order_window, self.order_has_been_created,
                                   self.skooter_button_header, self.yandex_button_header)
        main_yandex.all_order(name, surname, address, stantions, number_phone, date, comment)



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
