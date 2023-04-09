from selenium.webdriver.common.by import By

# кнопка с вопросом Сколько это стоит? И как оплатить?
Question_how_to_pay = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div/div/div"]
# кнопка с ответом на вопрос Сколько это стоит? И как оплатить?
Answer_how_to_pay = [By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]"]
# текст ответа на Сколько это стоит? И как оплатить?
text_how_to_pay  = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

# кнопка с вопросом Хочу сразу несколько самокатов! Так можно?
Question_several_scooters = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[2]/div/div"]
# кнопка с ответом на вопрос Хочу сразу несколько самокатов! Так можно?
Answer_several_scooters = [By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат.')]"]
# текст ответа на Хочу сразу несколько самокатов! Так можно?
text_several_scooters = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

#кнопка с вопросом Как рассчитывается время аренды?
Question_rental_time_calculated = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[3]/div/div"]
#кнопка с ответом на вопрос Как рассчитывается время аренды?
Answer_rental_time_calculated = [By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая.')]"]
# текст ответа на Как рассчитывается время аренды?
text_rental_time_calculated = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

#кнопка с вопросом Можно ли заказать самокат прямо на сегодня?
Question_order_scooter_today = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[4]/div/div"]
#кнопка с ответом на вопрос Можно ли заказать самокат прямо на сегодня?
Answer_order_scooter_today = [By.XPATH,"//p[contains(text(),'Только начиная с завтрашнего дня.')]"]
# текст ответа на Можно ли заказать самокат прямо на сегодня?
text_order_scooter_today = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

#кнопка с вопросом Можно ли продлить заказ или вернуть самокат раньше?
Question_return_scooter_earlier = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[5]/div/div"]
#кнопка с ответом на вопрос Можно ли продлить заказ или вернуть самокат раньше?
Answer_return_scooter_earlier = [By.XPATH,"//p[contains(text(),'Пока что нет! Но если что-то срочное')]"]
# текст ответа на Можно ли продлить заказ или вернуть самокат раньше?
text_return_scooter_earlier = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

#кнопка с вопросом Вы привозите зарядку вместе с самокатом?
Question_charging_with_scooter = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[6]/div/div"]
#кнопка с ответом на Вы привозите зарядку вместе с самокатом?
Answer_charging_with_scooter = [By.XPATH,"//p[contains(text(),'Самокат приезжает к вам с полной зарядкой.')]"]
# текст ответа на Вы привозите зарядку вместе с самокатом?
text_charging_with_scooter = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

#кнопка с вопросом Можно ли отменить заказ?
Question_cancel_order = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[7]/div/div"]
#кнопка с ответом на вопрос Можно ли отменить заказ?
Answer_cancel_order = [By.XPATH,"//p[contains(text(),'Да, пока самокат не привезли.')]"]
# текст ответа на вопрос Можно ли отменить заказ?
text_cancel_order = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

#кнопка с вопросом Я жизу за МКАДом, привезёте?
Question_beyond_MKAD = [By.XPATH,"//div[@class='Home_FAQ__3uVm4']/div/div[8]/div/div"]
#кнопка с ответом на вопрос Я жизу за МКАДом, привезёте?
Answer_beyond_MKAD = [By.XPATH,"//p[contains(text(),'Да, обязательно. Всем самокатов!')]"]
# текст ответа на вопрос Я жизу за МКАДом, привезёте?
text_beyond_MKAD = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


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
