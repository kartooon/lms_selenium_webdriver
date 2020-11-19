import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 20)

    zones = len(driver.find_elements_by_css_selector("tr.row"))

    while zones:
        zones -= 1
        countries = driver.find_elements_by_css_selector("td:nth-child(3) > a")
        countries[zones].click()
        zone = [i.get_attribute("textContent") for i in driver.find_elements_by_css_selector("td:nth-child(3) > select option[selected]")]
        assert (zone == sorted(zone))
        driver.back()