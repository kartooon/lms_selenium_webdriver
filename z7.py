import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 10)

    menu_num = len(driver.find_elements_by_css_selector("ul#box-apps-menu > li"))
    while menu_num: #прыжки по меню
        menu_num -= 1
        menu_items = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
        menu_items[menu_num].click()

        submenu_num = len(driver.find_elements_by_css_selector(".docs > li > a"))
        while submenu_num: #прыжки по подменю
            submenu_num -= 1
            submenu_items = driver.find_elements_by_css_selector(".docs > li > a")
            submenu_items[submenu_num].click()