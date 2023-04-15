в папке pages содержутся классы с тестовыми методами order_scooter.py и page_yandex_scooter.py.


order_scooter.py содержит данные для нахождения, действий и ожиданий для составления заказа самоката:
waiting_form_who_scooter_fo - ждем пока появится первая форма создания заказа
find_and_input_name - находим и заполняем поле имя
find_and_input_surname - находим и заполняем поле фамилия
find_and_input_address - находим и заполняем поле адрес
find_and_input_metro - находим и заполняем поле станция метро
find_and_input_number_phone - находим и заполняем поле телефон
click_button_next - находим и нажимаем кнопку далее
waiting_form_about_rent - проверяем что прогрузилась вторая форма создания заказа
choose_delivery_date - находим и заполняем поле когда привезти
choose_rental_period - находим и заполняем поле срок оренды
choose_scooter_color - находим и заполняем поле цвет
find_and_input_comment_field - находим и заполняем поле комментарий
click_end_order_button - нажимаем на кнопку заказать
wait_and_click_yes_confirmation_form - проверяем появление формы подтверждения. находим и жмем да
wait_and_clock_wath_status_successful_order_window - проверяем появление окна об успешном заказе. нажимаем заказать   
check_order_has_been_created - проверяем что заказ создался
click_skooter_button_header_and_check_transition - находим кнопку самоката и жмем. проверяем переход на главную страницу Самоката
all_actions_withs_questions - все шаги


page_yandex_scooter.py  содержит данные для нахождения, действий и ожиданий для промотра вопросов и ответов: 
scroll_to_questions - скролим до вопросов
click_to_question - ждем что все прогрузилось и нажимаем на вопрос
wait_to_answer - ждем что ответ появился
match_checking - возвращаем текст ответа
find_button_order_scooter_header_and_click находим кнопку в хедере, ожидаем прогрузку и нажимаем на кнопку
find_button_order_scooter_header_and_click находим  большую кнопку в центре страницы, ожидаем прогрузку и нажимаем на кнопку
click_yandex_button_header_and_check_transition находим кнопку самоката и жмем. проверяем переход на главную страницу «Яндекса».
        
в папке tests содержутся тесты test_order.py и test_questions.py.


test_order.py содержит тесты:
def test_order_from_big_button - Тест создания заказа по кнопке в хедере и первым набором данных
test_order_from_button_order_header - Тест создания заказа по  большой кнопке в центре сайта и вторым набором данных


test_questions.py содержит тесты: 
Тест вопроса: Сколько это стоит? И как оплатить?
test_question_how_to_pay - Тест вопроса: Сколько это стоит? И как оплатить?
test_question_several_scooters - Тест вопроса: Хочу сразу несколько самокатов! Так можно?
test_question_rental_time_calculated - Тест вопроса: Как рассчитывается время аренды?
test_question_order_scooter_today - Тест вопроса: Можно ли заказать самокат прямо на сегодня?
test_question_return_scooter_earlier - Тест вопроса: Можно ли продлить заказ или вернуть самокат раньше?
test_question_charging_with_scooter - Тест вопроса:Вы привозите зарядку вместе с самокатом?
test_question_cancel_order - Тест вопроса:Можно ли отменить заказ?
test_question_beyond_MKAD - Тест вопроса:Я жизу за МКАДом, привезёте?

в папке locators содержутся локаторы
 папке text_answer содержутся тексты ответов для сравнения 
