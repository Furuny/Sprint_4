import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--windows-size=1920,1300')
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')

    yield driver
    driver.quit()
