import time

import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    catalog = driver.find_element_by_xpath("//span[text()='Catalog']")
    catalog.click()
    btn_add = driver.find_element_by_css_selector("div>.button:nth-child(2)")
    btn_add.click()
    time.sleep(3)
# Заполняем General
    status_radio = driver.find_element_by_xpath("//label[text()=' Enabled']/input")
    status_radio.click()
    name = driver.find_element_by_xpath("//input[@name='name[en]']")
    name.send_keys("super-duck")
    code = driver.find_element_by_xpath("//input[@name='code']")
    code.send_keys("rd006")
    categories_root = driver.find_element_by_xpath("//input[@data-name='Root']")
    categories_root.click()
    categories = driver.find_element_by_xpath("//input[@data-name='Rubber Ducks']")
    categories.click()
    default_category = driver.find_element_by_xpath("//select[@name='default_category_id']")
    ActionChains(driver).move_to_element(default_category).click().perform()
    list = driver.find_element_by_xpath("//option[text()='Rubber Ducks']")
    list.click()
    time.sleep(3)
    product_groups = driver.find_element_by_xpath("//input[@value='1-3']")
    product_groups.click()
    quantity = driver.find_element_by_xpath("//input[@name='quantity']")
    quantity.clear()
    quantity.send_keys("100")
    abs_path = os.path.abspath("images\\super-duck.jpg")
    send_file = driver.find_element_by_xpath("//input[@type='file']")
    send_file.send_keys(abs_path)
    date_valid_from = driver.find_element_by_xpath("//input[@name='date_valid_from']")
    date_valid_from.send_keys("01122021")
    date_valid_to = driver.find_element_by_xpath("//input[@name='date_valid_to']")
    date_valid_to.send_keys("01122022")
    btn_information = driver.find_element_by_xpath("//a[text()='Information']")
    btn_information.click()
    time.sleep(3)
# Заполняем Information
    manufacturer = driver.find_element_by_xpath("//select[@name='manufacturer_id']")
    time.sleep(3)
    ActionChains(driver).move_to_element(manufacturer).click().perform()
    list = driver.find_element_by_xpath("//option[text()='ACME Corp.']")
    list.click()
    keywords = driver.find_element_by_xpath("//input[@name='keywords']")
    keywords.send_keys("duck super big size")
    short_description = driver.find_element_by_xpath("//input[@name='short_description[en]']")
    short_description.send_keys("this is super duck!")
    description = driver.find_element_by_xpath("//div[@dir='ltr']")
    description.send_keys("big description for big duck")
    head_title = driver.find_element_by_xpath("//input[@name='head_title[en]']")
    head_title.send_keys("super duck")
    meta_description = driver.find_element_by_xpath("//input[@name='meta_description[en]']")
    meta_description.send_keys("meta description for big suer duck")
    driver.execute_script("window.scrollTo(0, 0);")
    btn_prices = driver.find_element_by_xpath("//a[text()='Prices']")
    btn_prices.click()
    time.sleep(3)
# Заполним Prices
    purchase_price = driver.find_element_by_xpath("//input[@name='purchase_price']")
    purchase_price.clear()
#    ActionChains(driver).move_to_element(purchase_price).double_click().key_up("backspace").release().perform()
    purchase_price.send_keys("100")
    purchase_price_list = driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']")
    ActionChains(driver).move_to_element(purchase_price_list).click().perform()
    list = driver.find_element_by_xpath("//option[@value='USD']")
    list.click()
    price = driver.find_element_by_xpath("//input[@name='prices[USD]']")
    price.send_keys("500")
    btn_save = driver.find_element_by_xpath("//button[@name='save']")
    btn_save.click()
    time.sleep(3)
    assert driver.find_element_by_xpath("//a[text()='super-duck']")












