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
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    rows = driver.find_elements_by_css_selector(".row [href]:not([title])")
    rows_len = len(driver.find_elements_by_css_selector(".row [href]:not([title])"))
    list_count = 0
    l = []
    l_sort = []
    print(l)
    print(rows)
    while (list_count < rows_len):
        rows_1 = driver.find_elements_by_css_selector(".row [href]:not([title])")
        country = rows_1[list_count].get_attribute("outerText")
        l.append(country)
        l_sort.append(country)
        print(l)
        list_count += 1
    l_sort.sort()











