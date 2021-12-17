import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Edge()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.yandex.ru/")
