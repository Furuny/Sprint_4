from selenium.webdriver.common.by import By

# кнопка с вопросом Сколько это стоит? И как оплатить?
Question_how_to_pay = [By.XPATH,"//div[@id='accordion__heading-0']"]
# кнопка с ответом на вопрос Сколько это стоит? И как оплатить?
Answer_how_to_pay = [By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]"]
# кнопка с вопросом Хочу сразу несколько самокатов! Так можно?
Question_several_scooters = [By.XPATH,"//div[@id='accordion__heading-1']"]
# кнопка с ответом на вопрос Хочу сразу несколько самокатов! Так можно?
Answer_several_scooters = [By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат.')]"]
#кнопка с вопросом Как рассчитывается время аренды?
Question_rental_time_calculated = [By.XPATH,"//div[@id='accordion__heading-2']"]
#кнопка с ответом на вопрос Как рассчитывается время аренды?
Answer_rental_time_calculated = [By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая.')]"]
#кнопка с вопросом Можно ли заказать самокат прямо на сегодня?
Question_order_scooter_today = [By.XPATH,"//div[@id='accordion__heading-3']"]
#кнопка с ответом на вопрос Можно ли заказать самокат прямо на сегодня?
Answer_order_scooter_today = [By.XPATH,"//p[contains(text(),'Только начиная с завтрашнего дня.')]"]
#кнопка с вопросом Можно ли продлить заказ или вернуть самокат раньше?
Question_return_scooter_earlier = [By.XPATH,"//div[@id='accordion__heading-4']"]
#кнопка с ответом на вопрос Можно ли продлить заказ или вернуть самокат раньше?
Answer_return_scooter_earlier = [By.XPATH,"//p[contains(text(),'Пока что нет! Но если что-то срочное')]"]
#кнопка с вопросом Вы привозите зарядку вместе с самокатом?
Question_charging_with_scooter = [By.XPATH,"//div[@id='accordion__heading-5']"]
#кнопка с ответом на Вы привозите зарядку вместе с самокатом?
Answer_charging_with_scooter = [By.XPATH,"//p[contains(text(),'Самокат приезжает к вам с полной зарядкой.')]"]
#кнопка с вопросом Можно ли отменить заказ?
Question_cancel_order = [By.XPATH,"//div[@id='accordion__heading-6']"]
#кнопка с ответом на вопрос Можно ли отменить заказ?
Answer_cancel_order = [By.XPATH,"//p[contains(text(),'Да, пока самокат не привезли.')]"]
#кнопка с вопросом Я жизу за МКАДом, привезёте?
Question_beyond_MKAD = [By.XPATH,"//div[@id='accordion__heading-7']"]
#кнопка с ответом на вопрос Я жизу за МКАДом, привезёте?
Answer_beyond_MKAD = [By.XPATH,"//p[contains(text(),'Да, обязательно. Всем самокатов!')]"]

# локаторы для заказов

#кнопка заказать в хедере
button_order_header = [By.CLASS_NAME, "Button_Button__ra12g"]  #возможно кнопки неверные
# большая кнопка заказать в центре сайта
big_button_order = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button"]
# всплывашка кому скутер с полями
form_who_scooter_fo = [By.XPATH, "//div[contains(text(),'Для кого самокат')]"]
# поле имя
input_name = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[1]/input"]
#поле фамилия
input_surname = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[2]/input"]
# поле адрес
input_address = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[3]/input"]
#  поле станция метро
input_metro = [By.XPATH, "//div[@class = 'select-search__value']/input"]
#  поле телефон
input_number_phone = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[5]/input"]
# кнопка далее в первой форме заказа
button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]

# вторая форма заказа
about_rent = [By.XPATH, "//div[contains(text(),'Про аренду')]"]
# поле когда привезти
delivery_date = [By.XPATH, "//div[@class='react-datepicker-wrapper']/div/input"]
# поле срок аренды
lease_term_field = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]
# выпадающее значение в поле срок аренды
rental_period = [By.XPATH, "//div[@class = 'Dropdown-menu']/div[2]"]
# поле цвет
scooter_color = [By.XPATH, "//input[@id='black']"]
#поле комментарий
comment_field = [By.XPATH, "//div[@class='Order_Form__17u6u']/div[4]/input"]
# кнопка заказать
end_order_button = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[2]"]

# форма подтверждения. кнопка да
confirmation_form = [By.XPATH, "//button[contains(text(),'Да')]"]
# окно об успешном заказе
successful_order_window = [By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button"]
# заказ создался. страница с заказом
order_has_been_created = [By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']"]

# кнопка самоката в хедере
skooter_button_header = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
# кнопка яндекса в хедере
yandex_button_header = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

Button_yandex_search = [By.CLASS_NAME, "dzen-desktop__search-37"]
