import locators
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys

class OrderScooter():

    def __init__(self, driver):
        self.driver = driver
        self.form_who_scooter_fo = locators.form_who_scooter_fo
        self.input_name = locators.input_name
        self.input_surname = locators.input_surname
        self.input_address = locators.input_address
        self.input_metro = locators.input_metro
        self.input_number_phone = locators.input_number_phone
        self.black_button_next = locators.button_next
        self.about_rent = locators.about_rent
        self.delivery_date = locators.delivery_date
        self.lease_term_field = locators.lease_term_field
        self.rental_period = locators. rental_period
        self.scooter_color = locators.scooter_color
        self.comment_field = locators.comment_field
        self.end_order_button = locators.end_order_button
        self.confirmation_form = locators.confirmation_form
        self.successful_order_window = locators.successful_order_window
        self.order_has_been_created = locators.order_has_been_created
        self.skooter_button_header = locators.skooter_button_header
        self.button_order_header = locators.button_order_header




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
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.skooter_button_header)).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.button_order_header))


    @allure.step('все шаги')
    def all_order(self, driver, name, surname, address, stantions, number_phone, date, comment):

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

