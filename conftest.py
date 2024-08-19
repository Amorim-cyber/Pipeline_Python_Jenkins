import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    chrome_path = '/home/lucasa/auto_python_pipeline/chrome-linux64/chrome'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()

