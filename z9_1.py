import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 20)

# 1a ---
    countries = [i.text for i in driver.find_elements_by_css_selector("tr.row a") if i.text != '']
    assert (countries == sorted(countries))

# 1b ---
    zones = [j.text for j in driver.find_elements_by_css_selector("td:nth-child(6)")]
    zones_indexs = [zones.index(j) for j in zones if j != '0'] #получение индекса страны с зонами

    for k in zones_indexs:
        country = driver.find_elements_by_css_selector("td:nth-child(5) > a")
        country[k].click()
        zones = [k.get_attribute("textContent") for k in driver.find_elements_by_css_selector("#table-zones tr > td:nth-child(3)") if k.get_attribute("textContent") != ""]
        assert (zones == sorted(zones))
        driver.back()
