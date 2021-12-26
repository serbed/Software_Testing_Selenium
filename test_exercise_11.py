import pytest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    wd.implicitly_wait(15)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
# Перейдем на страницу регистрации нового пользователя
    driver.get("http://localhost/litecart/en/create_account")
# Заполним Имя
    first_name = driver.find_element_by_css_selector("input[name=firstname]")
    first_name.send_keys("Selene")
# Фамилия
    last_name = driver.find_element_by_css_selector("input[name=lastname]")
    last_name.send_keys("Gomez")
# Адрес
    address = driver.find_element_by_css_selector("input[name=address1]")
    address.send_keys("544 W 12th St, Juneau")
# Индекс
    postcode = driver.find_element_by_css_selector("input[name=postcode]")
    postcode.send_keys("99801")
# Город
    city = driver.find_element_by_css_selector("input[name=city]")
    city.send_keys("Juneau")
# Выберем страну
    country = driver.find_element_by_css_selector(".select2-selection__rendered")
    ActionChains(driver).move_to_element(country).click().perform()
    find = driver.find_element_by_css_selector(".select2-search__field")
    find.send_keys("united")
    search_list = driver.find_element_by_xpath("//li[text()='United States']")
    search_list.click()
# Выберем штат
    zone_list = driver.find_element_by_css_selector("select[name=zone_code]")
    sel_zone = Select(zone_list)
    sel_zone.select_by_visible_text('Alaska')
# Составим уникальный email
    now = datetime.now().microsecond
    now = str(now)
    email = 'selene' + now + '@ya.com'
    email_window = driver.find_element_by_css_selector("input[type=email]")
    email_window.send_keys(email)
# Телефон
    phone = driver.find_element_by_css_selector("input[type=tel]")
    phone.send_keys("+19073644625")
# Пароль
    p = "selene1234"
    password = driver.find_element_by_css_selector("input[name=password]")
    password.send_keys(p)
    password_conf = driver.find_element_by_css_selector("input[name=confirmed_password]")
    password_conf.send_keys(p)
# Создадим пользователя
    btn_create = driver.find_element_by_css_selector("button[type=submit]")
    btn_create.click()
    time.sleep(3)
# Разлогинимся
    link_logout = driver.find_element_by_css_selector("#box-account>.content li:nth-child(4)>a")
    link_logout.click()
    time.sleep(3)
# Введем email, пароль и залогинимся
    email_Address_window = driver.find_element_by_css_selector("input[name=email]")
    email_Address_window.send_keys(email)
    password_window = driver.find_element_by_css_selector("input[name=password]")
    password_window.send_keys(p)
    btn_login = driver.find_element_by_css_selector("button[name=login]")
    btn_login.click()
    time.sleep(3)
# Разлогинимся
    link_logout = driver.find_element_by_css_selector("#box-account>.content li:nth-child(4)>a")
    link_logout.click()
    time.sleep(3)



































