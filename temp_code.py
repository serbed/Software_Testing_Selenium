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
    app_len = len(driver.find_elements_by_css_selector("#box-apps-menu>#app-"))
    list_count = 0
    while (list_count < app_len):
        find = driver.find_elements_by_css_selector("#box-apps-menu>#app-")
        find[list_count].click()
        driver.find_element_by_tag_name("h1")
        app_len_2 = len (driver.find_elements_by_xpath("//td//li[@id='app-']//li"))
        list_count_2 = 0
        find_l = len(driver.find_elements_by_xpath("//td//li[@id='app-']//li"))
        print(find_l)
        if find_l > 0:
            while (list_count_2 < app_len_2):
                find_2 = driver.find_elements_by_xpath("//td//li[@id='app-']//li")
                find_2[list_count_2].click()
                driver.find_element_by_tag_name("h1")
                list_count_2 += 1
        else:
            pass
        list_count +=1




""""  
    l_sort.append('Tundra')
    g = 2
    if l_sort == l:
        g=1
    else:
        g=0
    print(g)
"""

"""        if zone_atr_int > 0:
            rows_1[list_count].click()
            list_count_sub = 0
            l_sub = []
            l_sub_sort = []
            rows_2 = driver.find_elements_by_css_selector(".dataTable tr:not(.header) [name$='name]'][type=hidden]")
            rows_2_len = len(driver.find_elements_by_css_selector(".dataTable tr:not(.header) [name$='name]'][type=hidden]"))
            while (list_count_sub < rows_2_len):
                country_2 = rows_2[list_count_sub].get_attribute("value")
                l_sub.append(country_2)
                l_sub_sort.append(country_2)
                list_count_sub +=1
            l_sub_sort.sort()
            assert l_sub_sort == l_sub
            driver.find_elements_by_css_selector("[name=cancel]")
        else:
            pass """