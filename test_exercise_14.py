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
    def there_is_window_other_than(old_windows):
        new_windows = driver.window_handles
        wait = WebDriverWait(driver, 4)  # seconds
        wait.until(lambda d: len(old_windows) < len(new_windows))
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    add_button = driver.find_element_by_xpath("//a[@class='button']")
    add_button.click()
    my_window = driver.current_window_handle
    old_windows = driver.window_handles
    links = driver.find_elements_by_xpath("//i[@class='fa fa-external-link']")
    links_len = len(driver.find_elements_by_xpath("//i[@class='fa fa-external-link']"))
    list_count = 0
    while (list_count < links_len):
        click_btn = links[list_count]
        click_btn.click()
        there_is_window_other_than(old_windows)
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(my_window)
        list_count +=1














