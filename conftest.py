import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():

    service = Service()

    browser = webdriver.Firefox(service=service)

    browser.set_page_load_timeout(60)

    browser.maximize_window()

    yield browser

    browser.quit()
    