import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

def random_str(key, len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(len)])

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd = webdriver.Firefox()
    return wd

def test_example(driver):
    account_info = dict(
        firstname = random_str("", 8),
        lastname = random_str("", 8),
        address1 = random_str("", 8),
        postcode = "12345", #5 - US, 6 - RU
        city = random_str("", 8),
        email = random_str("", 8) + "@m.com",
        phone = "+19001234567",
        password = "qwerty123",
        confirmed_password = "qwerty123"
    )

    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector("tr:last-of-type").click()
    driver.implicitly_wait(20)

    for key, item in account_info.items():
        driver.find_element_by_name(key).send_keys(item)

    Select(driver.find_element_by_name("country_code")).select_by_value("US")
    Select(driver.find_element_by_css_selector("select[name = zone_code]")).select_by_value("NY")
    driver.find_element_by_name("create_account").click()

    driver.find_element_by_css_selector("#box-account li:last-of-type a").click()
    driver.implicitly_wait(20)

    #проверка входа в аккаунт
    driver.find_element_by_name("email").send_keys(account_info["email"])
    driver.find_element_by_name("password").send_keys(account_info["password"])
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("[href$='/logout']").click()
    driver.back()
