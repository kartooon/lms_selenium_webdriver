import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector(".row a").click()

    main_window = driver.current_window_handle
    ex_links = driver.find_elements_by_css_selector(".fa.fa-external-link")

    for i in ex_links:
        i.click()
        new_window = [i for i in driver.window_handles if i != main_window]
        for window in new_window:
            WebDriverWait(driver, 600)
            driver.switch_to.window(window)
            driver.close()
        driver.switch_to.window(main_window)