import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Если нужно запускать без GUI (например, в CI), раскомментируйте строку ниже:
    # options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
