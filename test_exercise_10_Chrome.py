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
    driver.get("http://localhost/litecart")
# Найдем блок campaigns
    campaigns_ducks = driver.find_element_by_css_selector("#box-campaigns>.content>ul")
# В блоке найдем первую уточку (по умолчанию возвращается первый элемент, поэтому очередность в локаторе не указываем)
    first_duck = campaigns_ducks.find_element_by_css_selector(" li")
# Запишем наименование уточки, обычную и акционные цены в переменные, для будущего сравнения на другой странице (duck_name_first , regular_price_first , campaign_price_first )
    duck_name_first = first_duck.find_element_by_css_selector(".name").text
    regular_price_first = first_duck.find_element_by_css_selector(".regular-price").text
    regular_price_first = regular_price_first.lstrip('$')
    regular_price_first = int(regular_price_first)
    campaign_price_first = first_duck.find_element_by_css_selector(".campaign-price").text
    campaign_price_first = campaign_price_first.lstrip('$')
    campaign_price_first = int(campaign_price_first)
# Проверим что цена серого цвета
    regular_price_color =  first_duck.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regular_price_color = regular_price_color.rstrip(')')
    regular_price_color = regular_price_color.lstrip('rgba(')
    regular_price_color = regular_price_color.split(',')
    regular_price_color = list(regular_price_color)
    regular_price_color = list(map(int, regular_price_color))
    assert regular_price_color[0] == regular_price_color[1] == regular_price_color[2]
# Проверим что цена зачёркнута
    regular_price_text = first_duck.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    print(regular_price_text)
    assert regular_price_text == 'line-through'
# Проверим что цена скидки красного цвета
    campaign_price_color = first_duck.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    campaign_price_color = campaign_price_color.rstrip(')')
    campaign_price_color = campaign_price_color.lstrip('rgba(')
    campaign_price_color = campaign_price_color.split(',')
    campaign_price_color = list(campaign_price_color)
    campaign_price_color = list(map(int, campaign_price_color))
    assert campaign_price_color[1] == 0 and campaign_price_color[2] == 0
# Проверим что акционная цена жирная:
    campaign_price_text = first_duck.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    campaign_price_text = int(campaign_price_text)
# Для шрифтов, которые предоставляют только normal и bold начертания, 100-500 normal, и 600-900 bold.
    assert campaign_price_text > 599 and campaign_price_text < 901
# Акционная цена крупнее, чем обычная
# Найдем площадь для акционной цены
    campaign_price_size = first_duck.find_element_by_css_selector(".campaign-price").size
    cps_height = campaign_price_size.get('height')
    cps_width = campaign_price_size.get('width')
    cpa_area = cps_height * cps_width
# Найдем площадь элемента обычноё цены цены
    regular_price_size = first_duck.find_element_by_css_selector(".regular-price").size
    rps_height = regular_price_size.get('height')
    rps_width = regular_price_size.get('width')
    rps_area = rps_height * rps_width
# Проверим что обычная цена меньше акционной
    assert  rps_area < cpa_area
# Перейдем на страницу товара
    btn = driver.find_element_by_css_selector("#box-campaigns .link")
    btn.click()
# Найдем текст названия товара и сравним с текстом главной страницы
    duck_name_second = driver.find_element_by_css_selector("h1.title").text
    assert duck_name_first == duck_name_second
# Найдем обычную цену и сравним с ценой главной страницы
    regular_price_second = driver.find_element_by_css_selector(".regular-price").text
    regular_price_second = regular_price_second.lstrip('$')
    regular_price_second = int(regular_price_second)
    assert regular_price_first == regular_price_second
# Найдем акционную цену и сравним с ценой главной страницы
    campaign_price_second = driver.find_element_by_css_selector(".campaign-price").text
    campaign_price_second = campaign_price_second.lstrip('$')
    campaign_price_second = int(campaign_price_second)
    assert campaign_price_first == campaign_price_second
# Проверим что цена серого цвета
    regular_price_color = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    regular_price_color = regular_price_color.rstrip(')')
    regular_price_color = regular_price_color.lstrip('rgba(')
    regular_price_color = regular_price_color.split(',')
    regular_price_color = list(regular_price_color)
    regular_price_color = list(map(int, regular_price_color))
    assert regular_price_color[0] == regular_price_color[1] == regular_price_color[2]
# Проверим что цена зачёркнута
    regular_price_text = driver.find_element_by_css_selector(".regular-price").value_of_css_property("text-decoration-line")
    print(regular_price_text)
    assert regular_price_text == 'line-through'
# Проверим что цена скидки красного цвета
    campaign_price_color = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    campaign_price_color = campaign_price_color.rstrip(')')
    campaign_price_color = campaign_price_color.lstrip('rgba(')
    campaign_price_color = campaign_price_color.split(',')
    campaign_price_color = list(campaign_price_color)
    campaign_price_color = list(map(int, campaign_price_color))
    assert campaign_price_color[1] == 0 and campaign_price_color[2] == 0
# Проверим что акционная цена жирная:
    campaign_price_text = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("font-weight")
    campaign_price_text = int(campaign_price_text)
# Для шрифтов, которые предоставляют только normal и bold начертания, 100-500 normal, и 600-900 bold.
    assert campaign_price_text > 599 and campaign_price_text < 901
# Акционная цена крупнее, чем обычная
# Найдем площадь для акционной цены
    campaign_price_size = driver.find_element_by_css_selector(".campaign-price").size
    cps_height = campaign_price_size.get('height')
    cps_width = campaign_price_size.get('width')
    cpa_area = cps_height * cps_width
# Найдем площадь элемента обычноё цены цены
    regular_price_size = driver.find_element_by_css_selector(".regular-price").size
    rps_height = regular_price_size.get('height')
    rps_width = regular_price_size.get('width')
    rps_area = rps_height * rps_width
# Проверим что обычная цена меньше акционной
    assert rps_area < cpa_area


























