import time

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
#    log_list = list()
#    for l in driver.get_log("browser"):
#       print(l)
#       log_list.append(l)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    ducks_len = len(driver.find_elements_by_xpath("//table[@class='dataTable']//tr//td[3]//a"))
    list_count = 3
    while (list_count < ducks_len):
        ducks = driver.find_elements_by_xpath("//table[@class='dataTable']//tr//td[3]//a")
        ducks[list_count].click()
        driver.back()
        list_count += 1
# Заберем лог из браузера и проверим что он пуст.
    log_list = driver.get_log("browser")
    print(log_list)
    assert len(log_list) == 0

















