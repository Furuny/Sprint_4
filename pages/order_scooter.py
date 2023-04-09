import locators
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys

class OrderScooter():

    def __init__(self, driver, button_order, form_who_scooter_fo, input_name, input_surname, input_address,
                 input_metro, input_number_phone, black_button_next, about_rent, delivery_date, lease_term_field,
                 rental_period, scooter_color, comment_field, end_order_button, confirmation_form,
                 successful_order_window, order_has_been_created, skooter_button_header, yandex_button_header):
        self.driver = driver
        self.button_order = button_order
        self.form_who_scooter_fo = form_who_scooter_fo
        self.input_name = input_name
        self.input_surname = input_surname
        self.input_address = input_address
        self.input_metro = input_metro
        self.input_number_phone = input_number_phone
        self.black_button_next = black_button_next
        self.about_rent = about_rent
        self.delivery_date = delivery_date
        self.lease_term_field = lease_term_field
        self.rental_period = rental_period
        self.scooter_color = scooter_color
        self.comment_field = comment_field
        self.end_order_button = end_order_button
        self.confirmation_form = confirmation_form
        self.successful_order_window = successful_order_window
        self.order_has_been_created = order_has_been_created
        self.skooter_button_header = skooter_button_header
        self.yandex_button_header = yandex_button_header

    @allure.step('находим кнопку')
    def find_button_order_scooter(self):
        element = self.driver.find_element(*self.button_order)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step(' ожидаем прогрузку и нажимаем на кнопку')
    def clik_button_order_scooter(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.button_order))
        self.driver.find_element(*self.button_order).click()

    @allure.step('ждем пока появится первая форма создания заказа')
    def waiting_form_who_scooter_fo(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.form_who_scooter_fo))

    @allure.step('находим и заполняем поле имя')
    def find_and_input_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    @allure.step('# находим и заполняем поле фамилия')
    def find_and_input_surname(self, surname):
        self.driver.find_element(*self.input_surname).send_keys(surname)

    @allure.step('находим и заполняем поле адрес')
    def find_and_input_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    @allure.step('находим и заполняем поле станция метро')
    def find_and_input_metro(self, stantions):
        self.driver.find_element(*self.input_metro).send_keys(stantions)
        self.driver.find_element(*self.input_metro).send_keys(Keys.DOWN)
        self.driver.find_element(*self.input_metro).send_keys(Keys.ENTER)

    @allure.step('находим и заполняем поле телефон')
    def find_and_input_number_phone(self, number_phone):
        self.driver.find_element(*self.input_number_phone).send_keys(number_phone)

    @allure.step(' находим и нажимаем кнопку далее')
    def click_button_next(self):
        self.driver.find_element(*self.black_button_next).click()

    @allure.step('проверяем что прогрузилась вторая форма создания заказа')
    def waiting_form_about_rent(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.about_rent))

    @allure.step('находим и заполняем поле когда привезти')
    def choose_delivery_date(self, date):
        self.driver.find_element(*self.delivery_date).send_keys(date)
        self.driver.find_element(*self.delivery_date).send_keys(Keys.ENTER)

    @allure.step('находим и заполняем поле срок оренды')
    def choose_rental_period(self):
        self.driver.find_element(*self.lease_term_field).click()
        self.driver.find_element(*self.rental_period).click()

    @allure.step('находим и заполняем поле цвет')
    def choose_scooter_color(self):
        self.driver.find_element(*self.scooter_color).click()

    @allure.step('находим и заполняем поле комментарий')
    def  find_and_input_comment_field(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('нажимаем на кнопку заказать')
    def click_end_order_button(self):
        self.driver.find_element(*self.end_order_button).click()

    @allure.step('проверяем появление формы подтверждения. находим и жмем да')
    def wait_and_click_yes_confirmation_form(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.confirmation_form))
        self.driver.find_element(*self.confirmation_form).click()

    @allure.step('#проверяем появление окна об успешном заказе. нажимаем заказать')
    def wait_and_clock_wath_status_successful_order_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.successful_order_window))
        self.driver.find_element(*self.successful_order_window).click()

    @allure.step('проверяем что заказ создался')
    def check_order_has_been_created(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.order_has_been_created))

    @allure.step('находим кнопку самоката и жмем. проверяем переход на главную страницу «Самоката».')
    def click_skooter_button_header_and_check_transition(self):
        self.driver.find_element(*self.skooter_button_header).click()
        time.sleep(3)
        url_scooter = self.driver.current_url
        assert url_scooter == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('находим кнопку самоката и жмем. проверяем переход на главную страницу «Яндекса».')
    def click_yandex_button_header_and_check_transition(self):
        self.driver.find_element(*self.yandex_button_header).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        url_yandex = self.driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step('все шаги')
    def all_order(self, name, surname, address, stantions, number_phone, date, comment):
        self.find_button_order_scooter()
        self.clik_button_order_scooter()
        self.waiting_form_who_scooter_fo()
        self.find_and_input_name(name)
        self.find_and_input_surname(surname)
        self.find_and_input_address(address)
        self.find_and_input_metro(stantions)
        self.find_and_input_number_phone(number_phone)
        self.click_button_next()
        self.waiting_form_about_rent()
        self.choose_delivery_date(date)
        self.choose_rental_period()
        self.choose_scooter_color()
        self.find_and_input_comment_field(comment)
        self.click_end_order_button()
        self.wait_and_click_yes_confirmation_form()
        self.wait_and_clock_wath_status_successful_order_window()
        self.check_order_has_been_created()
        self.click_skooter_button_header_and_check_transition()
        self.click_yandex_button_header_and_check_transition()
