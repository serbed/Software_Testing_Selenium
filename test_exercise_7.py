import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/")
    duck_len = len(driver.find_elements_by_css_selector(".product"))
    ducks = driver.find_elements_by_css_selector(".product")
    list_count = 0
    while (list_count < duck_len):
        sticks = ducks[list_count].find_elements_by_css_selector(".sticker")
        sticks_len = len(sticks)
        assert sticks_len == 1
        list_count += 1










