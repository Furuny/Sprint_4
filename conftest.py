import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--windows-size=1920,1300')
    browser = webdriver.Firefox()
    browser.get(url)

    yield browser
    browser.quit()
