import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wait = WebDriverWait(driver, 600)
    return wd
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 10)
    add_to_cart(driver, 3)
    delele_from_cart(driver)


def add_to_cart(driver, count = 1):
    for i in range(count):
        driver.find_element_by_css_selector("#box-most-popular a").click()
        driver.find_element_by_name("add_cart_product").click()
        counter = int(driver.find_element_by_css_selector("span.quantity").text)
        WebDriverWait(driver, 10).until(lambda s: int(s.find_element_by_css_selector("span.quantity").text) == counter + 1)
        driver.back()


def delete_from_cart(driver):
    driver.find_element_by_css_selector("div#cart a.link").click()
    counter = len(driver.find_elements_by_css_selector("table.dataTable tr"))
    while counter > 0:
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 10).until(lambda s: len(s.find_elements_by_css_selector("table.dataTable tr")) < counter)
        counter = len(driver.find_elements_by_css_selector("table.dataTable tr"))
    driver.back()