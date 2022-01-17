
import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart")
    list_count = 0
    wait = WebDriverWait(driver, 10)
    def check_by_xpath(xpath):
        driver.implicitly_wait(0)
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True
        return False
        driver.implicitly_wait(10)
    size_list = "//select[@name='options[Size]']"
    while (list_count < 3):
        first_duck = driver.find_element_by_xpath("//div[@id='box-most-popular']//ul[@class='listing-wrapper products']/li[1]")
        first_duck.click()
        if check_by_xpath("//select[@name='options[Size]']") == False:
            list = driver.find_element_by_xpath(size_list)
            ActionChains(driver).move_to_element(list).click().perform()
            list_1 = driver.find_element_by_xpath("//option[text()='Small']")
            list_1.click()
        else:
          pass
        list_count += 1
        add_button = driver.find_element_by_xpath("//button[@name='add_cart_product']")
        add_button.click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="quantity"]'), str(list_count)))
        driver.get("http://localhost/litecart")
    basket_btn = driver.find_element_by_xpath("//a[@class='content']")
    basket_btn.click()
# //tr/td[@class='item']
    ducks_len = len(driver.find_elements_by_xpath("//tr/td[@class='item']"))
    counter = 0
    while (counter < ducks_len):
        time.sleep(1)
        if check_by_xpath("//strong") == False:
            table_str = driver.find_element_by_xpath("//table[@class='dataTable rounded-corners']/tbody/tr[2]")
            remove_btn = driver.find_element_by_xpath("//button[@name='remove_cart_item']")
            remove_btn.click()
            wait.until(EC.staleness_of(table_str))
        else:
            pass
        counter +=1













