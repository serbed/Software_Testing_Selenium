import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
#    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    app_len = len(driver.find_elements_by_css_selector("#box-apps-menu>#app-"))
    list_count = 0
    while (list_count < app_len):
        find = driver.find_elements_by_css_selector("#box-apps-menu>#app-")
        find[list_count].click()
        driver.find_element_by_tag_name("h1")
        app_len_2 = len (driver.find_elements_by_xpath("//td//li[@id='app-']//li"))
        list_count_2 = 0
        while (list_count_2 < app_len_2):
            find_2 = driver.find_elements_by_xpath("//td//li[@id='app-']//li")
            find_2[list_count_2].click()
            driver.find_element_by_tag_name("h1")
            list_count_2 += 1
        list_count +=1




