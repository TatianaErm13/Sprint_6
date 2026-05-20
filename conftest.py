import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    browser = webdriver.Firefox()

    browser.set_page_load_timeout(30)

    yield browser

    browser.quit()