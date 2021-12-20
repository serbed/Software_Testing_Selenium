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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    countries = driver.find_elements_by_css_selector("td:not([style])>a")
    countries_len = len(countries)
    list_count = 0
    while (list_count < countries_len):
        countries = driver.find_elements_by_css_selector("td:not([style])>a")
# Кликнем по ссылке
        countries[list_count].click()
# Объявим списки
        l = []
        l_sort = []
# Найдем все зоны
        zones = driver.find_elements_by_css_selector("[name*='zone_code']>[selected]")
# Посчитаем длину для списка
        zones_len = len(zones)
        list_count_sub = 0
# В цикле наполним все элементы и наполним ими списки
        while (list_count_sub < zones_len):
            zone_sub = zones[list_count_sub].text
            l.append(zone_sub)
            l_sort.append(zone_sub)
            list_count_sub += 1
# К одному из списков применим сортировку для сравнения
        l_sort.sort()
# Сравним списки
        assert  l == l_sort
# Возвращаемся на страницу со странами
        btn = driver.find_element_by_css_selector("button[name=cancel]")
        btn.click()
        list_count += 1














