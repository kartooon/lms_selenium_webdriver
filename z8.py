import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    wait = WebDriverWait(driver, 10)
    driver.find_elements_by_css_selector("li.product")
    products = driver.find_elements_by_css_selector("li.product")
    count_stickers = 0
    #print('\nproducts =', len(products))

    for products in products:
        count_stickers += 1
        stickers = products.find_elements_by_css_selector(".sticker")
        assert (len(stickers) == 1)
    #print('stickers =', count_stickers)