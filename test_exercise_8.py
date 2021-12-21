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
#Определим количество элементов содержащих страны
    rows_len = len(driver.find_elements_by_css_selector(".row [href]:not([title])"))
    list_count = 0
#Зададим два пустых списка для сравнения
    l = []
    l_sort = []
    rows_1 = driver.find_elements_by_css_selector(".row [href]:not([title])")
#Вцикле наполням пустые списки, в конце сравниваем их (к одному из списков в конце применяем сортировку по алфавиту)
    while (list_count < rows_len):
        country = rows_1[list_count].text
        l.append(country)
        l_sort.append(country)
        zones = driver.find_elements_by_css_selector(".row>:nth-child(6n)")
        zone = zones[list_count]
        zone_atr = zone.text
        zone_atr_int = int(zone_atr)
#Если количество зон больше нуля, кликаем по ссылке, задаём списки и сравниваем их (к одному из списков в конце применяем сортировку по алфавиту):
        if zone_atr_int > 0:
            rows_1[list_count].click()
            list_count_sub = 0
            l_sub = []
            l_sub_sort = []
            rows_2 = driver.find_element_by_css_selector(".dataTable>tbody")
            rows_tr = rows_2.find_elements_by_css_selector("tr>td:nth-child(3)")
            rows_2_len = len(driver.find_elements_by_css_selector(".dataTable tr:not(.header)"))
            while (list_count_sub < rows_2_len- 1):
                  country_2 = rows_tr[list_count_sub].text
                  l_sub.append(country_2)
                  l_sub_sort.append(country_2)
                  list_count_sub +=1
# Применим к одному из списков сортировку по алфавиту
            l_sub_sort.sort()
# Сравниваем сортировку по алфавиту из браузера с сотрировкой, получившейся в результате sort():
            assert l_sub_sort == l_sub
# Находим кнопку выхода, кликаем по ней и переходим на более верзний уровень цикла, продолжаем идти по списку:
            btn = driver.find_element_by_css_selector("button[name=cancel]")
            btn.click()
            rows_1 = driver.find_elements_by_css_selector(".row [href]:not([title])")
        else:
            pass
        list_count += 1
# Сравниваем сортировки стран:
    l_sort.sort()
    assert l == l_sort











