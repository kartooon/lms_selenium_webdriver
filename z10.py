import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd = webdriver.Firefox()
    wd = webdriver.Ie()
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/")
    wait = WebDriverWait(driver, 20)
    driver.find_element_by_css_selector("li.product")

    correct_name(driver)
    correct_price(driver, ".regular-price")
    correct_price(driver, ".campaign-price")

    color_price_list = [
        [["#box-campaigns s.regular-price", "rgba(119, 119, 119, 1)"], ["#box-campaigns strong.campaign-price", "rgba(204, 0, 0, 1)"]],
        [["s.regular-price", "rgba(102, 102, 102, 1)"], ["strong.campaign-price", "rgba(204, 0, 0, 1)"]]
    ]

    for i in color_price_list[0:1]:
        correct_prices_style(driver, i, "color")
        correct_prices_style(driver, i, "font-size")

    driver.find_element_by_css_selector("#box-campaigns a").click()

    for i in color_price_list[1:]:
        correct_prices_style(driver, i, "color")
        correct_prices_style(driver, i, "font-size")
    driver.back()

def correct_name(driver): #проверка наименования на страницах
    name_from_main = driver.find_element_by_css_selector("#box-campaigns .name").text
    driver.find_element_by_css_selector("#box-campaigns a").click()
    name_from_product = driver.find_element_by_css_selector("h1.title").text
    assert (name_from_main == name_from_product)
    driver.back()


def correct_price(driver, type_price): #проверка цены
    price_from_main = driver.find_element_by_css_selector("#box-campaigns " + type_price).text
    driver.find_element_by_css_selector("#box-campaigns a").click()
    price_from_product = driver.find_element_by_css_selector(type_price).text
    assert (price_from_main == price_from_product)
    driver.back()


def correct_prices_style(driver, list, value): #проверка стиля
    if value == "color":
        assert driver.find_element_by_css_selector(list[0][0]).value_of_css_property(value) == list[0][1]
        assert driver.find_element_by_css_selector(list[1][0]).value_of_css_property(value) == list[1][1]
    elif value == "font-size":
        assert driver.find_element_by_css_selector(list[0][0]).value_of_css_property(value) < driver.find_element_by_css_selector(list[1][0]).value_of_css_property(value)
    else:
        assert False
        print("Изъян")