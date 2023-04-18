from locators import SearchLocators
import allure
from Base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys

class OrderScooter(BasePage, SearchLocators):

    def __init__(self, driver):
        self.driver = driver


    @allure.step('ждем пока появится первая форма создания заказа')
    def waiting_form_who_scooter_fo(self):
       self.wait_element(SearchLocators.form_who_scooter_fo)

    @allure.step('находим и заполняем поле имя')
    def find_and_input_name(self, name):

        self.find_element(*SearchLocators.input_name).send_keys(name)


    @allure.step('# находим и заполняем поле фамилия')
    def find_and_input_surname(self, surname):

        self.find_element(*SearchLocators.input_surname).send_keys(surname)

    @allure.step('находим и заполняем поле адрес')
    def find_and_input_address(self, address):

        self.find_element(*SearchLocators.input_address).send_keys(address)

    @allure.step('находим и заполняем поле станция метро')
    def find_and_input_metro(self, stantions):


        self.find_element(*SearchLocators.input_metro).send_keys(stantions)
        self.find_element(*SearchLocators.input_metro).send_keys(Keys.DOWN)
        self.find_element(*SearchLocators.input_metro).send_keys(Keys.ENTER)

    @allure.step('находим и заполняем поле телефон')
    def find_and_input_number_phone(self, number_phone):


        self.find_element(*SearchLocators.input_number_phone).send_keys(number_phone)

    @allure.step(' находим и нажимаем кнопку далее')
    def click_button_next(self):


        self.find_element(*SearchLocators.button_next).click()

    @allure.step('проверяем что прогрузилась вторая форма создания заказа')
    def waiting_form_about_rent(self):


        self.wait_element(SearchLocators.about_rent)

    @allure.step('находим и заполняем поле когда привезти')
    def choose_delivery_date(self, date):


        self.find_element(*SearchLocators.delivery_date).send_keys(date)
        self.find_element(*SearchLocators.delivery_date).send_keys(Keys.ENTER)

    @allure.step('находим и заполняем поле срок оренды')
    def choose_rental_period(self):


        self.find_element(*SearchLocators.lease_term_field).click()
        self.find_element(*SearchLocators.rental_period).click()

    @allure.step('находим и заполняем поле цвет')
    def choose_scooter_color(self):


        self.find_element(*SearchLocators.scooter_color).click()

    @allure.step('находим и заполняем поле комментарий')
    def  find_and_input_comment_field(self, comment):


        self.find_element(*SearchLocators.comment_field).send_keys(comment)

    @allure.step('нажимаем на кнопку заказать')
    def click_end_order_button(self):


        self.find_element(*SearchLocators.end_order_button).click()

    @allure.step('проверяем появление формы подтверждения. находим и жмем да')
    def wait_and_click_yes_confirmation_form(self):
        self.wait_element(SearchLocators.confirmation_form)
        self.find_element(*SearchLocators.confirmation_form).click()

    @allure.step('#проверяем появление окна об успешном заказе. нажимаем заказать')
    def wait_and_clock_wath_status_successful_order_window(self):
        self.wait_element(SearchLocators.successful_order_window)
        self.find_element(*SearchLocators.successful_order_window).click()

    @allure.step('проверяем что заказ создался')


    def check_order_has_been_created(self):
        self.wait_element(SearchLocators.order_has_been_created)

    @allure.step('находим кнопку самоката и жмем. проверяем переход на главную страницу «Самоката».')
    def click_skooter_button_header_and_check_transition(self):
        self.wait_element(SearchLocators.skooter_button_header).click()
        self.wait_element(SearchLocators.button_order_header)


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

